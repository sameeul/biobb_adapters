# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_train_npy_path = PluginVariable(
    id="input_train_npy_path",  # ID of the variable, will allow us to identify the value
    name="input_train_npy_path",  # The name that will appear in the frontend
    description='Path to the input train data file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['npy']
)

input_model_pth_path = PluginVariable(
    id="input_model_pth_path",  # ID of the variable, will allow us to identify the value
    name="input_model_pth_path",  # The name that will appear in the frontend
    description='Path to the input model file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pth']
)


output_model_pth_path = PluginVariable(
    id="output_model_pth_path",  # ID of the variable, will allow us to identify the value
    name="output_model_pth_path",  # The name that will appear in the frontend
    description='Path to the output model file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pth']
)

output_train_data_npz_path = PluginVariable(
    id="output_train_data_npz_path",  # ID of the variable, will allow us to identify the value
    name="output_train_data_npz_path",  # The name that will appear in the frontend
    description='Path to the output train data file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['npz']
)

output_performance_npz_path = PluginVariable(
    id="output_performance_npz_path",  # ID of the variable, will allow us to identify the value
    name="output_performance_npz_path",  # The name that will appear in the frontend
    description='Path to the output performance file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['npz']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

latent_dimensions = PluginVariable(
    id="latent_dimensions",
    name="latent_dimensions",
    description='min dimensionality of the latent space.',
    type=VariableTypes.INTEGER
)

num_layers = PluginVariable(
    id="num_layers",
    name="num_layers",
    description='number of layers in the encoder/decoder (4 to encode and 4 to decode).',
    type=VariableTypes.INTEGER
)

num_epochs = PluginVariable(
    id="num_epochs",
    name="num_epochs",
    description='number of epochs (iterations of whole dataset) for training.',
    type=VariableTypes.INTEGER
)

lr = PluginVariable(
    id="lr",
    name="lr",
    description='learning rate.',
    type=VariableTypes.NUMBER
)

lr_step_size = PluginVariable(
    id="lr_step_size",
    name="lr_step_size",
    description='Period of learning rate decay.',
    type=VariableTypes.INTEGER
)

gamma = PluginVariable(
    id="gamma",
    name="gamma",
    description='Multiplicative factor of learning rate decay.',
    type=VariableTypes.NUMBER
)

checkpoint_interval = PluginVariable(
    id="checkpoint_interval",
    name="checkpoint_interval",
    description='number of epochs interval to save model checkpoints o 0 to disable.',
    type=VariableTypes.INTEGER
)

output_checkpoint_prefix = PluginVariable(
    id="output_checkpoint_prefix",
    name="output_checkpoint_prefix",
    description='prefix for the checkpoint files.',
    type=VariableTypes.STRING
)

partition = PluginVariable(
    id="partition",
    name="partition",
    description='0.8 = 80% partition of the data for training and validation.',
    type=VariableTypes.NUMBER
)

batch_size = PluginVariable(
    id="batch_size",
    name="batch_size",
    description='number of samples/frames per batch.',
    type=VariableTypes.INTEGER
)

log_interval = PluginVariable(
    id="log_interval",
    name="log_interval",
    description='number of epochs interval to log the training progress.',
    type=VariableTypes.INTEGER
)

input_dimensions = PluginVariable(
    id="input_dimensions",
    name="input_dimensions",
    description='input dimensions by default it should be the number of features in the input data (number of atoms * 3 corresponding to x, y, z coordinates).',
    type=VariableTypes.INTEGER
)

output_dimensions = PluginVariable(
    id="output_dimensions",
    name="output_dimensions",
    description='output dimensions by default it should be the number of features in the input data (number of atoms * 3 corresponding to x, y, z coordinates).',
    type=VariableTypes.INTEGER
)

loss_function = PluginVariable(
    id="loss_function",
    name="loss_function",
    description='Loss function to be used. ',
    type=VariableTypes.STRING
)

optimizer = PluginVariable(
    id="optimizer",
    name="optimizer",
    description='Optimizer algorithm to be used. ',
    type=VariableTypes.STRING
)

seed = PluginVariable(
    id="seed",
    name="seed",
    description='Random seed for reproducibility.',
    type=VariableTypes.INTEGER
)

# Define the action that the block will perform
def train_mdae_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_train_npy_path_value = biobb_block.inputs["input_train_npy_path"]
    
    input_model_pth_path_value = biobb_block.inputs["input_model_pth_path"]
    
    
    output_model_pth_path_value = biobb_block.inputs["output_model_pth_path"]
    
    output_train_data_npz_path_value = biobb_block.inputs["output_train_data_npz_path"]
    
    output_performance_npz_path_value = biobb_block.inputs["output_performance_npz_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["latent_dimensions"] = biobb_block.variables["latent_dimensions"]
    
    properties_values["num_layers"] = biobb_block.variables["num_layers"]
    
    properties_values["num_epochs"] = biobb_block.variables["num_epochs"]
    
    properties_values["lr"] = biobb_block.variables["lr"]
    
    properties_values["lr_step_size"] = biobb_block.variables["lr_step_size"]
    
    properties_values["gamma"] = biobb_block.variables["gamma"]
    
    properties_values["checkpoint_interval"] = biobb_block.variables["checkpoint_interval"]
    
    properties_values["output_checkpoint_prefix"] = biobb_block.variables["output_checkpoint_prefix"]
    
    properties_values["partition"] = biobb_block.variables["partition"]
    
    properties_values["batch_size"] = biobb_block.variables["batch_size"]
    
    properties_values["log_interval"] = biobb_block.variables["log_interval"]
    
    properties_values["input_dimensions"] = biobb_block.variables["input_dimensions"]
    
    properties_values["output_dimensions"] = biobb_block.variables["output_dimensions"]
    
    properties_values["loss_function"] = biobb_block.variables["loss_function"]
    
    properties_values["optimizer"] = biobb_block.variables["optimizer"]
    
    properties_values["seed"] = biobb_block.variables["seed"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("train_mdae.json", "w", encoding="utf-8") as f:
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
            "train_mdae",
            "--config",
            "/tmp/train_mdae.json",
            
            "--input_train_npy_path",
            f"/tmp/{Path(input_train_npy_path_value).name}",
            
            "--input_model_pth_path",
            f"/tmp/{Path(input_model_pth_path_value).name}",
            
            
            "--output_model_pth_path",
            f"/tmp/{Path(output_model_pth_path_value).name}",
            
            "--output_train_data_npz_path",
            f"/tmp/{Path(output_train_data_npz_path_value).name}",
            
            "--output_performance_npz_path",
            f"/tmp/{Path(output_performance_npz_path_value).name}",
            
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
        abs_path_out = Path(output_model_pth_path_value).absolute()
        abs_path_name = Path(Path(output_model_pth_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_model_pth_path_value).name}", output_model_pth_path_value)
        biobb_block.setOutput("output_model_pth_path", output_model_pth_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_train_data_npz_path_value).absolute()
        abs_path_name = Path(Path(output_train_data_npz_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_train_data_npz_path_value).name}", output_train_data_npz_path_value)
        biobb_block.setOutput("output_train_data_npz_path", output_train_data_npz_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_performance_npz_path_value).absolute()
        abs_path_name = Path(Path(output_performance_npz_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_performance_npz_path_value).name}", output_performance_npz_path_value)
        biobb_block.setOutput("output_performance_npz_path", output_performance_npz_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_train_npy_path)

inputs_list.append(input_model_pth_path)


outputs_list.append(output_model_pth_path)

outputs_list.append(output_train_data_npz_path)

outputs_list.append(output_performance_npz_path)


variables_list.append(latent_dimensions)

variables_list.append(num_layers)

variables_list.append(num_epochs)

variables_list.append(lr)

variables_list.append(lr_step_size)

variables_list.append(gamma)

variables_list.append(checkpoint_interval)

variables_list.append(output_checkpoint_prefix)

variables_list.append(partition)

variables_list.append(batch_size)

variables_list.append(log_interval)

variables_list.append(input_dimensions)

variables_list.append(output_dimensions)

variables_list.append(loss_function)

variables_list.append(optimizer)

variables_list.append(seed)


train_mdae_block = PluginBlock(
    # The name which will appear on the frontend
    name="train_mdae",
    # Its description
    description='Train a Molecular Dynamics AutoEncoder (MDAE) PyTorch model.',
    # The action
    action=train_mdae_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)