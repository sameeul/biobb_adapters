#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the AsiteDesign module.

doc: |-
  repository combines the PyRosetta modules with enhanced sampling techniques to design both the catalytic and non-catalytic residues in given active sites.

baseCommand: asitedesign

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_asitedesign:4.0.0--pyhdfd78af_1

inputs:
  input_pdb:
    label: Path to the input file pdb
    doc: |-
      Path to the input file pdb
      Type: string
      File type: input
      Accepted formats: PDB
      Example file: null
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_pdb

  input_yaml:
    label: Path to the input file yaml
    doc: |-
      Path to the input file yaml
      Type: string
      File type: input
      Accepted formats: YAML
      Example file: null
    type: File
    format:
    - edam:format_3750
    inputBinding:
      position: 2
      prefix: --input_yaml

  params_folder:
    label: Path to the params folder
    doc: |-
      Path to the params folder
      Type: string
      File type: input
      Accepted formats: PARAMS
      Example file: null
    type: File
    format:
    - edam:format_
    inputBinding:
      position: 3
      prefix: --params_folder

  output_path:
    label: Path to the output file
    doc: |-
      Path to the output file
      Type: string
      File type: output
      Accepted formats: zip
      Example file: null
    type: string
    format:
    - edam:format_3987
    inputBinding:
      position: 4
      prefix: --output_path
    default: system.zip

  config:
    label: Advanced configuration options for biobb_asitedesignsitedesign Asitedesign
    doc: |-
      Advanced configuration options for biobb_asitedesignsitedesign Asitedesign. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_asitedesignsitedesign Asitedesign documentation: https://biobb-asitedesign.readthedocs.io/en/latest/asitedesign.html#module-asitedesign.asitedesign
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_path:
    label: Path to the output file
    doc: |-
      Path to the output file
    type: File
    outputBinding:
      glob: $(inputs.output_path)
    format: edam:format_3987

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
