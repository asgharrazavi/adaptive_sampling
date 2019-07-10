## These are conformations for 15 macro states that was created and referenced in hDAT-wildtype MSM paper:

###     A Markov State-based Quantitative Kinetic Model of Sodium Release from the Dopamine Transporter

<a href="https://www.nature.com/articles/srep40076">https://www.nature.com/articles/srep40076</a>

------

### Comments
   * `center_macro_*.pdb` are selected centers for each macro state.
   * `img_center_macro_location_on_tica.png` shows location of each selected macrostate center on tICA landscape. 
   * `original_SREP_tica.h5` is the original tICA object (with keys: `['components', 'covariance', 'lag_time', 'vals', 'vecs']` ) that was used in the above-cited paper. 
   * `raw_data.npy` contains the 12 tICA parameter values for each selected macrostate pdb file. 
   * The folder ***tcls*** contains tcl files for calculating tICA parameters.
   * The folder ***toppar_all*** contains charmm files to create mutants using 15 macrostate pdb files.
   * The folder ***i312f*** contains pdb files fir the I312F mutation for all 15 macrostates.
   * The folder ***t356m*** contains pdb files fir the I312F mutation for all 15 macrostates.
   * `t356m/00_creat_mutants.sh` is used to creat mutated pdb files, which uses `t356m/tcl_for_mutating_T356M_from_SREP_15macros.tcl` tcl file. 
