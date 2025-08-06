#!/bin/bash
#SBATCH --job-name=gas_1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=150:00:00
#SBATCH --partition=MAIN
#SBATCH --gpus=1

module add gcc/7.5.0 icc mkl anaconda/python3 mpi/openmpi/gnu7
module unload cuda/10.2
module load cuda/11.7
conda activate mace

/location/of/lammps/executable/lmp -k on g 1 -sf kk < lammps.inp

exit 0;
