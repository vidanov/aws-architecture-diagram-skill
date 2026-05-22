# Contributing

Thanks for your interest in improving this skill. Here's how to help.

## Adding new icons

1. Open draw.io, search for the AWS service in the shape panel
2. Drag it onto the canvas, then right-click → "Edit Style"
3. Note the `resIcon=` or `shape=` value and the `fillColor`
4. Add it to the appropriate `references/aws-icons-*.md` file
5. Specify whether it's service-level (`resIcon`) or resource-level (standalone `shape`)
6. Include the correct `strokeColor` (`#ffffff` for service-level, `none` for resource-level)

## Testing templates

1. Open any `.drawio` template in draw.io (app.diagrams.net or desktop app)
2. Verify all icons render correctly (no empty squares)
3. Export to PNG and check for black background areas
4. If issues found, open an issue with a screenshot

## Submitting changes

1. Fork the repo
2. Create a branch (`git checkout -b add-kinesis-icons`)
3. Make your changes
4. Test by installing locally:
   - Claude Code: `/plugin marketplace add ./your-fork`
   - Kiro CLI: copy to `~/.kiro/skills/aws-architecture-diagram/`
5. Open a PR with:
   - What you added/changed
   - Screenshot showing icons render correctly

## Style rules for templates

- Left-to-right flow
- 78x78 icons (service-level) or 48x48 (resource-level)
- `strokeWidth=2` on all edges
- `fillColor=none` on all group containers
- Include `#F5F5F5` background rectangle
- No XML comments

## Reporting broken icons

If you find an icon that doesn't render, open an issue with:
- The `resIcon` or `shape` value you tried
- What it renders as (screenshot)
- The draw.io version you're using
