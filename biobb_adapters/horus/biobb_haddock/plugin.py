from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_haddock.haddock.capri_eval import capri_eval_block

from biobb_haddock.haddock.clust_fcc import clust_fcc_block

from biobb_haddock.haddock.em_ref import em_ref_block

from biobb_haddock.haddock.flex_ref import flex_ref_block

from biobb_haddock.haddock.rigid_body import rigid_body_block

from biobb_haddock.haddock.sele_top_clusts import sele_top_clusts_block

from biobb_haddock.haddock.sele_top import sele_top_block

from biobb_haddock.haddock.topology import topology_block

plugin = Plugin(id='biobb_haddock')

plugin.addBlock(capri_eval_block)

plugin.addBlock(clust_fcc_block)

plugin.addBlock(em_ref_block)

plugin.addBlock(flex_ref_block)

plugin.addBlock(rigid_body_block)

plugin.addBlock(sele_top_clusts_block)

plugin.addBlock(sele_top_block)

plugin.addBlock(topology_block)


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