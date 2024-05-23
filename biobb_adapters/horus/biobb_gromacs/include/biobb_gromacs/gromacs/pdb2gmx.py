# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_pdb_path = PluginVariable(
    id="input_pdb_path",  # ID of the variable, will allow us to identify the value
    name="input_pdb_path",  # The name that will appear in the frontend
    description='Path to the input PDB file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)


output_gro_path = PluginVariable(
    id="output_gro_path",  # ID of the variable, will allow us to identify the value
    name="output_gro_path",  # The name that will appear in the frontend
    description='Path to the output GRO file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['gro']
)

output_top_zip_path = PluginVariable(
    id="output_top_zip_path",  # ID of the variable, will allow us to identify the value
    name="output_top_zip_path",  # The name that will appear in the frontend
    description='Path the output TOP topology in zip format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

water_type = PluginVariable(
    id="water_type",
    name="water_type",
    description='Water molecule type. ',
    type=VariableTypes.STRING
)

force_field = PluginVariable(
    id="force_field",
    name="force_field",
    description='Force field to be used during the conversion.  ',
    type=VariableTypes.STRING
)

ignh = PluginVariable(
    id="ignh",
    name="ignh",
    description='Should pdb2gmx ignore the hidrogens in the original structure.',
    type=VariableTypes.BOOLEAN
)

his = PluginVariable(
    id="his",
    name="his",
    description='Histidine protonation array.',
    type=VariableTypes.STRING
)

merge = PluginVariable(
    id="merge",
    name="merge",
    description='Merge all chains into a single molecule.',
    type=VariableTypes.BOOLEAN
)

gmx_lib = PluginVariable(
    id="gmx_lib",
    name="gmx_lib",
    description='Path set GROMACS GMXLIB environment variable.',
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to the GROMACS executable binary.',
    type=VariableTypes.STRING
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

container_path = PluginVariable(
    id="container_path",
    name="container_path",
    description='Path to the binary executable of your container.',
    type=VariableTypes.STRING
)

container_image = PluginVariable(
    id="container_image",
    name="container_image",
    description='Container Image identifier.',
    type=VariableTypes.STRING
)

container_volume_path = PluginVariable(
    id="container_volume_path",
    name="container_volume_path",
    description='Path to an internal directory in the container.',
    type=VariableTypes.STRING
)

container_working_dir = PluginVariable(
    id="container_working_dir",
    name="container_working_dir",
    description='Path to the internal CWD in the container.',
    type=VariableTypes.STRING
)

container_user_id = PluginVariable(
    id="container_user_id",
    name="container_user_id",
    description='User number id to be mapped inside the container.',
    type=VariableTypes.STRING
)

container_shell_path = PluginVariable(
    id="container_shell_path",
    name="container_shell_path",
    description='Path to the binary executable of the container shell.',
    type=VariableTypes.STRING
)

# Define the action that the block will perform
def pdb2gmx_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_pdb_path_value = biobb_block.inputs["input_pdb_path"]
    
    
    output_gro_path_value = biobb_block.inputs["output_gro_path"]
    
    output_top_zip_path_value = biobb_block.inputs["output_top_zip_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["water_type"] = biobb_block.variables["water_type"]
    
    properties_values["force_field"] = biobb_block.variables["force_field"]
    
    properties_values["ignh"] = biobb_block.variables["ignh"]
    
    properties_values["his"] = biobb_block.variables["his"]
    
    properties_values["merge"] = biobb_block.variables["merge"]
    
    properties_values["gmx_lib"] = biobb_block.variables["gmx_lib"]
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    properties_values["container_path"] = biobb_block.variables["container_path"]
    
    properties_values["container_image"] = biobb_block.variables["container_image"]
    
    properties_values["container_volume_path"] = biobb_block.variables["container_volume_path"]
    
    properties_values["container_working_dir"] = biobb_block.variables["container_working_dir"]
    
    properties_values["container_user_id"] = biobb_block.variables["container_user_id"]
    
    properties_values["container_shell_path"] = biobb_block.variables["container_shell_path"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("pdb2gmx.json", "w", encoding="utf-8") as f:
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
            "pdb2gmx",
            "--config",
            "/tmp/pdb2gmx.json",
            
            "--input_pdb_path",
            f"/tmp/{Path(input_pdb_path_value).name}",
            
            
            "--output_gro_path",
            f"/tmp/{Path(output_gro_path_value).name}",
            
            "--output_top_zip_path",
            f"/tmp/{Path(output_top_zip_path_value).name}",
            
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
        abs_path_out = Path(output_gro_path_value).absolute()
        abs_path_name = Path(Path(output_gro_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_gro_path_value).name}", output_gro_path_value)
        biobb_block.setOutput("output_gro_path", output_gro_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_top_zip_path_value).absolute()
        abs_path_name = Path(Path(output_top_zip_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_top_zip_path_value).name}", output_top_zip_path_value)
        biobb_block.setOutput("output_top_zip_path", output_top_zip_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pdb_path)


outputs_list.append(output_gro_path)

outputs_list.append(output_top_zip_path)


variables_list.append(water_type)

variables_list.append(force_field)

variables_list.append(ignh)

variables_list.append(his)

variables_list.append(merge)

variables_list.append(gmx_lib)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


pdb2gmx_block = PluginBlock(
    # The name which will appear on the frontend
    name="pdb2gmx",
    # Its description
    description='Wrapper class for the GROMACS pdb2gmx module.',
    # The action
    action=pdb2gmx_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)