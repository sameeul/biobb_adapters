# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_tpr_path = PluginVariable(
    id="input_tpr_path",  # ID of the variable, will allow us to identify the value
    name="input_tpr_path",  # The name that will appear in the frontend
    description="Path to the portable binary run input file TPR",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['tpr']
)

input_cpt_path = PluginVariable(
    id="input_cpt_path",  # ID of the variable, will allow us to identify the value
    name="input_cpt_path",  # The name that will appear in the frontend
    description="Path to the input GROMACS checkpoint file CPT",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cpt']
)


output_gro_path = PluginVariable(
    id="output_gro_path",  # ID of the variable, will allow us to identify the value
    name="output_gro_path",  # The name that will appear in the frontend
    description="Path to the output GROMACS structure GRO file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['gro']
)

output_edr_path = PluginVariable(
    id="output_edr_path",  # ID of the variable, will allow us to identify the value
    name="output_edr_path",  # The name that will appear in the frontend
    description="Path to the output GROMACS portable energy file EDR",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['edr']
)

output_log_path = PluginVariable(
    id="output_log_path",  # ID of the variable, will allow us to identify the value
    name="output_log_path",  # The name that will appear in the frontend
    description="Path to the output GROMACS trajectory log file LOG",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['log']
)

output_trr_path = PluginVariable(
    id="output_trr_path",  # ID of the variable, will allow us to identify the value
    name="output_trr_path",  # The name that will appear in the frontend
    description="Path to the GROMACS uncompressed raw trajectory file TRR",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['trr']
)

output_xtc_path = PluginVariable(
    id="output_xtc_path",  # ID of the variable, will allow us to identify the value
    name="output_xtc_path",  # The name that will appear in the frontend
    description="Path to the GROMACS compressed trajectory file XTC",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['xtc']
)

output_cpt_path = PluginVariable(
    id="output_cpt_path",  # ID of the variable, will allow us to identify the value
    name="output_cpt_path",  # The name that will appear in the frontend
    description="Path to the output GROMACS checkpoint file CPT",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cpt']
)

