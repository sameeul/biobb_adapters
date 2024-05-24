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
    description="Input 3D structure PDB file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

input_lib_path = PluginVariable(
    id="input_lib_path",  # ID of the variable, will allow us to identify the value
    name="input_lib_path",  # The name that will appear in the frontend
    description="Input ligand library parameters file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['lib', 'zip']
)

input_frcmod_path = PluginVariable(
    id="input_frcmod_path",  # ID of the variable, will allow us to identify the value
    name="input_frcmod_path",  # The name that will appear in the frontend
    description="Input ligand frcmod parameters file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['frcmod', 'zip']
)

input_params_path = PluginVariable(
    id="input_params_path",  # ID of the variable, will allow us to identify the value
    name="input_params_path",  # The name that will appear in the frontend
    description="Additional leap parameter files to load with loadAmberParams Leap command",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['in', 'leapin', 'txt', 'zip']
)

input_source_path = PluginVariable(
    id="input_source_path",  # ID of the variable, will allow us to identify the value
    name="input_source_path",  # The name that will appear in the frontend
    description="Additional leap command files to load with source Leap command",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['in', 'leapin', 'txt', 'zip']
)


output_pdb_path = PluginVariable(
    id="output_pdb_path",  # ID of the variable, will allow us to identify the value
    name="output_pdb_path",  # The name that will appear in the frontend
    description="Output 3D structure PDB file matching the topology file",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['pdb']
)

output_top_path = PluginVariable(
    id="output_top_path",  # ID of the variable, will allow us to identify the value
    name="output_top_path",  # The name that will appear in the frontend
    description="Output topology file (AMBER ParmTop)",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['top', 'parmtop', 'prmtop']
)

output_crd_path = PluginVariable(
    id="output_crd_path",  # ID of the variable, will allow us to identify the value
    name="output_crd_path",  # The name that will appear in the frontend
    description="Output coordinates file (AMBER crd)",  # The description that will appear in the frontend
    type=VariableTypes.FILE,  # The type. This will render the variable accrodingly
    # The allowedValues parameter depends on the type of variable,
    # in the case of files, they denote the allowed extensions.
    allowedValues=['crd', 'mdcrd', 'inpcrd']
)

######################
# Define Variables
# These variables appear under the block "config" button
######################

forcefield = PluginVariable(
    id="forcefield",
    name="forcefield",
    description="Forcefield to be used for the structure generation. ",
    type=VariableTypes.STRING
)

water_type = PluginVariable(
    id="water_type",
    name="water_type",
    description="Water molecule parameters to be used for the topology. ",
    type=VariableTypes.STRING
)

box_type = PluginVariable(
    id="box_type",
    name="box_type",
    description="Type for the MD system box. ",
    type=VariableTypes.STRING
)

ions_type = PluginVariable(
    id="ions_type",
    name="ions_type",
    description="Ions type. ",
    type=VariableTypes.STRING
)

neutralise = PluginVariable(
    id="neutralise",
    name="neutralise",
    description="Energetically neutralise the system adding the necessary counterions.",
    type=VariableTypes.BOOLEAN
)

ionic_concentration = PluginVariable(
    id="ionic_concentration",
    name="ionic_concentration",
    description="Additional ionic concentration to include in the system box. Units in Mol/L.",
    type=VariableTypes.NUMBER
)

positive_ions_number = PluginVariable(
    id="positive_ions_number",
    name="positive_ions_number",
    description="Number of additional positive ions to include in the system box.",
    type=VariableTypes.INTEGER
)

negative_ions_number = PluginVariable(
    id="negative_ions_number",
    name="negative_ions_number",
    description="Number of additional negative ions to include in the system box.",
    type=VariableTypes.INTEGER
)

positive_ions_type = PluginVariable(
    id="positive_ions_type",
    name="positive_ions_type",
    description="Type of additional positive ions to include in the system box. ",
    type=VariableTypes.STRING
)

negative_ions_type = PluginVariable(
    id="negative_ions_type",
    name="negative_ions_type",
    description="Type of additional negative ions to include in the system box. ",
    type=VariableTypes.STRING
)

