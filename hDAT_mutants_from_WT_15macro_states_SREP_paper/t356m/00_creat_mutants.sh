#!/bin/bash

for i in `seq 0 14` ; do

/Applications/VMD_1.9.2.app/Contents/vmd/vmd_MACOSXX86 -dispdev none   ../ionized.psf ../center_macro_${i}.pdb <<EOF

play tcl_for_mutating_T356M_from_SREP_15macros.tcl

quit
EOF

mv mol_t356m.pdb mol_t356m_${i}.pdb

done 
