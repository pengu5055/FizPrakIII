import matplotlib.pyplot as plt
import numpy as np

URMS = np.genfromtxt("precni_prerez.txt")
URMS_shift = np.genfromtxt("precni_prerez_3cm.txt")

startpos = 11.5  # Starting position in mm
poschange = 1  # Change in position between two subsequent measurements in mm

pos = [startpos + i * poschange for i in range(len(URMS))]
pos_shift = [startpos + i * poschange for i in range(len(URMS_shift))]
xerr = [0.01 * value for value in pos]
xerr_shift = [0.01 * value for value in pos_shift]

plt.errorbar(pos, URMS, xerr=xerr, markersize=1, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data (Srediscna lega)")
plt.errorbar(pos_shift, URMS_shift, xerr=xerr_shift, markersize=1, color="#34e0aa", linestyle='None',
             marker="o", capsize=3, label="Data (3 cm shift)")

plt.title("Precni prerez uklonske slike tockastega vira")
plt.xlabel("x [mm]")
plt.ylabel(r"$U_{RMS}$ [mV]")
plt.legend()
plt.show()
