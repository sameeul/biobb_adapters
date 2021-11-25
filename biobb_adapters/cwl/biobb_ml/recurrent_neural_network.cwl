#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Wrapper of the TensorFlow Keras LSTM method using Recurrent Neural Networks.

doc: |-
  Trains and tests a given dataset and save the complete model for a Recurrent Neural Network. Visit the LSTM documentation page in the TensorFlow Keras official website for further information.

baseCommand: recurrent_neural_network

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
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/data/neural_networks/dataset_recurrent.csv
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
      Accepted formats: h5
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/neural_networks/ref_output_model_recurrent.h5
    type: string
    format:
    - edam:format_3590
    inputBinding:
      position: 2
      prefix: --output_model_path
    default: system.h5

  output_test_table_path:
    label: Path to the test table file
    doc: |-
      Path to the test table file
      Type: string
      File type: output
      Accepted formats: csv
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/neural_networks/ref_output_test_recurrent.csv
    type: string
    format:
    - edam:format_3752
    inputBinding:
      prefix: --output_test_table_path
    default: system.csv

  output_plot_path:
    label: Loss, accuracy and MSE plots
    doc: |-
      Loss, accuracy and MSE plots
      Type: string
      File type: output
      Accepted formats: png
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/neural_networks/ref_output_plot_recurrent.png
    type: string
    format:
    - edam:format_3603
    inputBinding:
      prefix: --output_plot_path
    default: system.png

  config:
    label: Advanced configuration options for biobb_ml RecurrentNeuralNetwork
    doc: |-
      Advanced configuration options for biobb_ml RecurrentNeuralNetwork. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_ml RecurrentNeuralNetwork documentation: https://biobb-ml.readthedocs.io/en/latest/neural_networks.html#module-neural_networks.recurrent_neural_network
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
    format: edam:format_3590

  output_test_table_path:
    label: Path to the test table file
    doc: |-
      Path to the test table file
    type: File?
    outputBinding:
      glob: $(inputs.output_test_table_path)
    format: edam:format_3752

  output_plot_path:
    label: Loss, accuracy and MSE plots
    doc: |-
      Loss, accuracy and MSE plots
    type: File?
    outputBinding:
      glob: $(inputs.output_plot_path)
    format: edam:format_3603

$namespaces:
  edam: http://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
