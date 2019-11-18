import numpy as np
import re
import matplotlib.pyplot as plt

data = open("msd_paths.txt", 'r')

msd = []
for line in data:
    line_string = re.split('\s+', line)
    arr = []
    for i in line_string:
        try:
            arr.append(float(i))
        except:
            pass
    
    msd.append(arr)

print(msd[0][-1000])
print("\n")
print(msd[59][-1000])

msd_mean = np.mean(msd, axis=0)

#plt.plot(range(0, 9950), msd_mean)
#plt.show()
