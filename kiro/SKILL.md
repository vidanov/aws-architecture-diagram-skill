---
name: aws-architecture-diagram
description: Generate AWS architecture diagrams in draw.io format. Activates when the user asks to create, generate, or build an architecture diagram, system diagram, or draw.io diagram for AWS services.
---

## Instructions

Generate a draw.io (.drawio) XML file representing an AWS architecture diagram.

### Layout
- **Left-to-right flow** for data/request path
- **UI/Frontend on the LEFT** (users access from left side)
- **Data sources / external systems on the RIGHT**
- Use horizontal lanes for parallel paths (top lane, bottom lane)
- Minimum 150px horizontal spacing, 200px vertical between lanes

### Canvas
- Large canvas: `pageWidth="2400" pageHeight="1400"` minimum
- Set `dx="2800" dy="1600"` for proper viewport

### Icon Style
- Icons are from draw.io's built-in `mxgraph.aws4` stencil library — the **official AWS Architecture Icons** (https://aws.amazon.com/architecture/icons/, updated quarterly)
- Icon size: **78x78px** for main services, **65x65px** for secondary
- Use `sketch=0` on all icons
- Use `strokeColor=#ffffff` on all AWS service icons
- Use `strokeWidth=2` on all edges
- Edge style: `edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;`
- Font size: **12px** for labels

### AWS Icon Patterns (VERIFIED WORKING)

**Lambda:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;fillColor=#ED7100
```

**API Gateway:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;fillColor=#E7157B
```

**EventBridge:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;fillColor=#E7157B
```

**SNS:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;fillColor=#E7157B
```

**SQS (use productIcon style — taller with header bar):**
```
shape=mxgraph.aws4.productIcon;prIcon=mxgraph.aws4.sqs;fillColor=#232F3E;strokeColor=#ffffff
```

**DynamoDB (use for tables AND streams — differentiate by label):**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.dynamodb;fillColor=#C925D1
```

**S3:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;fillColor=#7AA116
```

**CloudFront:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;fillColor=#8C4FFF
```

**RDS:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;fillColor=#C925D1
```

**ECS:**
```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ecs;fillColor=#ED7100
```

### Group Boundaries
- **AWS Cloud:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=none`
- **Account:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none`
- **On-premise:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_on_premise;strokeColor=#5A6C86;fillColor=none`
- **Logical groups:** Simple dashed boxes: `whiteSpace=wrap;html=1;fillColor=none;dashed=1;dashPattern=8 8`
- **NO colored backgrounds** on group boxes — always `fillColor=none`

### DO NOT USE (broken/empty icons)
- `resIcon=mxgraph.aws4.dynamodb_table` — renders as empty colored square
- `resIcon=mxgraph.aws4.dynamodb_stream` — renders as empty colored square
- `resIcon=mxgraph.aws4.general_saml_token` — renders as black square
- `resIcon=mxgraph.aws4.endpoint` — may not render
- `resIcon=mxgraph.aws4.kinesis_data_streams` — unreliable as DDB Streams substitute

### Correct Alternatives
- DynamoDB tables/streams: use `resIcon=mxgraph.aws4.dynamodb` with descriptive labels
- External systems: use `shape=mxgraph.aws4.traditional_server` (standalone, no resIcon)
- Browsers/clients: use `shape=mxgraph.aws4.client` (standalone, no resIcon)

### File Splitting
Since draw.io XML can be large, split creation across multiple tool calls:
1. Header + left side (frontend, delivery layer)
2. Middle (processing lambdas, database)
3. Right side (ingest, messaging, data sources)
4. Bottom (optional/outbound flows) + close XML

### Output
- Save with descriptive filename ending in `.drawio`
- Open with `open` command (macOS) or `xdg-open` (Linux) after creation
- For PNG/SVG/PDF export, use draw.io CLI:
  - macOS: `/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -e -b 10 -o output.drawio.png input.drawio`
  - Linux: `drawio -x -f png -e -b 10 -o output.drawio.png input.drawio`
  Flags: `-x` export, `-f` format, `-e` embed diagram XML, `-b 10` border
- Exported files use double extension: `name.drawio.png` (signals embedded XML, re-editable in draw.io)

### XML Well-formedness (CRITICAL)
- **NEVER include XML comments (`<!-- -->`)** — they cause parse errors
- Escape special characters in values: `&amp;` `&lt;` `&gt;` `&quot;`
- Always use unique `id` values for each mxCell
- Every edge MUST have `<mxGeometry relative="1" as="geometry" />` as child element
- Basic structure must include root cells `id="0"` and `id="1"` (parent="0")

### Official Reference
- Full XML/style reference: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md
- Style properties: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/style-reference.md
