# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_filename_shear = PluginVariable(
    id="input_filename_shear",  # ID of the variable, will allow us to identify the value
    name="input_filename_shear",  # The name that will appear in the frontend
    description="Path to .csv file with data for helical parameter 'shear'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

input_filename_stretch = PluginVariable(
    id="input_filename_stretch",  # ID of the variable, will allow us to identify the value
    name="input_filename_stretch",  # The name that will appear in the frontend
    description="Path to .csv file with data for helical parameter 'stretch'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

input_filename_stagger = PluginVariable(
    id="input_filename_stagger",  # ID of the variable, will allow us to identify the value
    name="input_filename_stagger",  # The name that will appear in the frontend
    description="Path to .csv file with data for helical parameter 'stagger'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

input_filename_buckle = PluginVariable(
    id="input_filename_buckle",  # ID of the variable, will allow us to identify the value
    name="input_filename_buckle",  # The name that will appear in the frontend
    description="Path to .csv file with data for helical parameter 'buckle'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

input_filename_propel = PluginVariable(
    id="input_filename_propel",  # ID of the variable, will allow us to identify the value
    name="input_filename_propel",  # The name that will appear in the frontend
    description="Path to .csv file with data for helical parameter 'propeller'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

input_filename_opening = PluginVariable(
    id="input_filename_opening",  # ID of the variable, will allow us to identify the value
    name="input_filename_opening",  # The name that will appear in the frontend
    description="Path to .csv file with data for helical parameter 'opening'",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)


output_csv_path = PluginVariable(
    id="output_csv_path",  # ID of the variable, will allow us to identify the value
    name="output_csv_path",  # The name that will appear in the frontend
    description="Path to directory where output is saved",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['csv']
)

output_jpg_path = PluginVariable(
    id="output_jpg_path",  # ID of the variable, will allow us to identify the value
    name="output_jpg_path",  # The name that will appear in the frontend
    description="Path to .jpg file where output is saved",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['jpg']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

remove_tmp = PluginVariable(
    id="remove_tmp",
    name="remove_tmp",
    description="Remove temporal files.",
    type=VariableTypes.BOOLEAN
)

restart = PluginVariable(
    id="restart",
    name="restart",
    description="Do not execute if output files exist.",
    type=VariableTypes.BOOLEAN
)

base = PluginVariable(
    id="base",
    name="base",
    description="Name of base analyzed.",
    type=VariableTypes.STRING
)

# Define the action that the block will perform
def intrahpcorr_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_filename_shear_value = biobb_block.inputs["input_filename_shear"]
    
    input_filename_stretch_value = biobb_block.inputs["input_filename_stretch"]
    
    input_filename_stagger_value = biobb_block.inputs["input_filename_stagger"]
    
    input_filename_buckle_value = biobb_block.inputs["input_filename_buckle"]
    
    input_filename_propel_value = biobb_block.inputs["input_filename_propel"]
    
    input_filename_opening_value = biobb_block.inputs["input_filename_opening"]
    
    
    output_csv_path_value = biobb_block.inputs["output_csv_path"]
    
    output_jpg_path_value = biobb_block.inputs["output_jpg_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    properties_values["base"] = biobb_block.variables["base"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("intrahpcorr.json", "w", encoding="utf-8") as f:
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
            "intrahpcorr",
            "--config",
            "/tmp/intrahpcorr.json",
            
            "--input_filename_shear",
            f"/tmp/{Path(input_filename_shear_value).name}",
            
            "--input_filename_stretch",
            f"/tmp/{Path(input_filename_stretch_value).name}",
            
            "--input_filename_stagger",
            f"/tmp/{Path(input_filename_stagger_value).name}",
            
            "--input_filename_buckle",
            f"/tmp/{Path(input_filename_buckle_value).name}",
            
            "--input_filename_propel",
            f"/tmp/{Path(input_filename_propel_value).name}",
            
            "--input_filename_opening",
            f"/tmp/{Path(input_filename_opening_value).name}",
            
            
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

inputs_list.append(input_filename_shear)

inputs_list.append(input_filename_stretch)

inputs_list.append(input_filename_stagger)

inputs_list.append(input_filename_buckle)

inputs_list.append(input_filename_propel)

inputs_list.append(input_filename_opening)


outputs_list.append(output_csv_path)

outputs_list.append(output_jpg_path)


variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(base)


intrahpcorr_block = PluginBlock(
    # The name which will appear on the frontend
    name="intrahpcorr",
    # Its description
    description="Calculate correlation between helical parameters for a single intra-base pair.",
    # The action
    action=intrahpcorr_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)