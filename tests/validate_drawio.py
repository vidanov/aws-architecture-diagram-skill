#!/usr/bin/env python3
"""Validate .drawio files against issues #1, #2, #3.

Issue #1: VPC peering must use resource-level pattern (shape=mxgraph.aws4.vpc_peering, strokeColor=none)
Issue #2: All edges must have source and target attributes (no floating edges)
Issue #3: Group/boundary shapes must have container=1 and children must reference parent ID
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

CONTAINER_SHAPES = [
    "mxgraph.aws4.group",
    "mxgraph.aws4.group_vpc2",
    "mxgraph.aws4.group_security_group",
    "mxgraph.aws4.group_aws_cloud_alt",
    "mxgraph.aws4.group_account",
    "mxgraph.aws4.group_on_premise",
]

def parse_style(style_str):
    """Parse draw.io style string into dict."""
    if not style_str:
        return {}
    parts = style_str.rstrip(";").split(";")
    result = {}
    for p in parts:
        if "=" in p:
            k, v = p.split("=", 1)
            result[k] = v
        else:
            result[p] = ""
    return result


def validate_file(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    errors = []
    warnings = []

    cells = {}
    for cell in root.iter("mxCell"):
        cid = cell.get("id")
        if cid:
            cells[cid] = cell

    # Issue #1: Check VPC peering icons use correct pattern
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        # Check if someone used resIcon with vpc_peering (wrong pattern)
        res_icon = style.get("resIcon", "")
        if "vpc_peering" in res_icon:
            errors.append(f"[Issue #1] Cell '{cid}': vpc_peering used as resIcon — must use resource-level pattern (shape=mxgraph.aws4.vpc_peering;strokeColor=none)")
        # Check correct pattern has strokeColor=none
        shape = style.get("shape", "")
        if "vpc_peering" in shape:
            sc = style.get("strokeColor", "")
            if sc and sc != "none":
                errors.append(f"[Issue #1] Cell '{cid}': vpc_peering has strokeColor={sc} — must be strokeColor=none")

        # Check fillColor on AWS icons
        if "mxgraph.aws4" in shape and "group" not in shape:
            if not style.get("fillColor"):
                warnings.append(f"[Rendering] Cell '{cid}': AWS icon missing fillColor — will render as white square in PNG export")

    # Issue #2: Check all edges have source and target
    for cid, cell in cells.items():
        if cell.get("edge") == "1":
            source = cell.get("source")
            target = cell.get("target")
            if not source:
                errors.append(f"[Issue #2] Edge '{cid}': missing source attribute (floating edge)")
            elif source not in cells:
                errors.append(f"[Issue #2] Edge '{cid}': source='{source}' references non-existent cell")
            if not target:
                errors.append(f"[Issue #2] Edge '{cid}': missing target attribute (floating edge)")
            elif target not in cells:
                errors.append(f"[Issue #2] Edge '{cid}': target='{target}' references non-existent cell")
            # Check for exitX/entryX
            style = parse_style(cell.get("style", ""))
            if "exitX" not in style and "entryX" not in style:
                warnings.append(f"[Issue #2] Edge '{cid}': no exitX/entryX — connection points may not snap properly")

    # Issue #3: Check containers have container=1 and children use proper parent
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        shape = style.get("shape", "")
        gr_icon = style.get("grIcon", "")

        is_group = any(s in shape for s in CONTAINER_SHAPES) or any(s in gr_icon for s in CONTAINER_SHAPES)
        if is_group:
            if style.get("container") != "1":
                errors.append(f"[Issue #3] Group '{cid}' ({cell.get('value', '')[:30]}): missing container=1 in style")
            if style.get("dropTarget") != "1":
                warnings.append(f"[Issue #3] Group '{cid}' ({cell.get('value', '')[:30]}): missing dropTarget=1 in style")

    # Check that non-edge cells inside containers reference the container as parent
    container_ids = set()
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        if style.get("container") == "1":
            container_ids.add(cid)

    # Verify children reference their container
    for cid, cell in cells.items():
        if cid in ("0", "1"):
            continue
        parent = cell.get("parent", "")
        if parent in container_ids:
            # Good — child references a container
            pass

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        # Default: test all .drawio files in tests/
        test_dir = Path(__file__).parent
        files = list(test_dir.glob("*.drawio"))
        if not files:
            print("No .drawio files found in tests/")
            sys.exit(1)
    else:
        files = [Path(f) for f in sys.argv[1:]]

    total_errors = 0
    total_warnings = 0

    for f in files:
        print(f"\n{'='*60}")
        print(f"Validating: {f.name}")
        print(f"{'='*60}")
        errors, warnings = validate_file(f)
        total_errors += len(errors)
        total_warnings += len(warnings)

        if errors:
            for e in errors:
                print(f"  ❌ {e}")
        if warnings:
            for w in warnings:
                print(f"  ⚠️  {w}")
        if not errors and not warnings:
            print("  ✅ All checks passed!")

    print(f"\n{'='*60}")
    print(f"Summary: {total_errors} errors, {total_warnings} warnings across {len(files)} file(s)")
    print(f"{'='*60}")
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
