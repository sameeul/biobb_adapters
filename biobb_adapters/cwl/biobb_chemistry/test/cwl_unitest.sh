#!/usr/bin/env bash

RUNNER=cwltool

BIOBB_CHEMISTRY=$HOME/projects/BioBB/biobb_adapters/biobb_adapters/cwl/biobb_chemistry
$RUNNER $BIOBB_CHEMISTRY/acpype/acpype_params_ac.cwl $BIOBB_CHEMISTRY/test/acpype/acpype_params_ac.yml
$RUNNER $BIOBB_CHEMISTRY/acpype/acpype_params_cns.cwl $BIOBB_CHEMISTRY/test/acpype/acpype_params_cns.yml
$RUNNER $BIOBB_CHEMISTRY/acpype/acpype_params_gmx.cwl $BIOBB_CHEMISTRY/test/acpype/acpype_params_gmx.yml
$RUNNER $BIOBB_CHEMISTRY/acpype/acpype_params_gmx_opls.cwl $BIOBB_CHEMISTRY/test/acpype/acpype_params_gmx_opls.yml