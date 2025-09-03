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
/synth-data cook times for a brisket, make sure to include the stall
/synth-data generate 100 names and addresses for the state of Ohio use JSON
/synth-data 10 key webpages metrics and telemetry during black friday
/synth-data create 100 json files with data about open source projects
/synth-data generate a ground truth dataset for a 4Runner agent that can answer questions about 2025 Toyota 4Runners. Here is a sample record that demonstrates the schema I want the data produced in: {"context": "Road sign assist uses camera technology to recognize traffic signs and display them on the dashboard for driver awareness.", "question": "How does road sign assist work?", "ground_truth": "Camera recognizes signs, displays on dashboard"}
```