# Changelog

## [Unreleased]

### Added
- 3D/isometric diagram support via draw.io's legacy `mxgraph.aws3d.*` icon library (`references/aws-icons-3d.md`), including the native `isometricEdgeStyle` connector guidance and a documented coverage-gap table (this legacy set predates services like API Gateway, ECS/EKS, Step Functions, etc.)
- Bonus generic isometric hardware icons via the bundled Allied Telesis image library (`references/aws-icons-allied-telesis.md`) — clients, servers, server racks, and network hardware — for filling `aws3d` coverage gaps
- General "Visual Quality" layout rules (straight arrows, no overlapping/crossing edges, consistent node alignment and spacing, single-bend-max routing) — applies to every diagram the skill produces, not just 3D ones
- New examples: `examples/example-3d-serverless-api.drawio` and `examples/example-3d-ecommerce-website-architecture.drawio` demonstrating both new icon libraries together, with rendered screenshots in `docs/`

### Notes
- `tests/validate_drawio.py` currently warns on `isometricEdgeStyle` edges for missing `exitX`/`entryX` (Issue #2 check). This is a false positive for that edge style, which computes its own connection points — worth a follow-up to scope that check to `orthogonalEdgeStyle` edges only.

## [1.1.0] - 2026-05-22

### Added
- Audience mode (technical vs non-technical label adjustment)
- Numbered flow edges (① ② ③) for presentation diagrams
- Companion markdown guide generation
- Post-generation validation checklist
- IoT, Migration, Developer Tools icon categories
- CONTRIBUTING.md
- GitHub Actions validation workflow
- Claude Code plugin marketplace structure (one-line install)
- 5 reference architecture templates
- Multi-page diagram support
- Legend/title block standard

### Fixed
- Documented two-pattern rule (service-level vs resource-level strokeColor)
- Added PNG export background fix (#F5F5F5 rectangle)

## [1.0.0] - 2026-05-22

### Added
- Initial release
- 8 category reference files with 270+ verified icons
- Kiro CLI and Claude Code support
- Left-to-right layout rules
- Verified icon catalog extracted from Sidebar-AWS4.js
- Broken icons documentation
