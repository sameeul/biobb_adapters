from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_model.model.fix_side_chain import fix_side_chain_block

from biobb_model.model.fix_backbone import fix_backbone_block

from biobb_model.model.mutate import mutate_block

from biobb_model.model.checking_log import checking_log_block

from biobb_model.model.fix_amides import fix_amides_block

from biobb_model.model.fix_chirality import fix_chirality_block

from biobb_model.model.fix_altlocs import fix_altlocs_block

from biobb_model.model.fix_ssbonds import fix_ssbonds_block

from biobb_model.model.fix_pdb import fix_pdb_block

plugin = Plugin(id='biobb_model')

plugin.addBlock(fix_side_chain_block)

plugin.addBlock(fix_backbone_block)

plugin.addBlock(mutate_block)

plugin.addBlock(checking_log_block)

plugin.addBlock(fix_amides_block)

plugin.addBlock(fix_chirality_block)

plugin.addBlock(fix_altlocs_block)

plugin.addBlock(fix_ssbonds_block)

plugin.addBlock(fix_pdb_block)


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