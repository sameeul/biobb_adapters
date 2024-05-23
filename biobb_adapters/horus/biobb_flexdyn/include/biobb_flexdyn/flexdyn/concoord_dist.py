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
    description='Input structure file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'gro']
)


output_pdb_path = PluginVariable(
    id="output_pdb_path",  # ID of the variable, will allow us to identify the value
    name="output_pdb_path",  # The name that will appear in the frontend
    description='Output pdb file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_gro_path = PluginVariable(
    id="output_gro_path",  # ID of the variable, will allow us to identify the value
    name="output_gro_path",  # The name that will appear in the frontend
    description='Output gro file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['gro']
)

output_dat_path = PluginVariable(
    id="output_dat_path",  # ID of the variable, will allow us to identify the value
    name="output_dat_path",  # The name that will appear in the frontend
    description='Output dat with structure interpretation and bond definitions',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Concoord dist binary path to be used.',
    type=VariableTypes.STRING
)

vdw = PluginVariable(
    id="vdw",
    name="vdw",
    description='Select a set of Van der Waals parameters. ',
    type=VariableTypes.INTEGER
)

bond_angle = PluginVariable(
    id="bond_angle",
    name="bond_angle",
    description='Select a set of bond/angle parameters. ',
    type=VariableTypes.INTEGER
)

retain_hydrogens = PluginVariable(
    id="retain_hydrogens",
    name="retain_hydrogens",
    description='Retain hydrogen atoms',
    type=VariableTypes.BOOLEAN
)

nb_interactions = PluginVariable(
    id="nb_interactions",
    name="nb_interactions",
    description='Try to find alternatives for non-bonded interactions (by default the native contacts will be preserved)',
    type=VariableTypes.BOOLEAN
)

cutoff = PluginVariable(
    id="cutoff",
    name="cutoff",
    description='cut-off radius (Angstroms) for non-bonded interacting pairs (the cut-off distances are additional to the sum of VDW radii)',
    type=VariableTypes.NUMBER
)

min_distances = PluginVariable(
    id="min_distances",
    name="min_distances",
    description='Minimum number of distances to be defined for each atom',
    type=VariableTypes.INTEGER
)

damp = PluginVariable(
    id="damp",
    name="damp",
    description='Multiply each distance margin by this value',
    type=VariableTypes.NUMBER
)

fixed_atoms = PluginVariable(
    id="fixed_atoms",
    name="fixed_atoms",
    description='Interpret zero occupancy as atoms to keep fixed',
    type=VariableTypes.BOOLEAN
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

# Define the action that the block will perform
def concoord_dist_action(biobb_block: PluginBlock):

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
    
    
    output_pdb_path_value = biobb_block.inputs["output_pdb_path"]
    
    output_gro_path_value = biobb_block.inputs["output_gro_path"]
    
    output_dat_path_value = biobb_block.inputs["output_dat_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["vdw"] = biobb_block.variables["vdw"]
    
    properties_values["bond_angle"] = biobb_block.variables["bond_angle"]
    
    properties_values["retain_hydrogens"] = biobb_block.variables["retain_hydrogens"]
    
    properties_values["nb_interactions"] = biobb_block.variables["nb_interactions"]
    
    properties_values["cutoff"] = biobb_block.variables["cutoff"]
    
    properties_values["min_distances"] = biobb_block.variables["min_distances"]
    
    properties_values["damp"] = biobb_block.variables["damp"]
    
    properties_values["fixed_atoms"] = biobb_block.variables["fixed_atoms"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("concoord_dist.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_flexdyn:4.1.0--pyhdfd78af_0",
            "concoord_dist",
            "--config",
            "/tmp/concoord_dist.json",
            
            "--input_structure_path",
            f"/tmp/{Path(input_structure_path_value).name}",
            
            
            "--output_pdb_path",
            f"/tmp/{Path(output_pdb_path_value).name}",
            
            "--output_gro_path",
            f"/tmp/{Path(output_gro_path_value).name}",
            
            "--output_dat_path",
            f"/tmp/{Path(output_dat_path_value).name}",
            
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
        abs_path_out = Path(output_gro_path_value).absolute()
        abs_path_name = Path(Path(output_gro_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_gro_path_value).name}", output_gro_path_value)
        biobb_block.setOutput("output_gro_path", output_gro_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_dat_path_value).absolute()
        abs_path_name = Path(Path(output_dat_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_dat_path_value).name}", output_dat_path_value)
        biobb_block.setOutput("output_dat_path", output_dat_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_structure_path)


outputs_list.append(output_pdb_path)

outputs_list.append(output_gro_path)

outputs_list.append(output_dat_path)


variables_list.append(binary_path)

variables_list.append(vdw)

variables_list.append(bond_angle)

variables_list.append(retain_hydrogens)

variables_list.append(nb_interactions)

variables_list.append(cutoff)

variables_list.append(min_distances)

variables_list.append(damp)

variables_list.append(fixed_atoms)

variables_list.append(remove_tmp)

variables_list.append(restart)


concoord_dist_block = PluginBlock(
    # The name which will appear on the frontend
    name="concoord_dist",
    # Its description
    description='Wrapper of the Dist tool from the Concoord package.',
    # The action
    action=concoord_dist_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)