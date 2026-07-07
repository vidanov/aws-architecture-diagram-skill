# AWS Architecture Diagram Skill

[![Website](https://img.shields.io/badge/Website-vidanov.github.io-8C4FFF)](https://vidanov.github.io/aws-architecture-diagram-skill/)

![Prompt → AI Agent + Skill → .drawio diagram](docs/hero.png)

A reusable skill for generating AWS architecture diagrams in draw.io format. Works with **any AI assistant** — ChatGPT, Claude Projects, Kiro CLI, Claude Code, or any internal AI agent that supports custom prompts and file uploads.

Generates production-quality `.drawio` files using official AWS Architecture Icons with proper styling, layout, and color coding.

## Features

- **Left-to-right flow** — UI/Frontend on left, data sources on right
- **Official AWS icons** — from draw.io's built-in `mxgraph.aws4` stencil library (sourced from [AWS Architecture Icons](https://aws.amazon.com/architecture/icons/))
- **Verified icon catalog** — only icons confirmed to render correctly
- **Consistent styling** — 78px icons, strokeWidth=2 edges, proper AWS color palette
- **Export support** — PNG/SVG/PDF via draw.io Desktop CLI with embedded XML

## Installation

### Skills CLI (recommended — works with Claude Code, Cursor, Codex, Kiro, and 50+ agents)

```bash
npx skills add vidanov/aws-architecture-diagram-skill
```

Install to a specific agent:

```bash
npx skills add vidanov/aws-architecture-diagram-skill --agent claude-code
npx skills add vidanov/aws-architecture-diagram-skill --agent cursor
npx skills add vidanov/aws-architecture-diagram-skill --agent kiro-cli
```

Install globally (available in all projects):

```bash
npx skills add vidanov/aws-architecture-diagram-skill --global
```

[![skills.sh](https://skills.sh/b/vidanov/aws-architecture-diagram-skill)](https://skills.sh/vidanov/aws-architecture-diagram-skill)

### Any AI Assistant (ChatGPT, Claude Projects, Internal Agents)

No code or CLI required. Works with any AI that supports custom instructions and file uploads:

1. **Copy the prompt** from [`chatgpt/PROMPT.md`](chatgpt/PROMPT.md) into your assistant's system prompt / custom instructions field
2. **Upload the reference files** from [`chatgpt/references/`](chatgpt/references/) to the knowledge base / project files
3. **Start asking** for AWS architecture diagrams

This works with:
- **ChatGPT** → Custom GPT or Project with instructions + files
- **Claude Projects** → Project instructions + project knowledge
- **Internal corporate AI agents** → System prompt + knowledge base uploads
- **Any LLM with file context** → Paste prompt + reference content

> **Tip:** Set temperature to 0.3 for consistent XML output.

### Claude Code (Plugin — recommended)

```bash
/plugin marketplace add vidanov/aws-architecture-diagram-skill
/plugin install aws-architecture-diagram@vidanov-skills
```

Then use it:
```
/aws-architecture-diagram:aws-architecture-diagram
```

Or just ask naturally — the skill activates automatically when you mention AWS architecture diagrams.

### Claude Code (Manual)

```bash
mkdir -p ~/.claude/skills/aws-architecture-diagram
cp claude/SKILL.md ~/.claude/skills/aws-architecture-diagram/SKILL.md
cp -r references ~/.claude/skills/aws-architecture-diagram/references
```

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

## Usage

Just ask to create an AWS architecture diagram:

```
Create an AWS architecture diagram for a serverless API with Lambda, DynamoDB, and API Gateway
```

Or with export:

```
Create an AWS architecture diagram as PNG for a real-time data pipeline with Kinesis, Lambda, and S3
```

## Example Output

### Event-Driven Order Processing
> "Create an event-driven order processing architecture with SQS, Lambda, DynamoDB, and EventBridge"

![Event-Driven Order Processing](docs/example-event-driven.png)
[Download .drawio](examples/example-event-driven.drawio)

### Real-Time IoT Analytics
> "Create a real-time IoT analytics pipeline with Kinesis, Lambda, S3 data lake, and DynamoDB"

![Real-Time IoT Analytics](docs/example-streaming.png)
[Download .drawio](examples/example-streaming.drawio)

### 3-Tier Web Application
> "Create a 3-tier web application with CloudFront, ALB, ECS Fargate, Aurora, and ElastiCache"

![3-Tier Web Application](docs/example-3tier.png)
[Download .drawio](examples/example-3tier.drawio)

## Structure

```
aws-architecture-diagram-skill/
├── README.md
├── LICENSE
├── chatgpt/
│   ├── PROMPT.md                       # Universal prompt (ChatGPT, Claude Projects, any AI)
│   └── references/                     # Same icons in .txt format for upload
│       ├── aws-icons-common.txt
│       ├── aws-icons-compute.txt
│       ├── aws-icons-database.txt
│       ├── aws-icons-integration.txt
│       ├── aws-icons-networking.txt
│       ├── aws-icons-storage.txt
│       ├── aws-icons-security.txt
│       ├── aws-icons-analytics-ml.txt
│       └── aws-icons-iot-migration-devtools.txt
├── kiro/
│   └── SKILL.md                        # Kiro CLI version
├── claude/
│   └── SKILL.md                        # Claude Code version
└── references/
    ├── aws-icons-compute.md            # Lambda, EC2, ECS, EKS, Fargate (25+ icons)
    ├── aws-icons-database.md           # DynamoDB, RDS, Aurora, ElastiCache (40+ icons)
    ├── aws-icons-integration.md        # API GW, SQS, SNS, EventBridge, Step Functions (35+ icons)
    ├── aws-icons-networking.md         # CloudFront, Route 53, VPC, ELB (40+ icons)
    ├── aws-icons-storage.md            # S3, EFS, EBS, Glacier, Backup (40+ icons)
    ├── aws-icons-security.md           # IAM, Cognito, KMS, WAF, Shield (45+ icons)
    ├── aws-icons-analytics-ml.md       # Kinesis, Athena, Bedrock, SageMaker (45+ icons)
    └── aws-icons-common.md             # Groups, general resources, edge styles, base template
```

## Key Insight: Two Icon Patterns

draw.io AWS icons have **two patterns** with opposite `strokeColor` rules:

| Pattern | Style | strokeColor | Use for |
|---------|-------|-------------|---------|
| Service-level | `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<name>` | `#ffffff` (REQUIRED) | Main service icons (colored square + white glyph) |
| Resource-level | `shape=mxgraph.aws4.<name>` | `none` (REQUIRED) | Sub-resources (silhouette icons) |

**Confusing these patterns is the #1 cause of broken icons in AI-generated diagrams.**

## Key Insight: Legacy Stencil Names

draw.io stencil names don't always match current AWS service names. Renamed services keep their old stencil identifiers:

| AWS Service | draw.io `resIcon` | Reason |
|---|---|---|
| Amazon OpenSearch Service | `elasticsearch_service` | Renamed from Elasticsearch (2021) |

**Empty icon = wrong stencil name.** The skill includes a verified icon catalog to prevent this.

## Two-Step Edit Approach

The skill instructs the AI agent to:
1. Generate the `.drawio` XML
2. Export to PNG and visually review for broken icons or layout issues
3. Fix and re-export

This catches rendering problems that are invisible in raw XML.

## Supported Services (110+ icons)

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

---

## Comparison with Alternatives

| Solution | Type | Output | Editable | Zero-deps | Verified Icons |
|----------|------|--------|----------|-----------|----------------|
| **[aws-architecture-diagram-skill](https://github.com/vidanov/aws-architecture-diagram-skill)** | Agent Skill | `.drawio` | ✅ | ✅ | ✅ |
| [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp) | MCP Server + Skill | `.drawio` | ✅ | ❌ (MCP) | ❌ |
| [awslabs/aws-diagram-mcp-server](https://pypi.org/project/awslabs.aws-diagram-mcp-server/) | MCP Server (Python) | PNG | ❌ | ❌ (Python+GraphViz) | N/A |
| [awslabs/diagram-as-code](https://github.com/awslabs/diagram-as-code) | CLI (Go) | PNG/SVG | ❌ | ❌ (Go binary) | N/A |
| [carlosmgv02/diagram-ai-generator](https://github.com/carlosmgv02/diagram-ai-generator) | MCP Server | Multi-cloud | ❌ | ❌ (MCP) | ❌ |
| [clouda.ai](https://clouda.ai/) | SaaS | PNG | ❌ | N/A | N/A |

**Why this approach wins:**
- No runtime dependencies. It's a markdown file, not a server.
- Output is native `.drawio` XML you can open, edit, and version-control.
- Verified icon catalog documents which `mxgraph.aws4.*` names actually render vs. silently break.
- Opinionated layout: left-to-right flow with consistent spacing, not random placement.
- Works with any AI assistant: ChatGPT, Claude, Kiro CLI, or internal corporate agents.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** this repository
2. **Create a branch** for your feature or fix (`git checkout -b my-feature`)
3. **Make your changes** — add icons, fix stencil names, improve layout rules, etc.
4. **Submit a Pull Request** with a clear description of what you changed and why

You can also **open an Issue** if you:
- Found a broken icon or wrong stencil name
- Want to request support for a new AWS service
- Have suggestions for layout or styling improvements
- Encountered a bug with a specific AI agent

## License

MIT

---

If this saved you a diagramming session, a star ⭐ helps the next person find it.

## Also by the author

- [writing-craft-skill](https://github.com/vidanov/writing-craft-skill): teach AI agents to write well using classic copywriting craft plus AI anti-pattern detection
- [shape](https://github.com/vidanov/shape): runtime governance for AI agents (phases, transactions, budget gates, proof traces)
