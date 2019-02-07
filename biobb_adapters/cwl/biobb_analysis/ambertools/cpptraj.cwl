#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: biobb_cpptraj
hints:
  DockerRequirement:
    dockerPull: mmbirb/biobb_analysis:0.1.3
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

  output_dat_path:
    type: string
    inputBinding:
      position: 3
      prefix: --output_dat_path
    default: "output_dat.dat"

  output_traj_path:
    type: string?
    inputBinding:
      prefix: --output_traj_path

  config:
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_dat_file:
    type: File
    outputBinding:
      glob: $(inputs.output_dat_path)
  output_traj_file:
    type: File?
    outputBinding:
      glob: $(inputs.output_traj_path)
