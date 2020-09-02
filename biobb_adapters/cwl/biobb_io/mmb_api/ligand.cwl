#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ligand
hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_io:latest
inputs:
  output_pdb_path:
    type: string
    inputBinding:
      position: 1
      prefix: --output_pdb_path
    default: "downloaded_ligand.pdb"

  config:
    type: string?
    inputBinding:
      position: 1
      prefix: --config
    default: "{\"ligand_code\" : \"12D\"}"
outputs:
  output_pdb_file:
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)

$namespaces:
  edam: http://edamontology.org/
$schemas:
  - http://edamontology.org/EDAM_1.22.owl
