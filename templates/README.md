# Architecture Templates

Ready-to-use draw.io templates following the skill's style rules. Use these as starting points or reference for icon placement and styling.

## Available Templates

| Template | Pattern | Services Used |
|----------|---------|---------------|
| `serverless-rest-api.drawio` | Serverless API | CloudFront → API Gateway → Lambda → DynamoDB + S3 + Cognito |
| `event-driven-processing.drawio` | Event-Driven | EventBridge → SQS/SNS/Step Functions → Lambda → DynamoDB |

## How to Use

1. Copy a template as starting point
2. Modify services, labels, and connections
3. Add/remove lanes as needed

## Style Conventions in Templates

- Background: `#F5F5F5` rectangle (prevents black on PNG export)
- Left-to-right flow
- 78x78 service icons
- strokeWidth=2 edges
- All groups use `fillColor=none`
