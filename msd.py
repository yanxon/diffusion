import os
import re
import matplotlib.pyplot as plt
import numpy as np
import subprocess

N = 100

MSD = []
STEP = []
TEMP = []

for n in range(N):
    p = subprocess.Popen(['lmp_serial', '-in', 'diff.in'], stdout=subprocess.PIPE)
    stdout = p.communicate()[0]
    rc = p.returncode
    if rc != 0:
        error_msg = "LAMMPS exited with return code %d" %rc
        print(error_msg)
    
    step = []
    temp = []
    msd = []
    log = open("log.lammps")
    for i, line in enumerate(log):
        if i > 83 and i <= 83+(10000+1): # 10000 = runtime/step
            arr = re.split(r'\s+', line)
            temperature = float(arr[2])
            step.append(float(arr[1])*0.001*1e-3) # 0.001 => tstep, 1e-3 to ns
            temp.append(float(arr[2]))
            msd.append(float(arr[3]))
    log.close()
    os.remove("log.lammps")

    MSD.append(msd)
    STEP.append(step)
    TEMP.append(temp)

m_msd = np.mean(MSD, axis=0)

np.savetxt('msd_paths.txt', MSD)
plt.plot(step, m_msd)
plt.savefig('msdvstime.png', dpi=1000)
