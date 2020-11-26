#!/usr/bin/env python3

"""Module containing the MDrunRmt class and the command line interface."""
import os
import argparse
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
#from biobb_common.command_wrapper import cmd_wrapper
#from biobb_md.gromacs.common import get_gromacs_version
#from biobb_md.gromacs.common import GromacsVersionError
from biobb_remote.slurm import Slurm
from biobb_remote.task import FINISHED
from biobb_remote.ssh_credentials import SSHCredentials


class MdrunRmt:
    """Adapter for remote execution of the biobb_md/gromacs/mdrun module.

    Args:   
        File paths passed to mdrun.
        input_tpr_path (str): Path to the portable binary run input file TPR. File type: input. `Sample file <https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/mdrun.tpr>`_. Accepted formats: tpr. Passed to mdrun.
        output_trr_path (str): Path to the GROMACS uncompressed raw trajectory file TRR. File type: output. `Sample file <https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_mdrun.trr>`_. Accepted formats: trr. Passed to mdrun
        output_gro_path (str): Path to the output GROMACS structure GRO file. File type: output. `Sample file <https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_mdrun.gro>`_. Accepted formats: gro. Passed to mdrun.
        output_edr_path (str): Path to the output GROMACS portable energy file EDR. File type: output. `Sample file <https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/reference/gromacs/ref_mdrun.edr>`_. Accepted formats: edr. Passed to mdrun.
        output_log_path (str): Path to the output GROMACS trajectory log file LOG. File type: output. Accepted formats: log. Passed to mdrun.
        output_xtc_path (str) (Optional): Path to the GROMACS compressed trajectory file XTC. File type: output. Accepted formats: xtc. Passed to mdrun.
        output_cpt_path (str) (Optional): Path to the output GROMACS checkpoint file CPT. File type: output. Accepted formats: cpt. Passed to mdrun.
        output_dhdl_path (str) (Optional): Path to the output dhdl.xvg file only used when free energy calculation is turned on. File type: output. Accepted formats: xvg. Passed to mdrun.
        Adapter files.
        keys_file (*str*) - Credentials (biobb_remote.ssh_credentials) file (optional, if missing users' own ssh keys are used.
        local_path (*str*) - Path to local files
        remote_path (*str*) - Path to remote base folder. Unique working will be created when necessary.
        task_data_path (*str*) - Path to task metadata file (json format). Used to keep live information of the remote task.
        
        properties (dic):
            * **host** (*str*) - Remote host name (optional if keys_file is provided)
            * **userid** (*str*) - Remote user ida (optional if keys_file is provided) 
            * **queue_settings** (*str*) - One of queue settings predefined sets (default: whole HPC node open_mp)
            * **modules** (*str*) - One of modules predifined hpc module setsi (default: Biobb module)
            * **wait** (*bool*) - Wait for job completion
            * **poll_time** (*int*) - Time between job status checks (seconds)
            * **re_use_task** (*bool*) - Reuse remote working dir if available (requires task_data_path)
            * **remove_tmp** (*bool*) - Remove remote working dir
       properties passed to mdrun
            * **num_threads** (*int*) - (0) Let GROMACS guess. The number of threads that are going to be used.
            * **gmx_lib** (*str*) - (None) Path set GROMACS GMXLIB environment variable.
            * **gmx_path** (*str*) - ("gmx") Path to the GROMACS executable binary.
            * **mpi_bin** (*str*) - (None) Path to the MPI runner. Usually "mpirun" or "srun".
            * **mpi_np** (*str*) - (None) Number of MPI processes. Usually an integer bigger than 1.
            * **mpi_hostlist** (*str*) - (None) Path to the MPI hostlist file.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - ("gromacs/gromacs:latest") Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.
        """

    def __init__(self, input_tpr_path: str, output_trr_path: str, output_gro_path: str, 
                output_edr_path: str, output_log_path: str, output_xtc_path: str = None, 
                output_cpt_path: str = None, output_dhdl_path: str = None, 
                host_config_path: str=None, keys_file: str=None, local_path: str=None, 
                remote_path: str=None, task_data_path: str= None,
                properties: dict =None, **kwargs) -> None:
        self.properties = properties or {}      
        
        self.host = properties.get('host', '')
        self.userid = properties.get('userid', '')
        self.queue_settings = properties.get('queue_settings', 'default')
        self.modules = properties.get('modules', 'biobb')
        self.poll_time = properties.get('poll_time', '10')
        self.wait = properties.get('wait', True)
        self.re_use_task = properties.get('re_use_task', True)

        self.io_dict = {
            "in": {
                'keys_file': keys_file, 
                'local_path': local_path, 
                'remote_path': remote_path,
                'host_config_path': host_config_path,
                },
            "inout": {
                'task_data_path': task_data_path
            }

        }
        
        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', False)
        self.restart = properties.get('restart', False)

        
        self.files = {
            'input_tpr_path' : input_tpr_path, 
            'output_trr_path' : output_trr_path, 
            'output_gro_path' : output_gro_path, 
            'output_edr_path' : output_edr_path, 
            'output_log_path' : output_log_path,
            'output_xtc_path' : output_xtc_path,
            'output_cpt_path' : output_cpt_path,
            'output_dhdl_path' : output_dhdl_path
        }
        #clean local properties
        for p in ('host', 'userid', 'queue_settings', 'modules', 'poll_time', 'wait'):
            if p in self.properties:
                del self.properties[p]

        # Check the properties
        fu.check_properties(self, properties)

    @launchlogger
    def launch(self) -> int:
        """Launches the execution of the remote GROMACS mdrun module."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)
        
        if self.io_dict['in']['keys_file']:
            self.credentials = SSHCredentials()
            self.credentials.load_from_file(self.io_dict['in']['keys_file'])
            slurm = Slurm()
            slurm.set_credentials(self.credentials)
        else:
            slurm = Slurm(host=self.host, userid=self.userid, look_for_keys=True)
        if self.re_use_task:
            try:
                slurm.load_data_from_file(self.io_dict['inout']['task_data_path'])
            except:
                print("Warning: Task data not found")
                pass
        slurm.load_host_config(self.io_dict['in']['host_config_path'])
        slurm.save(self.io_dict['inout']['task_data_path'])
        slurm.set_local_data_bundle(self.io_dict['in']['local_path'], add_files=False)
        slurm.task_data['local_data_bundle'].add_file(
            self.io_dict['in']['local_path'] + "/" + self.files['input_tpr_path']
        )
        slurm.send_input_data(self.io_dict['in']['remote_path'], overwrite=False)
        slurm.save(self.io_dict['inout']['task_data_path'])
        slurm.submit(
            queue_settings=self.queue_settings,
            modules=self.modules,
            poll_time=self.poll_time,
            local_run_script=slurm.get_remote_py_script(
                'from biobb_md.gromacs.mdrun import Mdrun',
                self.files, 
                'Mdrun',
                properties=self.properties)
        )
        slurm.save(self.io_dict['inout']['task_data_path'])
        if self.wait:
            slurm.check_job(poll_time=int(self.poll_time))
            if slurm.task_data['status'] == FINISHED:
                slurm.get_output_data(overwrite=False)
            out_log, err_log = slurm.get_logs()
            slurm.save(self.io_dict['inout']['task_data_path'])
        if self.remove_tmp:
            slurm.clean_remote()
        #return returncode


def main():
    parser = argparse.ArgumentParser(description="Wrapper for the GROMACS mdrun module.",
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help="This file can be a YAML file, JSON file or JSON string")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_tpr_path', required=True)
    required_args.add_argument('--output_trr_path', required=True)
    required_args.add_argument('--output_gro_path', required=True)
    required_args.add_argument('--output_edr_path', required=True)
    required_args.add_argument('--output_log_path', required=True)
    required_args.add_argument('--local_path', required=True)
    required_args.add_argument('--remote_path', required=True)
    required_args.add_argument('--task_data_path', required=True)
    required_args.add_argument('--host_config_path', required=False) 
    parser.add_argument('--output_xtc_path', required=False)
    parser.add_argument('--output_cpt_path', required=False)
    parser.add_argument('--output_dhdl_path', required=False)
    parser.add_argument('--keys_file_path', required=False)
    
    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # Specific call of each building block
    MdrunRmt(input_tpr_path=args.input_tpr_path, output_trr_path=args.output_trr_path,
          output_gro_path=args.output_gro_path, output_edr_path=args.output_edr_path,
          output_log_path=args.output_log_path, output_xtc_path=args.output_xtc_path,
          output_cpt_path=args.output_cpt_path, output_dhdl_path=args.output_dhdl_path,
          host_config_path=args.host_config_path, keys_file=args.keys_file_path, local_path=args.local_path, 
          remote_path=args.remote_path, task_data_path=args.task_data_path,
          properties=properties).launch()

if __name__ == '__main__':
    main()
