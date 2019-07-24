from sklearn.linear_model import LinearRegression as LR
import numpy as np
import matplotlib.pyplot as plt

Y = np.loadtxt("msd_paths.txt")
Y = np.mean(Y, axis=0)
X = np.arange(0.005, 1, 0.0001)
X = X.reshape(-1, 1)

reg = LR()
reg.fit(X, Y)

slope = reg.coef_
intercept = reg.intercept_
_Y = reg.predict(X)

print(f"The diffusion coefficient is: {slope[0]/6} A^2/ns")

plt.plot(X, Y, color='blue', linewidth=2, label="Mean Squared Displacement")
plt.plot(X, _Y, color='red', linewidth=2, label="fit")
plt.ylabel("MSD (A^2)")
plt.xlabel("time (ns)")
plt.title(f"D = {round(slope[0]/6, 2)} A^2/ns")
plt.legend()
plt.savefig('fit.png', dpi=100)
