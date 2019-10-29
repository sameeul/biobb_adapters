import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_analysis.gromacs import gmx_energy

@task(input_energy_path=FILE_IN, output_xvg_path=FILE_OUT)
def gmx_energy_pc(input_energy_path, output_xvg_path, properties, **kwargs):
    try:
        gmx_energy.GMXEnergy(input_energy_path=input_energy_path, output_xvg_path=output_xvg_path, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_xvg_path)
