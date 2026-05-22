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

### Two Icon Patterns — CRITICAL

**Pattern 1: Service-level (resourceIcon frame)**
- Style: `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<name>`
- **MUST use `strokeColor=#ffffff`** — without it, the white glyph disappears
- Size: 78x78

**Pattern 2: Resource-level (standalone shape)**
- Style: `shape=mxgraph.aws4.<name>` directly (no resIcon)
- **MUST use `strokeColor=none`** — using #ffffff breaks these
- Size: 78x78 or 48x48

**Confusing these patterns guarantees broken icons.**

### Icon Reference Files (load by category as needed)
- `references/aws-icons-compute.md` — Lambda, EC2, ECS, EKS, Fargate
- `references/aws-icons-database.md` — DynamoDB, RDS, Aurora, ElastiCache
- `references/aws-icons-integration.md` — API Gateway, SQS, SNS, EventBridge, Step Functions
- `references/aws-icons-networking.md` — CloudFront, Route 53, VPC, ELB
- `references/aws-icons-storage.md` — S3, EFS, EBS, Glacier, Backup
- `references/aws-icons-security.md` — IAM, Cognito, KMS, WAF, Shield
- `references/aws-icons-analytics-ml.md` — Kinesis, Athena, Bedrock, SageMaker
- `references/aws-icons-common.md` — Groups, general resources, edge styles, base template

**Always look up icons from reference files. Never guess icon names.**

### Group Boundaries
- **AWS Cloud:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=none`
- **Account:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none`
- **On-premise:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_on_premise;strokeColor=#5A6C86;fillColor=none`
- **Logical groups:** Simple dashed boxes: `whiteSpace=wrap;html=1;fillColor=none;dashed=1;dashPattern=8 8`
- **NO colored backgrounds** on group boxes — always `fillColor=none`

### PNG Export Background Fix
Place a light gray rectangle covering the entire diagram as the bottom-most element:
```
rounded=1;whiteSpace=wrap;fillColor=#F5F5F5;strokeColor=#E0E0E0;arcSize=2;
```
This prevents black background on areas outside groups when exporting to PNG.

### Multi-page Diagrams
For complex architectures, use multiple pages (tabs) in one .drawio file:
```xml
<mxfile>
  <diagram id="overview" name="Overview">...</diagram>
  <diagram id="networking" name="Networking Detail">...</diagram>
  <diagram id="data-flow" name="Data Flow">...</diagram>
</mxfile>
```
- Page 1: High-level overview (service-level icons only)
- Page 2+: Detail views (resource-level icons, subnet layouts, etc.)

### Legend / Title Block
Place in top-left corner of every diagram, inside the background rectangle:
```xml
<mxCell value="&lt;b&gt;Diagram Title&lt;/b&gt;&lt;br&gt;Author | Date | Version" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=14;spacing=8;" vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="300" height="50" as="geometry" />
</mxCell>
```
Optional color legend for edge types:
- Solid line: data flow
- Dashed line: optional/async
- Red dashed: error path

### File Splitting
Since draw.io XML can be large, split creation across multiple tool calls:
1. Header + left side (frontend, delivery layer)
2. Middle (processing lambdas, database)
3. Right side (ingest, messaging, data sources)
4. Bottom (optional/outbound flows) + close XML

### Audience Mode
Before generating, assess the target audience:
- **Technical**: Use service names, protocol labels (HTTPS, gRPC), CIDR blocks, instance types
- **Non-technical**: Use action labels ("Store Data", "Send Notification"), hide implementation details, use numbered flow (① ② ③)

If unclear, ask: "Technical audience or executive/non-technical?"

### Numbered Flow Edges (for non-technical mode)
Instead of technical labels, show flow order with circled numbers:
- Flow A: ① → ② → ③ → ④ (white circled numbers)
- Flow B: ❶ → ❷ → ❸ → ❹ (black circled numbers for second flow)

Use edge labels: `value="①"` with `fontSize=14;fontStyle=1;labelBackgroundColor=#ffffff;`

### Companion Guide
After generating the .drawio file, also generate a markdown guide:
- Same filename with `.md` extension (e.g., `serverless-api.drawio` + `serverless-api.md`)
- Contents: diagram title, flow description (numbered steps matching edge labels), service list with purpose, key design decisions

### Validation Step
After generating XML, mentally verify:
1. Every `resIcon=` value exists in the reference files
2. Service-level icons have `strokeColor=#ffffff`
3. Resource-level icons have `strokeColor=none`
4. No XML comments present
5. All cell IDs are unique
6. Every edge has `<mxGeometry relative="1" as="geometry" />`

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
