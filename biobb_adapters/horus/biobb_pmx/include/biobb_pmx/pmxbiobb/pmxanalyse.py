# Import all the required classes from the HorusAPI
import shutil
from pathlib import Path
from HorusAPI import PluginBlock, PluginVariable, VariableTypes

######################
# Define INPUTS
# These variables will appear under the palced block.
# They expect to be conected to the outputs of other blocks
######################

input_a_xvg_zip_path = PluginVariable(
    id="input_a_xvg_zip_path",  # ID of the variable, will allow us to identify the value
    name="input_a_xvg_zip_path",  # The name that will appear in the frontend
    description="Path the zip file containing the dgdl.xvg files of the A state",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)

input_b_xvg_zip_path = PluginVariable(
    id="input_b_xvg_zip_path",  # ID of the variable, will allow us to identify the value
    name="input_b_xvg_zip_path",  # The name that will appear in the frontend
    description="Path the zip file containing the dgdl.xvg files of the B state",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['zip']
)


output_result_path = PluginVariable(
    id="output_result_path",  # ID of the variable, will allow us to identify the value
    name="output_result_path",  # The name that will appear in the frontend
    description="Path to the TXT results file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['txt']
)

output_work_plot_path = PluginVariable(
    id="output_work_plot_path",  # ID of the variable, will allow us to identify the value
    name="output_work_plot_path",  # The name that will appear in the frontend
    description="Path to the PNG plot results file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['png']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

method = PluginVariable(
    id="method",
    name="method",
    description="Choose one or more estimators to use. ",
    type=VariableTypes.STRING
)

temperature = PluginVariable(
    id="temperature",
    name="temperature",
    description="Temperature in Kelvin.",
    type=VariableTypes.NUMBER
)

nboots = PluginVariable(
    id="nboots",
    name="nboots",
    description="Number of bootstrap samples to use for the bootstrap estimate of the standard errors.",
    type=VariableTypes.INTEGER
)

nblocks = PluginVariable(
    id="nblocks",
    name="nblocks",
    description="Number of blocks to divide the data into for an estimate of the standard error.",
    type=VariableTypes.INTEGER
)

integ_only = PluginVariable(
    id="integ_only",
    name="integ_only",
    description="Whether to do integration only.",
    type=VariableTypes.BOOLEAN
)

reverseB = PluginVariable(
    id="reverseB",
    name="reverseB",
    description="Whether to reverse the work values for the backward (B->A) transformation.",
    type=VariableTypes.BOOLEAN
)

skip = PluginVariable(
    id="skip",
    name="skip",
    description="Skip files.",
    type=VariableTypes.INTEGER
)

slice = PluginVariable(
    id="slice",
    name="slice",
    description="Subset of trajectories to analyze. Provide list slice, e.g. '10 50' will result in selecting dhdl_files[10:50].",
    type=VariableTypes.STRING
)

rand = PluginVariable(
    id="rand",
    name="rand",
    description="Take a random subset of trajectories. Default is None (do not take random subset).",
    type=VariableTypes.INTEGER
)

index = PluginVariable(
    id="index",
    name="index",
    description="Zero-based index of files to analyze (e.g. '0 10 20 50 60'). It keeps the dhdl.xvg files according to their position in the list, sorted according to the filenames.",
    type=VariableTypes.STRING
)

prec = PluginVariable(
    id="prec",
    name="prec",
    description="The decimal precision of the screen/file output.",
    type=VariableTypes.INTEGER
)

units = PluginVariable(
    id="units",
    name="units",
    description="The units of the output. ",
    type=VariableTypes.STRING
)

no_ks = PluginVariable(
    id="no_ks",
    name="no_ks",
    description="Whether to do a Kolmogorov-Smirnov test to check whether the Gaussian assumption for CGI holds.",
    type=VariableTypes.BOOLEAN
)

nbins = PluginVariable(
    id="nbins",
    name="nbins",
    description="Number of histograms bins for the plot.",
    type=VariableTypes.INTEGER
)

dpi = PluginVariable(
    id="dpi",
    name="dpi",
    description="Resolution of the plot.",
    type=VariableTypes.INTEGER
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="Path to the PMX command line interface.",
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
def pmxanalyse_action(biobb_block: PluginBlock):

    # It is better to have imports inside the function
    # because the environment gets cleaned up between each
    # of the blocks that run in the flow. Having the imports
    # inside will ensure integrity on the action of the block
    import subprocess
    import json

    # Obtain the variable values
    # biobb_block.inputs is just a dictionary with the ID of the variables as keys
    # and the value as the value the user enetered
    
    input_a_xvg_zip_path_value = biobb_block.inputs["input_a_xvg_zip_path"]
    
    input_b_xvg_zip_path_value = biobb_block.inputs["input_b_xvg_zip_path"]
    
    
    output_result_path_value = biobb_block.inputs["output_result_path"]
    
    output_work_plot_path_value = biobb_block.inputs["output_work_plot_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["method"] = biobb_block.variables["method"]
    
    properties_values["temperature"] = biobb_block.variables["temperature"]
    
    properties_values["nboots"] = biobb_block.variables["nboots"]
    
    properties_values["nblocks"] = biobb_block.variables["nblocks"]
    
    properties_values["integ_only"] = biobb_block.variables["integ_only"]
    
    properties_values["reverseB"] = biobb_block.variables["reverseB"]
    
    properties_values["skip"] = biobb_block.variables["skip"]
    
    properties_values["slice"] = biobb_block.variables["slice"]
    
    properties_values["rand"] = biobb_block.variables["rand"]
    
    properties_values["index"] = biobb_block.variables["index"]
    
    properties_values["prec"] = biobb_block.variables["prec"]
    
    properties_values["units"] = biobb_block.variables["units"]
    
    properties_values["no_ks"] = biobb_block.variables["no_ks"]
    
    properties_values["nbins"] = biobb_block.variables["nbins"]
    
    properties_values["dpi"] = biobb_block.variables["dpi"]
    
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


    with open("pmxanalyse.json", "w", encoding="utf-8") as f:
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
            "pmxanalyse",
            "--config",
            "/tmp/pmxanalyse.json",
            
            "--input_a_xvg_zip_path",
            f"/tmp/{Path(input_a_xvg_zip_path_value).name}",
            
            "--input_b_xvg_zip_path",
            f"/tmp/{Path(input_b_xvg_zip_path_value).name}",
            
            
            "--output_result_path",
            f"/tmp/{Path(output_result_path_value).name}",
            
            "--output_work_plot_path",
            f"/tmp/{Path(output_work_plot_path_value).name}",
            
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
        abs_path_out = Path(output_result_path_value).absolute()
        abs_path_name = Path(Path(output_result_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_result_path_value).name}", output_result_path_value)
        biobb_block.setOutput("output_result_path", output_result_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_work_plot_path_value).absolute()
        abs_path_name = Path(Path(output_work_plot_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_work_plot_path_value).name}", output_work_plot_path_value)
        biobb_block.setOutput("output_work_plot_path", output_work_plot_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_a_xvg_zip_path)

inputs_list.append(input_b_xvg_zip_path)


outputs_list.append(output_result_path)

outputs_list.append(output_work_plot_path)


variables_list.append(method)

variables_list.append(temperature)

variables_list.append(nboots)

variables_list.append(nblocks)

variables_list.append(integ_only)

variables_list.append(reverseB)

variables_list.append(skip)

variables_list.append(slice)

variables_list.append(rand)

variables_list.append(index)

variables_list.append(prec)

variables_list.append(units)

variables_list.append(no_ks)

variables_list.append(nbins)

variables_list.append(dpi)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


pmxanalyse_block = PluginBlock(
    # The name which will appear on the frontend
    name="pmxanalyse",
    # Its description
    description="Wrapper class for the PMX analyse module.",
    # The action
    action=pmxanalyse_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)