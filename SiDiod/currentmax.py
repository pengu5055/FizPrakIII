import matplotlib.pyplot as plt
import numpy as np

u1 = np.genfromtxt("nal02_dist00.txt", usecols=0)
i1 = np.genfromtxt("nal02_dist00.txt", usecols=1)
u2 = np.genfromtxt("nal02_dist05.txt", usecols=0)
i2 = np.genfromtxt("nal02_dist05.txt", usecols=1)
u3 = np.genfromtxt("nal02_dist10.txt", usecols=0)
i3 = np.genfromtxt("nal02_dist10.txt", usecols=1)
u4 = np.genfromtxt("nal02_dist15.txt", usecols=0)
i4 = np.genfromtxt("nal02_dist15.txt", usecols=1)

print("1: {}".format(min(i1)))
print("2: {}".format(min(i2)))
print("3: {}".format(min(i3)))
print("4: {}".format(min(i4)))
