# AWS Icons: 3D / Isometric (legacy `aws3d` library)

Use this file whenever the user asks for a **3D**, **isometric**, or "AWS 3D" style diagram instead of the default flat `aws4` icons. This is a real, separate stencil library built into draw.io — verified directly against draw.io's own source (`src/main/webapp/js/diagramly/sidebar/Sidebar-AWS3D.js`, function `addAWS3DPalette`). Do not guess names for this library any more than for `aws4` — if a name isn't in the table below, it doesn't exist here.

## Critical facts

- This is AWS's **legacy pre-2019 icon set** (the original chunky 3D/isometric AWS icons), frozen around 2015-2016. It is **not maintained** and covers only the services that existed then.
- **Coverage is much smaller than `aws4`.** Most modern services (API Gateway, ECS, EKS, Fargate, Step Functions, EventBridge, SNS, Aurora, Cognito, KMS, CloudWatch, IAM, Kinesis, SageMaker, Bedrock, etc.) have **no icon in this library**. Check the table below before assuming an icon exists — if it's missing, tell the user and propose a substitute (see Gaps section) rather than guessing a stencil name.
- Style prefix (prepend to every shape below, before the shape-specific properties):
  ```
  verticalLabelPosition=bottom;html=1;verticalAlign=top;strokeWidth=1;align=center;outlineConnect=0;dashed=0;shape=mxgraph.aws3d.<name>;
  ```
- Sizes below are already in absolute px (base tile is 100x100, scaled by the ratios draw.io uses internally) — use them directly as `width`/`height` in `mxGeometry`. `aspect=fixed` is set on nearly every shape, so keep the width:height ratio if you resize.
- No `resIcon`/`resourceIcon` wrapper pattern here — these are all standalone shapes referenced directly via `shape=mxgraph.aws3d.<name>`, unlike `aws4`'s two-pattern system.
- Shape names are **camelCase**, e.g. `dynamoDb` not `dynamodb`, `internetGateway` not `internet_gateway`.

## Verified shape table

