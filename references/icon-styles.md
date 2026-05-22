# Verified AWS Icon Styles for draw.io

## Source

The `mxgraph.aws4.*` stencil library in draw.io contains the **official AWS Architecture Icons**
(sourced from https://aws.amazon.com/architecture/icons/, updated quarterly).

Two icon patterns:
1. **`shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<name>`** — service icon inside colored square frame
2. **`shape=mxgraph.aws4.<name>`** — bare shape without frame

Pattern 1 is standard for AWS architecture diagrams.

## Verified Working Icons

### resIcon values (inside resourceIcon frame)
- `mxgraph.aws4.lambda` — AWS Lambda
- `mxgraph.aws4.s3` — Amazon S3
- `mxgraph.aws4.sns` — Amazon SNS
- `mxgraph.aws4.sqs` — Amazon SQS (also works as prIcon in productIcon)
- `mxgraph.aws4.eventbridge` — Amazon EventBridge
- `mxgraph.aws4.api_gateway` — Amazon API Gateway
- `mxgraph.aws4.ecs` — Amazon ECS
- `mxgraph.aws4.ec2` — Amazon EC2
- `mxgraph.aws4.route_53` — Amazon Route 53
- `mxgraph.aws4.cloudfront` — Amazon CloudFront
- `mxgraph.aws4.dynamodb` — Amazon DynamoDB
- `mxgraph.aws4.rds` — Amazon RDS
- `mxgraph.aws4.step_functions` — AWS Step Functions

### prIcon values (productIcon — taller box with service header)
- `mxgraph.aws4.sqs` — Amazon SQS

### Standalone shapes (no resIcon needed)
- `mxgraph.aws4.client` — Client/Browser
- `mxgraph.aws4.traditional_server` — Traditional server
- `mxgraph.aws4.generic_firewall` — Firewall
- `mxgraph.aws4.application_load_balancer` — ALB
- `mxgraph.aws4.network_load_balancer` — NLB
- `mxgraph.aws4.endpoints` — VPC Endpoint
- `mxgraph.aws4.s3_file_gateway` — S3 File Gateway
- `mxgraph.aws4.rds_instance` — RDS Instance

### grIcon values (group container icons)
- `mxgraph.aws4.group_account` — AWS Account boundary
- `mxgraph.aws4.group_aws_cloud_alt` — AWS Cloud boundary
- `mxgraph.aws4.group_corporate_data_center` — Corporate/on-premise
- `mxgraph.aws4.group_on_premise` — On-premise

## AWS Color Palette (official category colors)

| Category | fillColor | Services |
|----------|-----------|----------|
| Compute | `#ED7100` | Lambda, EC2, ECS, EKS, Fargate, Batch |
| App Integration | `#E7157B` | SNS, SQS, EventBridge, Step Functions, API Gateway, AppSync |
| Database | `#C925D1` | DynamoDB, RDS, Aurora, ElastiCache, Neptune |
| Storage | `#7AA116` | S3, EFS, EBS, FSx, Backup |
| Networking | `#8C4FFF` | CloudFront, Route 53, VPC, Direct Connect, ELB |
| Security | `#DD344C` | IAM, Cognito, KMS, WAF, Shield |
| Management | `#E7157B` | CloudWatch, CloudFormation, CloudTrail |
| ML/AI | `#01A88D` | SageMaker, Bedrock, Rekognition |
| General/Dark | `#232F3E` | Generic icons, clients, servers |

## Style Templates

### resourceIcon (78x78)
```
sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=<CATEGORY_COLOR>;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<SERVICE_NAME>
```

### productIcon (70x100)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;strokeColor=#ffffff;fillColor=#232F3E;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.productIcon;prIcon=mxgraph.aws4.<SERVICE_NAME>
```

### Standalone shape (78x78)
```
sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.<SHAPE_NAME>
```

### Group/Container
```
points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=1;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.<GROUP_ICON>;strokeColor=<BORDER_COLOR>;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=<BORDER_COLOR>;dashed=0;
```

### Edge
```
edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;
```

## BROKEN Icons (DO NOT USE)

| Icon | Problem | Alternative |
|------|---------|-------------|
| `mxgraph.aws4.dynamodb_table` | Empty colored square | Use `mxgraph.aws4.dynamodb` |
| `mxgraph.aws4.dynamodb_stream` | Empty colored square | Use `mxgraph.aws4.dynamodb` + label |
| `mxgraph.aws4.general_saml_token` | Black square | Use `mxgraph.aws4.traditional_server` |
| `mxgraph.aws4.kinesis_data_streams` | Unreliable | Use `mxgraph.aws4.dynamodb` + label |
