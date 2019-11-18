import numpy as np
import subprocess
import os


# Generate Pd bulk from LAMMPS
p = subprocess.Popen(['lmp_serial', '-in', 'generate_Pd_bulk.in'], 
                     stdout=subprocess.PIPE)
stdout = p.communicate()[0]
rc = p.returncode
if rc != 0:
    error_msg = "LAMMPS exited with return code %d" %rc
    print(error_msg)

os.remove('log.lammps')


# Insert Hydrogen atoms at random positions.
# The hydrogen atoms can't be too close to the Pd
# Therefore, the H atoms are inserted in between the lattice

pd = open("Pd.dump", "r")
lines = pd.readlines()

no_of_Pd = int(lines[3])

# The size of box in x, y, z directions
x_box = [float(i) for i in lines[5].split()]
y_box = [float(i) for i in lines[6].split()]
z_box = [float(i) for i in lines[7].split()]

atom_id = int(lines[-1].split()[0])
atom_type = 2
bond = 1.95715

# Make a new file for PdH dump
f = open("PdH.dump", "a+")

# Header
f.write("# PdH_x; x = 0.4\n")
f.write(f"{int(no_of_Pd+no_of_Pd*0.4)} atoms\n")
f.write(f"{atom_type} atom types\n")
f.write(f"{x_box[0]} {x_box[1]} xlo xhi\n")
f.write(f"{y_box[0]} {y_box[1]} ylo yhi\n")
f.write(f"{z_box[0]} {z_box[1]} zlo zhi\n")
f.write(f"\n")
f.write(f"Atoms\n")
f.write(f"\n")

for line in lines[9:]:
    f.write(line)

array = np.arange(9, 2057)
np.random.shuffle(array)

for i in array[:819]:
    row = lines[i].split()
    ran = np.random.randint(0, 3)
    atom_id += 1
    
    positions = []
    for i in range(3):
        if i == ran:
            positions.append(float(row[i+2])+bond/2)
        else:
            positions.append(float(row[i+2]))

    l = f"{atom_id} {atom_type} {positions[0]} {positions[1]} {positions[2]}\n"
    f.write(l)

f.close()
