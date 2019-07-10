#!/bin/bash

for i in `seq 0 14` ; do

/Applications/VMD_1.9.2.app/Contents/vmd/vmd_MACOSXX86 -dispdev none   ../ionized.psf ../center_macro_${i}.pdb <<EOF

play tcl_for_mutating_I312F_from_SREP_15macros.tcl

quit
EOF

mv mol_i312f.pdb mol_i312f_${i}.pdb

done 
