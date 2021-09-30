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
from biobb_ml.classification.support_vector_machine import SupportVectorMachine  # Importing class instead of module to avoid name collision

task_time_out = int(os.environ.get('TASK_TIME_OUT', 0))


@task(input_dataset_path=FILE_IN, output_model_path=FILE_OUT, output_test_table_path=FILE_OUT, output_plot_path=FILE_OUT, 
      on_failure="IGNORE", time_out=task_time_out)
def _supportvectormachine(input_dataset_path, output_model_path, output_test_table_path, output_plot_path,  properties, **kwargs):
    
    task_config.pop_pmi(os.environ)
    
    try:
        SupportVectorMachine(input_dataset_path=input_dataset_path, output_model_path=output_model_path, output_test_table_path=output_test_table_path, output_plot_path=output_plot_path, properties=properties, **kwargs).launch()
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def support_vector_machine(input_dataset_path, output_model_path, output_test_table_path=None, output_plot_path=None, properties=None, **kwargs):

    if (output_model_path is None or os.path.exists(output_model_path)) and \
       (output_test_table_path is None or os.path.exists(output_test_table_path)) and \
       (output_plot_path is None or os.path.exists(output_plot_path)) and \
       True:
        print("WARN: Task SupportVectorMachine already executed.")
    else:
        _supportvectormachine( input_dataset_path,  output_model_path,  output_test_table_path,  output_plot_path,  properties, **kwargs)