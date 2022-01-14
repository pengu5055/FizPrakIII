import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def split(word):
    return [char for char in word]


def LinearFit(x, k, n):
    return k*x + n


letter_s = {"A": "4.5",
            "B": "6.5",
            "G": "129.1",
            "H": "161",
            "I": "206",
            "J": "258",
            "K": "328",
            "L": "419",
            "M": "516",
            "N": "590",
            "O": "645",
            "P": "849"}

def decode(data):
    t = []
    for item in data:
        l = split(item)
        for char in l:
            if char.isalpha() and char in letter_s.keys():
                l[l.index(char)] = float(letter_s[char])/(rho) * 10
        l = [str(char) for char in l]
        t.append("".join(l))
    return [float(eval(value)) for value in t]

rho = 2700
background = 0.361
x_import = np.genfromtxt("naloga03_abs_beta.txt", usecols=0, dtype=str)
n = np.genfromtxt("naloga03_abs_beta.txt", usecols=1)
x = decode(x_import)  # Thickness in mm
x = np.array([value/(10*100) * rho for value in x])
n = [value/300 - background for value in n]
y = n
combine = zip(x, y)
combine_s = sorted(list(combine))
x_s = [i for (i, s) in combine_s]
y_s = [s for (i, s) in combine_s]

r = 19  # Linear fit first r points
fitpar, fitcov = curve_fit(LinearFit, xdata=x_s[:r], ydata=y_s[:r])
yfit = LinearFit(np.array(x_s[:r]), fitpar[0], fitpar[1])
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))

phi0 = n[0]
xerr = [0.02]

x1 = [item for item in x if item >= 2]
n1 = [item for item in n if item <= 1.2]

fig, ax = plt.subplots()
fitpar1, fitcov1 = curve_fit(LinearFit, xdata=x1, ydata=n1)
yfit1 = LinearFit(x, fitpar1[0], fitpar1[1])

# Error computation
yerr = [value * 0.03 for value in n]

# Graph plot
plt.errorbar(x, n, yerr=yerr, label="Data", c="#88fc03", linestyle='None', marker="o", capsize=1)
plt.plot(x, [0.978 for i in x], label=r'$\overline{A_\gamma}$', c="#e67f53")
plt.text(0.52, 0.68, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#ed9de8", alpha=0.5))
plt.plot(x_s[:r], yfit, label="Linear Fit", c="#24C7F0")
plt.title(r"Ocena dosega sevanja $\beta$")
plt.xlabel(r"s [$kgm^{-2}$]")
plt.ylabel("A [Bq]")
plt.legend()
plt.show()
