#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: cpptraj_rmsf
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_analysis:latest
inputs:
  input_top_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_top_path

  input_traj_path:
    type: File
    inputBinding:
      position: 2
      prefix: --input_traj_path

  input_exp_path:
    type: File?
    inputBinding:
      position: 3
      prefix: --input_exp_path

  output_cpptraj_path:
    type: string
    inputBinding:
      position: 4
      prefix: --output_cpptraj_path
    default: "output.nc"

  config:
    type: string?
    inputBinding:
      position: 5
      prefix: --config

outputs:
  output_cpptraj_file:
    type: File
    outputBinding:
      glob: $(inputs.output_cpptraj_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
