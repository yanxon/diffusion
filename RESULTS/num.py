import numpy as np

def delete_headers(filename):
    with open(f"{filename}.chkpt", "r") as fin:
        data = fin.read().splitlines(True)
    with open(filename, 'w') as fout:
        fout.writelines(data[8:])

for i in range(1):
    delete_headers(str(i))
   
    data = np.loadtxt("0", skiprows=1)
    assert len(data) == 819, "The length doesn't match!"
    data = data[data[:, 0].argsort()]

    
