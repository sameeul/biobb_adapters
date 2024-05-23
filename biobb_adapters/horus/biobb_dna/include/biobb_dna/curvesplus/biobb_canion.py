# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_cdi_path = PluginVariable(
    id="input_cdi_path",  # ID of the variable, will allow us to identify the value
    name="input_cdi_path",  # The name that will appear in the frontend
    description='Trajectory input file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cdi']
)

input_afr_path = PluginVariable(
    id="input_afr_path",  # ID of the variable, will allow us to identify the value
    name="input_afr_path",  # The name that will appear in the frontend
    description='Helical axis frames corresponding to the input conformation to be analyzed',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['afr']
)

input_avg_struc_path = PluginVariable(
    id="input_avg_struc_path",  # ID of the variable, will allow us to identify the value
    name="input_avg_struc_path",  # The name that will appear in the frontend
    description='Average DNA conformation',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)


output_zip_path = PluginVariable(
    id="output_zip_path",  # ID of the variable, will allow us to identify the value
    name="output_zip_path",  # The name that will appear in the frontend
    description='Filename for .zip files containing Canion output files',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

bases = PluginVariable(
    id="bases",
    name="bases",
    description='Sequence of bases to be analyzed (default is blank, meaning no specified sequence).',
    type=VariableTypes.STRING
)

type = PluginVariable(
    id="type",
    name="type",
    description='Ions (or atoms) to be analyzed. Options are 'Na+', 'K', 'K+', 'Cl', 'Cl-', 'CL', 'P', 'C1*', 'NH1', 'NH2', 'NZ', '1' for all cations, '-1' for all anions, '0' for neutral species or '*' for all available data.',
    type=VariableTypes.STRING
)

dlow = PluginVariable(
    id="dlow",
    name="dlow",
    description='Select starting segment of the oglimer to analyze. If both dhig and dlow are 0, entire oglimer is analyzed.',
    type=VariableTypes.NUMBER
)

dhig = PluginVariable(
    id="dhig",
    name="dhig",
    description='Select ending segment of the oglimer to analyze, being the maximum value the total number of base pairs in the oligomer. If both dhig and dlow are 0, entire oglimer is analyzed.',
    type=VariableTypes.NUMBER
)

rlow = PluginVariable(
    id="rlow",
    name="rlow",
    description='Minimal distances from the helical axis taken into account in the analysis.',
    type=VariableTypes.NUMBER
)

rhig = PluginVariable(
    id="rhig",
    name="rhig",
    description='Maximal distances from the helical axis taken into account in the analysis.',
    type=VariableTypes.NUMBER
)

alow = PluginVariable(
    id="alow",
    name="alow",
    description='Minimal angle range to analyze.',
    type=VariableTypes.NUMBER
)

ahig = PluginVariable(
    id="ahig",
    name="ahig",
    description='Maximal angle range to analyze.',
    type=VariableTypes.NUMBER
)

itst = PluginVariable(
    id="itst",
    name="itst",
    description='Number of first snapshot to be analyzed.',
    type=VariableTypes.INTEGER
)

itnd = PluginVariable(
    id="itnd",
    name="itnd",
    description='Number of last snapshot to be analyzed.',
    type=VariableTypes.INTEGER
)

itdel = PluginVariable(
    id="itdel",
    name="itdel",
    description='Spacing between analyzed snapshots.',
    type=VariableTypes.INTEGER
)

rmsf = PluginVariable(
    id="rmsf",
    name="rmsf",
    description='If set to True uses the combination of the helical ion parameters and an average helical axis to map the ions into Cartesian space and then calculates their average position (pdb output) and their root mean square fluctuation values (rmsf output). A single pass rmsf algorithm to make this calculation possible with a single read of the trajectory file. This option is generally used for solute atoms and not for solvent molecules or ions.',
    type=VariableTypes.BOOLEAN
)

circ = PluginVariable(
    id="circ",
    name="circ",
    description='If set to True, minicircles are analyzed.',
    type=VariableTypes.BOOLEAN
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to Canion executable, otherwise the program wil look for Canion executable in the binaries folder.',
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

# Define the action that the block will perform
def biobb_canion_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_cdi_path_value = biobb_block.inputs["input_cdi_path"]
    
    input_afr_path_value = biobb_block.inputs["input_afr_path"]
    
    input_avg_struc_path_value = biobb_block.inputs["input_avg_struc_path"]
    
    
    output_zip_path_value = biobb_block.inputs["output_zip_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["bases"] = biobb_block.variables["bases"]
    
    properties_values["type"] = biobb_block.variables["type"]
    
    properties_values["dlow"] = biobb_block.variables["dlow"]
    
    properties_values["dhig"] = biobb_block.variables["dhig"]
    
    properties_values["rlow"] = biobb_block.variables["rlow"]
    
    properties_values["rhig"] = biobb_block.variables["rhig"]
    
    properties_values["alow"] = biobb_block.variables["alow"]
    
    properties_values["ahig"] = biobb_block.variables["ahig"]
    
    properties_values["itst"] = biobb_block.variables["itst"]
    
    properties_values["itnd"] = biobb_block.variables["itnd"]
    
    properties_values["itdel"] = biobb_block.variables["itdel"]
    
    properties_values["rmsf"] = biobb_block.variables["rmsf"]
    
    properties_values["circ"] = biobb_block.variables["circ"]
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("biobb_canion.json", "w", encoding="utf-8") as f:
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
            "quay.io/biocontainers/biobb_gromacs:4.1.1--pyhdfd78af_0",
            "biobb_canion",
            "--config",
            "/tmp/biobb_canion.json",
            
            "--input_cdi_path",
            f"/tmp/{Path(input_cdi_path_value).name}",
            
            "--input_afr_path",
            f"/tmp/{Path(input_afr_path_value).name}",
            
            "--input_avg_struc_path",
            f"/tmp/{Path(input_avg_struc_path_value).name}",
            
            
            "--output_zip_path",
            f"/tmp/{Path(output_zip_path_value).name}",
            
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
        abs_path_out = Path(output_zip_path_value).absolute()
        abs_path_name = Path(Path(output_zip_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_zip_path_value).name}", output_zip_path_value)
        biobb_block.setOutput("output_zip_path", output_zip_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_cdi_path)

inputs_list.append(input_afr_path)

inputs_list.append(input_avg_struc_path)


outputs_list.append(output_zip_path)


variables_list.append(bases)

variables_list.append(type)

variables_list.append(dlow)

variables_list.append(dhig)

variables_list.append(rlow)

variables_list.append(rhig)

variables_list.append(alow)

variables_list.append(ahig)

variables_list.append(itst)

variables_list.append(itnd)

variables_list.append(itdel)

variables_list.append(rmsf)

variables_list.append(circ)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)


biobb_canion_block = PluginBlock(
    # The name which will appear on the frontend
    name="biobb_canion",
    # Its description
    description='Wrapper for the Canion executable  that is part of the Curves+ software suite.',
    # The action
    action=biobb_canion_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)