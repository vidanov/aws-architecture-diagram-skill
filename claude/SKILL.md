---
name: aws-architecture-diagram
description: Always use when user asks to create, generate, or build an AWS architecture diagram, cloud infrastructure diagram, or system diagram with AWS services. Also activates for draw.io diagrams mentioning AWS services like Lambda, DynamoDB, S3, API Gateway, etc.
---

# AWS Architecture Diagram Skill

Generate AWS architecture diagrams as native `.drawio` files using official AWS Architecture Icons. Optionally export to PNG, SVG, or PDF with embedded XML (so exported files remain editable in draw.io).

## How to create a diagram

1. **Generate draw.io XML** in mxGraphModel format following the rules below
2. **Write the XML** to a `.drawio` file using the Write tool
3. **If the user requested an export format** (png, svg, pdf), export using the draw.io CLI (see Export section)
4. **Open the result** with `open` (macOS), `xdg-open` (Linux), or print the path

## Layout Rules

- **Left-to-right flow** for data/request path
- **UI/Frontend on the LEFT** (users access from left side)
- **Data sources / external systems on the RIGHT**
- Use horizontal lanes for parallel paths (top lane, bottom lane)
- Minimum 150px horizontal spacing, 200px vertical between lanes
- Canvas: `pageWidth="2400" pageHeight="1400"`, viewport `dx="2800" dy="1600"`

## Icon Style

- Icons are from draw.io's built-in `mxgraph.aws4` stencil library — the **official AWS Architecture Icons** (https://aws.amazon.com/architecture/icons/)
- Icon size: **78x78px** for main services, **65x65px** for secondary
- Use `sketch=0` on all icons
- Use `strokeColor=#ffffff` on all AWS service icons
- Use `strokeWidth=2` on all edges
- Edge style: `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;`
- Font size: **12px** for labels
- **NO colored backgrounds** on group boxes — always `fillColor=none`

## AWS Icon Patterns (VERIFIED WORKING)

### resourceIcon (78x78, colored square frame)

| Service | resIcon | fillColor |
|---------|---------|-----------|
| Lambda | `mxgraph.aws4.lambda` | `#ED7100` |
| API Gateway | `mxgraph.aws4.api_gateway` | `#E7157B` |
| EventBridge | `mxgraph.aws4.eventbridge` | `#E7157B` |
| SNS | `mxgraph.aws4.sns` | `#E7157B` |
| Step Functions | `mxgraph.aws4.step_functions` | `#E7157B` |
| DynamoDB | `mxgraph.aws4.dynamodb` | `#C925D1` |
| RDS | `mxgraph.aws4.rds` | `#C925D1` |
| S3 | `mxgraph.aws4.s3` | `#7AA116` |
| CloudFront | `mxgraph.aws4.cloudfront` | `#8C4FFF` |
| Route 53 | `mxgraph.aws4.route_53` | `#8C4FFF` |
| ECS | `mxgraph.aws4.ecs` | `#ED7100` |
| EC2 | `mxgraph.aws4.ec2` | `#ED7100` |

Style template:
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=<COLOR>;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<SERVICE>
```

### productIcon (70x100, taller with service header bar)

| Service | prIcon |
|---------|--------|
| SQS | `mxgraph.aws4.sqs` |

Style template:
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;strokeColor=#ffffff;fillColor=#232F3E;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.productIcon;prIcon=mxgraph.aws4.<SERVICE>
```

### Standalone shapes (no resIcon needed)

| Shape | shape value | fillColor |
|-------|-------------|-----------|
| Client/Browser | `mxgraph.aws4.client` | `#232F3D` |
| Traditional Server | `mxgraph.aws4.traditional_server` | `#232F3D` |
| Firewall | `mxgraph.aws4.generic_firewall` | `#232F3D` |
| ALB | `mxgraph.aws4.application_load_balancer` | `#8C4FFF` |
| NLB | `mxgraph.aws4.network_load_balancer` | `#8C4FFF` |
| VPC Endpoint | `mxgraph.aws4.endpoints` | `#8C4FFF` |

### Group boundaries

| Group | grIcon | strokeColor |
|-------|--------|-------------|
| AWS Cloud | `mxgraph.aws4.group_aws_cloud_alt` | `#232F3E` |
| Account | `mxgraph.aws4.group_account` | `#CD2264` |
| On-premise | `mxgraph.aws4.group_on_premise` | `#5A6C86` |
| Corporate DC | `mxgraph.aws4.group_corporate_data_center` | `#388E3C` |

## BROKEN Icons — DO NOT USE

- `resIcon=mxgraph.aws4.dynamodb_table` — renders as empty colored square
- `resIcon=mxgraph.aws4.dynamodb_stream` — renders as empty colored square
- `resIcon=mxgraph.aws4.general_saml_token` — renders as black square
- `resIcon=mxgraph.aws4.endpoint` — may not render
- `resIcon=mxgraph.aws4.kinesis_data_streams` — unreliable

**Alternatives:**
- DynamoDB tables/streams → use `resIcon=mxgraph.aws4.dynamodb` with descriptive labels
- External systems → use `shape=mxgraph.aws4.traditional_server`
- Browsers/clients → use `shape=mxgraph.aws4.client`

## Audience Mode

Before generating, assess the target audience:
- **Technical**: Use service names, protocol labels (HTTPS, gRPC), CIDR blocks, instance types
- **Non-technical**: Use action labels ("Store Data", "Send Notification"), hide implementation details, use numbered flow (① ② ③)

If unclear, ask: "Technical audience or executive/non-technical?"

### Numbered flow edges (for non-technical mode)
Instead of technical labels, show flow order with circled numbers:
- Flow A: ① → ② → ③ → ④ (white circled numbers)
- Flow B: ❶ → ❷ → ❸ → ❹ (black circled numbers for second flow)

Use edge labels: `value="①"` with `fontSize=14;fontStyle=1;labelBackgroundColor=#ffffff;`

## Companion Guide

After generating the .drawio file, also generate a markdown guide:
- Same filename with `.md` extension
- Contents: diagram title, flow description (numbered steps), service list with purpose, key design decisions

## Validation Step

After generating XML, verify:
1. Every `resIcon=` value exists in the reference files
2. Service-level icons have `strokeColor=#ffffff`
3. Resource-level icons have `strokeColor=none`
4. No XML comments present
5. All cell IDs are unique
6. Every edge has `<mxGeometry relative="1" as="geometry" />`

## Export

For PNG/SVG/PDF export using draw.io Desktop CLI:

| Platform | CLI Path |
|----------|----------|
| macOS | `/Applications/draw.io.app/Contents/MacOS/draw.io` |
| Linux | `drawio` (on PATH via snap/apt) |
| Windows | `"C:\Program Files\draw.io\draw.io.exe"` |

```bash
<CLI> -x -f <format> -e -b 10 -o <output> <input>
```

Flags: `-x` export, `-f` format (png/svg/pdf), `-e` embed diagram XML, `-b 10` border

Exported files use double extension: `name.drawio.png` — signals embedded XML, re-editable in draw.io.

## XML Well-formedness (CRITICAL)

- **NEVER include XML comments (`<!-- -->`)** — they cause parse errors
- Escape special characters: `&amp;` `&lt;` `&gt;` `&quot;`
- Always use unique `id` values for each mxCell
- Every edge MUST have `<mxGeometry relative="1" as="geometry" />` as child
- Root structure requires cells `id="0"` (root) and `id="1"` (default layer, parent="0")

## Official Reference

- XML reference: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md
- Style reference: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/style-reference.md
