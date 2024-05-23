from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_analysis.ambertools.cpptraj_average import cpptraj_average_block

from biobb_analysis.ambertools.cpptraj_bfactor import cpptraj_bfactor_block

from biobb_analysis.ambertools.cpptraj_convert import cpptraj_convert_block

from biobb_analysis.ambertools.cpptraj_dry import cpptraj_dry_block

from biobb_analysis.ambertools.cpptraj_image import cpptraj_image_block

from biobb_analysis.ambertools.cpptraj_mask import cpptraj_mask_block

from biobb_analysis.ambertools.cpptraj_rgyr import cpptraj_rgyr_block

from biobb_analysis.ambertools.cpptraj_rms import cpptraj_rms_block

from biobb_analysis.ambertools.cpptraj_rmsf import cpptraj_rmsf_block

from biobb_analysis.ambertools.cpptraj_slice import cpptraj_slice_block

from biobb_analysis.ambertools.cpptraj_snapshot import cpptraj_snapshot_block

from biobb_analysis.ambertools.cpptraj_strip import cpptraj_strip_block

from biobb_analysis.gromacs.gmx_cluster import gmx_cluster_block

from biobb_analysis.gromacs.gmx_energy import gmx_energy_block

from biobb_analysis.gromacs.gmx_image import gmx_image_block

from biobb_analysis.gromacs.gmx_rgyr import gmx_rgyr_block

from biobb_analysis.gromacs.gmx_rms import gmx_rms_block

from biobb_analysis.gromacs.gmx_trjconv_str import gmx_trjconv_str_block

from biobb_analysis.gromacs.gmx_trjconv_str_ens import gmx_trjconv_str_ens_block

from biobb_analysis.gromacs.gmx_trjconv_trj import gmx_trjconv_trj_block

plugin = Plugin(id='biobb_analysis')

plugin.addBlock(cpptraj_average_block)

plugin.addBlock(cpptraj_bfactor_block)

plugin.addBlock(cpptraj_convert_block)

plugin.addBlock(cpptraj_dry_block)

plugin.addBlock(cpptraj_image_block)

plugin.addBlock(cpptraj_mask_block)

plugin.addBlock(cpptraj_rgyr_block)

plugin.addBlock(cpptraj_rms_block)

plugin.addBlock(cpptraj_rmsf_block)

plugin.addBlock(cpptraj_slice_block)

plugin.addBlock(cpptraj_snapshot_block)

plugin.addBlock(cpptraj_strip_block)

plugin.addBlock(gmx_cluster_block)

plugin.addBlock(gmx_energy_block)

plugin.addBlock(gmx_image_block)

plugin.addBlock(gmx_rgyr_block)

plugin.addBlock(gmx_rms_block)

plugin.addBlock(gmx_trjconv_str_block)

plugin.addBlock(gmx_trjconv_str_ens_block)

plugin.addBlock(gmx_trjconv_trj_block)


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