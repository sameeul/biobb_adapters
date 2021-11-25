#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the scikit-learn DBSCAN method.

doc: |-
  Clusters a given dataset. Visit the DBSCAN documentation page in the sklearn official website for further information.

baseCommand: dbscan

hints:
  DockerRequirement:
    dockerPull: quay.io/biocontainers/biobb_ml:3.7.0--pyhdfd78af_2

inputs:
  input_dataset_path:
    label: Path to the input dataset
    doc: |-
      Path to the input dataset
      Type: string
      File type: input
      Accepted formats: csv
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/data/clustering/dataset_dbscan.csv
    type: File
    format:
    - edam:format_3752
    inputBinding:
      position: 1
      prefix: --input_dataset_path

  output_results_path:
    label: Path to the clustered dataset
    doc: |-
      Path to the clustered dataset
      Type: string
      File type: output
      Accepted formats: csv
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/clustering/ref_output_results_dbscan.csv
    type: string
    format:
    - edam:format_3752
    inputBinding:
      position: 2
      prefix: --output_results_path
    default: system.csv

  output_plot_path:
    label: Path to the clustering plot
    doc: |-
      Path to the clustering plot
      Type: string
      File type: output
      Accepted formats: png
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/clustering/ref_output_plot_dbscan.png
    type: string
    format:
    - edam:format_3603
    inputBinding:
      prefix: --output_plot_path
    default: system.png

  config:
    label: Advanced configuration options for biobb_ml DBSCANClustering
    doc: |-
      Advanced configuration options for biobb_ml DBSCANClustering. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_ml DBSCANClustering documentation: https://biobb-ml.readthedocs.io/en/latest/clustering.html#module-clustering.dbscan
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_results_path:
    label: Path to the clustered dataset
    doc: |-
      Path to the clustered dataset
    type: File
    outputBinding:
      glob: $(inputs.output_results_path)
    format: edam:format_3752

  output_plot_path:
    label: Path to the clustering plot
    doc: |-
      Path to the clustering plot
    type: File?
    outputBinding:
      glob: $(inputs.output_plot_path)
    format: edam:format_3603

$namespaces:
  edam: http://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
