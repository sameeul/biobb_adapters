# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_struc_path = PluginVariable(
    id="input_struc_path",  # ID of the variable, will allow us to identify the value
    name="input_struc_path",  # The name that will appear in the frontend
    description='Trajectory or PDB input file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['trj', 'pdb', 'netcdf', 'nc']
)

input_top_path = PluginVariable(
    id="input_top_path",  # ID of the variable, will allow us to identify the value
    name="input_top_path",  # The name that will appear in the frontend
    description='Topology file, needed along with .trj file (optional)',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['top']
)


output_cda_path = PluginVariable(
    id="output_cda_path",  # ID of the variable, will allow us to identify the value
    name="output_cda_path",  # The name that will appear in the frontend
    description='Filename for Curves+ output .cda file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cda']
)

output_lis_path = PluginVariable(
    id="output_lis_path",  # ID of the variable, will allow us to identify the value
    name="output_lis_path",  # The name that will appear in the frontend
    description='Filename for Curves+ output .lis file',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['lis']
)

output_zip_path = PluginVariable(
    id="output_zip_path",  # ID of the variable, will allow us to identify the value
    name="output_zip_path",  # The name that will appear in the frontend
    description='Filename for .zip files containing Curves+ output that is not .cda or .lis files',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

s1range = PluginVariable(
    id="s1range",
    name="s1range",
    description='Range of first strand. Must be specified in the form "start:end".',
    type=VariableTypes.STRING
)

s2range = PluginVariable(
    id="s2range",
    name="s2range",
    description='Range of second strand. Must be specified in the form "start:end".',
    type=VariableTypes.STRING
)

stdlib_path = PluginVariable(
    id="stdlib_path",
    name="stdlib_path",
    description='Path to Curves' standard library files for nucleotides. If not specified will look for 'standard' files in current directory.',
    type=VariableTypes.STRING
)

itst = PluginVariable(
    id="itst",
    name="itst",
    description='Iteration start index.',
    type=VariableTypes.INTEGER
)

itnd = PluginVariable(
    id="itnd",
    name="itnd",
    description='Iteration end index.',
    type=VariableTypes.INTEGER
)

itdel = PluginVariable(
    id="itdel",
    name="itdel",
    description='Iteration delimiter.',
    type=VariableTypes.INTEGER
)

ions = PluginVariable(
    id="ions",
    name="ions",
    description='If True, helicoidal analysis of ions (or solvent molecules) around solute is carried out.',
    type=VariableTypes.BOOLEAN
)

test = PluginVariable(
    id="test",
    name="test",
    description='If True, provide addition output in .lis file on fitting and axis generation.',
    type=VariableTypes.BOOLEAN
)

line = PluginVariable(
    id="line",
    name="line",
    description='if True, find the best linear helical axis.',
    type=VariableTypes.BOOLEAN
)

fit = PluginVariable(
    id="fit",
    name="fit",
    description='if True, fit a standard bases to the input coordinates (important for MD snapshots to avoid base distortions leading to noisy helical parameters).',
    type=VariableTypes.BOOLEAN
)

axfrm = PluginVariable(
    id="axfrm",
    name="axfrm",
    description='if True, generates closely spaced helical axis frames as input for Canal and Canion.',
    type=VariableTypes.BOOLEAN
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to Curves+ executable, otherwise the program wil look for Cur+ executable in the binaries folder.',
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
def biobb_curves_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_struc_path_value = biobb_block.inputs["input_struc_path"]
    
    input_top_path_value = biobb_block.inputs["input_top_path"]
    
    
    output_cda_path_value = biobb_block.inputs["output_cda_path"]
    
    output_lis_path_value = biobb_block.inputs["output_lis_path"]
    
    output_zip_path_value = biobb_block.inputs["output_zip_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["s1range"] = biobb_block.variables["s1range"]
    
    properties_values["s2range"] = biobb_block.variables["s2range"]
    
    properties_values["stdlib_path"] = biobb_block.variables["stdlib_path"]
    
    properties_values["itst"] = biobb_block.variables["itst"]
    
    properties_values["itnd"] = biobb_block.variables["itnd"]
    
    properties_values["itdel"] = biobb_block.variables["itdel"]
    
    properties_values["ions"] = biobb_block.variables["ions"]
    
    properties_values["test"] = biobb_block.variables["test"]
    
    properties_values["line"] = biobb_block.variables["line"]
    
    properties_values["fit"] = biobb_block.variables["fit"]
    
    properties_values["axfrm"] = biobb_block.variables["axfrm"]
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("biobb_curves.json", "w", encoding="utf-8") as f:
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
            "biobb_curves",
            "--config",
            "/tmp/biobb_curves.json",
            
            "--input_struc_path",
            f"/tmp/{Path(input_struc_path_value).name}",
            
            "--input_top_path",
            f"/tmp/{Path(input_top_path_value).name}",
            
            
            "--output_cda_path",
            f"/tmp/{Path(output_cda_path_value).name}",
            
            "--output_lis_path",
            f"/tmp/{Path(output_lis_path_value).name}",
            
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
        abs_path_out = Path(output_cda_path_value).absolute()
        abs_path_name = Path(Path(output_cda_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_cda_path_value).name}", output_cda_path_value)
        biobb_block.setOutput("output_cda_path", output_cda_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_lis_path_value).absolute()
        abs_path_name = Path(Path(output_lis_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_lis_path_value).name}", output_lis_path_value)
        biobb_block.setOutput("output_lis_path", output_lis_path_value)
        
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

inputs_list.append(input_struc_path)

inputs_list.append(input_top_path)


outputs_list.append(output_cda_path)

outputs_list.append(output_lis_path)

outputs_list.append(output_zip_path)


variables_list.append(s1range)

variables_list.append(s2range)

variables_list.append(stdlib_path)

variables_list.append(itst)

variables_list.append(itnd)

variables_list.append(itdel)

variables_list.append(ions)

variables_list.append(test)

variables_list.append(line)

variables_list.append(fit)

variables_list.append(axfrm)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)


biobb_curves_block = PluginBlock(
    # The name which will appear on the frontend
    name="biobb_curves",
    # Its description
    description='Wrapper for the Cur+ executable  that is part of the Curves+ software suite.',
    # The action
    action=biobb_curves_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)