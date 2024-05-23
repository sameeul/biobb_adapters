from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_flexdyn.flexdyn.concoord_dist import concoord_dist_block

from biobb_flexdyn.flexdyn.concoord_disco import concoord_disco_block

from biobb_flexdyn.flexdyn.prody_anm import prody_anm_block

from biobb_flexdyn.flexdyn.nolb_nma import nolb_nma_block

from biobb_flexdyn.flexdyn.imod_imode import imod_imode_block

from biobb_flexdyn.flexdyn.imod_imove import imod_imove_block

from biobb_flexdyn.flexdyn.imod_imc import imod_imc_block

plugin = Plugin(id='biobb_flexdyn')

plugin.addBlock(concoord_dist_block)

plugin.addBlock(concoord_disco_block)

plugin.addBlock(prody_anm_block)

plugin.addBlock(nolb_nma_block)

plugin.addBlock(imod_imode_block)

plugin.addBlock(imod_imove_block)

plugin.addBlock(imod_imc_block)


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