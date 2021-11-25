#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the scikit-learn RandomForestClassifier method.

doc: |-
  Trains and tests a given dataset and saves the model and scaler. Visit the RandomForestClassifier documentation page in the sklearn official website for further information.

baseCommand: random_forest_classifier

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
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/data/classification/dataset_random_forest_classifier.csv
    type: File
    format:
    - edam:format_3752
    inputBinding:
      position: 1
      prefix: --input_dataset_path

  output_model_path:
    label: Path to the output model file
    doc: |-
      Path to the output model file
      Type: string
      File type: output
      Accepted formats: pkl
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_model_random_forest_classifier.pkl
    type: string
    format:
    - edam:format_3653
    inputBinding:
      position: 2
      prefix: --output_model_path
    default: system.pkl

  output_test_table_path:
    label: Path to the test table file
    doc: |-
      Path to the test table file
      Type: string
      File type: output
      Accepted formats: csv
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_test_random_forest_classifier.csv
    type: string
    format:
    - edam:format_3752
    inputBinding:
      prefix: --output_test_table_path
    default: system.csv

  output_plot_path:
    label: Path to the statistics plot. If target is binary it shows confusion matrix,
      distributions of the predicted probabilities of both classes and ROC curve.
      If target is non-binary it shows confusion matrix
    doc: |-
      Path to the statistics plot. If target is binary it shows confusion matrix, distributions of the predicted probabilities of both classes and ROC curve. If target is non-binary it shows confusion matrix
      Type: string
      File type: output
      Accepted formats: png
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_plot_random_forest_classifier.png
    type: string
    format:
    - edam:format_3603
    inputBinding:
      prefix: --output_plot_path
    default: system.png

  config:
    label: Advanced configuration options for biobb_ml RandomForestClassifier
    doc: |-
      Advanced configuration options for biobb_ml RandomForestClassifier. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_ml RandomForestClassifier documentation: https://biobb-ml.readthedocs.io/en/latest/classification.html#module-classification.random_forest_classifier
    type: string?
    inputBinding:
      prefix: --config

outputs:
  output_model_path:
    label: Path to the output model file
    doc: |-
      Path to the output model file
    type: File
    outputBinding:
      glob: $(inputs.output_model_path)
    format: edam:format_3653

  output_test_table_path:
    label: Path to the test table file
    doc: |-
      Path to the test table file
    type: File?
    outputBinding:
      glob: $(inputs.output_test_table_path)
    format: edam:format_3752

  output_plot_path:
    label: Path to the statistics plot. If target is binary it shows confusion matrix,
      distributions of the predicted probabilities of both classes and ROC curve.
      If target is non-binary it shows confusion matrix
    doc: |-
      Path to the statistics plot. If target is binary it shows confusion matrix, distributions of the predicted probabilities of both classes and ROC curve. If target is non-binary it shows confusion matrix
    type: File?
    outputBinding:
      glob: $(inputs.output_plot_path)
    format: edam:format_3603

$namespaces:
  edam: http://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
