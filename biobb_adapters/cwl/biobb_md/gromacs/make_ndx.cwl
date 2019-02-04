#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: make_ndx
hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:0.1.4--py_0
inputs:
  input_structure_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_structure_path

  output_ndx_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_ndx_path
    default: "custom_index.ndx"

  input_ndx_path:
    type: File?
    inputBinding:
      prefix: --input_ndx_path

  config:
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_ndx_file:
    type: File
    outputBinding:
      glob: $(inputs.output_ndx_path)
