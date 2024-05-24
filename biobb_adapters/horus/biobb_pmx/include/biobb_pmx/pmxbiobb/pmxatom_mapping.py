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


output_pairs1_path = PluginVariable(
    id="output_pairs1_path",  # ID of the variable, will allow us to identify the value
    name="output_pairs1_path",  # The name that will appear in the frontend
    description="Path to the output pairs for the ligand structure 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt']
)

output_pairs2_path = PluginVariable(
    id="output_pairs2_path",  # ID of the variable, will allow us to identify the value
    name="output_pairs2_path",  # The name that will appear in the frontend
    description="Path to the output pairs for the ligand structure 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt']
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
    description="Path to the superimposed structure for the ligand structure 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_structure2_path = PluginVariable(
    id="output_structure2_path",  # ID of the variable, will allow us to identify the value
    name="output_structure2_path",  # The name that will appear in the frontend
    description="Path to the superimposed structure for the ligand structure 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_morph1_path = PluginVariable(
    id="output_morph1_path",  # ID of the variable, will allow us to identify the value
    name="output_morph1_path",  # The name that will appear in the frontend
    description="Path to the morphable atoms for the ligand structure 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_morph2_path = PluginVariable(
    id="output_morph2_path",  # ID of the variable, will allow us to identify the value
    name="output_morph2_path",  # The name that will appear in the frontend
    description="Path to the morphable atoms for the ligand structure 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_scaffold1_path = PluginVariable(
    id="output_scaffold1_path",  # ID of the variable, will allow us to identify the value
    name="output_scaffold1_path",  # The name that will appear in the frontend
    description="Path to the index of atoms to consider for the ligand structure 1",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ndx']
)

output_scaffold2_path = PluginVariable(
    id="output_scaffold2_path",  # ID of the variable, will allow us to identify the value
    name="output_scaffold2_path",  # The name that will appear in the frontend
    description="Path to the index of atoms to consider for the ligand structure 2",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['ndx']
)

