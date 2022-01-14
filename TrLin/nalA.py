import matplotlib.pyplot as plt
import numpy as np

freq = np.genfromtxt("odziv_A.txt", usecols=1)
RMS = np.genfromtxt("odziv_A.txt", usecols=2)


plt.plot(freq, RMS, c="#008bfc")
plt.scatter(freq, RMS, c="#008bfc", s=3)
plt.title("Odvisnost amplitude napetosti od frekvence signala v tocki A")
plt.xlabel(r'$\nu$[Hz]')
plt.ylabel(r"$U_{RMS}$ [V]")
plt.show()
