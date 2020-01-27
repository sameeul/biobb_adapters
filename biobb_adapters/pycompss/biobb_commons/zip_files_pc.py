import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.multinode import multinode
from pycompss.api.parameter import COLLECTION_FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
import os
import sys


@constraint(computingUnits="1")
@task(input_file_paths=COLLECTION_FILE_IN, output_zip_path=FILE_OUT,
      on_failure="IGNORE")
def zip_files_pc(input_file_paths, output_zip_path):
    try:
        os.environ.pop('PMI_FD', None)
        os.environ.pop('PMI_JOBID', None)
        os.environ.pop('PMI_RANK', None)
        os.environ.pop('PMI_SIZE', None)
        fu.zip_list(output_zip_path, input_file_paths)
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
