#!/usr/bin/env bash

BIOBB_IO=$HOME/projects/biobb_adapters/biobb_adapters/biobb_io
cwl-runner $BIOBB_IO/cwl/mmb_api/pdb.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdb.yml
cwl-runner $BIOBB_IO/cwl/mmb_api/pdb_variants.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdbvariants.yml
cwl-runner $BIOBB_IO/cwl/mmb_api/pdb_cluster_zip.cwl $BIOBB_IO/cwl/test/mmb_api/mmbpdbclusterzip.yml
