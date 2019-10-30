#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: renumber_structure
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_structure_utils:latest
inputs:
  input_structure_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_structure_path

  output_structure_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_structure_path
    default: "output.pdb"

  output_mapping_json_path:
    type: string
    inputBinding:
      position: 3
      prefix: --output_mapping_json_path
    default: "output.json"

  config:
    type: string?
    inputBinding:
      position: 4
      prefix: --config

outputs:

  output_structure_file:
    type: File
    outputBinding:
      glob: $(inputs.output_structure_path)

  output_mapping_json_file:
    type: File
    outputBinding:
      glob: $(inputs.output_mapping_json_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
