# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_data_npy_path = PluginVariable(
    id="input_data_npy_path",  # ID of the variable, will allow us to identify the value
    name="input_data_npy_path",  # The name that will appear in the frontend
    description="Path to the input data file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['npy']
)

input_model_pth_path = PluginVariable(
    id="input_model_pth_path",  # ID of the variable, will allow us to identify the value
    name="input_model_pth_path",  # The name that will appear in the frontend
    description="Path to the input model file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pth']
)


output_reconstructed_data_npy_path = PluginVariable(
    id="output_reconstructed_data_npy_path",  # ID of the variable, will allow us to identify the value
    name="output_reconstructed_data_npy_path",  # The name that will appear in the frontend
    description="Path to the output reconstructed data file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['npy']
)

output_latent_space_npy_path = PluginVariable(
    id="output_latent_space_npy_path",  # ID of the variable, will allow us to identify the value
    name="output_latent_space_npy_path",  # The name that will appear in the frontend
    description="Path to the reduced dimensionality file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['npy']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

batch_size = PluginVariable(
    id="batch_size",
    name="batch_size",
    description="number of samples/frames per batch.",
    type=VariableTypes.INTEGER
)

latent_dimensions = PluginVariable(
    id="latent_dimensions",
    name="latent_dimensions",
    description="min dimensionality of the latent space.",
    type=VariableTypes.INTEGER
)

num_layers = PluginVariable(
    id="num_layers",
    name="num_layers",
    description="number of layers in the encoder/decoder (4 to encode and 4 to decode).",
    type=VariableTypes.INTEGER
)

input_dimensions = PluginVariable(
    id="input_dimensions",
    name="input_dimensions",
    description="input dimensions by default it should be the number of features in the input data (number of atoms * 3 corresponding to x, y, z coordinates).",
    type=VariableTypes.INTEGER
)

output_dimensions = PluginVariable(
    id="output_dimensions",
    name="output_dimensions",
    description="output dimensions by default it should be the number of features in the input data (number of atoms * 3 corresponding to x, y, z coordinates).",
    type=VariableTypes.INTEGER
)

# Define the action that the block will perform
def apply_mdae_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_data_npy_path_value = biobb_block.inputs["input_data_npy_path"]
    
    input_model_pth_path_value = biobb_block.inputs["input_model_pth_path"]
    
    
    output_reconstructed_data_npy_path_value = biobb_block.inputs["output_reconstructed_data_npy_path"]
    
    output_latent_space_npy_path_value = biobb_block.inputs["output_latent_space_npy_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["batch_size"] = biobb_block.variables["batch_size"]
    
    properties_values["latent_dimensions"] = biobb_block.variables["latent_dimensions"]
    
    properties_values["num_layers"] = biobb_block.variables["num_layers"]
    
    properties_values["input_dimensions"] = biobb_block.variables["input_dimensions"]
    
    properties_values["output_dimensions"] = biobb_block.variables["output_dimensions"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("apply_mdae.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_pytorch:4.1.3--pyhdfd78af_0",
            "apply_mdae",
            "--config",
            "/tmp/apply_mdae.json",
            
            "--input_data_npy_path",
            f"/tmp/{Path(input_data_npy_path_value).name}",
            
            "--input_model_pth_path",
            f"/tmp/{Path(input_model_pth_path_value).name}",
            
            
            "--output_reconstructed_data_npy_path",
            f"/tmp/{Path(output_reconstructed_data_npy_path_value).name}",
            
            "--output_latent_space_npy_path",
            f"/tmp/{Path(output_latent_space_npy_path_value).name}",
            
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
        abs_path_out = Path(output_reconstructed_data_npy_path_value).absolute()
        abs_path_name = Path(Path(output_reconstructed_data_npy_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_reconstructed_data_npy_path_value).name}", output_reconstructed_data_npy_path_value)
        biobb_block.setOutput("output_reconstructed_data_npy_path", output_reconstructed_data_npy_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_latent_space_npy_path_value).absolute()
        abs_path_name = Path(Path(output_latent_space_npy_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_latent_space_npy_path_value).name}", output_latent_space_npy_path_value)
        biobb_block.setOutput("output_latent_space_npy_path", output_latent_space_npy_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_data_npy_path)

inputs_list.append(input_model_pth_path)


outputs_list.append(output_reconstructed_data_npy_path)

outputs_list.append(output_latent_space_npy_path)


variables_list.append(batch_size)

variables_list.append(latent_dimensions)

variables_list.append(num_layers)

variables_list.append(input_dimensions)

variables_list.append(output_dimensions)


apply_mdae_block = PluginBlock(
    # The name which will appear on the frontend
    name="apply_mdae",
    # Its description
    description="Apply a Molecular Dynamics AutoEncoder (MDAE) PyTorch model.",
    # The action
    action=apply_mdae_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)