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
    allowedValues=['pdb', 'mdl', 'mol2']
)


output_path_frcmod = PluginVariable(
    id="output_path_frcmod",  # ID of the variable, will allow us to identify the value
    name="output_path_frcmod",  # The name that will appear in the frontend
    description="Path to the FRCMOD output file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['frcmod']
)

output_path_inpcrd = PluginVariable(
    id="output_path_inpcrd",  # ID of the variable, will allow us to identify the value
    name="output_path_inpcrd",  # The name that will appear in the frontend
    description="Path to the INPCRD output file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['inpcrd']
)

output_path_lib = PluginVariable(
    id="output_path_lib",  # ID of the variable, will allow us to identify the value
    name="output_path_lib",  # The name that will appear in the frontend
    description="Path to the LIB output file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['lib']
)

output_path_prmtop = PluginVariable(
    id="output_path_prmtop",  # ID of the variable, will allow us to identify the value
    name="output_path_prmtop",  # The name that will appear in the frontend
    description="Path to the PRMTOP output file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['prmtop']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

basename = PluginVariable(
    id="basename",
    name="basename",
    description="A basename for the project (folder and output files).",
    type=VariableTypes.STRING
)

charge = PluginVariable(
    id="charge",
    name="charge",
    description="Net molecular charge, for gas default is 0. If None the charge is guessed by acpype.",
    type=VariableTypes.INTEGER
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="Path to the acpype executable binary.",
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
def acpype_params_ac_action(biobb_block: PluginBlock):

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
    
    
    output_path_frcmod_value = biobb_block.inputs["output_path_frcmod"]
    
    output_path_inpcrd_value = biobb_block.inputs["output_path_inpcrd"]
    
    output_path_lib_value = biobb_block.inputs["output_path_lib"]
    
    output_path_prmtop_value = biobb_block.inputs["output_path_prmtop"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["basename"] = biobb_block.variables["basename"]
    
    properties_values["charge"] = biobb_block.variables["charge"]
    
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


    with open("acpype_params_ac.json", "w", encoding="utf-8") as f:
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
            "acpype_params_ac",
            "--config",
            "/tmp/acpype_params_ac.json",
            
            "--input_path",
            f"/tmp/{Path(input_path_value).name}",
            
            
            "--output_path_frcmod",
            f"/tmp/{Path(output_path_frcmod_value).name}",
            
            "--output_path_inpcrd",
            f"/tmp/{Path(output_path_inpcrd_value).name}",
            
            "--output_path_lib",
            f"/tmp/{Path(output_path_lib_value).name}",
            
            "--output_path_prmtop",
            f"/tmp/{Path(output_path_prmtop_value).name}",
            
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
        abs_path_out = Path(output_path_frcmod_value).absolute()
        abs_path_name = Path(Path(output_path_frcmod_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_path_frcmod_value).name}", output_path_frcmod_value)
        biobb_block.setOutput("output_path_frcmod", output_path_frcmod_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_path_inpcrd_value).absolute()
        abs_path_name = Path(Path(output_path_inpcrd_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_path_inpcrd_value).name}", output_path_inpcrd_value)
        biobb_block.setOutput("output_path_inpcrd", output_path_inpcrd_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_path_lib_value).absolute()
        abs_path_name = Path(Path(output_path_lib_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_path_lib_value).name}", output_path_lib_value)
        biobb_block.setOutput("output_path_lib", output_path_lib_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_path_prmtop_value).absolute()
        abs_path_name = Path(Path(output_path_prmtop_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_path_prmtop_value).name}", output_path_prmtop_value)
        biobb_block.setOutput("output_path_prmtop", output_path_prmtop_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_path)


outputs_list.append(output_path_frcmod)

outputs_list.append(output_path_inpcrd)

outputs_list.append(output_path_lib)

outputs_list.append(output_path_prmtop)


variables_list.append(basename)

variables_list.append(charge)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


acpype_params_ac_block = PluginBlock(
    # The name which will appear on the frontend
    name="acpype_params_ac",
    # Its description
    description="This class is a wrapper of Acpype tool for small molecule parameterization for AMBER MD package.",
    # The action
    action=acpype_params_ac_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)