output_dhdl_path = PluginVariable(
    id="output_dhdl_path",  # ID of the variable, will allow us to identify the value
    name="output_dhdl_path",  # The name that will appear in the frontend
    description="Path to the output dhdl.xvg file only used when free energy calculation is turned on",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['xvg']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

mpi_bin = PluginVariable(
    id="mpi_bin",
    name="mpi_bin",
    description="Path to the MPI runner. Usually 'mpirun' or 'srun'.",
    type=VariableTypes.STRING
)

mpi_np = PluginVariable(
    id="mpi_np",
    name="mpi_np",
    description="Number of MPI processes. Usually an integer bigger than 1.",
    type=VariableTypes.INTEGER
)

mpi_flags = PluginVariable(
    id="mpi_flags",
    name="mpi_flags",
    description="Path to the MPI hostlist file.",
    type=VariableTypes.STRING
)

checkpoint_time = PluginVariable(
    id="checkpoint_time",
    name="checkpoint_time",
    description="Checkpoint writing interval in minutes. Only enabled if an output_cpt_path is provided.",
    type=VariableTypes.INTEGER
)

num_threads = PluginVariable(
    id="num_threads",
    name="num_threads",
    description="Let GROMACS guess. The number of threads that are going to be used.",
    type=VariableTypes.INTEGER
)

num_threads_mpi = PluginVariable(
    id="num_threads_mpi",
    name="num_threads_mpi",
    description="Let GROMACS guess. The number of GROMACS MPI threads that are going to be used.",
    type=VariableTypes.INTEGER
)

num_threads_omp = PluginVariable(
    id="num_threads_omp",
    name="num_threads_omp",
    description="Let GROMACS guess. The number of GROMACS OPENMP threads that are going to be used.",
    type=VariableTypes.INTEGER
)

num_threads_omp_pme = PluginVariable(
    id="num_threads_omp_pme",
    name="num_threads_omp_pme",
    description="Let GROMACS guess. The number of GROMACS OPENMP_PME threads that are going to be used.",
    type=VariableTypes.INTEGER
)

use_gpu = PluginVariable(
    id="use_gpu",
    name="use_gpu",
    description="Use settings appropriate for GPU. Adds: -nb gpu -pme gpu",
    type=VariableTypes.BOOLEAN
)

gpu_id = PluginVariable(
    id="gpu_id",
    name="gpu_id",
    description="List of unique GPU device IDs available to use.",
    type=VariableTypes.STRING
)

gpu_tasks = PluginVariable(
    id="gpu_tasks",
    name="gpu_tasks",
    description="List of GPU device IDs, mapping each PP task on each node to a device.",
    type=VariableTypes.STRING
)

gmx_lib = PluginVariable(
    id="gmx_lib",
    name="gmx_lib",
    description="Path set GROMACS GMXLIB environment variable.",
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="Path to the GROMACS executable binary.",
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
    description="Path to the binary executable of your container.",
    type=VariableTypes.STRING
)

container_image = PluginVariable(
    id="container_image",
    name="container_image",
    description="Container Image identifier.",
    type=VariableTypes.STRING
)

container_volume_path = PluginVariable(
    id="container_volume_path",
    name="container_volume_path",
    description="Path to an internal directory in the container.",
    type=VariableTypes.STRING
)

container_working_dir = PluginVariable(
    id="container_working_dir",
    name="container_working_dir",
    description="Path to the internal CWD in the container.",
    type=VariableTypes.STRING
)

container_user_id = PluginVariable(
    id="container_user_id",
    name="container_user_id",
    description="User number id to be mapped inside the container.",
    type=VariableTypes.STRING
)

container_shell_path = PluginVariable(
    id="container_shell_path",
    name="container_shell_path",
    description="Path to the binary executable of the container shell.",
    type=VariableTypes.STRING
)

# Define the action that the block will perform
def mdrun_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_tpr_path_value = biobb_block.inputs["input_tpr_path"]
    
    input_cpt_path_value = biobb_block.inputs["input_cpt_path"]
    
    
    output_gro_path_value = biobb_block.inputs["output_gro_path"]
    
    output_edr_path_value = biobb_block.inputs["output_edr_path"]
    
    output_log_path_value = biobb_block.inputs["output_log_path"]
    
    output_trr_path_value = biobb_block.inputs["output_trr_path"]
    
    output_xtc_path_value = biobb_block.inputs["output_xtc_path"]
    
    output_cpt_path_value = biobb_block.inputs["output_cpt_path"]
    
    output_dhdl_path_value = biobb_block.inputs["output_dhdl_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["mpi_bin"] = biobb_block.variables["mpi_bin"]
    
    properties_values["mpi_np"] = biobb_block.variables["mpi_np"]
    
    properties_values["mpi_flags"] = biobb_block.variables["mpi_flags"]
    
    properties_values["checkpoint_time"] = biobb_block.variables["checkpoint_time"]
    
    properties_values["num_threads"] = biobb_block.variables["num_threads"]
    
    properties_values["num_threads_mpi"] = biobb_block.variables["num_threads_mpi"]
    
    properties_values["num_threads_omp"] = biobb_block.variables["num_threads_omp"]
    
    properties_values["num_threads_omp_pme"] = biobb_block.variables["num_threads_omp_pme"]
    
    properties_values["use_gpu"] = biobb_block.variables["use_gpu"]
    
    properties_values["gpu_id"] = biobb_block.variables["gpu_id"]
    
    properties_values["gpu_tasks"] = biobb_block.variables["gpu_tasks"]
    
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


    with open("mdrun.json", "w", encoding="utf-8") as f:
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
            "mdrun",
            "--config",
            "/tmp/mdrun.json",
            
            "--input_tpr_path",
            f"/tmp/{Path(input_tpr_path_value).name}",
            
            "--input_cpt_path",
            f"/tmp/{Path(input_cpt_path_value).name}",
            
            
            "--output_gro_path",
            f"/tmp/{Path(output_gro_path_value).name}",
            
            "--output_edr_path",
            f"/tmp/{Path(output_edr_path_value).name}",
            
            "--output_log_path",
            f"/tmp/{Path(output_log_path_value).name}",
            
            "--output_trr_path",
            f"/tmp/{Path(output_trr_path_value).name}",
            
            "--output_xtc_path",
            f"/tmp/{Path(output_xtc_path_value).name}",
            
            "--output_cpt_path",
            f"/tmp/{Path(output_cpt_path_value).name}",
            
            "--output_dhdl_path",
            f"/tmp/{Path(output_dhdl_path_value).name}",
            
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
        abs_path_out = Path(output_edr_path_value).absolute()
        abs_path_name = Path(Path(output_edr_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_edr_path_value).name}", output_edr_path_value)
        biobb_block.setOutput("output_edr_path", output_edr_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_log_path_value).absolute()
        abs_path_name = Path(Path(output_log_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_log_path_value).name}", output_log_path_value)
        biobb_block.setOutput("output_log_path", output_log_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_trr_path_value).absolute()
        abs_path_name = Path(Path(output_trr_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_trr_path_value).name}", output_trr_path_value)
        biobb_block.setOutput("output_trr_path", output_trr_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_xtc_path_value).absolute()
        abs_path_name = Path(Path(output_xtc_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_xtc_path_value).name}", output_xtc_path_value)
        biobb_block.setOutput("output_xtc_path", output_xtc_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_cpt_path_value).absolute()
        abs_path_name = Path(Path(output_cpt_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cpt_path_value).name}", output_cpt_path_value)
        biobb_block.setOutput("output_cpt_path", output_cpt_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_dhdl_path_value).absolute()
        abs_path_name = Path(Path(output_dhdl_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_dhdl_path_value).name}", output_dhdl_path_value)
        biobb_block.setOutput("output_dhdl_path", output_dhdl_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_tpr_path)

inputs_list.append(input_cpt_path)


outputs_list.append(output_gro_path)

outputs_list.append(output_edr_path)

outputs_list.append(output_log_path)

outputs_list.append(output_trr_path)

outputs_list.append(output_xtc_path)

outputs_list.append(output_cpt_path)

outputs_list.append(output_dhdl_path)


variables_list.append(mpi_bin)

variables_list.append(mpi_np)

variables_list.append(mpi_flags)

variables_list.append(checkpoint_time)

variables_list.append(num_threads)

variables_list.append(num_threads_mpi)

variables_list.append(num_threads_omp)

variables_list.append(num_threads_omp_pme)

variables_list.append(use_gpu)

variables_list.append(gpu_id)

variables_list.append(gpu_tasks)

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


mdrun_block = PluginBlock(
    # The name which will appear on the frontend
    name="mdrun",
    # Its description
    description="Wrapper of the GROMACS mdrun module.",
    # The action
    action=mdrun_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)