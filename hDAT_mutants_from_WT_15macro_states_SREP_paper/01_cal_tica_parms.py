import numpy as np
import mdtraj as md
import os,sys


vmd = "/Applications/VMD_1.9.2.app/Contents/vmd/vmd_MACOSXX86 -dispdev none"

os.system(''' %s ionized.psf center_macro_?.pdb center_macro_??.pdb <<EOF

play tcls/tk_d436_r445.tcl       
play tcls/tk_na2_d421.tcl        
play tcls/tk_na2_e428.tcl        
play tcls/tk_na2_water_coord.tcl 
play tcls/tk_r60_e428.tcl        
play tcls/tk_r60_y335.tcl
play tcls/tk_e428_r445.tcl       
play tcls/tk_na2_d79.tcl         
play tcls/tk_na2_na1.tcl         
play tcls/tk_r60_d436.tcl        
play tcls/tk_r60_e446.tcl        
play tcls/tk_y335_e428.tcl


quit
EOF
 ''' %(vmd))


names = [
'r60_y335',
'r60_e446',        
'r60_e428',        
'na2_water_coord',
'na2_e428',        
'na2_d421',        
'na2_d79',         
'e428_r445',       
'y335_e428',
'd436_r445',       
'r60_d436',        
'na2_na1',         
]

data = np.ones((15,12)) * -1
for i in range(len(names)):
    data[:,i] = np.loadtxt('%s.txt' %names[i])

print data, data.shape
np.save('raw_data.npy',data)


