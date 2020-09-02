#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: acpype_params_gmx_opls
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_chemistry:latest
inputs:
  input_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_path

  output_path_itp:
    type: string
    inputBinding:
      position: 2
      prefix: --output_path_itp
    default: "output.itp"

  output_path_top:
    type: string
    inputBinding:
      position: 3
      prefix: --output_path_top
    default: "output.top"

  config:
    type: string?
    inputBinding:
      position: 4
      prefix: --config

outputs:
  output_file_itp:
    type: File
    outputBinding:
      glob: $(inputs.output_path_itp)

  output_file_top:
    type: File
    outputBinding:
      glob: $(inputs.output_path_top)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
