# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_structure1_path = PluginVariable(
    id="input_structure1_path",  # ID of the variable, will allow us to identify the value
    name="input_structure1_path",  # The name that will appear in the frontend
    description="Path to the input ligand structure file 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_structure2_path = PluginVariable(
    id="input_structure2_path",  # ID of the variable, will allow us to identify the value
    name="input_structure2_path",  # The name that will appear in the frontend
    description="Path to the input ligand structure file 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_topology1_path = PluginVariable(
    id="input_topology1_path",  # ID of the variable, will allow us to identify the value
    name="input_topology1_path",  # The name that will appear in the frontend
    description="Path to the input ligand topology file 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['itp']
)

input_topology2_path = PluginVariable(
    id="input_topology2_path",  # ID of the variable, will allow us to identify the value
    name="input_topology2_path",  # The name that will appear in the frontend
    description="Path to the input ligand topology file 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['itp']
)

input_pairs_path = PluginVariable(
    id="input_pairs_path",  # ID of the variable, will allow us to identify the value
    name="input_pairs_path",  # The name that will appear in the frontend
    description="Path to the input atom pair mapping",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt']
)

input_scaffold1_path = PluginVariable(
    id="input_scaffold1_path",  # ID of the variable, will allow us to identify the value
    name="input_scaffold1_path",  # The name that will appear in the frontend
    description="Path to the index of atoms to consider for the ligand structure 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ndx']
)

input_scaffold2_path = PluginVariable(
    id="input_scaffold2_path",  # ID of the variable, will allow us to identify the value
    name="input_scaffold2_path",  # The name that will appear in the frontend
    description="Path to the index of atoms to consider for the ligand structure 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ndx']
)


output_log_path = PluginVariable(
    id="output_log_path",  # ID of the variable, will allow us to identify the value
    name="output_log_path",  # The name that will appear in the frontend
    description="Path to the log file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['log', 'txt', 'out']
)

output_structure1_path = PluginVariable(
    id="output_structure1_path",  # ID of the variable, will allow us to identify the value
    name="output_structure1_path",  # The name that will appear in the frontend
    description="Path to the output hybrid structure based on the ligand 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_structure2_path = PluginVariable(
    id="output_structure2_path",  # ID of the variable, will allow us to identify the value
    name="output_structure2_path",  # The name that will appear in the frontend
    description="Path to the output hybrid structure based on the ligand 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_topology_path = PluginVariable(
    id="output_topology_path",  # ID of the variable, will allow us to identify the value
    name="output_topology_path",  # The name that will appear in the frontend
    description="Path to the output hybrid topology",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['itp']
)