| resIcon suffix | Display Name | Extra style properties | Size (w x h) |
|---|---|---|---|
| `client` | Client | `strokeColor=none;fillColor=#777777;aspect=fixed;` | 60 x 104 |
| `end_user` | User (person) | `strokeColor=none;fillColor=#777777;aspect=fixed;` | 49 x 100 |
| `mobile_worker` | Mobile Worker | `strokeColor=none;fillColor=#777777;aspect=fixed;` | 36 x 90 |
| `image` | Image/Video | `strokeColor=none;fillColor=#777777;aspect=fixed;` | 50 x 86 |
| `lambda` | **Lambda** | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;strokeColor3=#ffffff;aspect=fixed;` | 92 x 109 |
| `dynamoDb` | **DynamoDB** | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 182 x 210 |
| `rds` | RDS | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;strokeColor3=#ffffff;aspect=fixed;` | 123 x 133 |
| `rdsMaster` | RDS Master | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 133 |
| `rdsSlave` | RDS Slave | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 133 |
| `simpleDb` | SimpleDB | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 133 |
| `simpleDb2` | SimpleDB (alt) | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 182 x 193 |
| `redshift` | Redshift | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 150 x 190 |
| `s3` | S3 | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 232 x 239 |
| `s3Bucket` | S3 Bucket | `fillColor=#4286c5;strokeColor=#57A2D8;strokeColor2=#292929;aspect=fixed;` | 62 x 64 |
| `glacier` | Glacier | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 181 x 192 |
| `ebs` / `ebs2` | EBS | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 92 x 60 |
| `snapshot` | Snapshot | `fillColor=#4286c5;strokeColor=#57A2D8;strokeColor2=#292929;aspect=fixed;` | 92 x 60 |
| `ami` | AMI | `fillColor=#E8CA45;strokeColor=#FFF215;strokeColor2=#292929;aspect=fixed;` | 92 x 60 |
| `ami2` | AMI (alt) | `fillColor=#FF9900;strokeColor=#ffffff;strokeColor2=#292929;aspect=fixed;` | 74 x 50 |
| `application_server` | EC2 Instance | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 124 |
| `instance` | Spot Instance | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 97 |
| `elasticBeanstalk` | Elastic Beanstalk | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 182 x 140 |
| `elasticLoadBalancing` | Elastic Load Balancing | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 92 x 88 |
| `elasticMapReduce` | Elastic MapReduce | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 133 |
| `elasticache` | ElastiCache | Composite (4 stacked `application_server` cells) — use `createVertexTemplateFromCells` pattern or approximate with one `application_server` cell if a single icon is acceptable | 264 x 204 |
| `sqs` | SQS | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 184 x 213 |
| `email` | Email | `strokeColor=#292929;aspect=fixed;` | 43 x 57 |
| `email_service` | Email Service (SES) | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 151 x 192 |
| `route53` | Route 53 | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 117 x 134 |
| `cloudfront` | CloudFront | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 104 x 170 |
| `internetGateway` | Internet Gateway *(also usable as an API Gateway stand-in — see Gaps below)* | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 117 x 103 |
| `vpcGateway` | VPC Gateway | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 117 x 103 |
| `customerGateway` | Customer Gateway | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 117 x 103 |
| `dataCenter` | Data Center | `strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 142 |
| `dataServer` | Data Server | `strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 123 x 106 |
| `oracleDataCenter` | Oracle Data Center | `fillColor=#ffffff;strokeColor=#5E5E5E;strokeColor2=#292929;fillColor2=#ff0000;fillColor3=#ffffff;aspect=fixed;` | 123 x 142 |
| `oracleDbServer` | Oracle Database Server | `fillColor=#ffffff;strokeColor=#5E5E5E;strokeColor2=#292929;fillColor2=#ff0000;fillColor3=#ffffff;aspect=fixed;` | 123 x 133 |
| `oracleServer` | Oracle Server | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;fillColor2=#ff0000;fillColor3=#ffffff;aspect=fixed;` | 123 x 142 |
| `searchEngine` | Search Engine (CloudSearch) | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 180 x 192 |
| `securityTokenService` | Security Token Service (STS) | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 180 x 192 |
| `secureConnection` | Secure Connection (VPN) | `fillColor=#000000;strokeColor=#ffffff;aspect=fixed;` | 57 x 34 |
| `decider` | SWF Decider | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 74 x 50 |
| `worker` | SWF Worker | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 74 x 50 |
| `workflowService` | SWF Workflow Service | `fillColor=#ECECEC;strokeColor=#5E5E5E;strokeColor2=#292929;aspect=fixed;` | 182 x 148 |
| `application` | Application | `fillColor=#4286c5;strokeColor=#57A2D8;strokeColor2=#292929;aspect=fixed;` | 62 x 69 |
| `application2` | Application (alt) | `fillColor=#86E83A;strokeColor=#B0F373;strokeColor2=#292929;aspect=fixed;` | 62 x 53 |
| `file` | File / Content | `strokeColor=#292929;aspect=fixed;` (or `strokeColor=#2d6195;fillColor=#ffffff;` for the "Content" variant) | 31 x 71 |

## Decorative 3D arrows and connectors

Standalone chevron/edge **shapes** (not edge marker styles) that can be placed near a connector to reinforce direction, matching the original AWS reference-architecture look:

| suffix | Meaning | Style | Size |
|---|---|---|---|
| `arrowNE` / `arrowSE` / `arrowSW` / `arrowNW` | Solid directional 3D arrow | `fillColor=#000000;aspect=fixed;` | 46 x 26 |
| `arrowlessNE` | Directional edge without arrowhead | `fillColor=#000000;aspect=fixed;` | 32 x 18 |
| `arrowhead2` | Small arrowhead only | `fillColor=#000000;aspect=fixed;` | 19 x 11 |
| `edge2` | Plain 3D edge segment | `strokeColor=#000000;aspect=fixed;` | 97 x 107 |
| `dashedEdge2` / `dashedEdgeDouble2` / `dashedArrowlessEdge2` | Dashed variants | `strokeColor=#2D6195;aspect=fixed;` | 32 x 18 |
| `flatEdge2` / `flatDoubleEdge2` | Flat ribbon connector | `strokeColor=none;fillColor=#F4B934;aspect=fixed;` | 63x36 / 253x144 |
| `reference2` | Reference marker | `fillColor=#2d6195;strokeColor=none;aspect=fixed;` | 30 x 20 |
| `spot2` | Spot marker | `fillColor=#F4B934;strokeColor=none;aspect=fixed;` | 62 x 36 |

