import matplotlib.pyplot as plt
import numpy as np

URMS = np.genfromtxt("vzdolzni_prerez.txt")

startpos = -83  # Starting measurement position in mm
changepos = 4.5  # Step of position change between two measurements

pos = [startpos + i * changepos for i in range(len(URMS))]
xerr = [0.03 * value for value in URMS]

plt.errorbar(pos, URMS, xerr=xerr, markersize=1, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data")
plt.plot(pos, URMS, c="#C44BC4", alpha=0.1)

plt.title("Vzdolzni prerez uklonske slike tockastega vira")
plt.xlabel("x [mm]")
plt.ylabel(r"$U_{RMS}$ [mV]")
plt.show()
