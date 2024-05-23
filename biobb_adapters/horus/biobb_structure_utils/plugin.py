from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_structure_utils.utils.cat_pdb import cat_pdb_block

from biobb_structure_utils.utils.extract_atoms import extract_atoms_block

from biobb_structure_utils.utils.extract_chain import extract_chain_block

from biobb_structure_utils.utils.extract_heteroatoms import extract_heteroatoms_block

from biobb_structure_utils.utils.extract_residues import extract_residues_block

from biobb_structure_utils.utils.extract_model import extract_model_block

from biobb_structure_utils.utils.extract_molecule import extract_molecule_block

from biobb_structure_utils.utils.remove_ligand import remove_ligand_block

from biobb_structure_utils.utils.remove_molecules import remove_molecules_block

from biobb_structure_utils.utils.closest_residues import closest_residues_block

from biobb_structure_utils.utils.remove_pdb_water import remove_pdb_water_block

from biobb_structure_utils.utils.renumber_structure import renumber_structure_block

from biobb_structure_utils.utils.sort_gro_residues import sort_gro_residues_block

from biobb_structure_utils.utils.str_check_add_hydrogens import str_check_add_hydrogens_block

from biobb_structure_utils.utils.structure_check import structure_check_block

plugin = Plugin(id='biobb_structure_utils')

plugin.addBlock(cat_pdb_block)

plugin.addBlock(extract_atoms_block)

plugin.addBlock(extract_chain_block)

plugin.addBlock(extract_heteroatoms_block)

plugin.addBlock(extract_residues_block)

plugin.addBlock(extract_model_block)

plugin.addBlock(extract_molecule_block)

plugin.addBlock(remove_ligand_block)

plugin.addBlock(remove_molecules_block)

plugin.addBlock(closest_residues_block)

plugin.addBlock(remove_pdb_water_block)

plugin.addBlock(renumber_structure_block)

plugin.addBlock(sort_gro_residues_block)

plugin.addBlock(str_check_add_hydrogens_block)

plugin.addBlock(structure_check_block)


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