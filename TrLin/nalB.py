import matplotlib.pyplot as plt
from matplotlib import axes
import numpy as np


def listorder(list1, list2):
    combine = zip(list1, list2)
    combine_s = sorted(list(combine))
    list1_s = [i for (i, s) in combine_s]
    list2_s = [s for (i, s) in combine_s]

    return list1_s, list2_s


def listinterval(list1, list2, a=-np.inf, b=np.inf, c=-np.inf, d=np.inf, sort=False):
    if sort:
        list1_s, list2_s = listorder(list1, list2)
        combine = list(zip(list1_s, list2_s))
    else:
        combine = list(zip(list1, list2))

    list2_i = [s for (i, s) in combine if a <= i <= b and c <= s <= d]
    list1_i = [i for (i, s) in combine if a <= i <= b and c <= s <= d]

    return list1_i, list2_i


freq1 = np.genfromtxt("odziv_B_000.txt", usecols=1)
RMS1 = np.genfromtxt("odziv_B_000.txt", usecols=2)

freq2 = np.genfromtxt("odziv_B_005.txt", usecols=1)
RMS2 = np.genfromtxt("odziv_B_005.txt", usecols=2)

freq3 = np.genfromtxt("odziv_B_010.txt", usecols=1)
RMS3 = np.genfromtxt("odziv_B_010.txt", usecols=2)

freq4 = np.genfromtxt("odziv_B_015.txt", usecols=1)
RMS4 = np.genfromtxt("odziv_B_015.txt", usecols=2)

freq5 = np.genfromtxt("odziv_B_022.txt", usecols=1)
RMS5 = np.genfromtxt("odziv_B_022.txt", usecols=2)

freq6 = np.genfromtxt("odziv_B_033.txt", usecols=1)
RMS6 = np.genfromtxt("odziv_B_033.txt", usecols=2)

freq7 = np.genfromtxt("odziv_B_051.txt", usecols=1)
RMS7 = np.genfromtxt("odziv_B_051.txt", usecols=2)

freq8 = np.genfromtxt("odziv_B_100.txt", usecols=1)
RMS8 = np.genfromtxt("odziv_B_100.txt", usecols=2)

freq9 = np.genfromtxt("odziv_B_215.txt", usecols=1)
RMS9 = np.genfromtxt("odziv_B_215.txt", usecols=2)

freq10 = np.genfromtxt("odziv_B_560.txt", usecols=1)
RMS10 = np.genfromtxt("odziv_B_560.txt", usecols=2)

freq11 = np.genfromtxt("odziv_B_inf.txt", usecols=1)
RMS11 = np.genfromtxt("odziv_B_inf.txt", usecols=2)

freq1_s, RMS1_s = listinterval(freq1, RMS1, a=0.2*10**7, b=10**7, sort=True)
freq2_s, RMS2_s = listinterval(freq2, RMS2, a=0.2*10**7, b=10**7, sort=True)
freq3_s, RMS3_s = listinterval(freq3, RMS3, a=0.2*10**7, b=10**7, sort=True)
freq4_s, RMS4_s = listinterval(freq4, RMS4, a=0.2*10**7, b=10**7, sort=True)
freq5_s, RMS5_s = listinterval(freq5, RMS5, a=0.2*10**7, b=10**7, sort=True)
freq6_s, RMS6_s = listinterval(freq6, RMS6, a=0.2*10**7, b=10**7, sort=True)
freq7_s, RMS7_s = listinterval(freq7, RMS7, a=0.2*10**7, b=10**7, sort=True)
freq8_s, RMS8_s = listinterval(freq8, RMS8, a=0.2*10**7, b=10**7, sort=True)
freq9_s, RMS9_s = listinterval(freq9, RMS9, a=0.2*10**7, b=10**7, sort=True)
freq10_s, RMS10_s = listinterval(freq10, RMS10, a=0.2*10**7, b=10**7, sort=True)
freq11_s, RMS11_s = listinterval(freq11, RMS11, a=0.2*10**7, b=10**7, sort=True)


plt.plot(freq1_s[14:], RMS1_s[14:])
plt.plot(freq2_s, RMS2_s)
plt.plot(freq3_s, RMS3_s)
plt.plot(freq4_s, RMS4_s)
plt.plot(freq5_s, RMS5_s)
plt.plot(freq6_s, RMS6_s)
plt.plot(freq7_s, RMS7_s)
plt.plot(freq8_s, RMS8_s)
plt.plot(freq9_s, RMS9_s)
plt.plot(freq10_s, RMS10_s)
plt.plot(freq11_s[5:], RMS11_s[5:], c="#88f257")

plt.scatter(freq1_s, RMS1_s, s=3, label=r'0 $\Omega$')
plt.scatter(freq2_s, RMS2_s, s=3, label=r'5 $\Omega$')
plt.scatter(freq3_s, RMS3_s, s=3, label=r'10 $\Omega$')
plt.scatter(freq4_s, RMS4_s, s=3, label=r'15 $\Omega$')
plt.scatter(freq5_s, RMS5_s, s=3, label=r'22 $\Omega$')
plt.scatter(freq6_s, RMS6_s, s=3, label=r'33 $\Omega$')
plt.scatter(freq7_s, RMS7_s, s=3, label=r'51 $\Omega$')
plt.scatter(freq8_s, RMS8_s, s=3, label=r'100 $\Omega$')
plt.scatter(freq9_s, RMS9_s, s=3, label=r'215 $\Omega$')
plt.scatter(freq10_s, RMS10_s, s=3, label=r'560 $\Omega$')
plt.scatter(freq11_s, RMS11_s, s=3, c="#88f257", label=r'$\inf$ $\Omega$')



plt.title("Odvisnost amplitude napetosti od frekvence signala v tocki B")
plt.ticklabel_format(axis="x", style="sci", scilimits=(7, 6))
plt.xlabel(r'$\nu$[Hz]')
plt.ylabel(r"$U_{RMS}$ [V]")
plt.legend()
plt.show()
