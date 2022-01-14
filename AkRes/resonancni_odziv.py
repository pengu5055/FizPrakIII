import matplotlib.pyplot as plt
import numpy as np

freq = np.genfromtxt("nal02_resonancni_odziv.txt", usecols=0)
amp = np.genfromtxt("nal02_resonancni_odziv.txt", usecols=1)
amp_sttdev = np.genfromtxt("nal02_resonancni_odziv.txt", usecols=2)
amp_lock = np.genfromtxt("nal02_resonancni_odziv.txt", usecols=3)

plt.scatter(freq, amp, c="#2FDEC6", s=1, label="A")
plt.scatter(freq, amp_sttdev, c="#BEDE2F", s=1, label=r'$\sigma_A$')
plt.scatter(freq, amp_lock, c="#DE2F83", s=1, label=r'$A_\nu$')

plt.title("Resonancni odziv brez absorberja")
plt.xlabel(r'$\nu$ [Hz]')
plt.ylabel("Amplituda")
plt.legend()

plt.show()