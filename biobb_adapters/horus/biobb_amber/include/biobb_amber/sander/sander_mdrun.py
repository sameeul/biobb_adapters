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
    description='Input topology file (AMBER ParmTop)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['top', 'parmtop', 'prmtop']
)

input_crd_path = PluginVariable(
    id="input_crd_path",  # ID of the variable, will allow us to identify the value
    name="input_crd_path",  # The name that will appear in the frontend
    description='Input coordinates file (AMBER crd)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['crd', 'mdcrd', 'inpcrd', 'netcdf', 'nc', 'ncrst']
)

input_mdin_path = PluginVariable(
    id="input_mdin_path",  # ID of the variable, will allow us to identify the value
    name="input_mdin_path",  # The name that will appear in the frontend
    description='Input configuration file (MD run options) (AMBER mdin)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['mdin', 'in', 'txt']
)

input_cpin_path = PluginVariable(
    id="input_cpin_path",  # ID of the variable, will allow us to identify the value
    name="input_cpin_path",  # The name that will appear in the frontend
    description='Input constant pH file (AMBER cpin)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cpin']
)

input_ref_path = PluginVariable(
    id="input_ref_path",  # ID of the variable, will allow us to identify the value
    name="input_ref_path",  # The name that will appear in the frontend
    description='Input reference coordinates for position restraints',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['rst', 'rst7', 'netcdf', 'nc', 'ncrst', 'crd']
)


output_log_path = PluginVariable(
    id="output_log_path",  # ID of the variable, will allow us to identify the value
    name="output_log_path",  # The name that will appear in the frontend
    description='Output log file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['log', 'out', 'txt', 'o']
)

output_traj_path = PluginVariable(
    id="output_traj_path",  # ID of the variable, will allow us to identify the value
    name="output_traj_path",  # The name that will appear in the frontend
    description='Output trajectory file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['trj', 'crd', 'mdcrd', 'x', 'netcdf', 'nc']
)

output_rst_path = PluginVariable(
    id="output_rst_path",  # ID of the variable, will allow us to identify the value
    name="output_rst_path",  # The name that will appear in the frontend
    description='Output restart file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['rst', 'rst7', 'netcdf', 'nc', 'ncrst']
)

output_cpout_path = PluginVariable(
    id="output_cpout_path",  # ID of the variable, will allow us to identify the value
    name="output_cpout_path",  # The name that will appear in the frontend
    description='Output constant pH file (AMBER cpout)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cpout']
)

output_cprst_path = PluginVariable(
    id="output_cprst_path",  # ID of the variable, will allow us to identify the value
    name="output_cprst_path",  # The name that will appear in the frontend
    description='Output constant pH restart file (AMBER rstout)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cprst', 'rst', 'rst7']
)

