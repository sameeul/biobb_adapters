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
    description='Input structure file in PDB format',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_dat_path = PluginVariable(
    id="input_dat_path",  # ID of the variable, will allow us to identify the value
    name="input_dat_path",  # The name that will appear in the frontend
    description='Input dat with structure interpretation and bond definitions',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt']
)


output_traj_path = PluginVariable(
    id="output_traj_path",  # ID of the variable, will allow us to identify the value
    name="output_traj_path",  # The name that will appear in the frontend
    description='Output trajectory file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb', 'xtc', 'gro']
)

output_rmsd_path = PluginVariable(
    id="output_rmsd_path",  # ID of the variable, will allow us to identify the value
    name="output_rmsd_path",  # The name that will appear in the frontend
    description='Output rmsd file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat']
)

output_bfactor_path = PluginVariable(
    id="output_bfactor_path",  # ID of the variable, will allow us to identify the value
    name="output_bfactor_path",  # The name that will appear in the frontend
    description='Output B-factor file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Concoord disco binary path to be used.',
    type=VariableTypes.STRING
)

vdw = PluginVariable(
    id="vdw",
    name="vdw",
    description='Select a set of Van der Waals parameters. ',
    type=VariableTypes.INTEGER
)

num_structs = PluginVariable(
    id="num_structs",
    name="num_structs",
    description='Number of structures to be generated',
    type=VariableTypes.INTEGER
)

num_iterations = PluginVariable(
    id="num_iterations",
    name="num_iterations",
    description='Maximum number of iterations per structure',
    type=VariableTypes.INTEGER
)

chirality_check = PluginVariable(
    id="chirality_check",
    name="chirality_check",
    description='Chirality check. ',
    type=VariableTypes.INTEGER
)

bs = PluginVariable(
    id="bs",
    name="bs",
    description='Number of rounds of triangular bound smoothing (default 0), (if >= 6, tetragonal BS is activated)',
    type=VariableTypes.INTEGER
)

nofit = PluginVariable(
    id="nofit",
    name="nofit",
    description='Do not fit generated structures to reference',
    type=VariableTypes.BOOLEAN
)

seed = PluginVariable(
    id="seed",
    name="seed",
    description='Initial random seed',
    type=VariableTypes.INTEGER
)

violation = PluginVariable(
    id="violation",
    name="violation",
    description='Maximal acceptable sum of violations (nm)',
    type=VariableTypes.NUMBER
)

convergence = PluginVariable(
    id="convergence",
    name="convergence",
    description='Consider convergence failed after this number of non-productive iterations',
    type=VariableTypes.INTEGER
)

trials = PluginVariable(
    id="trials",
    name="trials",
    description='Maximum number of trials per run',
    type=VariableTypes.INTEGER
)

damp = PluginVariable(
    id="damp",
    name="damp",
    description='Damping factor for distance corrections. ',
    type=VariableTypes.INTEGER
)

dyn = PluginVariable(
    id="dyn",
    name="dyn",
    description='Number of rounds to dynamically set tolerances',
    type=VariableTypes.INTEGER
)

bump = PluginVariable(
    id="bump",
    name="bump",
    description='Do extra bump check',
    type=VariableTypes.BOOLEAN
)

pairlist_freq = PluginVariable(
    id="pairlist_freq",
    name="pairlist_freq",
    description='Pairlist update frequency in steps (only valid together with bump)',
    type=VariableTypes.INTEGER
)

cutoff = PluginVariable(
    id="cutoff",
    name="cutoff",
    description='Cut-off radius for pairlist (nm) (only valid together with bump)',
    type=VariableTypes.NUMBER
)

ref = PluginVariable(
    id="ref",
    name="ref",
    description='Use input coordinates instead of random starting coordinates',
    type=VariableTypes.BOOLEAN
)

