import numpy as np
import mdtraj as md


#ref = md.load('/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_carver/ionized.pdb')
ref = md.load('/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_carver/ionized.pdb')

for i in [0]:
#    t = md.load('/Users/asr2031/Desktop/transfer/dDAT_WT_ensemble_carver/msm/tica_l16ns_new_pars12_2/projected/16ns/100micros/15macros/frames_for_macros/small_frames/macro_%d.xtc' %i, top=ref)
    ind = 76 #np.random.choice(range(t.xyz.shape[0]),1)
    print i, t.xyz.shape, ind
    ref.xyz = t.xyz[ind,:,:]
    ref.save_pdb('center_macro_%d.pdb' %i)