output_mdinfo_path = PluginVariable(
    id="output_mdinfo_path",  # ID of the variable, will allow us to identify the value
    name="output_mdinfo_path",  # The name that will appear in the frontend
    description='Output MD info',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['mdinfo']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

mdin = PluginVariable(
    id="mdin",
    name="mdin",
    description='Sander MD run options specification. (Used if *input_mdin_path* is None)',
    type=VariableTypes.STRING
)

simulation_type = PluginVariable(
    id="simulation_type",
    name="simulation_type",
    description='Default options for the mdin file. Each creates a different mdin file. ',
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='sander binary path to be used.',
    type=VariableTypes.STRING
)

direct_mdin = PluginVariable(
    id="direct_mdin",
    name="direct_mdin",
    description='Use input_mdin_path as it is, skip file parsing.',
    type=VariableTypes.BOOLEAN
)

mpi_bin = PluginVariable(
    id="mpi_bin",
    name="mpi_bin",
    description='Path to the MPI runner. Usually "mpirun" or "srun".',
    type=VariableTypes.STRING
)

mpi_np = PluginVariable(
    id="mpi_np",
    name="mpi_np",
    description='Number of MPI processes. Usually an integer bigger than 1.',
    type=VariableTypes.INTEGER
)

mpi_flags = PluginVariable(
    id="mpi_flags",
    name="mpi_flags",
    description='Path to the MPI hostlist file.',
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
def sander_mdrun_action(biobb_block: PluginBlock):

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
    
    input_crd_path_value = biobb_block.inputs["input_crd_path"]
    
    input_mdin_path_value = biobb_block.inputs["input_mdin_path"]
    
    input_cpin_path_value = biobb_block.inputs["input_cpin_path"]
    
    input_ref_path_value = biobb_block.inputs["input_ref_path"]
    
    
    output_log_path_value = biobb_block.inputs["output_log_path"]
    
    output_traj_path_value = biobb_block.inputs["output_traj_path"]
    
    output_rst_path_value = biobb_block.inputs["output_rst_path"]
    
    output_cpout_path_value = biobb_block.inputs["output_cpout_path"]
    
    output_cprst_path_value = biobb_block.inputs["output_cprst_path"]
    
    output_mdinfo_path_value = biobb_block.inputs["output_mdinfo_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["mdin"] = biobb_block.variables["mdin"]
    
    properties_values["simulation_type"] = biobb_block.variables["simulation_type"]
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["direct_mdin"] = biobb_block.variables["direct_mdin"]
    
    properties_values["mpi_bin"] = biobb_block.variables["mpi_bin"]
    
    properties_values["mpi_np"] = biobb_block.variables["mpi_np"]
    
    properties_values["mpi_flags"] = biobb_block.variables["mpi_flags"]
    
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


    with open("sander_mdrun.json", "w", encoding="utf-8") as f:
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
            "sander_mdrun",
            "--config",
            "/tmp/sander_mdrun.json",
            
            "--input_top_path",
            f"/tmp/{Path(input_top_path_value).name}",
            
            "--input_crd_path",
            f"/tmp/{Path(input_crd_path_value).name}",
            
            "--input_mdin_path",
            f"/tmp/{Path(input_mdin_path_value).name}",
            
            "--input_cpin_path",
            f"/tmp/{Path(input_cpin_path_value).name}",
            
            "--input_ref_path",
            f"/tmp/{Path(input_ref_path_value).name}",
            
            
            "--output_log_path",
            f"/tmp/{Path(output_log_path_value).name}",
            
            "--output_traj_path",
            f"/tmp/{Path(output_traj_path_value).name}",
            
            "--output_rst_path",
            f"/tmp/{Path(output_rst_path_value).name}",
            
            "--output_cpout_path",
            f"/tmp/{Path(output_cpout_path_value).name}",
            
            "--output_cprst_path",
            f"/tmp/{Path(output_cprst_path_value).name}",
            
            "--output_mdinfo_path",
            f"/tmp/{Path(output_mdinfo_path_value).name}",
            
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
        abs_path_out = Path(output_log_path_value).absolute()
        abs_path_name = Path(Path(output_log_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_log_path_value).name}", output_log_path_value)
        biobb_block.setOutput("output_log_path", output_log_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_traj_path_value).absolute()
        abs_path_name = Path(Path(output_traj_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_traj_path_value).name}", output_traj_path_value)
        biobb_block.setOutput("output_traj_path", output_traj_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_rst_path_value).absolute()
        abs_path_name = Path(Path(output_rst_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_rst_path_value).name}", output_rst_path_value)
        biobb_block.setOutput("output_rst_path", output_rst_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_cpout_path_value).absolute()
        abs_path_name = Path(Path(output_cpout_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cpout_path_value).name}", output_cpout_path_value)
        biobb_block.setOutput("output_cpout_path", output_cpout_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_cprst_path_value).absolute()
        abs_path_name = Path(Path(output_cprst_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cprst_path_value).name}", output_cprst_path_value)
        biobb_block.setOutput("output_cprst_path", output_cprst_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_mdinfo_path_value).absolute()
        abs_path_name = Path(Path(output_mdinfo_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_mdinfo_path_value).name}", output_mdinfo_path_value)
        biobb_block.setOutput("output_mdinfo_path", output_mdinfo_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_top_path)

inputs_list.append(input_crd_path)

inputs_list.append(input_mdin_path)

inputs_list.append(input_cpin_path)

inputs_list.append(input_ref_path)


outputs_list.append(output_log_path)

outputs_list.append(output_traj_path)

outputs_list.append(output_rst_path)

outputs_list.append(output_cpout_path)

outputs_list.append(output_cprst_path)

outputs_list.append(output_mdinfo_path)


variables_list.append(mdin)

variables_list.append(simulation_type)

variables_list.append(binary_path)

variables_list.append(direct_mdin)

variables_list.append(mpi_bin)

variables_list.append(mpi_np)

variables_list.append(mpi_flags)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


sander_mdrun_block = PluginBlock(
    # The name which will appear on the frontend
    name="sander_mdrun",
    # Its description
    description='Wrapper of the AmberTools (AMBER MD Package) sander tool module.',
    # The action
    action=sander_mdrun_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)