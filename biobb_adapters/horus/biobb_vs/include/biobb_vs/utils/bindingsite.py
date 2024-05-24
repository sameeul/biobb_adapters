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
    description="Path to the PDB structure where the binding site is to be found",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_clusters_zip = PluginVariable(
    id="input_clusters_zip",  # ID of the variable, will allow us to identify the value
    name="input_clusters_zip",  # The name that will appear in the frontend
    description="Path to the ZIP file with all the PDB members of the identity cluster",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)


output_pdb_path = PluginVariable(
    id="output_pdb_path",  # ID of the variable, will allow us to identify the value
    name="output_pdb_path",  # The name that will appear in the frontend
    description="Path to the PDB containig the residues belonging to the binding site",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

ligand = PluginVariable(
    id="ligand",
    name="ligand",
    description="Ligand to be found in the protein structure. If no ligand provided, the largest one will be selected, if more than one.",
    type=VariableTypes.STRING
)

radius = PluginVariable(
    id="radius",
    name="radius",
    description="Cut-off distance (Ångstroms) around ligand atoms to consider a protein atom as a binding site atom.",
    type=VariableTypes.NUMBER
)

max_num_ligands = PluginVariable(
    id="max_num_ligands",
    name="max_num_ligands",
    description="Total number of superimposed ligands to be extracted from the identity cluster. For populated clusters, the restriction avoids to superimpose redundant structures. If 0, all ligands extracted will be considered.",
    type=VariableTypes.INTEGER
)

matrix_name = PluginVariable(
    id="matrix_name",
    name="matrix_name",
    description="Substitution matrices for use in alignments. ",
    type=VariableTypes.STRING
)

gap_open = PluginVariable(
    id="gap_open",
    name="gap_open",
    description="Gap open penalty.",
    type=VariableTypes.NUMBER
)

gap_extend = PluginVariable(
    id="gap_extend",
    name="gap_extend",
    description="Gap extend penalty.",
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

# Define the action that the block will perform
def bindingsite_action(biobb_block: PluginBlock):

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
    
    input_clusters_zip_value = biobb_block.inputs["input_clusters_zip"]
    
    
    output_pdb_path_value = biobb_block.inputs["output_pdb_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["ligand"] = biobb_block.variables["ligand"]
    
    properties_values["radius"] = biobb_block.variables["radius"]
    
    properties_values["max_num_ligands"] = biobb_block.variables["max_num_ligands"]
    
    properties_values["matrix_name"] = biobb_block.variables["matrix_name"]
    
    properties_values["gap_open"] = biobb_block.variables["gap_open"]
    
    properties_values["gap_extend"] = biobb_block.variables["gap_extend"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("bindingsite.json", "w", encoding="utf-8") as f:
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
            "bindingsite",
            "--config",
            "/tmp/bindingsite.json",
            
            "--input_pdb_path",
            f"/tmp/{Path(input_pdb_path_value).name}",
            
            "--input_clusters_zip",
            f"/tmp/{Path(input_clusters_zip_value).name}",
            
            
            "--output_pdb_path",
            f"/tmp/{Path(output_pdb_path_value).name}",
            
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
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pdb_path)

inputs_list.append(input_clusters_zip)


outputs_list.append(output_pdb_path)


variables_list.append(ligand)

variables_list.append(radius)

variables_list.append(max_num_ligands)

variables_list.append(matrix_name)

variables_list.append(gap_open)

variables_list.append(gap_extend)

variables_list.append(remove_tmp)

variables_list.append(restart)


bindingsite_block = PluginBlock(
    # The name which will appear on the frontend
    name="bindingsite",
    # Its description
    description="This class finds the binding site of the input_pdb.",
    # The action
    action=bindingsite_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)