**Placing these precisely (rotation, exact midpoint of a bent isometric edge) generally requires visual iteration in draw.io — don't try to hand-compute exact placement on a bent path.** Prefer the edge-style approach below unless you can render and check the result.

## Edges: use the native isometric edge style

draw.io ships two ready-made edge templates specifically for this library:

```
edgeStyle=isometricEdgeStyle;endArrow=none;html=1;
edgeStyle=isometricEdgeStyle;endArrow=none;html=1;elbow=vertical;
```

Notes:
- `isometricEdgeStyle` is a real, native mxGraph edge routing style — it bends the connector along true isometric axes instead of routing orthogonally. This is what makes an arrow read as "isometric," not a rotated straight line.
- The stock templates use `endArrow=none` (the original AWS3D deck relied on the decorative arrow shapes above for direction). For diagrams you can't visually re-render and fix, it's more reliable to override with a normal arrowhead — e.g. `endArrow=block;startArrow=none;` — so direction is guaranteed correct without needing exact placement of a separate decorative shape.
- `elbow=vertical` vs the default (horizontal-first) changes which axis the bend happens on first — pick whichever avoids routing through an icon, same judgment call as `orthogonalEdgeStyle`.
- **Keep the edge a single straight-looking segment**: make every node's placement delta from its connected neighbor an exact multiple of the same isometric step vector (e.g. always `dx=+400, dy=-200`, never a slightly different ratio for one hop). A consistent step vector is what makes `isometricEdgeStyle` render as one clean diagonal instead of a visible dogleg. See "Visual Quality" in the base SKILL.md for the general straight-arrows/no-overlap rules this library inherits.

## Layout for 3D/isometric diagrams

These icons already look three-dimensional on their own — unlike a hand-built fake-isometric layout, you do **not** need platform/pedestal shapes underneath them.
- Arrange services along an ascending isometric staircase (each next node offset diagonally, e.g. `dx=+400, dy=-200` from the previous one) so the flow reads left-to-right while staying visually 3D.
- Icon sizes vary a lot in this library (a `client` is 60x104, `dynamoDb` is 182x210) — anchor each icon by its **bottom-center** point on a shared "ground line" per diagonal step, not by top-left corner, so bases line up visually despite the size differences.
- Keep the same title/legend/companion-`.md` conventions as the standard flow.

## Gaps and substitutions

When a requested service has no icon in this library, do not invent a stencil name. Either:
1. Flag it to the user and ask whether to substitute a conceptually-close icon (and label it clearly, noting the substitution in the diagram legend and companion `.md`), or
2. Fall back to the modern `aws4` icon for just that one service (mixing libraries is visually inconsistent but better than a guessed/broken icon), or
3. Use a plain labeled 3D-ish placeholder (e.g. `application_server` or `dataServer`) with a clear label, or a generic device icon from `aws-icons-allied-telesis.md` if it's hardware-shaped (servers, racks, network gear).

Known common gaps and reasonable stand-ins:

| Requested (no aws3d icon) | Suggested stand-in | Caveat |
|---|---|---|
| API Gateway | `internetGateway` | Conceptually a stretch — flag it in the diagram |
| ECS / EKS / Fargate / containers | `application_server`, or Allied Telesis `storage/Datacenter_Server_Rack.svg` | Generic box, not container-specific |
| SNS / EventBridge / Step Functions | none good | Prefer falling back to the `aws4` icon for just this node |
| Aurora / Neptune / DocumentDB | `rds` | Generic RDS box, not engine-specific |
| CloudWatch / IAM / KMS / Cognito / WAF | none | Prefer falling back to the `aws4` icon for just this node |
| Generic on-prem server / EC2 host | Allied Telesis `computer_and_terminals/Server_Desktop.svg` or `storage/Datacenter_Server_Rack.svg` | Better visual fit than `aws3d.application_server` for a plain "server" node |
| Network switch / router / VPN / load balancer hardware | Allied Telesis `switch/*` or `security/Router_VPN.svg` | Neither AWS library has real network hardware icons |

## Source of truth
Verified against: `https://raw.githubusercontent.com/jgraph/drawio/master/src/main/webapp/js/diagramly/sidebar/Sidebar-AWS3D.js`. If a future diagram needs a shape not listed here, re-fetch that file and grep it directly rather than guessing.
