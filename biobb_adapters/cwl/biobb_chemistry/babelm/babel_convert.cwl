#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: babel_convert
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_chemistry:latest
inputs:
  input_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_path

  output_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_path
    default: "output.mol2"

  config:
    type: string?
    inputBinding:
      position: 3
      prefix: --config

outputs:

  output_file:
    type: File
    outputBinding:
      glob: $(inputs.output_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
