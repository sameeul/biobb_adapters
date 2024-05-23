# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_top_path = PluginVariable(
    id="input_top_path",  # ID of the variable, will allow us to identify the value
    name="input_top_path",  # The name that will appear in the frontend
    description='Path to the input structure or topology file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['top', 'pdb', 'prmtop', 'parmtop', 'zip']
)

input_traj_path = PluginVariable(
    id="input_traj_path",  # ID of the variable, will allow us to identify the value
    name="input_traj_path",  # The name that will appear in the frontend
    description='Path to the input trajectory to be processed',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['mdcrd', 'crd', 'cdf', 'netcdf', 'nc', 'restart', 'ncrestart', 'restartnc', 'dcd', 'charmm', 'cor', 'pdb', 'mol2', 'trr', 'gro', 'binpos', 'xtc', 'cif', 'arc', 'sqm', 'sdf', 'conflib']
)

input_exp_path = PluginVariable(
    id="input_exp_path",  # ID of the variable, will allow us to identify the value
    name="input_exp_path",  # The name that will appear in the frontend
    description='Path to the experimental reference file (required if reference = experimental)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)


output_cpptraj_path = PluginVariable(
    id="output_cpptraj_path",  # ID of the variable, will allow us to identify the value
    name="output_cpptraj_path",  # The name that will appear in the frontend
    description='Path to the output processed analysis',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'agr', 'xmgr', 'gnu']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

start = PluginVariable(
    id="start",
    name="start",
    description='Starting frame for slicing',
    type=VariableTypes.INTEGER
)

end = PluginVariable(
    id="end",
    name="end",
    description='Ending frame for slicing',
    type=VariableTypes.INTEGER
)

steps = PluginVariable(
    id="steps",
    name="steps",
    description='Step for slicing',
    type=VariableTypes.INTEGER
)

mask = PluginVariable(
    id="mask",
    name="mask",
    description='Mask definition. ',
    type=VariableTypes.STRING
)

reference = PluginVariable(
    id="reference",
    name="reference",
    description='Reference definition. ',
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to the cpptraj executable binary.',
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
    description='Container path definition.',
    type=VariableTypes.STRING
)

container_image = PluginVariable(
    id="container_image",
    name="container_image",
    description='Container image definition.',
    type=VariableTypes.STRING
)

container_volume_path = PluginVariable(
    id="container_volume_path",
    name="container_volume_path",
    description='Container volume path definition.',
    type=VariableTypes.STRING
)

container_working_dir = PluginVariable(
    id="container_working_dir",
    name="container_working_dir",
    description='Container working directory definition.',
    type=VariableTypes.STRING
)

container_user_id = PluginVariable(
    id="container_user_id",
    name="container_user_id",
    description='Container user_id definition.',
    type=VariableTypes.STRING
)

container_shell_path = PluginVariable(
    id="container_shell_path",
    name="container_shell_path",
    description='Path to default shell inside the container.',
    type=VariableTypes.STRING
)

# Define the action that the block will perform
def cpptraj_rmsf_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_top_path_value = biobb_block.inputs["input_top_path"]
    
    input_traj_path_value = biobb_block.inputs["input_traj_path"]
    
    input_exp_path_value = biobb_block.inputs["input_exp_path"]
    
    
    output_cpptraj_path_value = biobb_block.inputs["output_cpptraj_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["start"] = biobb_block.variables["start"]
    
    properties_values["end"] = biobb_block.variables["end"]
    
    properties_values["steps"] = biobb_block.variables["steps"]
    
    properties_values["mask"] = biobb_block.variables["mask"]
    
    properties_values["reference"] = biobb_block.variables["reference"]
    
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


    with open("cpptraj_rmsf.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_analysis:4.1.0--pyhdfd78af_0",
            "cpptraj_rmsf",
            "--config",
            "/tmp/cpptraj_rmsf.json",
            
            "--input_top_path",
            f"/tmp/{Path(input_top_path_value).name}",
            
            "--input_traj_path",
            f"/tmp/{Path(input_traj_path_value).name}",
            
            "--input_exp_path",
            f"/tmp/{Path(input_exp_path_value).name}",
            
            
            "--output_cpptraj_path",
            f"/tmp/{Path(output_cpptraj_path_value).name}",
            
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
        abs_path_out = Path(output_cpptraj_path_value).absolute()
        abs_path_name = Path(Path(output_cpptraj_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cpptraj_path_value).name}", output_cpptraj_path_value)
        biobb_block.setOutput("output_cpptraj_path", output_cpptraj_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_top_path)

inputs_list.append(input_traj_path)

inputs_list.append(input_exp_path)


outputs_list.append(output_cpptraj_path)


variables_list.append(start)

variables_list.append(end)

variables_list.append(steps)

variables_list.append(mask)

variables_list.append(reference)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


cpptraj_rmsf_block = PluginBlock(
    # The name which will appear on the frontend
    name="cpptraj_rmsf",
    # Its description
    description='Wrapper of the Ambertools Cpptraj module for calculating the Root Mean Square fluctuations (RMSf) of a given cpptraj compatible trajectory.',
    # The action
    action=cpptraj_rmsf_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)