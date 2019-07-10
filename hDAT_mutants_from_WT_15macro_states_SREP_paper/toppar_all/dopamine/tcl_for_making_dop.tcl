

package require psfgen
topology dop_2.rtf

segment DOP {
      pdb dop.pdb
   }
coordpdb dop.pdb DOP

guesscoord
regenerate angles dihedrals 

writepdb dop2.pdb
writepsf dop2.psf


