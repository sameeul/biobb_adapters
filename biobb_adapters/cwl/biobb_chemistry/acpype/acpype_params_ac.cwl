#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: acpype_params_ac
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_chemistry:latest
inputs:
  input_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_path

  output_path_frcmod:
    type: string
    inputBinding:
      position: 2
      prefix: --output_path_frcmod
    default: "output.frcmod"

  output_path_inpcrd:
    type: string
    inputBinding:
      position: 3
      prefix: --output_path_inpcrd
    default: "output.inpcrd"

  output_path_lib:
    type: string
    inputBinding:
      position: 4
      prefix: --output_path_lib
    default: "output.lib"

  output_path_prmtop:
    type: string
    inputBinding:
      position: 5
      prefix: --output_path_prmtop
    default: "output.prmtop"

  config:
    type: string?
    inputBinding:
      position: 6
      prefix: --config

outputs:
  output_file_frcmod:
    type: File
    outputBinding:
      glob: $(inputs.output_path_frcmod)

  output_file_inpcrd:
    type: File
    outputBinding:
      glob: $(inputs.output_path_inpcrd)

  output_file_lib:
    type: File
    outputBinding:
      glob: $(inputs.output_path_lib)

  output_file_prmtop:
    type: File
    outputBinding:
      glob: $(inputs.output_path_prmtop)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
