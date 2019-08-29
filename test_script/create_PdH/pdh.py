import numpy as np

f = open("PdH.dump", "r")
lines = f.readlines()
f.close()

atom_id = int(lines[-1].split()[0])
atom_type = 2
bond = 1.95715

f = open("PdH.dump", "a+")

array = np.arange(9, 2057)
np.random.shuffle(array)
print(array[:819])

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
