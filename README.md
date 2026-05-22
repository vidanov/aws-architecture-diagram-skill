# AWS Architecture Diagram Skill

A reusable skill for generating AWS architecture diagrams in draw.io format. Works with both **Kiro CLI** and **Claude Code**.

Generates production-quality `.drawio` files using official AWS Architecture Icons with proper styling, layout, and color coding.

## Features

- **Left-to-right flow** — UI/Frontend on left, data sources on right
- **Official AWS icons** — from draw.io's built-in `mxgraph.aws4` stencil library (sourced from [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/))
- **Verified icon catalog** — only icons confirmed to render correctly
- **Consistent styling** — 78px icons, strokeWidth=2 edges, proper AWS color palette
- **Export support** — PNG/SVG/PDF via draw.io Desktop CLI with embedded XML

## Installation

### Kiro CLI

```bash
# Global (all projects)
mkdir -p ~/.kiro/skills/aws-architecture-diagram
cp kiro/SKILL.md ~/.kiro/skills/aws-architecture-diagram/SKILL.md
cp -r references ~/.kiro/skills/aws-architecture-diagram/references

# Per-project
mkdir -p .kiro/skills/aws-architecture-diagram
cp kiro/SKILL.md .kiro/skills/aws-architecture-diagram/SKILL.md
cp -r references .kiro/skills/aws-architecture-diagram/references
```

### Claude Code

```bash
# Global (all projects)
mkdir -p ~/.claude/skills/aws-architecture-diagram
cp claude/SKILL.md ~/.claude/skills/aws-architecture-diagram/SKILL.md
cp -r references ~/.claude/skills/aws-architecture-diagram/references

# Per-project
mkdir -p .claude/skills/aws-architecture-diagram
cp claude/SKILL.md .claude/skills/aws-architecture-diagram/SKILL.md
cp -r references .claude/skills/aws-architecture-diagram/references
```

## Usage

Just ask to create an AWS architecture diagram:

```
Create an AWS architecture diagram for a serverless API with Lambda, DynamoDB, and API Gateway
```

Or with export:

```
Create an AWS architecture diagram as PNG for a real-time data pipeline with Kinesis, Lambda, and S3
```

## Structure

```
aws-architecture-diagram-skill/
├── README.md
├── LICENSE
├── kiro/
│   └── SKILL.md          # Kiro CLI version
├── claude/
│   └── SKILL.md          # Claude Code version
└── references/
    └── icon-styles.md    # Verified icon catalog & color palette
```

## Supported Services

| Category | Icons |
|----------|-------|
| Compute | Lambda, EC2, ECS, EKS, Fargate |
| App Integration | API Gateway, SNS, SQS, EventBridge, Step Functions |
| Database | DynamoDB, RDS, Aurora, ElastiCache |
| Storage | S3, EFS, EBS |
| Networking | CloudFront, Route 53, VPC, ELB (ALB/NLB) |
| Security | IAM, Cognito, KMS, WAF |

## Known Broken Icons

These `resIcon` values do NOT render in draw.io — avoid them:

- `mxgraph.aws4.dynamodb_table` → use `mxgraph.aws4.dynamodb` instead
- `mxgraph.aws4.dynamodb_stream` → use `mxgraph.aws4.dynamodb` with label
- `mxgraph.aws4.general_saml_token` → use `mxgraph.aws4.traditional_server`

## License

MIT
