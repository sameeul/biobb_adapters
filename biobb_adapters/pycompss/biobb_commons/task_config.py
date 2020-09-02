import os
import sys
import uuid

def config_gromacs_multinode( properties , all_mpi=True):
    num_nodes = int(os.environ["COMPSS_NUM_NODES"])
    num_threads = int(os.environ["COMPSS_NUM_THREADS"])
    if all_mpi :
        properties["mpi_np"] = num_nodes * num_threads
        #properties["num_omp_threads"] = 1
        os.environ["OMP_NUM_THREADS"] = "1"
    else :
        #properties["num_omp_threads"] = num_threads
        properties["mpi_np"] = num_nodes
    hostnames = os.environ["COMPSS_HOSTNAMES"]
    hostlist_file=str(uuid.uuid1())+".hostfile"
    with open(hostlist_file, "w") as h_file:
       h_file.write(hostnames.replace(",","\n"))
    properties["mpi_hostlist"] = hostlist_file

