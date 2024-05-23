# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_ser_path = PluginVariable(
    id="input_ser_path",  # ID of the variable, will allow us to identify the value
    name="input_ser_path",  # The name that will appear in the frontend
    description='Path to .ser file with data for single helical parameter',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ser']
)


output_csv_path = PluginVariable(
    id="output_csv_path",  # ID of the variable, will allow us to identify the value
    name="output_csv_path",  # The name that will appear in the frontend
    description='Path to directory where output is saved',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

output_jpg_path = PluginVariable(
    id="output_jpg_path",  # ID of the variable, will allow us to identify the value
    name="output_jpg_path",  # The name that will appear in the frontend
    description='Path to .jpg file where output is saved',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['jpg']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

sequence = PluginVariable(
    id="sequence",
    name="sequence",
    description='Nucleic acid sequence for the input .ser file. Length of sequence is expected to be the same as the total number of columns in the .ser file, minus the index column (even if later on a subset of columns is selected with the *seqpos* option).',
    type=VariableTypes.STRING
)

helpar_name = PluginVariable(
    id="helpar_name",
    name="helpar_name",
    description='helical parameter name to add to plot title.',
    type=VariableTypes.STRING
)

seqpos = PluginVariable(
    id="seqpos",
    name="seqpos",
    description='list of sequence positions (columns indices starting by 0) to analyze.  If not specified it will analyse the complete sequence.',
    type=VariableTypes.ARRAY
)

remove_tmp = PluginVariable(
    id="remove_tmp",
    name="remove_tmp",
    description='Remove temporal files.',
    type=VariableTypes.BOOLEAN
)

restart = PluginVariable(
    id="restart",
    name="restart",
    description='Do not execute if output files exist.',
    type=VariableTypes.BOOLEAN
)

# Define the action that the block will perform
def intraseqcorr_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_ser_path_value = biobb_block.inputs["input_ser_path"]
    
    
    output_csv_path_value = biobb_block.inputs["output_csv_path"]
    
    output_jpg_path_value = biobb_block.inputs["output_jpg_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["sequence"] = biobb_block.variables["sequence"]
    
    properties_values["helpar_name"] = biobb_block.variables["helpar_name"]
    
    properties_values["seqpos"] = biobb_block.variables["seqpos"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("intraseqcorr.json", "w", encoding="utf-8") as f:
        json.dump(properties, f)

    # Get the executable and engine form the config
    executable = biobb_block.config["executable_path"]

    # Copy inputs to the tmp folder
    for key, value in biobb_block.inputs.items():
        if value is not None:
            if Path(value).exists():
                abs_path_out = Path(value).absolute()
                abs_path_name = Path(Path(value).name).absolute()
                if not abs_path_name.samefile(abs_path_out):
                    shutil.copy(value, f"{Path(value).name}")

    # Call the docker biobb tool
    with subprocess.Popen(
        [
            executable,
            "run",
            "-v",
            ".:/tmp",
            "quay.io/biocontainers/biobb_dna:4.1.0--pyhdfd78af_0",
            "intraseqcorr",
            "--config",
            "/tmp/intraseqcorr.json",
            
            "--input_ser_path",
            f"/tmp/{Path(input_ser_path_value).name}",
            
            
            "--output_csv_path",
            f"/tmp/{Path(output_csv_path_value).name}",
            
            "--output_jpg_path",
            f"/tmp/{Path(output_jpg_path_value).name}",
            
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    ) as process:
        if process.stdout is not None:
            for line in process.stdout:
                # printing anything inside the block action will
                # redirect the output to the Horus integrated terminal
                print(line)

        if process.stderr is not None:
            for line in process.stderr:
                print(line)

        process.wait()

        if process.returncode != 0:
            # Raising an exception inside the block action will display the block as with an error,
            # and will display the error inside the block
            raise Exception(
                process.stderr
                if process.stderr
                else "An error ocurred while running the flow"
            )


        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_csv_path_value).absolute()
        abs_path_name = Path(Path(output_csv_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_csv_path_value).name}", output_csv_path_value)
        biobb_block.setOutput("output_csv_path", output_csv_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_jpg_path_value).absolute()
        abs_path_name = Path(Path(output_jpg_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_jpg_path_value).name}", output_jpg_path_value)
        biobb_block.setOutput("output_jpg_path", output_jpg_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_ser_path)


outputs_list.append(output_csv_path)

outputs_list.append(output_jpg_path)


variables_list.append(sequence)

variables_list.append(helpar_name)

variables_list.append(seqpos)

variables_list.append(remove_tmp)

variables_list.append(restart)


intraseqcorr_block = PluginBlock(
    # The name which will appear on the frontend
    name="intraseqcorr",
    # Its description
    description='Calculate correlation between all intra-base pairs of a single sequence and for a single helical parameter.',
    # The action
    action=intraseqcorr_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)