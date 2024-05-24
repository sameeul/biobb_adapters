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
    description="Input PDB file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_crd_path = PluginVariable(
    id="input_crd_path",  # ID of the variable, will allow us to identify the value
    name="input_crd_path",  # The name that will appear in the frontend
    description="Input Trajectory file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['crd', 'mdcrd', 'inpcrd']
)


output_pcz_path = PluginVariable(
    id="output_pcz_path",  # ID of the variable, will allow us to identify the value
    name="output_pcz_path",  # The name that will appear in the frontend
    description="Output compressed trajectory",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pcz']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="pcazip binary path to be used.",
    type=VariableTypes.STRING
)

neigenv = PluginVariable(
    id="neigenv",
    name="neigenv",
    description="Number of generated eigenvectors",
    type=VariableTypes.INTEGER
)

variance = PluginVariable(
    id="variance",
    name="variance",
    description="Percentage of variance captured by the final set of eigenvectors",
    type=VariableTypes.INTEGER
)

verbose = PluginVariable(
    id="verbose",
    name="verbose",
    description="Make output verbose",
    type=VariableTypes.BOOLEAN
)

gauss_rmsd = PluginVariable(
    id="gauss_rmsd",
    name="gauss_rmsd",
    description="Use a gaussian RMSd for fitting",
    type=VariableTypes.BOOLEAN
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
def pcz_zip_action(biobb_block: PluginBlock):

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
    
    input_crd_path_value = biobb_block.inputs["input_crd_path"]
    
    
    output_pcz_path_value = biobb_block.inputs["output_pcz_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["neigenv"] = biobb_block.variables["neigenv"]
    
    properties_values["variance"] = biobb_block.variables["variance"]
    
    properties_values["verbose"] = biobb_block.variables["verbose"]
    
    properties_values["gauss_rmsd"] = biobb_block.variables["gauss_rmsd"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("pcz_zip.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_flexserv:4.1.0--pypl5321hdfd78af_0",
            "pcz_zip",
            "--config",
            "/tmp/pcz_zip.json",
            
            "--input_pdb_path",
            f"/tmp/{Path(input_pdb_path_value).name}",
            
            "--input_crd_path",
            f"/tmp/{Path(input_crd_path_value).name}",
            
            
            "--output_pcz_path",
            f"/tmp/{Path(output_pcz_path_value).name}",
            
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
        abs_path_out = Path(output_pcz_path_value).absolute()
        abs_path_name = Path(Path(output_pcz_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pcz_path_value).name}", output_pcz_path_value)
        biobb_block.setOutput("output_pcz_path", output_pcz_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pdb_path)

inputs_list.append(input_crd_path)


outputs_list.append(output_pcz_path)


variables_list.append(binary_path)

variables_list.append(neigenv)

variables_list.append(variance)

variables_list.append(verbose)

variables_list.append(gauss_rmsd)

variables_list.append(remove_tmp)

variables_list.append(restart)


pcz_zip_block = PluginBlock(
    # The name which will appear on the frontend
    name="pcz_zip",
    # Its description
    description="Wrapper of the pcazip tool from the PCAsuite FlexServ module.",
    # The action
    action=pcz_zip_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)