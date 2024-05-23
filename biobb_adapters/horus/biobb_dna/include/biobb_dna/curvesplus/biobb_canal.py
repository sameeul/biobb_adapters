# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_cda_file = PluginVariable(
    id="input_cda_file",  # ID of the variable, will allow us to identify the value
    name="input_cda_file",  # The name that will appear in the frontend
    description='Input cda file, from Cur+ output',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['cda']
)

input_lis_file = PluginVariable(
    id="input_lis_file",  # ID of the variable, will allow us to identify the value
    name="input_lis_file",  # The name that will appear in the frontend
    description='Input lis file, from Cur+ output',  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['lis']
)


output_zip_path = PluginVariable(
    id="output_zip_path",  # ID of the variable, will allow us to identify the value
    name="output_zip_path",  # The name that will appear in the frontend
    description='zip filename for output files',  # The description that will appear in the frontend
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
    description='sequence of bases to be searched for in the I/P data (default is blank, meaning no specified sequence).',
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

lev1 = PluginVariable(
    id="lev1",
    name="lev1",
    description='Lower base level limit (i.e. base pairs) used for analysis.',
    type=VariableTypes.INTEGER
)

lev2 = PluginVariable(
    id="lev2",
    name="lev2",
    description='Upper base level limit used for analysis. If lev1 > 0 and lev2 = 0, lev2 is set to lev1 (i.e. analyze lev1 only). If lev1=lev2=0, lev1 is set to 1 and lev2 is set to the length of the oligmer (i.e. analyze all levels).',
    type=VariableTypes.INTEGER
)

nastr = PluginVariable(
    id="nastr",
    name="nastr",
    description='character string used to indicate missing data in .ser files.',
    type=VariableTypes.STRING
)

cormin = PluginVariable(
    id="cormin",
    name="cormin",
    description='minimal absolute value for printing linear correlation coefficients between pairs of analyzed variables.',
    type=VariableTypes.NUMBER
)

series = PluginVariable(
    id="series",
    name="series",
    description='if True then output spatial or time series data. Only possible for the analysis of single structures or single trajectories.',
    type=VariableTypes.STRING
)

histo = PluginVariable(
    id="histo",
    name="histo",
    description='if True then output histogram data.',
    type=VariableTypes.STRING
)

corr = PluginVariable(
    id="corr",
    name="corr",
    description='if True than output linear correlation coefficients between all variables.',
    type=VariableTypes.STRING
)

sequence = PluginVariable(
    id="sequence",
    name="sequence",
    description='sequence of the first strand of the corresponding DNA fragment, for each .cda file. If not given it will be parsed from .lis file.',
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description='Path to Canal executable, otherwise the program wil look for Canal executable in the binaries folder.',
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
def biobb_canal_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_cda_file_value = biobb_block.inputs["input_cda_file"]
    
    input_lis_file_value = biobb_block.inputs["input_lis_file"]
    
    
    output_zip_path_value = biobb_block.inputs["output_zip_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["bases"] = biobb_block.variables["bases"]
    
    properties_values["itst"] = biobb_block.variables["itst"]
    
    properties_values["itnd"] = biobb_block.variables["itnd"]
    
    properties_values["itdel"] = biobb_block.variables["itdel"]
    
    properties_values["lev1"] = biobb_block.variables["lev1"]
    
    properties_values["lev2"] = biobb_block.variables["lev2"]
    
    properties_values["nastr"] = biobb_block.variables["nastr"]
    
    properties_values["cormin"] = biobb_block.variables["cormin"]
    
    properties_values["series"] = biobb_block.variables["series"]
    
    properties_values["histo"] = biobb_block.variables["histo"]
    
    properties_values["corr"] = biobb_block.variables["corr"]
    
    properties_values["sequence"] = biobb_block.variables["sequence"]
    
    properties_values["binary_path"] = biobb_block.variables["binary_path"]
    
    properties_values["remove_tmp"] = biobb_block.variables["remove_tmp"]
    
    properties_values["restart"] = biobb_block.variables["restart"]
    
    for key in list(properties_values.keys()):
        if properties_values[key] is None:
            del properties_values[key]
    properties = {"properties": properties_values}


    with open("biobb_canal.json", "w", encoding="utf-8") as f:
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
            "biobb_canal",
            "--config",
            "/tmp/biobb_canal.json",
            
            "--input_cda_file",
            f"/tmp/{Path(input_cda_file_value).name}",
            
            "--input_lis_file",
            f"/tmp/{Path(input_lis_file_value).name}",
            
            
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

inputs_list.append(input_cda_file)

inputs_list.append(input_lis_file)


outputs_list.append(output_zip_path)


variables_list.append(bases)

variables_list.append(itst)

variables_list.append(itnd)

variables_list.append(itdel)

variables_list.append(lev1)

variables_list.append(lev2)

variables_list.append(nastr)

variables_list.append(cormin)

variables_list.append(series)

variables_list.append(histo)

variables_list.append(corr)

variables_list.append(sequence)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)


biobb_canal_block = PluginBlock(
    # The name which will appear on the frontend
    name="biobb_canal",
    # Its description
    description='Wrapper for the Canal executable that is part of the Curves+ software suite.',
    # The action
    action=biobb_canal_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)