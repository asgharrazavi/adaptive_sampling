
animate write psf non_protein.psf sel [atomselect top "not protein"]
animate write pdb non_protein.pdb sel [atomselect top "not protein"]

animate write pdb prot_A.pdb sel [atomselect top "protein"]


package require psfgen

# these are important
topology /Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/top_all36_carb.rtf
topology /Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/top_all36_cgenff.rtf
topology /Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/top_all36_lipid.rtf
topology /Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/top_all36_na.rtf
topology /Users/asr2031/Dropbox/pyscripts/Namd/toppar_all/top_all36_prot.rtf

pdbalias residue HIS HSD
pdbalias atom ILE CD1 CD
pdbalias residue NA SOD
pdbalias atom NA NA SOD
pdbalias residue HOH TIP3
pdbalias atom TIP3 OW OH2

resetpsf


segment PROT {
      pdb prot_A.pdb
      mutate 356 MET
   }
coordpdb prot_A.pdb 


#patch NTER PROT:1
#patch CTER PROT:620
patch DISU PROT:180  PROT:189
patch GLUP PROT:491

# it is important these two be here at last
guesscoord
regenerate angles dihedrals 


writepdb protein.pdb
writepsf protein.psf



resetpsf

readpsf  protein.psf
coordpdb protein.pdb

readpsf  non_protein.psf
coordpdb non_protein.pdb

writepdb mol_t356m.pdb
writepsf mol_t356m.psf

