# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_csv_file = PluginVariable(
    id="input_csv_file",  # ID of the variable, will allow us to identify the value
    name="input_csv_file",  # The name that will appear in the frontend
    description='Path to .csv file with helical parameter series. If `input_zip_file` is passed, this should be just the filename of the .csv file inside .zip',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

input_zip_file = PluginVariable(
    id="input_zip_file",  # ID of the variable, will allow us to identify the value
    name="input_zip_file",  # The name that will appear in the frontend
    description='.zip file containing the `input_csv_file` .csv file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)


output_csv_path = PluginVariable(
    id="output_csv_path",  # ID of the variable, will allow us to identify the value
    name="output_csv_path",  # The name that will appear in the frontend
    description='Path to .csv file where output is saved',  # The description that will appear in the frontend
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

helpar_name = PluginVariable(
    id="helpar_name",
    name="helpar_name",
    description='helical parameter name.',
    type=VariableTypes.STRING
)

confidence_level = PluginVariable(
    id="confidence_level",
    name="confidence_level",
    description='Confidence level for Byes Factor test (in percentage).',
    type=VariableTypes.NUMBER
)

max_iter = PluginVariable(
    id="max_iter",
    name="max_iter",
    description='Number of maximum iterations for EM algorithm.',
    type=VariableTypes.INTEGER
)

tol = PluginVariable(
    id="tol",
    name="tol",
    description='Tolerance value for EM algorithm.',
    type=VariableTypes.NUMBER
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
    description='Do not execute if output files exist.1',
    type=VariableTypes.BOOLEAN
)

# Define the action that the block will perform
def dna_bimodality_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_csv_file_value = biobb_block.inputs["input_csv_file"]
    
    input_zip_file_value = biobb_block.inputs["input_zip_file"]
    
    
    output_csv_path_value = biobb_block.inputs["output_csv_path"]
    
    output_jpg_path_value = biobb_block.inputs["output_jpg_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["helpar_name"] = biobb_block.variables["helpar_name"]
    
    properties_values["confidence_level"] = biobb_block.variables["confidence_level"]
    
    properties_values["max_iter"] = biobb_block.variables["max_iter"]
    
    properties_values["tol"] = biobb_block.variables["tol"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("dna_bimodality.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_gromacs:4.1.1--pyhdfd78af_0",
            "dna_bimodality",
            "--config",
            "/tmp/dna_bimodality.json",
            
            "--input_csv_file",
            f"/tmp/{Path(input_csv_file_value).name}",
            
            "--input_zip_file",
            f"/tmp/{Path(input_zip_file_value).name}",
            
            
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

inputs_list.append(input_csv_file)

inputs_list.append(input_zip_file)


outputs_list.append(output_csv_path)

outputs_list.append(output_jpg_path)


variables_list.append(helpar_name)

variables_list.append(confidence_level)

variables_list.append(max_iter)

variables_list.append(tol)

variables_list.append(remove_tmp)

variables_list.append(restart)


dna_bimodality_block = PluginBlock(
    # The name which will appear on the frontend
    name="dna_bimodality",
    # Its description
    description='Determine binormality/bimodality from a helical parameter series dataset.',
    # The action
    action=dna_bimodality_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)