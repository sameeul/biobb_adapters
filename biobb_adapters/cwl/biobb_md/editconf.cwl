#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper class for the GROMACS editconf module.

doc: |-
  The GROMACS solvate module generates a box around the selected structure.

baseCommand: editconf

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_md:3.7.2--pyhdfd78af_0

inputs:
  input_crd_path:
    label: Path to the input GRO file
    doc: |-
      Path to the input GRO file
      Type: string
      File type: input
      Accepted formats: gro, pdb
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/editconf.gro
    type: File
    format:
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_gro_path

  output_crd_path:
    label: Path to the output GRO file
    doc: |-
      Path to the output GRO file
      Type: string
      File type: output
      Accepted formats: pdb, gro
      Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_editconf.gro
    type: string
    format:
    - edam:format_2033
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_gro_path
#    default: system.pdb
#    default: system.gro
    default: system.g96
  config:
    label: Advanced configuration options for biobb_md Editconf
    doc: |-
      Advanced configuration options for biobb_md Editconf. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_md Editconf documentation: https://biobb-md.readthedocs.io/en/latest/gromacs.html#module-gromacs.editconf
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
#    format: edam:format_1476
    format: edam:format_2033

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
