import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_structure_utils.utils import sort_gro_residues

@task(input_gro_path=FILE_IN, output_gro_path=FILE_OUT)
def sort_gro_residues_pc(input_gro_path, output_gro_path, properties, **kwargs):
    try:
        sort_gro_residues.SortGroResidues(input_gro_path=input_gro_path, output_gro_path=output_gro_path, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_gro_path)