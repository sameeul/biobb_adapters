from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_io.api.drugbank import drugbank_block

from biobb_io.api.ligand import ligand_block

from biobb_io.api.pdb import pdb_block

from biobb_io.api.alphafold import alphafold_block

from biobb_io.api.pdb_cluster_zip import pdb_cluster_zip_block

from biobb_io.api.pdb_variants import pdb_variants_block

from biobb_io.api.memprotmd_sim_list import memprotmd_sim_list_block

from biobb_io.api.memprotmd_sim_search import memprotmd_sim_search_block

from biobb_io.api.memprotmd_sim import memprotmd_sim_block

from biobb_io.api.api_binding_site import api_binding_site_block

from biobb_io.api.canonical_fasta import canonical_fasta_block

from biobb_io.api.mmcif import mmcif_block

from biobb_io.api.ideal_sdf import ideal_sdf_block

from biobb_io.api.structure_info import structure_info_block

plugin = Plugin(id='biobb_io')

plugin.addBlock(drugbank_block)

plugin.addBlock(ligand_block)

plugin.addBlock(pdb_block)

plugin.addBlock(alphafold_block)

plugin.addBlock(pdb_cluster_zip_block)

plugin.addBlock(pdb_variants_block)

plugin.addBlock(memprotmd_sim_list_block)

plugin.addBlock(memprotmd_sim_search_block)

plugin.addBlock(memprotmd_sim_block)

plugin.addBlock(api_binding_site_block)

plugin.addBlock(canonical_fasta_block)

plugin.addBlock(mmcif_block)

plugin.addBlock(ideal_sdf_block)

plugin.addBlock(structure_info_block)


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