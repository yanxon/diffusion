import re
import numpy as np
import matplotlib.pyplot as plt

box = 1.9629018200000001e+01
N = 1000000
tstep = 0.1

positions = []

for i in range(0, N+100, 100):
    log = open("hydrogen_0/"+str(i)+".chkpt")
    array = re.split(r'\s+', log.readlines()[-1])
    positions.append([float(array[3]),
                      float(array[4]),
                      float(array[5])])
    
positions = np.array(positions)

def msd(array, box):
    MSD = []
    
    for i in range(0, len(array)-6001):
        msd = []
        r0 = array[i]
    
        X_b = 0
        Y_b = 0
        Z_b = 0
        
        for j in range(i+1, len(array)):
            rt = array[j]
            _rt = array[j-1]
            r = np.zeros(3,)
        
            # Check x-pos
            if rt[0] - _rt[0] > box/2.:
                X_b -= 1
            elif rt[0] - _rt[0] < -box/2.:
                X_b += 1
            r[0] += rt[0] + X_b * box
        
            # Check y-pos
            if rt[1] - _rt[1] > box/2.:
                Y_b -= 1
            elif rt[1] - _rt[1] < -box/2.:
                Y_b += 1
            r[1] += rt[1] + Y_b * box
        
            # Check z-pos
            if rt[2] - _rt[2] > box/2.:
                Z_b -= 1
            elif rt[2] - _rt[2] < -box/2.:
                Z_b += 1
            r[2] = rt[2] + Z_b * box
        
            dr = r - r0
            dr_square = dr ** 2
        
            msd.append(np.sum(dr_square))
            
        print(len(msd))
            
        MSD.append(msd)

    total = np.zeros(6000)
    
    for z in range(len(MSD)):
        total += MSD[z][:6000]
    
    total = total / len(MSD)
        
    return total
        
msd = msd(positions, box)
time = [x * tstep * 1e-3 for x in range(1, 6001)]
plt.plot(time, msd)
plt.show()
plt.savefig('result.png')
