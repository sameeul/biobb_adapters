import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_analysis.gromacs import gmx_trjconv_str_ens

@task(input_traj_path=FILE_IN, input_top_path=FILE_IN, output_str_ens_path=FILE_OUT, input_index_path=FILE_IN)
def gmx_trjconv_str_ens_pc(input_traj_path, input_top_path, output_str_ens_path, input_index_path, properties, **kwargs):
    try:
        gmx_trjconv_str_ens.GMXTrjConvStrEns(input_traj_path=input_traj_path, input_top_path=input_top_path, output_str_ens_path=output_str_ens_path, input_index_path=input_index_path, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_str_ens_path)
