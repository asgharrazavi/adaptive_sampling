from openmm import *
#from simtk.unit import *
#from sys import stdout
#from sys import stdout, exit, stderr
from openmm import unit
from openmm import app
import numpy as np
#import mdtraj as md
import os,sys
#import simtk.openmm as mm
import time
#from openmmplumed import PlumedForce

from openff.toolkit import Molecule
from openmmforcefields.generators import SMIRNOFFTemplateGenerator


print('building protein and solvating...')
omm_forcefield = app.ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')#,'./ligand_fix_eps_manually.xml')
prot_pdb_file = app.PDBFile('test_vhl_6zhc_prot_lig.pdb') 
top = prot_pdb_file.topology
    
lig = Molecule.from_file('test_vhl_6zhc_lig.sdf')
smirnoff = SMIRNOFFTemplateGenerator(forcefield="openff-2.0.0", molecules=lig)
omm_forcefield.registerTemplateGenerator(smirnoff.generator)

modeller = app.Modeller(top, prot_pdb_file.positions)
    
print('Adding hydrogens...')
modeller.addHydrogens(omm_forcefield)
    
with open('preps_prot.pdb', 'w') as f:
    app.PDBFile.writeFile(modeller.topology, modeller.positions, f, keepIds=True)
    
print('Adding solvent...')
modeller.addSolvent(omm_forcefield, model='tip3p', padding=0.9*unit.nanometer, ionicStrength=0.1*unit.molar, positiveIon='Na+', negativeIon='Cl-')
    
with open('preps_sys.pdb', 'w') as f:
    app.PDBFile.writeFile(modeller.topology, modeller.positions, f, keepIds=True)
    
modeller.topology.setUnitCellDimensions(modeller.topology.getUnitCellDimensions())
    
    
positions = modeller.positions
topology = modeller.topology
    
print('Building system...')
system = omm_forcefield.createSystem(topology, nonbondedMethod=app.PME, nonbondedCutoff=0.9*unit.nanometer, constraints=app.HBonds) #, hydrogenMass=3.024*unit.amu)
    
barostat = MonteCarloBarostat(1.0*unit.bar, 310.0*unit.kelvin)
system.addForce(barostat)
    

integrator = LangevinMiddleIntegrator(310*unit.kelvin, 1/unit.picosecond, 0.002*unit.picoseconds)
log_name = 'log.log' 
traj_name = 'traj.dcd' 
do_minimization = 1 

save_stride = 1000
steps = 100000000 
dcdReporter = app.DCDReporter(traj_name, save_stride)
dataReporter = app.StateDataReporter(log_name, save_stride, totalSteps=steps, step=True, time=True, speed=True, progress=True, potentialEnergy=True, kineticEnergy=True, totalEnergy=True, temperature=True, volume=True, density=True, separator=',')

simulation = app.Simulation(topology, system, integrator)
simulation.reporters.append(dcdReporter)
simulation.reporters.append(dataReporter)
simulation.reporters.append(app.CheckpointReporter('checkpnt.chk', save_stride))

print('using GPU?: ', simulation.context.getPlatform().getName())

randomSeed = int(repr(time.time()).split('.')[1])
if do_minimization:
    simulation.context.setPositions(positions)
    print('minimizing...')
    print('Initial potential energy = %s' % simulation.context.getState(getEnergy=True).getPotentialEnergy())
    initial_time = time.time()
    simulation.minimizeEnergy() #maxIterations=10000)
    final_time = time.time()
    print('Final potential energy   = %s' % simulation.context.getState(getEnergy=True).getPotentialEnergy())
    elapsed_time = final_time - initial_time
    print('Time elapsed: %f seconds' % elapsed_time)
    positions = simulation.context.getState(getPositions=True).getPositions()
    app.PDBFile.writeFile(simulation.topology, positions, open('minimized.pdb', 'w'), keepIds=True)
    # Check for minimization errors:
    forces = simulation.context.getState(getForces=True).getForces().value_in_unit(unit.kilojoules/unit.mole/unit.nanometer)
    for atom, f in zip(topology.atoms(), forces):
        if unit.norm(f) > 1e4:
            print(atom, f)
    randomSeed = int(repr(time.time()).split('.')[1])
    simulation.context.setVelocitiesToTemperature(10, randomSeed)
    temperatures = range(0,300,10)
    for temp in temperatures:
        print('temperature:', temp)
        integrator.setTemperature(temp*unit.kelvin)
        simulation.step(1000)
else:
    print('loading from checkpoint...')
    with open('checkpnt.chk', 'rb') as f:
        simulation.context.loadCheckpoint(f.read())

print('simulating...')

simulation.step(steps)
simulation.saveState('final_state_file_%s.xml' %(steps))
positions = simulation.context.getState(getPositions=True).getPositions()
app.PDBFile.writeFile(simulation.topology, positions, open('final_state_file_%s.pdb' %(steps), 'w'), keepIds=True)
