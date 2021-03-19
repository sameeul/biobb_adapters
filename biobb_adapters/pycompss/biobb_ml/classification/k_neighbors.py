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
from biobb_ml.classification.k_neighbors import KNeighborsTrain  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_dataset_path=FILE_IN, output_model_path=FILE_OUT, output_test_table_path=FILE_IN, output_plot_path=FILE_IN, 
      on_failure="IGNORE", time_out=task_time_out)
def _kneighborstrain(input_dataset_path, output_model_path, output_test_table_path, output_plot_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        KNeighborsTrain(input_dataset_path=input_dataset_path, output_model_path=output_model_path, output_test_table_path=output_test_table_path, output_plot_path=output_plot_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def kneighborstrain(input_dataset_path, output_model_path, output_test_table_path=None, output_plot_path=None, properties=None, **kwargs):

    if (output_model_path is None or os.path.exists(output_model_path)) and \
       True:
        print("WARN: Task KNeighborsTrain already executed.")
    else:
        _kneighborstrain( input_dataset_path,  output_model_path,  output_test_table_path,  output_plot_path,  properties, **kwargs)