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

input_probe_pdb_path = PluginVariable(
    id="input_probe_pdb_path",  # ID of the variable, will allow us to identify the value
    name="input_probe_pdb_path",  # The name that will appear in the frontend
    description='Path to the input probe file in PDB format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_rst_path = PluginVariable(
    id="input_rst_path",  # ID of the variable, will allow us to identify the value
    name="input_rst_path",  # The name that will appear in the frontend
    description='Path to the input restart file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['txt']
)

input_vdw_params_path = PluginVariable(
    id="input_vdw_params_path",  # ID of the variable, will allow us to identify the value
    name="input_vdw_params_path",  # The name that will appear in the frontend
    description='Path to the CMIP input Van der Waals force parameters, if not provided the CMIP conda installation one is used ("$CONDA_PREFIX/share/cmip/dat/vdwprm")',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['txt']
)

input_params_path = PluginVariable(
    id="input_params_path",  # ID of the variable, will allow us to identify the value
    name="input_params_path",  # The name that will appear in the frontend
    description='Path to the CMIP input parameters file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['txt']
)

input_json_box_path = PluginVariable(
    id="input_json_box_path",  # ID of the variable, will allow us to identify the value
    name="input_json_box_path",  # The name that will appear in the frontend
    description='Path to the input CMIP box in JSON format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['json']
)

input_json_external_box_path = PluginVariable(
    id="input_json_external_box_path",  # ID of the variable, will allow us to identify the value
    name="input_json_external_box_path",  # The name that will appear in the frontend
    description='Path to the input CMIP box in JSON format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['json']
)


output_pdb_path = PluginVariable(
    id="output_pdb_path",  # ID of the variable, will allow us to identify the value
    name="output_pdb_path",  # The name that will appear in the frontend
    description='Path to the output PDB file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_grd_path = PluginVariable(
    id="output_grd_path",  # ID of the variable, will allow us to identify the value
    name="output_grd_path",  # The name that will appear in the frontend
    description='Path to the output grid file in GRD format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['grd']
)

output_cube_path = PluginVariable(
    id="output_cube_path",  # ID of the variable, will allow us to identify the value
    name="output_cube_path",  # The name that will appear in the frontend
    description='Path to the output grid file in cube format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cube']
)

output_rst_path = PluginVariable(
    id="output_rst_path",  # ID of the variable, will allow us to identify the value
    name="output_rst_path",  # The name that will appear in the frontend
    description='Path to the output restart file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['txt']
)

output_byat_path = PluginVariable(
    id="output_byat_path",  # ID of the variable, will allow us to identify the value
    name="output_byat_path",  # The name that will appear in the frontend
    description='Path to the output atom by atom energy file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['txt', 'out']
)

output_log_path = PluginVariable(
    id="output_log_path",  # ID of the variable, will allow us to identify the value
    name="output_log_path",  # The name that will appear in the frontend
    description='Path to the output CMIP log file LOG',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['log']
)

output_json_box_path = PluginVariable(
    id="output_json_box_path",  # ID of the variable, will allow us to identify the value
    name="output_json_box_path",  # The name that will appear in the frontend
    description='Path to the output CMIP box in JSON format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['json']
)

