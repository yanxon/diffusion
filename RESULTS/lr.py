import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

d = ["300.out", "325.out", "350.out", "375.out",
     "400.out", "425.out", "450.out", "475.out",
     "500.out", "550.out", "600.out"]
temp = [300., 325, 350, 375,
        400., 425, 450, 475,
        500., 550., 600]
#d_ = ["300_.out", "400_.out", "500_.out", "600_.out"]
#temp_ = [300., 400., 500., 600.,]

D = []
for i in range(len(d)):
    data = np.loadtxt(d[i])

    time = (data[:, 0] * 5e-4).reshape(-1, 1)
    msd = data[:, 2]

    lr = LinearRegression()
    lr.fit(time, msd)
    msd_ = lr.predict(time)

    D.append(lr.coef_/6)
    
    plt.plot(time, msd_, 'r')
    plt.scatter(time, msd)
    plt.xlabel("time (ps)")
    plt.ylabel("msd (A^2)")
    plt.show()

#D_ = []
#for i in range(len(d_)):
#    data = np.loadtxt(d_[i])
#
#    time = (data[:, 0] * 5e-4).reshape(-1, 1)
#    msd = data[:, 2]
#    lr = LinearRegression()
#    lr.fit(time, msd)
#    msd_ = lr.predict(time)
#
#    D_.append(lr.coef_/6)
#
#    plt.plot(time, msd_, 'r')
#    plt.scatter(time, msd)
#    plt.xlabel("time (ps)")
#    plt.ylabel("msd (A^2)")
#    plt.show()

ln = np.log(D)
ln_ = np.log(D_)
T_ = (1 / (np.asarray(temp_) * 1.38064852e-23 * 6.242e+18)).reshape(-1, 1)
T = (1 / (np.asarray(temp) * 1.38064852e-23 * 6.242e+18)).reshape(-1, 1)
lr2 = LinearRegression()
lr2.fit(T, ln)
Q = abs(lr2.coef_[0][0])
print(Q)

plt.scatter(T, ln)
plt.scatter(T_, ln_, color='red')
plt.xlabel("1/kT (1/eV)")
plt.ylabel("ln(D)")
plt.title(f"Q = {Q} eV")
plt.savefig('arrhenius_plot.png')
