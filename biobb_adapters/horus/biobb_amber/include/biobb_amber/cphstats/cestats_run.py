# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_cein_path = PluginVariable(
    id="input_cein_path",  # ID of the variable, will allow us to identify the value
    name="input_cein_path",  # The name that will appear in the frontend
    description="Input cein or cpein file (from pmemd or sander) with titrating residue information",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cein', 'cpein']
)

input_ceout_path = PluginVariable(
    id="input_ceout_path",  # ID of the variable, will allow us to identify the value
    name="input_ceout_path",  # The name that will appear in the frontend
    description="Output ceout file (AMBER ceout)",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ceout', 'zip', 'gzip', 'gz']
)


output_dat_path = PluginVariable(
    id="output_dat_path",  # ID of the variable, will allow us to identify the value
    name="output_dat_path",  # The name that will appear in the frontend
    description="Output file to which the standard calceo-type statistics are written",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'out', 'txt', 'o']
)

output_population_path = PluginVariable(
    id="output_population_path",  # ID of the variable, will allow us to identify the value
    name="output_population_path",  # The name that will appear in the frontend
    description="Output file where protonation state populations are printed for every state of every residue",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'out', 'txt', 'o']
)

output_chunk_path = PluginVariable(
    id="output_chunk_path",  # ID of the variable, will allow us to identify the value
    name="output_chunk_path",  # The name that will appear in the frontend
    description="Output file where the time series data calculated over chunks of the simulation are printed",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'out', 'txt', 'o']
)

output_cumulative_path = PluginVariable(
    id="output_cumulative_path",  # ID of the variable, will allow us to identify the value
    name="output_cumulative_path",  # The name that will appear in the frontend
    description="Output file where the cumulative time series data is printed",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'out', 'txt', 'o']
)

output_conditional_path = PluginVariable(
    id="output_conditional_path",  # ID of the variable, will allow us to identify the value
    name="output_conditional_path",  # The name that will appear in the frontend
    description="Output file with requested conditional probabilities",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'out', 'txt', 'o']
)

output_chunk_conditional_path = PluginVariable(
    id="output_chunk_conditional_path",  # ID of the variable, will allow us to identify the value
    name="output_chunk_conditional_path",  # The name that will appear in the frontend
    description="Output file with a time series of the conditional probabilities over a trajectory split up into chunks",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'out', 'txt', 'o']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

timestep = PluginVariable(
    id="timestep",
    name="timestep",
    description="Simulation time step -in ps-, used to print data as a function of time.",
    type=VariableTypes.NUMBER
)

verbose = PluginVariable(
    id="verbose",
    name="verbose",
    description="Controls how much information is printed to the calceo-style output file. Options are: False - Just print fraction protonated. True - Print everything calceo prints.",
    type=VariableTypes.BOOLEAN
)

interval = PluginVariable(
    id="interval",
    name="interval",
    description="Interval between which to print out time series data like chunks, cumulative data, and running averages. It is also used as the window of the conditional probability time series.",
    type=VariableTypes.INTEGER
)

reduced = PluginVariable(
    id="reduced",
    name="reduced",
    description="Print out reduction fraction instead of oxidation fraction in time series data.",
    type=VariableTypes.BOOLEAN
)

eos = PluginVariable(
    id="eos",
    name="eos",
    description="Print predicted Eos -via Nernst equation- in place of fraction reduced or oxidized.",
    type=VariableTypes.BOOLEAN
)

calceo = PluginVariable(
    id="calceo",
    name="calceo",
    description="Triggers the calceo-style output.",
    type=VariableTypes.BOOLEAN
)

running_avg_window = PluginVariable(
    id="running_avg_window",
    name="running_avg_window",
    description="Defines a window size -in MD steps- for a moving, running average time series.",
    type=VariableTypes.INTEGER
)

chunk_window = PluginVariable(
    id="chunk_window",
    name="chunk_window",
    description="Computes the time series data over a chunk of the simulation of this specified size -window- time steps.",
    type=VariableTypes.INTEGER
)

cumulative = PluginVariable(
    id="cumulative",
    name="cumulative",
    description="Computes the cumulative average time series data over the course of the trajectory.",
    type=VariableTypes.BOOLEAN
)

fix_remd = PluginVariable(
    id="fix_remd",
    name="fix_remd",
    description="This option will trigger cestats to reassemble the titration data into pH-specific ensembles. This is an exclusive mode of the program, no other analyses will be done.",
    type=VariableTypes.STRING
)

