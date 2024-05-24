# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_path = PluginVariable(
    id="input_path",  # ID of the variable, will allow us to identify the value
    name="input_path",  # The name that will appear in the frontend
    description="Path to the input file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)


output_path = PluginVariable(
    id="output_path",  # ID of the variable, will allow us to identify the value
    name="output_path",  # The name that will appear in the frontend
    description="Path to the output file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

flip = PluginVariable(
    id="flip",
    name="flip",
    description="add H and rotate and flip NQH groups",
    type=VariableTypes.BOOLEAN
)

noflip = PluginVariable(
    id="noflip",
    name="noflip",
    description="add H and rotate groups with no NQH flips",
    type=VariableTypes.BOOLEAN
)

nuclear = PluginVariable(
    id="nuclear",
    name="nuclear",
    description="use nuclear X-H distances rather than default electron cloud distances",
    type=VariableTypes.BOOLEAN
)

nooh = PluginVariable(
    id="nooh",
    name="nooh",
    description="remove hydrogens on OH and SH groups",
    type=VariableTypes.BOOLEAN
)

oh = PluginVariable(
    id="oh",
    name="oh",
    description="add hydrogens on OH and SH groups (default)",
    type=VariableTypes.BOOLEAN
)

his = PluginVariable(
    id="his",
    name="his",
    description="create NH hydrogens on HIS rings (usually used with -HIS)",
    type=VariableTypes.BOOLEAN
)

noheth = PluginVariable(
    id="noheth",
    name="noheth",
    description="do not attempt to add NH proton on Het groups",
    type=VariableTypes.BOOLEAN
)

rotnh3 = PluginVariable(
    id="rotnh3",
    name="rotnh3",
    description="allow lysine NH3 to rotate (default)",
    type=VariableTypes.BOOLEAN
)

norotnh3 = PluginVariable(
    id="norotnh3",
    name="norotnh3",
    description="do not allow lysine NH3 to rotate",
    type=VariableTypes.BOOLEAN
)

rotexist = PluginVariable(
    id="rotexist",
    name="rotexist",
    description="allow existing rotatable groups (OH, SH, Met-CH3) to rotate",
    type=VariableTypes.BOOLEAN
)

rotexoh = PluginVariable(
    id="rotexoh",
    name="rotexoh",
    description="allow existing OH & SH groups to rotate",
    type=VariableTypes.BOOLEAN
)

allalt = PluginVariable(
    id="allalt",
    name="allalt",
    description="process adjustments for all conformations (default)",
    type=VariableTypes.BOOLEAN
)

onlya = PluginVariable(
    id="onlya",
    name="onlya",
    description="only adjust 'A' conformations",
    type=VariableTypes.BOOLEAN
)

charges = PluginVariable(
    id="charges",
    name="charges",
    description="output charge state for appropriate hydrogen records",
    type=VariableTypes.BOOLEAN
)

dorotmet = PluginVariable(
    id="dorotmet",
    name="dorotmet",
    description="allow methionine methyl groups to rotate (not recommended)",
    type=VariableTypes.BOOLEAN
)

noadjust = PluginVariable(
    id="noadjust",
    name="noadjust",
    description="do not process any rot or flip adjustments",
    type=VariableTypes.BOOLEAN
)

metal_bump = PluginVariable(
    id="metal_bump",
    name="metal_bump",
    description="H 'bumps' metals at radius plus this",
    type=VariableTypes.NUMBER
)

non_metal_bump = PluginVariable(
    id="non_metal_bump",
    name="non_metal_bump",
    description="'bumps' nonmetal at radius plus this",
    type=VariableTypes.NUMBER
)

build = PluginVariable(
    id="build",
    name="build",
    description="add H, including His sc NH, then rotate and flip groups (except for pre-existing methionine methyl hydrogens)",
    type=VariableTypes.BOOLEAN
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="Path to the reduce executable binary.",
    type=VariableTypes.STRING
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

container_path = PluginVariable(
    id="container_path",
    name="container_path",
    description="Container path definition.",
    type=VariableTypes.STRING
)

container_image = PluginVariable(
    id="container_image",
    name="container_image",
    description="Container image definition.",
    type=VariableTypes.STRING
)

container_volume_path = PluginVariable(
    id="container_volume_path",
    name="container_volume_path",
    description="Container volume path definition.",
    type=VariableTypes.STRING
)

container_working_dir = PluginVariable(
    id="container_working_dir",
    name="container_working_dir",
    description="Container working directory definition.",
    type=VariableTypes.STRING
)

container_user_id = PluginVariable(
    id="container_user_id",
    name="container_user_id",
    description="Container user_id definition.",
    type=VariableTypes.STRING
)

container_shell_path = PluginVariable(
    id="container_shell_path",
    name="container_shell_path",
    description="Path to default shell inside the container.",
    type=VariableTypes.STRING
)

# Define the action that the block will perform
def reduce_add_hydrogens_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_path_value = biobb_block.inputs["input_path"]
    
    
    output_path_value = biobb_block.inputs["output_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["flip"] = biobb_block.variables["flip"]
    
    properties_values["noflip"] = biobb_block.variables["noflip"]
    
    properties_values["nuclear"] = biobb_block.variables["nuclear"]
    
    properties_values["nooh"] = biobb_block.variables["nooh"]
    
    properties_values["oh"] = biobb_block.variables["oh"]
    
    properties_values["his"] = biobb_block.variables["his"]
    
    properties_values["noheth"] = biobb_block.variables["noheth"]
    
    properties_values["rotnh3"] = biobb_block.variables["rotnh3"]
    
    properties_values["norotnh3"] = biobb_block.variables["norotnh3"]
    
    properties_values["rotexist"] = biobb_block.variables["rotexist"]
    
    properties_values["rotexoh"] = biobb_block.variables["rotexoh"]
    
    properties_values["allalt"] = biobb_block.variables["allalt"]
    
    properties_values["onlya"] = biobb_block.variables["onlya"]
    
    properties_values["charges"] = biobb_block.variables["charges"]
    
    properties_values["dorotmet"] = biobb_block.variables["dorotmet"]
    
    properties_values["noadjust"] = biobb_block.variables["noadjust"]
    
    properties_values["metal_bump"] = biobb_block.variables["metal_bump"]
    
    properties_values["non_metal_bump"] = biobb_block.variables["non_metal_bump"]
    
    properties_values["build"] = biobb_block.variables["build"]
    
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


    with open("reduce_add_hydrogens.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_chemistry:4.2.0--pyhdfd78af_0",
            "reduce_add_hydrogens",
            "--config",
            "/tmp/reduce_add_hydrogens.json",
            
            "--input_path",
            f"/tmp/{Path(input_path_value).name}",
            
            
            "--output_path",
            f"/tmp/{Path(output_path_value).name}",
            
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
        abs_path_out = Path(output_path_value).absolute()
        abs_path_name = Path(Path(output_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_path_value).name}", output_path_value)
        biobb_block.setOutput("output_path", output_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_path)


outputs_list.append(output_path)


variables_list.append(flip)

variables_list.append(noflip)

variables_list.append(nuclear)

variables_list.append(nooh)

variables_list.append(oh)

variables_list.append(his)

variables_list.append(noheth)

variables_list.append(rotnh3)

variables_list.append(norotnh3)

variables_list.append(rotexist)

variables_list.append(rotexoh)

variables_list.append(allalt)

variables_list.append(onlya)

variables_list.append(charges)

variables_list.append(dorotmet)

variables_list.append(noadjust)

variables_list.append(metal_bump)

variables_list.append(non_metal_bump)

variables_list.append(build)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


reduce_add_hydrogens_block = PluginBlock(
    # The name which will appear on the frontend
    name="reduce_add_hydrogens",
    # Its description
    description="This class is a wrapper of the Ambertools reduce module for adding hydrogens to a given structure.",
    # The action
    action=reduce_add_hydrogens_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)