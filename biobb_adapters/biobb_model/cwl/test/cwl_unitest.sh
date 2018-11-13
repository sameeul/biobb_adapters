#!/usr/bin/env bash

BIOBB_MODEL=$HOME/projects/biobb_adapters/biobb_adapters/biobb_io/biobb_model
cwl-runner $BIOBB_MODEL/cwl/model/mutate.cwl $BIOBB_MODEL/cwl/test/model/mutate.yml
cwl-runner $BIOBB_MODEL/cwl/model/fix_side_chain.cwl $BIOBB_MODEL/cwl/test/model/fix_side_chain.yml
