import os
import re
import matplotlib.pyplot as plt
import numpy as np
import sympy
import subprocess

N = 100

def MSD(N):
    primes = list(sympy.primerange(500, 2000))
    
    MSD = []
    STEP = []
    TEMP = []

    for n in range(N):
        directory = 'hydrogen_'+str(primes[n])
        os.mkdir(directory)

        string_of_text = []
        with open("diff.in") as f:
            for line in f:
                if line[:15] == 'dump 1 2 custom':
                    line = f"dump 1 2 custom 100 {directory}/*.chkpt id type mass x y z\n"
                elif line[:27] == "variable Srandomseed equal ":
                    line = f"variable Srandomseed equal {primes[n]}\n"
                string_of_text.append(line)

        with open("diff.in", 'w') as f:
            for line in string_of_text:
                f.write(line)

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
            if i > 130 and i <= 80+(10000): # 10000 = runtime/step
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

    np.savetxt('results/msd_paths.txt', MSD)
    plt.plot(step, m_msd)
    plt.xlabel('time (ns)')
    plt.ylabel('MSD (A^2)')
    plt.savefig('results/msdvstime.png', dpi=1000)

if __name__ == '__main__':
    MSD(N)
