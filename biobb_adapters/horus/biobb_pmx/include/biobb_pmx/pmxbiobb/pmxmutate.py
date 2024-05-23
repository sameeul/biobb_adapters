# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_structure_path = PluginVariable(
    id="input_structure_path",  # ID of the variable, will allow us to identify the value
    name="input_structure_path",  # The name that will appear in the frontend
    description='Path to the input structure file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'gro']
)

input_b_structure_path = PluginVariable(
    id="input_b_structure_path",  # ID of the variable, will allow us to identify the value
    name="input_b_structure_path",  # The name that will appear in the frontend
    description='Path to the mutated input structure file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'gro']
)


output_structure_path = PluginVariable(
    id="output_structure_path",  # ID of the variable, will allow us to identify the value
    name="output_structure_path",  # The name that will appear in the frontend
    description='Path to the output structure file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'gro']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

mutation_list = PluginVariable(
    id="mutation_list",
    name="mutation_list",
    description='Mutation list in the format "Chain:Resnum MUT_AA_Code" or "Chain:Resnum MUT_NA_Code"  (no spaces between the elements) separated by commas. If no chain is provided as chain code all the chains in the pdb file will be mutated. ie: "A:15CYS". Possible MUT_AA_Code: 'ALA', 'ARG', 'ASN', 'ASP', 'ASPH', 'ASPP', 'ASH', 'CYS', 'CYS2', 'CYN', 'CYX', 'CYM', 'CYSH', 'GLU', 'GLUH', 'GLUP', 'GLH', 'GLN', 'GLY', 'HIS', 'HIE', 'HISE', 'HSE', 'HIP', 'HSP', 'HISH', 'HID', 'HSD', 'ILE', 'LEU', 'LYS', 'LYSH', 'LYP', 'LYN', 'LSN', 'MET', 'PHE', 'PRO', 'SER', 'SP1', 'SP2', 'THR', 'TRP', 'TYR', 'VAL'. Possible MUT_NA_Codes: 'A', 'T', 'C', 'G', 'U'.',
    type=VariableTypes.STRING
)

force_field = PluginVariable(
    id="force_field",
    name="force_field",
    description='Forcefield to use.',
    type=VariableTypes.STRING
)

resinfo = PluginVariable(
    id="resinfo",
    name="resinfo",
    description='Show the list of 3-letter -> 1-letter residues.',
    type=VariableTypes.BOOLEAN
)

gmx_lib = PluginVariable(
    id="gmx_lib",
    name="gmx_lib",
    description='Path to the GMXLIB folder in your computer.',
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to the PMX command line interface.',
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
def pmxmutate_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_structure_path_value = biobb_block.inputs["input_structure_path"]
    
    input_b_structure_path_value = biobb_block.inputs["input_b_structure_path"]
    
    
    output_structure_path_value = biobb_block.inputs["output_structure_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["mutation_list"] = biobb_block.variables["mutation_list"]
    
    properties_values["force_field"] = biobb_block.variables["force_field"]
    
    properties_values["resinfo"] = biobb_block.variables["resinfo"]
    
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


    with open("pmxmutate.json", "w", encoding="utf-8") as f:
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
            "pmxmutate",
            "--config",
            "/tmp/pmxmutate.json",
            
            "--input_structure_path",
            f"/tmp/{Path(input_structure_path_value).name}",
            
            "--input_b_structure_path",
            f"/tmp/{Path(input_b_structure_path_value).name}",
            
            
            "--output_structure_path",
            f"/tmp/{Path(output_structure_path_value).name}",
            
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
        abs_path_out = Path(output_structure_path_value).absolute()
        abs_path_name = Path(Path(output_structure_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_structure_path_value).name}", output_structure_path_value)
        biobb_block.setOutput("output_structure_path", output_structure_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_structure_path)

inputs_list.append(input_b_structure_path)


outputs_list.append(output_structure_path)


variables_list.append(mutation_list)

variables_list.append(force_field)

variables_list.append(resinfo)

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


pmxmutate_block = PluginBlock(
    # The name which will appear on the frontend
    name="pmxmutate",
    # Its description
    description='Wrapper class for the PMX mutate module.',
    # The action
    action=pmxmutate_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)