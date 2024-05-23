from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_pmx.pmxbiobb.pmxanalyse import pmxanalyse_block

from biobb_pmx.pmxbiobb.pmxgentop import pmxgentop_block

from biobb_pmx.pmxbiobb.pmxmutate import pmxmutate_block

from biobb_pmx.pmxbiobb.pmxatom_mapping import pmxatom_mapping_block

from biobb_pmx.pmxbiobb.pmxligand_hybrid import pmxligand_hybrid_block

from biobb_pmx.pmxbiobb.pmxmerge_ff import pmxmerge_ff_block

from biobb_pmx.pmxbiobb.pmxcreate_top import pmxcreate_top_block

plugin = Plugin(id='biobb_pmx')

plugin.addBlock(pmxanalyse_block)

plugin.addBlock(pmxgentop_block)

plugin.addBlock(pmxmutate_block)

plugin.addBlock(pmxatom_mapping_block)

plugin.addBlock(pmxligand_hybrid_block)

plugin.addBlock(pmxmerge_ff_block)

plugin.addBlock(pmxcreate_top_block)


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