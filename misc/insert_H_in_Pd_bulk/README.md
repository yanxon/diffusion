## A script to insert H atoms in bulk fcc Pd

The `insert_H_in_Pd_bulk.py` is a script to insert H atoms in bulk fcc Pd. The H atoms are inserted inside the bulk Pd at a random position. Meanwhile, The H atoms can't be too close to the Pd atoms. If so, the repulsive force will approach infinity, and the H atoms will fly out immediately.

The Python script depends on `LAMMPS` software to run.

After the script is run, `PdH.dump` can be visualized using `OVITO` visualization tool.
