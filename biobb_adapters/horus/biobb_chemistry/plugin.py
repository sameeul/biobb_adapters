from HorusAPI import Plugin, PluginConfig, PluginVariable, VariableTypes


from biobb_chemistry.acpype.acpype_params_ac import acpype_params_ac_block

from biobb_chemistry.acpype.acpype_params_cns import acpype_params_cns_block

from biobb_chemistry.acpype.acpype_params_gmx import acpype_params_gmx_block

from biobb_chemistry.acpype.acpype_params_gmx_opls import acpype_params_gmx_opls_block

from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens_block

from biobb_chemistry.ambertools.reduce_remove_hydrogens import reduce_remove_hydrogens_block

from biobb_chemistry.babelm.babel_add_hydrogens import babel_add_hydrogens_block

from biobb_chemistry.babelm.babel_convert import babel_convert_block

from biobb_chemistry.babelm.babel_minimize import babel_minimize_block

from biobb_chemistry.babelm.babel_remove_hydrogens import babel_remove_hydrogens_block

plugin = Plugin(id='biobb_chemistry')

plugin.addBlock(acpype_params_ac_block)

plugin.addBlock(acpype_params_cns_block)

plugin.addBlock(acpype_params_gmx_block)

plugin.addBlock(acpype_params_gmx_opls_block)

plugin.addBlock(reduce_add_hydrogens_block)

plugin.addBlock(reduce_remove_hydrogens_block)

plugin.addBlock(babel_add_hydrogens_block)

plugin.addBlock(babel_convert_block)

plugin.addBlock(babel_minimize_block)

plugin.addBlock(babel_remove_hydrogens_block)


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