output_json_external_box_path = PluginVariable(
    id="output_json_external_box_path",  # ID of the variable, will allow us to identify the value
    name="output_json_external_box_path",  # The name that will appear in the frontend
    description='Path to the output external CMIP box in JSON format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['json']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

execution_type = PluginVariable(
    id="execution_type",
    name="execution_type",
    description='Default options for the params file, each one creates a different params file. ',
    type=VariableTypes.STRING
)

params = PluginVariable(
    id="params",
    name="params",
    description='CMIP options specification.',
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to the CMIP cmip executable binary.',
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
def cmip_run_action(biobb_block: PluginBlock):

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
    
    input_probe_pdb_path_value = biobb_block.inputs["input_probe_pdb_path"]
    
    input_rst_path_value = biobb_block.inputs["input_rst_path"]
    
    input_vdw_params_path_value = biobb_block.inputs["input_vdw_params_path"]
    
    input_params_path_value = biobb_block.inputs["input_params_path"]
    
    input_json_box_path_value = biobb_block.inputs["input_json_box_path"]
    
    input_json_external_box_path_value = biobb_block.inputs["input_json_external_box_path"]
    
    
    output_pdb_path_value = biobb_block.inputs["output_pdb_path"]
    
    output_grd_path_value = biobb_block.inputs["output_grd_path"]
    
    output_cube_path_value = biobb_block.inputs["output_cube_path"]
    
    output_rst_path_value = biobb_block.inputs["output_rst_path"]
    
    output_byat_path_value = biobb_block.inputs["output_byat_path"]
    
    output_log_path_value = biobb_block.inputs["output_log_path"]
    
    output_json_box_path_value = biobb_block.inputs["output_json_box_path"]
    
    output_json_external_box_path_value = biobb_block.inputs["output_json_external_box_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["execution_type"] = biobb_block.variables["execution_type"]
    
    properties_values["params"] = biobb_block.variables["params"]
    
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


    with open("cmip_run.json", "w", encoding="utf-8") as f:
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
            "cmip_run",
            "--config",
            "/tmp/cmip_run.json",
            
            "--input_pdb_path",
            f"/tmp/{Path(input_pdb_path_value).name}",
            
            "--input_probe_pdb_path",
            f"/tmp/{Path(input_probe_pdb_path_value).name}",
            
            "--input_rst_path",
            f"/tmp/{Path(input_rst_path_value).name}",
            
            "--input_vdw_params_path",
            f"/tmp/{Path(input_vdw_params_path_value).name}",
            
            "--input_params_path",
            f"/tmp/{Path(input_params_path_value).name}",
            
            "--input_json_box_path",
            f"/tmp/{Path(input_json_box_path_value).name}",
            
            "--input_json_external_box_path",
            f"/tmp/{Path(input_json_external_box_path_value).name}",
            
            
            "--output_pdb_path",
            f"/tmp/{Path(output_pdb_path_value).name}",
            
            "--output_grd_path",
            f"/tmp/{Path(output_grd_path_value).name}",
            
            "--output_cube_path",
            f"/tmp/{Path(output_cube_path_value).name}",
            
            "--output_rst_path",
            f"/tmp/{Path(output_rst_path_value).name}",
            
            "--output_byat_path",
            f"/tmp/{Path(output_byat_path_value).name}",
            
            "--output_log_path",
            f"/tmp/{Path(output_log_path_value).name}",
            
            "--output_json_box_path",
            f"/tmp/{Path(output_json_box_path_value).name}",
            
            "--output_json_external_box_path",
            f"/tmp/{Path(output_json_external_box_path_value).name}",
            
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
        abs_path_out = Path(output_pdb_path_value).absolute()
        abs_path_name = Path(Path(output_pdb_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pdb_path_value).name}", output_pdb_path_value)
        biobb_block.setOutput("output_pdb_path", output_pdb_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_grd_path_value).absolute()
        abs_path_name = Path(Path(output_grd_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_grd_path_value).name}", output_grd_path_value)
        biobb_block.setOutput("output_grd_path", output_grd_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_cube_path_value).absolute()
        abs_path_name = Path(Path(output_cube_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cube_path_value).name}", output_cube_path_value)
        biobb_block.setOutput("output_cube_path", output_cube_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_rst_path_value).absolute()
        abs_path_name = Path(Path(output_rst_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_rst_path_value).name}", output_rst_path_value)
        biobb_block.setOutput("output_rst_path", output_rst_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_byat_path_value).absolute()
        abs_path_name = Path(Path(output_byat_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_byat_path_value).name}", output_byat_path_value)
        biobb_block.setOutput("output_byat_path", output_byat_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_log_path_value).absolute()
        abs_path_name = Path(Path(output_log_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_log_path_value).name}", output_log_path_value)
        biobb_block.setOutput("output_log_path", output_log_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_json_box_path_value).absolute()
        abs_path_name = Path(Path(output_json_box_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_json_box_path_value).name}", output_json_box_path_value)
        biobb_block.setOutput("output_json_box_path", output_json_box_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_json_external_box_path_value).absolute()
        abs_path_name = Path(Path(output_json_external_box_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_json_external_box_path_value).name}", output_json_external_box_path_value)
        biobb_block.setOutput("output_json_external_box_path", output_json_external_box_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pdb_path)

inputs_list.append(input_probe_pdb_path)

inputs_list.append(input_rst_path)

inputs_list.append(input_vdw_params_path)

inputs_list.append(input_params_path)

inputs_list.append(input_json_box_path)

inputs_list.append(input_json_external_box_path)


outputs_list.append(output_pdb_path)

outputs_list.append(output_grd_path)

outputs_list.append(output_cube_path)

outputs_list.append(output_rst_path)

outputs_list.append(output_byat_path)

outputs_list.append(output_log_path)

outputs_list.append(output_json_box_path)

outputs_list.append(output_json_external_box_path)


variables_list.append(execution_type)

variables_list.append(params)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


cmip_run_block = PluginBlock(
    # The name which will appear on the frontend
    name="cmip_run",
    # Its description
    description='Wrapper class for the CMIP cmip module.',
    # The action
    action=cmip_run_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)