import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_md.gromacs import grompp
import os
import sys


@constraint(computingUnits="1")
@task(input_gro_path=FILE_IN, input_top_zip_path=FILE_IN,
      output_tpr_path=FILE_OUT, on_failure="IGNORE")
def grompp_pc(input_gro_path, input_top_zip_path,
              output_tpr_path, properties, **kwargs):
    try:
        os.environ.pop('PMI_FD', None)
        os.environ.pop('PMI_JOBID', None)
        os.environ.pop('PMI_RANK', None)
        os.environ.pop('PMI_SIZE', None)
        grompp.Grompp(input_gro_path=input_gro_path, input_top_zip_path=input_top_zip_path,
                      output_tpr_path=output_tpr_path, properties=properties,
                      **kwargs).launch()
        if not os.path.exists(output_tpr_path):
            fu.write_failed_output(output_tpr_path)
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_tpr_path)
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
