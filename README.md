## Sample Diffusion Calculation with LAMMPS

The [diff.in](https://github.com/yanxon/diffusion/blob/master/diff.in) script constructs fcc bulk Pd with equilibrium lattice parameter 3.92580364 A at 800 K. A hydrogen atom is randomly generated on the fly and is tracked throughout the NVT MD simulation by LAMMPS software. In addition, the [mean squared displacement](https://en.wikipedia.org/wiki/Mean_squared_displacement) (MSD) of the hydrogen is calculated by LAMMPS for every time step.

To get better statictics, it is recommended to increase the number of NVT simulation in [msd.py](https://github.com/yanxon/diffusion/blob/master/msd.py), which is denoated as N. For each N, it will take about 10 mins depending on the computer power.

To run the script:
```
python msd.py
```

After calculation is done:
1. Check the result folder for the MSD vs time plot.
2. The movie of the hydrogen in the box can be viewed in the hydrogen_* folder using OVITO.

Dependencies:
- LAMMPS
- Python 3.x
