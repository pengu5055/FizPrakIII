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
r1 = u1/(-i1)
r2 = u2/(-i2)
r3 = u3/(-i3)
r4 = u4/(-i4)
p1 = u1*(-i1)
p2 = u2*(-i2)
p3 = u3*(-i3)
p4 = u4*(-i4)
print(r1)

plt.plot(r1, p1, c="#00E1FF", lw=2, alpha=0.2)
plt.plot(r2, p2, c="#00DEA3", lw=2, alpha=0.2)
plt.plot(r3, p3, c="#DE00B5", lw=2, alpha=0.2)
plt.plot(r4, p4, c="#DE0004", lw=2, alpha=0.2)
plt.scatter(r1, p1, c="#00E1FF", s=7, marker="v")
plt.scatter(r2, p2, c="#00DEA3", s=7, marker="^")
plt.scatter(r3, p3, c="#DE00B5", s=7, marker="*")
plt.scatter(r4, p4, c="#DE0004", s=7, marker="d")

plt.title("Moc v odvisnosti od upora na fotodiodi")
plt.xlabel(r'R [k$\Omega$]')
plt.ylabel("P [mW]")

plt.show()
