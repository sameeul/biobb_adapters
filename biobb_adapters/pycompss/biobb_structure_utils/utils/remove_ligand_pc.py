import traceback
from pycompss.api.task import task
from pycompss.api.constraint import constraint
from pycompss.api.parameter import FILE_IN, FILE_OUT
from biobb_common.tools import file_utils as fu
from biobb_structure_utils.utils import remove_ligand

@task(input_structure_path=FILE_IN, output_structure_path=FILE_OUT)
def remove_ligand_pc(input_structure_path, output_structure_path, properties, **kwargs):
    try:
        remove_ligand.RemoveLigand(input_structure_path=input_structure_path, output_structure_path=output_structure_path, properties=properties, **kwargs).launch()
    except Exception:
        traceback.print_exc()
        fu.write_failed_output(output_structure_path)