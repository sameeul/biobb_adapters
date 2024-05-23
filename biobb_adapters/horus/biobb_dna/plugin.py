from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_dna.dna.dna_averages import dna_averages_block

from biobb_dna.dna.dna_bimodality import dna_bimodality_block

from biobb_dna.dna.dna_timeseries import dna_timeseries_block

from biobb_dna.curvesplus.biobb_curves import biobb_curves_block

from biobb_dna.curvesplus.biobb_canal import biobb_canal_block

from biobb_dna.curvesplus.biobb_canion import biobb_canion_block

from biobb_dna.backbone.bipopulations import bipopulations_block

from biobb_dna.backbone.canonicalag import canonicalag_block

from biobb_dna.backbone.puckering import puckering_block

from biobb_dna.stiffness.average_stiffness import average_stiffness_block

from biobb_dna.stiffness.basepair_stiffness import basepair_stiffness_block

from biobb_dna.interbp_correlations.interbpcorr import interbpcorr_block

from biobb_dna.interbp_correlations.interhpcorr import interhpcorr_block

from biobb_dna.interbp_correlations.interseqcorr import interseqcorr_block

from biobb_dna.intrabp_correlations.intrabpcorr import intrabpcorr_block

from biobb_dna.intrabp_correlations.intrahpcorr import intrahpcorr_block

from biobb_dna.intrabp_correlations.intraseqcorr import intraseqcorr_block

plugin = Plugin(id='biobb_dna')

plugin.addBlock(dna_averages_block)

plugin.addBlock(dna_bimodality_block)

plugin.addBlock(dna_timeseries_block)

plugin.addBlock(biobb_curves_block)

plugin.addBlock(biobb_canal_block)

plugin.addBlock(biobb_canion_block)

plugin.addBlock(bipopulations_block)

plugin.addBlock(canonicalag_block)

plugin.addBlock(puckering_block)

plugin.addBlock(average_stiffness_block)

plugin.addBlock(basepair_stiffness_block)

plugin.addBlock(interbpcorr_block)

plugin.addBlock(interhpcorr_block)

plugin.addBlock(interseqcorr_block)

plugin.addBlock(intrabpcorr_block)

plugin.addBlock(intrahpcorr_block)

plugin.addBlock(intraseqcorr_block)


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