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
r1 = u1/-i1
r2 = u2/-i2
r3 = u3/-i3
r4 = u4/-i4

plt.plot(u1, r1, c="#00E1FF", lw=2, alpha=0.2)
plt.plot(u2, r2, c="#00DEA3", lw=2, alpha=0.2)
plt.plot(u3, r3, c="#DE00B5", lw=2, alpha=0.2)
plt.plot(u4, r4, c="#DE0004", lw=2, alpha=0.2)
plt.scatter(u1, r1, c="#00E1FF", s=4)
plt.scatter(u2, r2, c="#00DEA3", s=4)
plt.scatter(u3, r3, c="#DE00B5", s=4)
plt.scatter(u4, r4, c="#DE0004", s=4)
plt.errorbar(u1, i1, c="#00E1FF", xerr=0.0035, yerr=0.000001, fmt="none")  # fmt="none" creates error bars without connecting points
plt.errorbar(u2, i2, c="#00DEA3", xerr=0.0035, yerr=0.000001, fmt="none")
plt.errorbar(u3, i3, c="#DE00B5", xerr=0.0035, yerr=0.000001, fmt="none")
plt.errorbar(u4, i4, c="#DE0004", xerr=0.0035, yerr=0.000001, fmt="none")
plt.show()
