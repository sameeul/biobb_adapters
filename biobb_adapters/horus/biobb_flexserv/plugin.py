from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_flexserv.flexserv.bd_run import bd_run_block

from biobb_flexserv.flexserv.dmd_run import dmd_run_block

from biobb_flexserv.flexserv.nma_run import nma_run_block

from biobb_flexserv.pcasuite.pcz_zip import pcz_zip_block

from biobb_flexserv.pcasuite.pcz_unzip import pcz_unzip_block

from biobb_flexserv.pcasuite.pcz_animate import pcz_animate_block

from biobb_flexserv.pcasuite.pcz_bfactor import pcz_bfactor_block

from biobb_flexserv.pcasuite.pcz_hinges import pcz_hinges_block

from biobb_flexserv.pcasuite.pcz_stiffness import pcz_stiffness_block

from biobb_flexserv.pcasuite.pcz_similarity import pcz_similarity_block

from biobb_flexserv.pcasuite.pcz_collectivity import pcz_collectivity_block

from biobb_flexserv.pcasuite.pcz_info import pcz_info_block

from biobb_flexserv.pcasuite.pcz_evecs import pcz_evecs_block

from biobb_flexserv.pcasuite.pcz_lindemann import pcz_lindemann_block

plugin = Plugin(id='biobb_flexserv')

plugin.addBlock(bd_run_block)

plugin.addBlock(dmd_run_block)

plugin.addBlock(nma_run_block)

plugin.addBlock(pcz_zip_block)

plugin.addBlock(pcz_unzip_block)

plugin.addBlock(pcz_animate_block)

plugin.addBlock(pcz_bfactor_block)

plugin.addBlock(pcz_hinges_block)

plugin.addBlock(pcz_stiffness_block)

plugin.addBlock(pcz_similarity_block)

plugin.addBlock(pcz_collectivity_block)

plugin.addBlock(pcz_info_block)

plugin.addBlock(pcz_evecs_block)

plugin.addBlock(pcz_lindemann_block)


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