scale = PluginVariable(
    id="scale",
    name="scale",
    description='Pre-scale coordinates with this factor',
    type=VariableTypes.INTEGER
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
def concoord_disco_action(biobb_block: PluginBlock):

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
    
    input_dat_path_value = biobb_block.inputs["input_dat_path"]
    
    
    output_traj_path_value = biobb_block.inputs["output_traj_path"]
    
    output_rmsd_path_value = biobb_block.inputs["output_rmsd_path"]
    
    output_bfactor_path_value = biobb_block.inputs["output_bfactor_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["vdw"] = biobb_block.variables["vdw"]
    
    properties_values["num_structs"] = biobb_block.variables["num_structs"]
    
    properties_values["num_iterations"] = biobb_block.variables["num_iterations"]
    
    properties_values["chirality_check"] = biobb_block.variables["chirality_check"]
    
    properties_values["bs"] = biobb_block.variables["bs"]
    
    properties_values["nofit"] = biobb_block.variables["nofit"]
    
    properties_values["seed"] = biobb_block.variables["seed"]
    
    properties_values["violation"] = biobb_block.variables["violation"]
    
    properties_values["convergence"] = biobb_block.variables["convergence"]
    
    properties_values["trials"] = biobb_block.variables["trials"]
    
    properties_values["damp"] = biobb_block.variables["damp"]
    
    properties_values["dyn"] = biobb_block.variables["dyn"]
    
    properties_values["bump"] = biobb_block.variables["bump"]
    
    properties_values["pairlist_freq"] = biobb_block.variables["pairlist_freq"]
    
    properties_values["cutoff"] = biobb_block.variables["cutoff"]
    
    properties_values["ref"] = biobb_block.variables["ref"]
    
    properties_values["scale"] = biobb_block.variables["scale"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("concoord_disco.json", "w", encoding="utf-8") as f:
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
            "concoord_disco",
            "--config",
            "/tmp/concoord_disco.json",
            
            "--input_pdb_path",
            f"/tmp/{Path(input_pdb_path_value).name}",
            
            "--input_dat_path",
            f"/tmp/{Path(input_dat_path_value).name}",
            
            
            "--output_traj_path",
            f"/tmp/{Path(output_traj_path_value).name}",
            
            "--output_rmsd_path",
            f"/tmp/{Path(output_rmsd_path_value).name}",
            
            "--output_bfactor_path",
            f"/tmp/{Path(output_bfactor_path_value).name}",
            
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
        abs_path_out = Path(output_traj_path_value).absolute()
        abs_path_name = Path(Path(output_traj_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_traj_path_value).name}", output_traj_path_value)
        biobb_block.setOutput("output_traj_path", output_traj_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_rmsd_path_value).absolute()
        abs_path_name = Path(Path(output_rmsd_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_rmsd_path_value).name}", output_rmsd_path_value)
        biobb_block.setOutput("output_rmsd_path", output_rmsd_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_bfactor_path_value).absolute()
        abs_path_name = Path(Path(output_bfactor_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_bfactor_path_value).name}", output_bfactor_path_value)
        biobb_block.setOutput("output_bfactor_path", output_bfactor_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pdb_path)

inputs_list.append(input_dat_path)


outputs_list.append(output_traj_path)

outputs_list.append(output_rmsd_path)

outputs_list.append(output_bfactor_path)


variables_list.append(binary_path)

variables_list.append(vdw)

variables_list.append(num_structs)

variables_list.append(num_iterations)

variables_list.append(chirality_check)

variables_list.append(bs)

variables_list.append(nofit)

variables_list.append(seed)

variables_list.append(violation)

variables_list.append(convergence)

variables_list.append(trials)

variables_list.append(damp)

variables_list.append(dyn)

variables_list.append(bump)

variables_list.append(pairlist_freq)

variables_list.append(cutoff)

variables_list.append(ref)

variables_list.append(scale)

variables_list.append(remove_tmp)

variables_list.append(restart)


concoord_disco_block = PluginBlock(
    # The name which will appear on the frontend
    name="concoord_disco",
    # Its description
    description='Wrapper of the Disco tool from the Concoord package.',
    # The action
    action=concoord_disco_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)