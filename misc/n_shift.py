import numpy as np
import matplotlib.pyplot as plt


def delete_headers(filename):
    with open(f"{filename}.chkpt", "r") as fin:
        data = fin.read().splitlines(True)
    with open(filename, 'w') as fout:
        fout.writelines(data[9:])

def msd(positions, box, shift):
    MSD = np.zeros((shift, len(positions)-1))

    for i in range(shift):
        msd = []
        r0 = positions[i]
        X_b = 0
        Y_b = 0
        Z_b = 0

        for j in range(i+1, len(positions)):
            rt = positions[j]
            _rt = positions[j-1]
            r = np.zeros(3,)

            # Check x direction
            if rt[0] - _rt[0] > box/2.:
                X_b -= 1
            elif rt[0] - _rt[0] < -box/2.:
                X_b += 1
            r[0] += rt[0] + X_b * box

            # Check y direction
            if rt[1] - _rt[1] > box/2.:
                Y_b -= 1
            elif rt[1] - _rt[1] < -box/2.:
                Y_b += 1
            r[1] += rt[1] + Y_b * box

            # Check z direction
            if rt[2] - _rt[2] > box/2.:
                Z_b -= 1
            elif rt[2] - _rt[2] < -box/2.:
                Z_b += 1
            r[2] += rt[2] + Z_b * box

            dr = r - r0

            dr_square = dr ** 2

            msd.append(np.sum(dr_square))

        MSD[i][:len(msd)] += np.asarray(msd)
    
    trajectory = len(positions) - shift
    total = np.sum(MSD, axis=0)
    total = total[:trajectory] / len(MSD)

    return total

box = 33.31436605599842
N = 819 # num of particles
M = 8711 # num of timestep
positions = np.zeros((M, N, 3))
for i in range(M):
    delete_headers(str(i*4400))
   
    data = np.loadtxt(str(i*4400))
    #assert len(data) == 819, "The length doesn't match!"
    data = data[data[:, 0].argsort()]
    positions[i] += data[:, -3:]

MSD = []
for i in range(N):
    pos = positions[:, i, :]
    MSD.append(msd(pos, box, 10))

MSD = np.asarray(MSD)
MSD = np.sum(MSD, axis=0)

plt.plot(MSD)
plt.show()