output_atomtypes_path = PluginVariable(
    id="output_atomtypes_path",  # ID of the variable, will allow us to identify the value
    name="output_atomtypes_path",  # The name that will appear in the frontend
    description="Path to the atom types for the output hybrid topology",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['itp']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

fit = PluginVariable(
    id="fit",
    name="fit",
    description="Fit ligand structure 1 onto ligand structure 2 (Only used if input_pairs_path is provided).",
    type=VariableTypes.BOOLEAN
)

split = PluginVariable(
    id="split",
    name="split",
    description="Split the topology into separate transitions.",
    type=VariableTypes.BOOLEAN
)

scDUMm = PluginVariable(
    id="scDUMm",
    name="scDUMm",
    description="Scale dummy masses using the counterpart atoms.",
    type=VariableTypes.NUMBER
)

scDUMa = PluginVariable(
    id="scDUMa",
    name="scDUMa",
    description="Scale bonded dummy angle parameters.",
    type=VariableTypes.NUMBER
)

scDUMd = PluginVariable(
    id="scDUMd",
    name="scDUMd",
    description="Scale bonded dummy dihedral parameters.",
    type=VariableTypes.NUMBER
)

deAng = PluginVariable(
    id="deAng",
    name="deAng",
    description="Decouple angles composed of 1 dummy and 2 non-dummies.",
    type=VariableTypes.BOOLEAN
)

distance = PluginVariable(
    id="distance",
    name="distance",
    description="Distance (nm) between atoms to consider them morphable for alignment approach (Only used if input_pairs_path is not provided).",
    type=VariableTypes.NUMBER
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
def pmxligand_hybrid_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_structure1_path_value = biobb_block.inputs["input_structure1_path"]
    
    input_structure2_path_value = biobb_block.inputs["input_structure2_path"]
    
    input_topology1_path_value = biobb_block.inputs["input_topology1_path"]
    
    input_topology2_path_value = biobb_block.inputs["input_topology2_path"]
    
    input_pairs_path_value = biobb_block.inputs["input_pairs_path"]
    
    input_scaffold1_path_value = biobb_block.inputs["input_scaffold1_path"]
    
    input_scaffold2_path_value = biobb_block.inputs["input_scaffold2_path"]
    
    
    output_log_path_value = biobb_block.inputs["output_log_path"]
    
    output_structure1_path_value = biobb_block.inputs["output_structure1_path"]
    
    output_structure2_path_value = biobb_block.inputs["output_structure2_path"]
    
    output_topology_path_value = biobb_block.inputs["output_topology_path"]
    
    output_atomtypes_path_value = biobb_block.inputs["output_atomtypes_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["fit"] = biobb_block.variables["fit"]
    
    properties_values["split"] = biobb_block.variables["split"]
    
    properties_values["scDUMm"] = biobb_block.variables["scDUMm"]
    
    properties_values["scDUMa"] = biobb_block.variables["scDUMa"]
    
    properties_values["scDUMd"] = biobb_block.variables["scDUMd"]
    
    properties_values["deAng"] = biobb_block.variables["deAng"]
    
    properties_values["distance"] = biobb_block.variables["distance"]
    
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


    with open("pmxligand_hybrid.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_pmx:4.1.0--pyhdfd78af_0",
            "pmxligand_hybrid",
            "--config",
            "/tmp/pmxligand_hybrid.json",
            
            "--input_structure1_path",
            f"/tmp/{Path(input_structure1_path_value).name}",
            
            "--input_structure2_path",
            f"/tmp/{Path(input_structure2_path_value).name}",
            
            "--input_topology1_path",
            f"/tmp/{Path(input_topology1_path_value).name}",
            
            "--input_topology2_path",
            f"/tmp/{Path(input_topology2_path_value).name}",
            
            "--input_pairs_path",
            f"/tmp/{Path(input_pairs_path_value).name}",
            
            "--input_scaffold1_path",
            f"/tmp/{Path(input_scaffold1_path_value).name}",
            
            "--input_scaffold2_path",
            f"/tmp/{Path(input_scaffold2_path_value).name}",
            
            
            "--output_log_path",
            f"/tmp/{Path(output_log_path_value).name}",
            
            "--output_structure1_path",
            f"/tmp/{Path(output_structure1_path_value).name}",
            
            "--output_structure2_path",
            f"/tmp/{Path(output_structure2_path_value).name}",
            
            "--output_topology_path",
            f"/tmp/{Path(output_topology_path_value).name}",
            
            "--output_atomtypes_path",
            f"/tmp/{Path(output_atomtypes_path_value).name}",
            
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
        abs_path_out = Path(output_structure1_path_value).absolute()
        abs_path_name = Path(Path(output_structure1_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_structure1_path_value).name}", output_structure1_path_value)
        biobb_block.setOutput("output_structure1_path", output_structure1_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_structure2_path_value).absolute()
        abs_path_name = Path(Path(output_structure2_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_structure2_path_value).name}", output_structure2_path_value)
        biobb_block.setOutput("output_structure2_path", output_structure2_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_topology_path_value).absolute()
        abs_path_name = Path(Path(output_topology_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_topology_path_value).name}", output_topology_path_value)
        biobb_block.setOutput("output_topology_path", output_topology_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_atomtypes_path_value).absolute()
        abs_path_name = Path(Path(output_atomtypes_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_atomtypes_path_value).name}", output_atomtypes_path_value)
        biobb_block.setOutput("output_atomtypes_path", output_atomtypes_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_structure1_path)

inputs_list.append(input_structure2_path)

inputs_list.append(input_topology1_path)

inputs_list.append(input_topology2_path)

inputs_list.append(input_pairs_path)

inputs_list.append(input_scaffold1_path)

inputs_list.append(input_scaffold2_path)


outputs_list.append(output_log_path)

outputs_list.append(output_structure1_path)

outputs_list.append(output_structure2_path)

outputs_list.append(output_topology_path)

outputs_list.append(output_atomtypes_path)


variables_list.append(fit)

variables_list.append(split)

variables_list.append(scDUMm)

variables_list.append(scDUMa)

variables_list.append(scDUMd)

variables_list.append(deAng)

variables_list.append(distance)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


pmxligand_hybrid_block = PluginBlock(
    # The name which will appear on the frontend
    name="pmxligand_hybrid",
    # Its description
    description="Wrapper class for the PMX ligand_hybrid module.",
    # The action
    action=pmxligand_hybrid_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)