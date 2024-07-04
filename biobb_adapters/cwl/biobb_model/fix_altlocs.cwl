#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Fix alternate locations from residues.

doc: |-
  Fix alternate locations using the altlocs list or occupancy.

baseCommand: fix_altlocs

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_model:4.2.3--pyhdfd78af_0

inputs:
  input_pdb_path:
    label: Input PDB file path
    doc: |-
      Input PDB file path
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: https://github.com/bioexcel/biobb_model/raw/master/biobb_model/test/data/model/3ebp.pdb
    type: File
    format:
    - edam:format_1476
    inputBinding:
      position: 1
      prefix: --input_pdb_path

  output_pdb_path:
    label: Output PDB file path
    doc: |-
      Output PDB file path
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://raw.githubusercontent.com/bioexcel/biobb_model/master/biobb_model/test/reference/model/output_altloc.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      position: 2
      prefix: --output_pdb_path
    default: system.pdb

  config:
    label: Advanced configuration options for biobb_model FixAltLocs
    doc: |-
      Advanced configuration options for biobb_model FixAltLocs. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_model FixAltLocs documentation: https://biobb-model.readthedocs.io/en/latest/model.html#module-model.fix_altlocs
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_pdb_path:
    label: Output PDB file path
    doc: |-
      Output PDB file path
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
