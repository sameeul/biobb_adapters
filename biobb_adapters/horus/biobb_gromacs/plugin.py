from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_gromacs.gromacs.editconf import editconf_block

from biobb_gromacs.gromacs.genion import genion_block

from biobb_gromacs.gromacs.genrestr import genrestr_block

from biobb_gromacs.gromacs.grompp import grompp_block

from biobb_gromacs.gromacs.make_ndx import make_ndx_block

from biobb_gromacs.gromacs.mdrun import mdrun_block

from biobb_gromacs.gromacs.pdb2gmx import pdb2gmx_block

from biobb_gromacs.gromacs.gmxselect import gmxselect_block

from biobb_gromacs.gromacs.solvate import solvate_block

from biobb_gromacs.gromacs.grompp_mdrun import grompp_mdrun_block

from biobb_gromacs.gromacs.trjcat import trjcat_block

from biobb_gromacs.gromacs_extra.append_ligand import append_ligand_block

from biobb_gromacs.gromacs_extra.ndx2resttop import ndx2resttop_block

plugin = Plugin(id='biobb_gromacs')

plugin.addBlock(editconf_block)

plugin.addBlock(genion_block)

plugin.addBlock(genrestr_block)

plugin.addBlock(grompp_block)

plugin.addBlock(make_ndx_block)

plugin.addBlock(mdrun_block)

plugin.addBlock(pdb2gmx_block)

plugin.addBlock(gmxselect_block)

plugin.addBlock(solvate_block)

plugin.addBlock(grompp_mdrun_block)

plugin.addBlock(trjcat_block)

plugin.addBlock(append_ligand_block)

plugin.addBlock(ndx2resttop_block)


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