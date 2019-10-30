#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: remove_pdb_water
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_structure_utils:latest
inputs:
  input_pdb_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_pdb_path

  output_pdb_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_pdb_path
    default: "output.pdb"

  config:
    type: string?
    inputBinding:
      position: 3
      prefix: --config

outputs:

  output_pdb_file:
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
