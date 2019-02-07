#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ndx2resttop
hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:0.1.5--py_0
inputs:
  input_ndx_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_ndx_path

  input_top_zip_path:
    type: File
    inputBinding:
      position: 2
      prefix: --input_top_zip_path

  output_top_zip_path:
    type: string
    inputBinding:
      position: 3
      prefix: --output_top_zip_path
    default: "topology_restrained.zip"

  config:
    type: string?
    inputBinding:
      position: 4
      prefix: --config

outputs:
  output_top_zip_file:
    type: File
    outputBinding:
      glob: $(inputs.output_top_zip_path)
