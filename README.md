## Sample Diffusion Calculation with LAMMPS


### Introduction
This research is to reproduce the result in this [paper](https://www.sciencedirect.com/science/article/pii/S1359646218300824). 

In the paper, the authors focus on Pallalidum Hydride (PdHx) system, where x is the fractional concentration of Hydrogen atom with respect to one Palladium atom. PdHx is a metallic system that consists of many H atoms in the Pd crystal lattice. The main purpose of the paper is to inspect the hydrogen diffusivity in bulk fcc Pd. Since Hydrogen absorption in Palladium is reversible, PdHx is a promising material for hydrogen storage applications.

This research utilizes Force Field Molecular Dynamics (MD) simulations. First, a fcc Pd cell with 8 x 8 x 8 is created (2048 Pd atoms), while 819 H atoms (40% of Pd atoms) are inserted in the Pd lattice. Then, the PdHx (x=0.4) structure is minimize. Using Pd-H embedded-atom method (EAM) potential, MD simulations are performed with NPT ensemble at T = 300K, 325K, 350K, 375K, 400K, 425K, 450K, 475K, 500K, 525K, 550K, 575K, and 600K. In particular, Figure 1(a) is attempted.

### To run the code

```
python run.py
```
The calculations may take a while. If impatience, please reduce the runtime.

### Result

After the simulation is done, one can view and collect the [mean square displacement](https://en.wikipedia.org/wiki/Mean_squared_displacement) in the `.log` files for each temperature. Then, the diffusivity can be calculation using the Einstein relation for Brownian motion. Finally, the activation energy (Q) can be obtained from the slope of the Arrhenius plot:
![alt text](https://github.com/yanxon/diffusion/blob/master/RESULTS/Arrhenius_plot.png)


### Dependencies
- LAMMPS
- Python 3.x
