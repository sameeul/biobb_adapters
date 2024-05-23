from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_amber.ambpdb.amber_to_pdb import amber_to_pdb_block

from biobb_amber.cpptraj.cpptraj_randomize_ions import cpptraj_randomize_ions_block

from biobb_amber.leap.leap_build_linear_structure import leap_build_linear_structure_block

from biobb_amber.leap.leap_gen_top import leap_gen_top_block

from biobb_amber.leap.leap_solvate import leap_solvate_block

from biobb_amber.leap.leap_add_ions import leap_add_ions_block

from biobb_amber.nab.nab_build_dna_structure import nab_build_dna_structure_block

from biobb_amber.parmed.parmed_cpinutil import parmed_cpinutil_block

from biobb_amber.parmed.parmed_hmassrepartition import parmed_hmassrepartition_block

from biobb_amber.pdb4amber.pdb4amber_run import pdb4amber_run_block

from biobb_amber.process.process_minout import process_minout_block

from biobb_amber.process.process_mdout import process_mdout_block

from biobb_amber.sander.sander_mdrun import sander_mdrun_block

from biobb_amber.pmemd.pmemd_mdrun import pmemd_mdrun_block

from biobb_amber.cphstats.cphstats_run import cphstats_run_block

from biobb_amber.cphstats.cestats_run import cestats_run_block

plugin = Plugin(id='biobb_amber')

plugin.addBlock(amber_to_pdb_block)

plugin.addBlock(cpptraj_randomize_ions_block)

plugin.addBlock(leap_build_linear_structure_block)

plugin.addBlock(leap_gen_top_block)

plugin.addBlock(leap_solvate_block)

plugin.addBlock(leap_add_ions_block)

plugin.addBlock(nab_build_dna_structure_block)

plugin.addBlock(parmed_cpinutil_block)

plugin.addBlock(parmed_hmassrepartition_block)

plugin.addBlock(pdb4amber_run_block)

plugin.addBlock(process_minout_block)

plugin.addBlock(process_mdout_block)

plugin.addBlock(sander_mdrun_block)

plugin.addBlock(pmemd_mdrun_block)

plugin.addBlock(cphstats_run_block)

plugin.addBlock(cestats_run_block)


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