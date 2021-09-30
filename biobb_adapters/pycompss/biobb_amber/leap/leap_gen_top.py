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
from biobb_amber.leap.leap_gen_top import LeapGenTop  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_pdb_path=FILE_IN, output_pdb_path=FILE_OUT, output_top_path=FILE_OUT, output_crd_path=FILE_OUT, input_lib_path=FILE_IN, input_frcmod_path=FILE_IN, input_params_path=FILE_IN, input_source_path=FILE_IN, 
      on_failure="IGNORE", time_out=task_time_out)
def _leapgentop(input_pdb_path, output_pdb_path, output_top_path, output_crd_path, input_lib_path, input_frcmod_path, input_params_path, input_source_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        LeapGenTop(input_pdb_path=input_pdb_path, output_pdb_path=output_pdb_path, output_top_path=output_top_path, output_crd_path=output_crd_path, input_lib_path=input_lib_path, input_frcmod_path=input_frcmod_path, input_params_path=input_params_path, input_source_path=input_source_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def leap_gen_top(input_pdb_path, output_pdb_path, output_top_path, output_crd_path, input_lib_path=None, input_frcmod_path=None, input_params_path=None, input_source_path=None, properties=None, **kwargs):

    if (output_pdb_path is None or os.path.exists(output_pdb_path)) and \
       (output_top_path is None or os.path.exists(output_top_path)) and \
       (output_crd_path is None or os.path.exists(output_crd_path)) and \
       True:
        print("WARN: Task LeapGenTop already executed.")
    else:
        _leapgentop( input_pdb_path,  output_pdb_path,  output_top_path,  output_crd_path,  input_lib_path,  input_frcmod_path,  input_params_path,  input_source_path,  properties, **kwargs)