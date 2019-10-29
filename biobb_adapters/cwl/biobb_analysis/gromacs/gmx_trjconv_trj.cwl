#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: gmx_trjconv_trj
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_analysis:latest
inputs:
  input_traj_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_traj_path

  input_index_path:
    type: File?
    inputBinding:
      position: 2
      prefix: --input_index_path

  output_traj_path:
    type: string
    inputBinding:
      position: 3
      prefix: --output_traj_path
    default: "output.xtc"

  config:
    type: string?
    inputBinding:
      position: 4
      prefix: --config

outputs:
  output_traj_file:
    type: File
    outputBinding:
      glob: $(inputs.output_traj_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
