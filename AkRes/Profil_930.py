import matplotlib.pyplot as plt
import numpy as np

amp = np.genfromtxt("nal03_frekv_930.txt", usecols=0)
amp_sttdev = np.genfromtxt("nal03_frekv_930.txt", usecols=1)
amp_lock = np.genfromtxt("nal03_frekv_930.txt", usecols=2)

premik = 10  # Premik vzdolz x osi med vsakimi meritvami v mm
zacetnalega = 11.7  # Zacetna oddaljenost mikrofona od stene v mm
pos = [zacetnalega + i*premik for i in range(len(amp))]

print(pos)

plt.scatter(pos, amp, c="#2FDEC6", s=5, label="A")
plt.scatter(pos, amp_sttdev, c="#BEDE2F", s=5, label=r'$\sigma_A$')
plt.scatter(pos, amp_lock, c="#DE2F83", s=5, label=r'$A_\nu$')

plt.title("Zvocni profil v resonatorju pri 930Hz")
plt.xlabel(r'$r$ [mm]')
plt.ylabel("Amplituda")
plt.legend()

plt.show()