#!/usr/bin/env bash

BIOBB_MD=$HOME/projects/biobb_adapters/biobb_adapters/biobb_md
cwl-runner $BIOBB_MD/cwl/gromacs/pdb2gmx.cwl $BIOBB_MD/cwl/test/gromacs/pdb2gmx.yml
cwl-runner $BIOBB_MD/cwl/gromacs/editconf.cwl $BIOBB_MD/cwl/test/gromacs/editconf.yml
cwl-runner $BIOBB_MD/cwl/gromacs/genion.cwl $BIOBB_MD/cwl/test/gromacs/genion.yml
cwl-runner $BIOBB_MD/cwl/gromacs/genrestr.cwl $BIOBB_MD/cwl/test/gromacs/genrestr.yml
cwl-runner $BIOBB_MD/cwl/gromacs/grompp.cwl $BIOBB_MD/cwl/test/gromacs/grompp.yml
cwl-runner $BIOBB_MD/cwl/gromacs/mdrun.cwl $BIOBB_MD/cwl/test/gromacs/mdrun.yml
cwl-runner $BIOBB_MD/cwl/gromacs/solvate.cwl $BIOBB_MD/cwl/test/gromacs/solvate.yml
cwl-runner $BIOBB_MD/cwl/gromacs/make_ndx.cwl $BIOBB_MD/cwl/test/gromacs/make_ndx.yml
cwl-runner $BIOBB_MD/cwl/gromacs_extra/ndx2resttop.cwl $BIOBB_MD/cwl/test/gromacs_extra/ndx2resttop.yml
