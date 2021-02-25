import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.multinode import multinode
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_md.gromacs.mdrun import Mdrun  # Importing class instead of module to avoid name collission
from biobb_adapters.pycompss.biobb_commons import task_config
import os
import sys

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))
computing_nodes = str(os.environ.get('TASK_COMPUTING_NODES', "1"))
computing_units = str(os.environ.get('TASK_COMPUTING_UNITS', "1"))

@constraint(computingUnits=computing_units)
@multinode(computing_nodes=computing_nodes)
@task(input_tpr_path=FILE_IN, output_trr_path=FILE_OUT,
      output_gro_path=FILE_OUT, output_edr_path=FILE_OUT,
      output_xtc_path=FILE_OUT, output_log_path=FILE_OUT,
      output_dhdl_path=FILE_OUT, output_cpt_path=FILE_INOUT,
      input_cpt_path=FILE_IN,
      on_failure="IGNORE", time_out=task_time_out)
def mdrun(input_tpr_path, output_trr_path,
             output_gro_path, output_edr_path,
             output_xtc_path, output_log_path,
             output_dhdl_path, output_cpt_path,
             input_cpt_path,
             properties, **kwargs):
    # task_config.config_gromacs_multinode(properties)
    # What this does? is it needed? Can we pull this conf with env vars?
    # Talk to Jorge about biobb_adapters.pycompss.biobb_commons
    try:
        Mdrun(input_tpr_path=input_tpr_path, output_trr_path=output_trr_path,
              output_gro_path=output_gro_path, output_edr_path=output_edr_path,
              output_xtc_path=output_xtc_path, output_log_path=output_log_path,
              output_dhdl_path=output_dhdl_path, output_cpt_path=output_cpt_path,
              input_cpt_path=input_cpt_path,
              properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()

# Here there was the real mdrun def but as long
# as we don't need the ***pycompss continue*** we can call just the function above theese lines
# I expect that the ***pycompss restart*** works with this code.