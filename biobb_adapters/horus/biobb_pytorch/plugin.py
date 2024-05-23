from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_pytorch.mdae.train_mdae import train_mdae_block

from biobb_pytorch.mdae.apply_mdae import apply_mdae_block

plugin = Plugin(id='biobb_pytorch')

plugin.addBlock(train_mdae_block)

plugin.addBlock(apply_mdae_block)


executable_path_variable = PluginVariable(
    id="executable_path",
    name="Executable path",
    description="The path to the docker executable",
    defaultValue="docker",
    type=VariableTypes.STRING,
)

executable_path_variable_config = PluginConfig(
    name=executable_path_variable.name,
    description=executable_path_variable.description,
    action=None,
    variables=[executable_path_variable],
)

plugin.addConfig(executable_path_variable_config)