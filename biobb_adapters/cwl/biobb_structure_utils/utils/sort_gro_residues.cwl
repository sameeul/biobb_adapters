#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: sort_gro_residues
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_structure_utils:latest
inputs:
  input_gro_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_gro_path

  output_gro_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_gro_path
    default: "output.gro"

  config:
    type: string?
    inputBinding:
      position: 3
      prefix: --config

outputs:

  output_gro_file:
    type: File
    outputBinding:
      glob: $(inputs.output_gro_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
