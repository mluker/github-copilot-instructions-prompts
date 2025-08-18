# Copilot instructions and prompts

This repo is a hacking ground for prompts and instruction files.

## References

* https://code.visualstudio.com/docs/copilot/copilot-customization


## VSCode prompts

### synth-data

The [synth-data](./.github/prompts/synth-data.prompt.md) prompt is used to generate synthetic data and visualizations based on natural language. I've had good luck using Sonnet 4.

Example prompts:

```text
/synth-data chicago parking meters over the last 6 months
/synth-data cats vs dogs in MN
/synth-data cook times for a brisket
/synth-data generate 100 names and addresses for the state of Ohio use JSON
/synth-data 10 key webpages metrics and telemetry
/synth-data create 100 json files with data about open source projects
```