binary_path = PluginVariable(
    id="binary_path",
    name="binary_path",
    description="Path to the tleap executable binary.",
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
def leap_add_ions_action(biobb_block: PluginBlock):

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
    
    input_lib_path_value = biobb_block.inputs["input_lib_path"]
    
    input_frcmod_path_value = biobb_block.inputs["input_frcmod_path"]
    
    input_params_path_value = biobb_block.inputs["input_params_path"]
    
    input_source_path_value = biobb_block.inputs["input_source_path"]
    
    
    output_pdb_path_value = biobb_block.inputs["output_pdb_path"]
    
    output_top_path_value = biobb_block.inputs["output_top_path"]
    
    output_crd_path_value = biobb_block.inputs["output_crd_path"]
    
    # Define the properties for the biobb tool
    properties_values = {}
    
    properties_values["forcefield"] = biobb_block.variables["forcefield"]
    
    properties_values["water_type"] = biobb_block.variables["water_type"]
    
    properties_values["box_type"] = biobb_block.variables["box_type"]
    
    properties_values["ions_type"] = biobb_block.variables["ions_type"]
    
    properties_values["neutralise"] = biobb_block.variables["neutralise"]
    
    properties_values["ionic_concentration"] = biobb_block.variables["ionic_concentration"]
    
    properties_values["positive_ions_number"] = biobb_block.variables["positive_ions_number"]
    
    properties_values["negative_ions_number"] = biobb_block.variables["negative_ions_number"]
    
    properties_values["positive_ions_type"] = biobb_block.variables["positive_ions_type"]
    
    properties_values["negative_ions_type"] = biobb_block.variables["negative_ions_type"]
    
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


    with open("leap_add_ions.json", "w", encoding="utf-8") as f:
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
            "leap_add_ions",
            "--config",
            "/tmp/leap_add_ions.json",
            
            "--input_pdb_path",
            f"/tmp/{Path(input_pdb_path_value).name}",
            
            "--input_lib_path",
            f"/tmp/{Path(input_lib_path_value).name}",
            
            "--input_frcmod_path",
            f"/tmp/{Path(input_frcmod_path_value).name}",
            
            "--input_params_path",
            f"/tmp/{Path(input_params_path_value).name}",
            
            "--input_source_path",
            f"/tmp/{Path(input_source_path_value).name}",
            
            
            "--output_pdb_path",
            f"/tmp/{Path(output_pdb_path_value).name}",
            
            "--output_top_path",
            f"/tmp/{Path(output_top_path_value).name}",
            
            "--output_crd_path",
            f"/tmp/{Path(output_crd_path_value).name}",
            
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
        abs_path_out = Path(output_pdb_path_value).absolute()
        abs_path_name = Path(Path(output_pdb_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_pdb_path_value).name}", output_pdb_path_value)
        biobb_block.setOutput("output_pdb_path", output_pdb_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_top_path_value).absolute()
        abs_path_name = Path(Path(output_top_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_top_path_value).name}", output_top_path_value)
        biobb_block.setOutput("output_top_path", output_top_path_value)
        
        # Copy the outputs to the output folder
        abs_path_out = Path(output_crd_path_value).absolute()
        abs_path_name = Path(Path(output_crd_path_value).name).absolute()
        if not abs_path_name.samefile(abs_path_out):
            shutil.copy(f"{Path(output_crd_path_value).name}", output_crd_path_value)
        biobb_block.setOutput("output_crd_path", output_crd_path_value)
        
        # If the block has any output, one can set its value using the ID of the output variable
        # and the corresponding value


# Define the block
inputs_list = []
outputs_list = []
variables_list = []

inputs_list.append(input_pdb_path)

inputs_list.append(input_lib_path)

inputs_list.append(input_frcmod_path)

inputs_list.append(input_params_path)

inputs_list.append(input_source_path)


outputs_list.append(output_pdb_path)

outputs_list.append(output_top_path)

outputs_list.append(output_crd_path)


variables_list.append(forcefield)

variables_list.append(water_type)

variables_list.append(box_type)

variables_list.append(ions_type)

variables_list.append(neutralise)

variables_list.append(ionic_concentration)

variables_list.append(positive_ions_number)

variables_list.append(negative_ions_number)

variables_list.append(positive_ions_type)

variables_list.append(negative_ions_type)

variables_list.append(binary_path)

variables_list.append(remove_tmp)

variables_list.append(restart)

variables_list.append(container_path)

variables_list.append(container_image)

variables_list.append(container_volume_path)

variables_list.append(container_working_dir)

variables_list.append(container_user_id)

variables_list.append(container_shell_path)


leap_add_ions_block = PluginBlock(
    # The name which will appear on the frontend
    name="leap_add_ions",
    # Its description
    description="Wrapper of the AmberTools (AMBER MD Package) leap tool module.",
    # The action
    action=leap_add_ions_action,
    # A list of inputs, variables and outputs
    inputs=inputs_list + outputs_list,
    variables=variables_list,
    outputs=outputs_list,
)