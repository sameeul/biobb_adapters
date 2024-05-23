from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_cmip.cmip.cmip_titration import cmip_titration_block

from biobb_cmip.cmip.cmip_run import cmip_run_block

from biobb_cmip.cmip.cmip_prepare_structure import cmip_prepare_structure_block

from biobb_cmip.cmip.cmip_prepare_pdb import cmip_prepare_pdb_block

from biobb_cmip.cmip.cmip_ignore_residues import cmip_ignore_residues_block

plugin = Plugin(id='biobb_cmip')

plugin.addBlock(cmip_titration_block)

plugin.addBlock(cmip_run_block)

plugin.addBlock(cmip_prepare_structure_block)

plugin.addBlock(cmip_prepare_pdb_block)

plugin.addBlock(cmip_ignore_residues_block)


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