import re
import numpy as np
import matplotlib.pyplot as plt

box = 1.9629018200000001e+01
N = 1000000
tstep = 0.001

positions = []

for i in range(0, N+100, 100):
    log = open(str(i)+".chkpt")
    array = re.split(r'\s+', log.readlines()[-1])
    positions.append([float(array[3]),
                      float(array[4]),
                      float(array[5])])
    
positions = np.array(positions)
print(positions)

def msd(array, box):
    msd = []
    r0 = array[0]
    
    X_b = 0
    Y_b = 0
    Z_b = 0
    
    for i in range(1, len(array)):
        rt = array[i]
        _rt = array[i-1]
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
        
    return msd
        
msd = msd(positions, box)
time = [x * tstep * 1e-3 for x in range(100, 1000100, 100)]


plt.plot(time, msd)
plt.show()
