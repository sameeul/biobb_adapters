# Python
import os
import sys
import traceback
# Pycompss
from pycompss.api.task import task
from pycompss.api.parameter import FILE_IN, FILE_OUT
# Adapters commons pycompss
from biobb_adapters.pycompss.biobb_commons import task_config
# Wrapped Biobb
from biobb_analysis.gromacs.gmx_rgyr import GMXRgyr  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_structure_path=FILE_IN, input_traj_path=FILE_IN, output_xvg_path=FILE_OUT, input_index_path=FILE_IN, 
      on_failure="IGNORE", time_out=task_time_out)
def _gmxrgyr(input_structure_path, input_traj_path, output_xvg_path, input_index_path,  properties, **kwargs):
    
        task_config.pop_pmi(os.environ)
    
    try:
        GMXRgyr(input_structure_path=input_structure_path, input_traj_path=input_traj_path, output_xvg_path=output_xvg_path, input_index_path=input_index_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def gmxrgyr(input_structure_path, input_traj_path, output_xvg_path, input_index_path=None, properties=None, **kwargs):

    if (output_xvg_path is None or os.path.exists(output_xvg_path)) and \
       True:
        print("WARN: Task GMXRgyr already executed.")
    else:
        _gmxrgyr( input_structure_path,  input_traj_path,  output_xvg_path,  input_index_path,  properties, **kwargs)