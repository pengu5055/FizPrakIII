import matplotlib.pyplot as plt
import numpy as np


def rmse(ideal, measured):
    return np.sqrt(((ideal - measured) ** 2).mean())


h = np.genfromtxt("A_Bm.csv", delimiter=";", usecols=0)
bm = np.genfromtxt("A_Bm.csv", delimiter=";", usecols=1)
bt = np.genfromtxt("A_Bt.csv", delimiter=";", usecols=1)
bb = bm - 0.003
plt.plot(h, bm)
plt.plot(h, bt)
plt.legend(["Bm", "Bt", "Bb"])

print("RMSE between lists bt and bm is: " + str(rmse(bt, bm)))
plt.show()
