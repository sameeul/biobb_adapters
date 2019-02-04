#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: grompp
hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:0.1.4--py_0
inputs:
  input_gro_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_gro_path

  input_top_zip_path:
    type: File
    inputBinding:
      position: 2
      prefix: --input_top_zip_path

  output_tpr_path:
    type: string
    inputBinding:
      position: 3
      prefix: --output_tpr_path
    default: "system.tpr"

  input_cpt_path:
    type: File?
    inputBinding:
      prefix: --input_cpt_path

  config:
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_tpr_file:
    type: File
    outputBinding:
      glob: $(inputs.output_tpr_path)
