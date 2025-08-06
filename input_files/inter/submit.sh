#!/bin/bash

home=$(pwd)

for dir in ./walk*;
do
	cd $dir

	sbatch run.slurm 

	cd $home

done
