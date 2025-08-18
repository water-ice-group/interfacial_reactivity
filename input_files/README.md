Example input files for running well-tempered metadynamics across the gaseous, bulk and interfacial systems. 
We utilize multiple-walker metaD, the setup for which is shown in these subdirectories. For each walker, we include
* `init.lmpdat`: the lammps structure file for the starting configuration.
* `lammps.inp`:  the input lammps script for running MD.
* `plumed.dat`:  the plumed file used to specify collective variables and perform enhanced sampling MD.
* `run.slurm`:   example slurm script. 
