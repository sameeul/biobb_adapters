#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the GROMACS solvate module.

doc: |-
  The GROMACS solvate module, generates a box of solvent around the selected structure.

baseCommand: solvate

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:3.7.2--pyhdfd78af_0

inputs:
  input_solute_crd_path:
    label: Path to the input GRO file
    doc: |-
      Path to the input GRO file
      Type: string
      File type: input
      Accepted formats: gro, pdb
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/solvate.gro
    type: File
    format:
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_solute_gro_path

  output_crd_path:
    label: Path to the output GRO file
    doc: |-
      Path to the output GRO file
      Type: string
      File type: output
      Accepted formats: gro, pdb
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_solvate.gro
    type: string
    format:
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_gro_path
#    default: system.gro
    default: system.g96

  input_top_zip_path:
    label: Path the input TOP topology in zip format
    doc: |-
      Path the input TOP topology in zip format
      Type: string
      File type: input
      Accepted formats: zip
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/solvate.zip
    type: File
    format:
    - edam:format_3987
    inputBinding:
      position: 3
      prefix: --input_top_zip_path

  output_top_zip_path:
    label: Path the output topology in zip format
    doc: |-
      Path the output topology in zip format
      Type: string
      File type: output
      Accepted formats: zip
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_solvate.zip
    type: string
    format:
    - edam:format_3987
    inputBinding:
      position: 4
      prefix: --output_top_zip_path
    default: system.zip

  input_solvent_crd_path:
    label: (spc216.gro) Path to the GRO file containing the structure of the solvent
    doc: |-
      (spc216.gro) Path to the GRO file containing the structure of the solvent
      Type: string
      File type: input
      Accepted formats: gro
      Example file: null
    type: File?
    format:
    - edam:format_2033
    inputBinding:
      prefix: --input_solvent_gro_path

  config:
    label: Advanced configuration options for biobb_md Solvate
    doc: |-
      Advanced configuration options for biobb_md Solvate. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_md Solvate documentation: https://biobb-md.readthedocs.io/en/latest/gromacs.html#module-gromacs.solvate
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_crd_path:
    label: Path to the output GRO file
    doc: |-
      Path to the output GRO file
    type: File
    outputBinding:
      glob: $(inputs.output_crd_path)
    format: edam:format_2033

  output_top_zip_path:
    label: Path the output topology in zip format
    doc: |-
      Path the output topology in zip format
    type: File
    outputBinding:
      glob: $(inputs.output_top_zip_path)
    format: edam:format_3987

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