conditional = PluginVariable(
    id="conditional",
    name="conditional",
    description="Evaluates conditional probabilities. CONDITIONAL should be a string of the format: <resid>:<state>,<resid>:<state>,... or <resid>:PROT,<resid>:DEPROT,... or <resid>:<state1>;<state2>,<resid>:PROT,... where <resid> is the residue number in the prmtop and <state> is either the state number or -p-rotonated or -d-eprotonated, case-insensitive.",
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="Path to the cestats executable binary.",
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
def cestats_run_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_cein_path_value = biobb_block.inputs["input_cein_path"]
    
    input_ceout_path_value = biobb_block.inputs["input_ceout_path"]
    
    
    output_dat_path_value = biobb_block.inputs["output_dat_path"]
    
    output_population_path_value = biobb_block.inputs["output_population_path"]
    
    output_chunk_path_value = biobb_block.inputs["output_chunk_path"]
    
    output_cumulative_path_value = biobb_block.inputs["output_cumulative_path"]
    
    output_conditional_path_value = biobb_block.inputs["output_conditional_path"]
    
    output_chunk_conditional_path_value = biobb_block.inputs["output_chunk_conditional_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["timestep"] = biobb_block.variables["timestep"]
    
    properties_values["verbose"] = biobb_block.variables["verbose"]
    
    properties_values["interval"] = biobb_block.variables["interval"]
    
    properties_values["reduced"] = biobb_block.variables["reduced"]
    
    properties_values["eos"] = biobb_block.variables["eos"]
    
    properties_values["calceo"] = biobb_block.variables["calceo"]
    
    properties_values["running_avg_window"] = biobb_block.variables["running_avg_window"]
    
    properties_values["chunk_window"] = biobb_block.variables["chunk_window"]
    
    properties_values["cumulative"] = biobb_block.variables["cumulative"]
    
    properties_values["fix_remd"] = biobb_block.variables["fix_remd"]
    
    properties_values["conditional"] = biobb_block.variables["conditional"]
    
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


    with open("cestats_run.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_amber:4.2.0--pyhdfd78af_0",
            "cestats_run",
            "--config",
            "/tmp/cestats_run.json",
            
            "--input_cein_path",
            f"/tmp/{Path(input_cein_path_value).name}",
            
            "--input_ceout_path",
            f"/tmp/{Path(input_ceout_path_value).name}",
            
            
            "--output_dat_path",
            f"/tmp/{Path(output_dat_path_value).name}",
            
            "--output_population_path",
            f"/tmp/{Path(output_population_path_value).name}",
            
            "--output_chunk_path",
            f"/tmp/{Path(output_chunk_path_value).name}",
            
            "--output_cumulative_path",
            f"/tmp/{Path(output_cumulative_path_value).name}",
            
            "--output_conditional_path",
            f"/tmp/{Path(output_conditional_path_value).name}",
            
            "--output_chunk_conditional_path",
            f"/tmp/{Path(output_chunk_conditional_path_value).name}",
            
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
        abs_path_out = Path(output_dat_path_value).absolute()
        abs_path_name = Path(Path(output_dat_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_dat_path_value).name}", output_dat_path_value)
        biobb_block.setOutput("output_dat_path", output_dat_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_population_path_value).absolute()
        abs_path_name = Path(Path(output_population_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_population_path_value).name}", output_population_path_value)
        biobb_block.setOutput("output_population_path", output_population_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_chunk_path_value).absolute()
        abs_path_name = Path(Path(output_chunk_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_chunk_path_value).name}", output_chunk_path_value)
        biobb_block.setOutput("output_chunk_path", output_chunk_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_cumulative_path_value).absolute()
        abs_path_name = Path(Path(output_cumulative_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cumulative_path_value).name}", output_cumulative_path_value)
        biobb_block.setOutput("output_cumulative_path", output_cumulative_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_conditional_path_value).absolute()
        abs_path_name = Path(Path(output_conditional_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_conditional_path_value).name}", output_conditional_path_value)
        biobb_block.setOutput("output_conditional_path", output_conditional_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_chunk_conditional_path_value).absolute()
        abs_path_name = Path(Path(output_chunk_conditional_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_chunk_conditional_path_value).name}", output_chunk_conditional_path_value)
        biobb_block.setOutput("output_chunk_conditional_path", output_chunk_conditional_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_cein_path)

inputs_list.append(input_ceout_path)


outputs_list.append(output_dat_path)

outputs_list.append(output_population_path)

outputs_list.append(output_chunk_path)

outputs_list.append(output_cumulative_path)

outputs_list.append(output_conditional_path)

outputs_list.append(output_chunk_conditional_path)


variables_list.append(timestep)

variables_list.append(verbose)

variables_list.append(interval)

variables_list.append(reduced)

variables_list.append(eos)

variables_list.append(calceo)

variables_list.append(running_avg_window)

variables_list.append(chunk_window)

variables_list.append(cumulative)

variables_list.append(fix_remd)

variables_list.append(conditional)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


cestats_run_block = PluginBlock(
    # The name which will appear on the frontend
    name="cestats_run",
    # Its description
    description="Wrapper of the AmberTools (AMBER MD Package) cestats tool module.",
    # The action
    action=cestats_run_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)