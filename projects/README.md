# Projects

Projects are goal-oriented research efforts that pull papers from multiple [domains](../domains/). Each project file maps current research questions to relevant literature entries.

## Active Projects

| Project | Goal | Related Domains | Lead |
|---------|------|-----------------|------|
| [ocean-sr](ocean-sr.md) | Super-resolution for ocean remote sensing variables | ocean-forecasting, scientific-sr | @lkun45598-lgtm |
| [chl-sr-reliability](chl-sr-reliability.md) | Chlorophyll-a SR with calibrated uncertainty | scientific-sr, uncertainty-calibration | @lkun45598-lgtm |
| [agent-loss-migration](agent-loss-migration.md) | Agent-assisted loss function migration | code-agent | @lkun45598-lgtm |

## How Papers Connect to Projects

Every paper entry has a `projects` field in its YAML front matter. Use this to trace which papers are relevant to which projects. The project files below provide curated views with must-read lists, supplementary references, and identified gaps.

## Adding a New Project

1. Create `projects/<project-slug>.md` following the structure of existing project files
2. Add the project to the table above
3. Update `CODEOWNERS` to assign an owner
4. Add the project slug to the `paper_ingest.yml` issue template dropdown
