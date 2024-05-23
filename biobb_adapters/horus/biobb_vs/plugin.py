from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_vs.fpocket.fpocket_run import fpocket_run_block

from biobb_vs.fpocket.fpocket_filter import fpocket_filter_block

from biobb_vs.fpocket.fpocket_select import fpocket_select_block

from biobb_vs.vina.autodock_vina_run import autodock_vina_run_block

from biobb_vs.utils.bindingsite import bindingsite_block

from biobb_vs.utils.box import box_block

from biobb_vs.utils.box_residues import box_residues_block

from biobb_vs.utils.extract_model_pdbqt import extract_model_pdbqt_block

plugin = Plugin(id='biobb_vs')

plugin.addBlock(fpocket_run_block)

plugin.addBlock(fpocket_filter_block)

plugin.addBlock(fpocket_select_block)

plugin.addBlock(autodock_vina_run_block)

plugin.addBlock(bindingsite_block)

plugin.addBlock(box_block)

plugin.addBlock(box_residues_block)

plugin.addBlock(extract_model_pdbqt_block)


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