output_score_path = PluginVariable(
    id="output_score_path",  # ID of the variable, will allow us to identify the value
    name="output_score_path",  # The name that will appear in the frontend
    description="Path to the morphing score",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['dat', 'txt']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

noalignment = PluginVariable(
    id="noalignment",
    name="noalignment",
    description="Should the alignment method be disabled.",
    type=VariableTypes.BOOLEAN
)

nomcs = PluginVariable(
    id="nomcs",
    name="nomcs",
    description="Should the MCS method be disabled.",
    type=VariableTypes.BOOLEAN
)

noH2H = PluginVariable(
    id="noH2H",
    name="noH2H",
    description="Should non-polar hydrogens be discarded from morphing into any other hydrogen.",
    type=VariableTypes.BOOLEAN
)

H2Hpolar = PluginVariable(
    id="H2Hpolar",
    name="H2Hpolar",
    description="Should polar hydrogens be morphed into polar hydrogens.",
    type=VariableTypes.BOOLEAN
)

H2Heavy = PluginVariable(
    id="H2Heavy",
    name="H2Heavy",
    description="Should hydrogen be morphed into a heavy atom.",
    type=VariableTypes.BOOLEAN
)

RingsOnly = PluginVariable(
    id="RingsOnly",
    name="RingsOnly",
    description="Should rings only be used in the MCS search and alignemnt.",
    type=VariableTypes.BOOLEAN
)

dMCS = PluginVariable(
    id="dMCS",
    name="dMCS",
    description="Should the distance criterium be also applied in the MCS based search.",
    type=VariableTypes.BOOLEAN
)

swap = PluginVariable(
    id="swap",
    name="swap",
    description="Try swapping the molecule order which would be a cross-check and require double execution time.",
    type=VariableTypes.BOOLEAN
)

nochirality = PluginVariable(
    id="nochirality",
    name="nochirality",
    description="Perform chirality check for MCS mapping.",
    type=VariableTypes.BOOLEAN
)

distance = PluginVariable(
    id="distance",
    name="distance",
    description="Distance (nm) between atoms to consider them morphable for alignment approach.",
    type=VariableTypes.NUMBER
)

timeout = PluginVariable(
    id="timeout",
    name="timeout",
    description="Maximum time (s) for an MCS search.",
    type=VariableTypes.INTEGER
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
def pmxatom_mapping_action(biobb_block: PluginBlock):

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
    
    
    output_pairs1_path_value = biobb_block.inputs["output_pairs1_path"]
    
    output_pairs2_path_value = biobb_block.inputs["output_pairs2_path"]
    
    output_log_path_value = biobb_block.inputs["output_log_path"]
    
    output_structure1_path_value = biobb_block.inputs["output_structure1_path"]
    
    output_structure2_path_value = biobb_block.inputs["output_structure2_path"]
    
    output_morph1_path_value = biobb_block.inputs["output_morph1_path"]
    
    output_morph2_path_value = biobb_block.inputs["output_morph2_path"]
    
    output_scaffold1_path_value = biobb_block.inputs["output_scaffold1_path"]
    
    output_scaffold2_path_value = biobb_block.inputs["output_scaffold2_path"]
    
    output_score_path_value = biobb_block.inputs["output_score_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["noalignment"] = biobb_block.variables["noalignment"]
    
    properties_values["nomcs"] = biobb_block.variables["nomcs"]
    
    properties_values["noH2H"] = biobb_block.variables["noH2H"]
    
    properties_values["H2Hpolar"] = biobb_block.variables["H2Hpolar"]
    
    properties_values["H2Heavy"] = biobb_block.variables["H2Heavy"]
    
    properties_values["RingsOnly"] = biobb_block.variables["RingsOnly"]
    
    properties_values["dMCS"] = biobb_block.variables["dMCS"]
    
    properties_values["swap"] = biobb_block.variables["swap"]
    
    properties_values["nochirality"] = biobb_block.variables["nochirality"]
    
    properties_values["distance"] = biobb_block.variables["distance"]
    
    properties_values["timeout"] = biobb_block.variables["timeout"]
    
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


    with open("pmxatom_mapping.json", "w", encoding="utf-8") as f:
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
            "pmxatom_mapping",
            "--config",
            "/tmp/pmxatom_mapping.json",
            
            "--input_structure1_path",
            f"/tmp/{Path(input_structure1_path_value).name}",
            
            "--input_structure2_path",
            f"/tmp/{Path(input_structure2_path_value).name}",
            
            
            "--output_pairs1_path",
            f"/tmp/{Path(output_pairs1_path_value).name}",
            
            "--output_pairs2_path",
            f"/tmp/{Path(output_pairs2_path_value).name}",
            
            "--output_log_path",
            f"/tmp/{Path(output_log_path_value).name}",
            
            "--output_structure1_path",
            f"/tmp/{Path(output_structure1_path_value).name}",
            
            "--output_structure2_path",
            f"/tmp/{Path(output_structure2_path_value).name}",
            
            "--output_morph1_path",
            f"/tmp/{Path(output_morph1_path_value).name}",
            
            "--output_morph2_path",
            f"/tmp/{Path(output_morph2_path_value).name}",
            
            "--output_scaffold1_path",
            f"/tmp/{Path(output_scaffold1_path_value).name}",
            
            "--output_scaffold2_path",
            f"/tmp/{Path(output_scaffold2_path_value).name}",
            
            "--output_score_path",
            f"/tmp/{Path(output_score_path_value).name}",
            
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
        abs_path_out = Path(output_pairs1_path_value).absolute()
        abs_path_name = Path(Path(output_pairs1_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pairs1_path_value).name}", output_pairs1_path_value)
        biobb_block.setOutput("output_pairs1_path", output_pairs1_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_pairs2_path_value).absolute()
        abs_path_name = Path(Path(output_pairs2_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pairs2_path_value).name}", output_pairs2_path_value)
        biobb_block.setOutput("output_pairs2_path", output_pairs2_path_value)
        
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
        abs_path_out = Path(output_morph1_path_value).absolute()
        abs_path_name = Path(Path(output_morph1_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_morph1_path_value).name}", output_morph1_path_value)
        biobb_block.setOutput("output_morph1_path", output_morph1_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_morph2_path_value).absolute()
        abs_path_name = Path(Path(output_morph2_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_morph2_path_value).name}", output_morph2_path_value)
        biobb_block.setOutput("output_morph2_path", output_morph2_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_scaffold1_path_value).absolute()
        abs_path_name = Path(Path(output_scaffold1_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_scaffold1_path_value).name}", output_scaffold1_path_value)
        biobb_block.setOutput("output_scaffold1_path", output_scaffold1_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_scaffold2_path_value).absolute()
        abs_path_name = Path(Path(output_scaffold2_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_scaffold2_path_value).name}", output_scaffold2_path_value)
        biobb_block.setOutput("output_scaffold2_path", output_scaffold2_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_score_path_value).absolute()
        abs_path_name = Path(Path(output_score_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_score_path_value).name}", output_score_path_value)
        biobb_block.setOutput("output_score_path", output_score_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_structure1_path)

inputs_list.append(input_structure2_path)


outputs_list.append(output_pairs1_path)

outputs_list.append(output_pairs2_path)

outputs_list.append(output_log_path)

outputs_list.append(output_structure1_path)

outputs_list.append(output_structure2_path)

outputs_list.append(output_morph1_path)

outputs_list.append(output_morph2_path)

outputs_list.append(output_scaffold1_path)

outputs_list.append(output_scaffold2_path)

outputs_list.append(output_score_path)


variables_list.append(noalignment)

variables_list.append(nomcs)

variables_list.append(noH2H)

variables_list.append(H2Hpolar)

variables_list.append(H2Heavy)

variables_list.append(RingsOnly)

variables_list.append(dMCS)

variables_list.append(swap)

variables_list.append(nochirality)

variables_list.append(distance)

variables_list.append(timeout)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


pmxatom_mapping_block = PluginBlock(
    # The name which will appear on the frontend
    name="pmxatom_mapping",
    # Its description
    description="Wrapper class for the PMX atom_mapping module.",
    # The action
    action=pmxatom_mapping_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)