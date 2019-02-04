#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: mdrun
hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:0.1.4--py_0
inputs:
  input_tpr_path:
    type: File
    inputBinding:
      position: 1
      prefix: --input_tpr_path

  output_trr_path:
    type: string
    inputBinding:
      position: 2
      prefix: --output_trr_path
    default: "trajectory.trr"

  output_gro_path:
    type: string
    inputBinding:
      position: 3
      prefix: --output_gro_path
    default: "trajectory.gro"

  output_edr_path:
    type: string
    inputBinding:
      position: 4
      prefix: --output_edr_path
    default: "trajectory.edr"

  output_log_path:
    type: string
    inputBinding:
      position: 5
      prefix: --output_log_path
    default: "trajectory.log"

  output_xtc_path:
    type: string?
    inputBinding:
      prefix: --output_xtc_path
    default: "trajectory.xtc"

  output_cpt_path:
    type: string?
    inputBinding:
      prefix: --output_cpt_path

  config:
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_trr_file:
    type: File
    outputBinding:
      glob: $(inputs.output_trr_path)
  output_gro_file:
    type: File
    outputBinding:
      glob: $(inputs.output_gro_path)
  output_edr_file:
    type: File
    outputBinding:
      glob: $(inputs.output_edr_path)
  output_log_file:
    type: File
    outputBinding:
      glob: $(inputs.output_log_path)
  output_xtc_file:
    type: File?
    outputBinding:
      glob: $(inputs.output_xtc_path)
  output_cpt_file:
    type: File?
    outputBinding:
      glob: $(inputs.output_cpt_path)
