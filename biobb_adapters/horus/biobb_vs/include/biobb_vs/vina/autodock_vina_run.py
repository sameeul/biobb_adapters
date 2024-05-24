# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_ligand_pdbqt_path = PluginVariable(
    id="input_ligand_pdbqt_path",  # ID of the variable, will allow us to identify the value
    name="input_ligand_pdbqt_path",  # The name that will appear in the frontend
    description="Path to the input PDBQT ligand",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdbqt']
)

input_receptor_pdbqt_path = PluginVariable(
    id="input_receptor_pdbqt_path",  # ID of the variable, will allow us to identify the value
    name="input_receptor_pdbqt_path",  # The name that will appear in the frontend
    description="Path to the input PDBQT receptor",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdbqt']
)

input_box_path = PluginVariable(
    id="input_box_path",  # ID of the variable, will allow us to identify the value
    name="input_box_path",  # The name that will appear in the frontend
    description="Path to the PDB containig the residues belonging to the binding site",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)


output_pdbqt_path = PluginVariable(
    id="output_pdbqt_path",  # ID of the variable, will allow us to identify the value
    name="output_pdbqt_path",  # The name that will appear in the frontend
    description="Path to the output PDBQT file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdbqt']
)

output_log_path = PluginVariable(
    id="output_log_path",  # ID of the variable, will allow us to identify the value
    name="output_log_path",  # The name that will appear in the frontend
    description="Path to the log file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['log']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

cpu = PluginVariable(
    id="cpu",
    name="cpu",
    description="the number of CPUs to use.",
    type=VariableTypes.INTEGER
)

exhaustiveness = PluginVariable(
    id="exhaustiveness",
    name="exhaustiveness",
    description="exhaustiveness of the global search (roughly proportional to time).",
    type=VariableTypes.INTEGER
)

num_modes = PluginVariable(
    id="num_modes",
    name="num_modes",
    description="maximum number of binding modes to generate.",
    type=VariableTypes.INTEGER
)

min_rmsd = PluginVariable(
    id="min_rmsd",
    name="min_rmsd",
    description="minimum RMSD between output poses.",
    type=VariableTypes.INTEGER
)

energy_range = PluginVariable(
    id="energy_range",
    name="energy_range",
    description="maximum energy difference between the best binding mode and the worst one displayed (kcal/mol).",
    type=VariableTypes.INTEGER
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="path to vina in your local computer.",
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
def autodock_vina_run_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_ligand_pdbqt_path_value = biobb_block.inputs["input_ligand_pdbqt_path"]
    
    input_receptor_pdbqt_path_value = biobb_block.inputs["input_receptor_pdbqt_path"]
    
    input_box_path_value = biobb_block.inputs["input_box_path"]
    
    
    output_pdbqt_path_value = biobb_block.inputs["output_pdbqt_path"]
    
    output_log_path_value = biobb_block.inputs["output_log_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["cpu"] = biobb_block.variables["cpu"]
    
    properties_values["exhaustiveness"] = biobb_block.variables["exhaustiveness"]
    
    properties_values["num_modes"] = biobb_block.variables["num_modes"]
    
    properties_values["min_rmsd"] = biobb_block.variables["min_rmsd"]
    
    properties_values["energy_range"] = biobb_block.variables["energy_range"]
    
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


    with open("autodock_vina_run.json", "w", encoding="utf-8") as f:
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
            "autodock_vina_run",
            "--config",
            "/tmp/autodock_vina_run.json",
            
            "--input_ligand_pdbqt_path",
            f"/tmp/{Path(input_ligand_pdbqt_path_value).name}",
            
            "--input_receptor_pdbqt_path",
            f"/tmp/{Path(input_receptor_pdbqt_path_value).name}",
            
            "--input_box_path",
            f"/tmp/{Path(input_box_path_value).name}",
            
            
            "--output_pdbqt_path",
            f"/tmp/{Path(output_pdbqt_path_value).name}",
            
            "--output_log_path",
            f"/tmp/{Path(output_log_path_value).name}",
            
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
        abs_path_out = Path(output_pdbqt_path_value).absolute()
        abs_path_name = Path(Path(output_pdbqt_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pdbqt_path_value).name}", output_pdbqt_path_value)
        biobb_block.setOutput("output_pdbqt_path", output_pdbqt_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_log_path_value).absolute()
        abs_path_name = Path(Path(output_log_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_log_path_value).name}", output_log_path_value)
        biobb_block.setOutput("output_log_path", output_log_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_ligand_pdbqt_path)

inputs_list.append(input_receptor_pdbqt_path)

inputs_list.append(input_box_path)


outputs_list.append(output_pdbqt_path)

outputs_list.append(output_log_path)


variables_list.append(cpu)

variables_list.append(exhaustiveness)

variables_list.append(num_modes)

variables_list.append(min_rmsd)

variables_list.append(energy_range)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


autodock_vina_run_block = PluginBlock(
    # The name which will appear on the frontend
    name="autodock_vina_run",
    # Its description
    description="Wrapper of the AutoDock Vina software.",
    # The action
    action=autodock_vina_run_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)