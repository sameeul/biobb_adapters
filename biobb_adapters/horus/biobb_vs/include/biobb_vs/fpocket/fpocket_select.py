# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_pockets_zip = PluginVariable(
    id="input_pockets_zip",  # ID of the variable, will allow us to identify the value
    name="input_pockets_zip",  # The name that will appear in the frontend
    description="Path to the pockets found by fpocket",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)


output_pocket_pdb = PluginVariable(
    id="output_pocket_pdb",  # ID of the variable, will allow us to identify the value
    name="output_pocket_pdb",  # The name that will appear in the frontend
    description="Path to the PDB file with the cavity found by fpocket",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_pocket_pqr = PluginVariable(
    id="output_pocket_pqr",  # ID of the variable, will allow us to identify the value
    name="output_pocket_pqr",  # The name that will appear in the frontend
    description="Path to the PQR file with the pocket found by fpocket",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pqr']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

pocket = PluginVariable(
    id="pocket",
    name="pocket",
    description="Pocket id from the summary json given by the fpocket building block.",
    type=VariableTypes.INTEGER
)

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

# Define the action that the block will perform
def fpocket_select_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_pockets_zip_value = biobb_block.inputs["input_pockets_zip"]
    
    
    output_pocket_pdb_value = biobb_block.inputs["output_pocket_pdb"]
    
    output_pocket_pqr_value = biobb_block.inputs["output_pocket_pqr"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["pocket"] = biobb_block.variables["pocket"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("fpocket_select.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_vs:4.1.2--pyhdfd78af_0",
            "fpocket_select",
            "--config",
            "/tmp/fpocket_select.json",
            
            "--input_pockets_zip",
            f"/tmp/{Path(input_pockets_zip_value).name}",
            
            
            "--output_pocket_pdb",
            f"/tmp/{Path(output_pocket_pdb_value).name}",
            
            "--output_pocket_pqr",
            f"/tmp/{Path(output_pocket_pqr_value).name}",
            
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
        abs_path_out = Path(output_pocket_pdb_value).absolute()
        abs_path_name = Path(Path(output_pocket_pdb_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pocket_pdb_value).name}", output_pocket_pdb_value)
        biobb_block.setOutput("output_pocket_pdb", output_pocket_pdb_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_pocket_pqr_value).absolute()
        abs_path_name = Path(Path(output_pocket_pqr_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pocket_pqr_value).name}", output_pocket_pqr_value)
        biobb_block.setOutput("output_pocket_pqr", output_pocket_pqr_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pockets_zip)


outputs_list.append(output_pocket_pdb)

outputs_list.append(output_pocket_pqr)


variables_list.append(pocket)

variables_list.append(remove_tmp)

variables_list.append(restart)


fpocket_select_block = PluginBlock(
    # The name which will appear on the frontend
    name="fpocket_select",
    # Its description
    description="Selects a single pocket in the outputs of the fpocket building block.",
    # The action
    action=fpocket_select_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)