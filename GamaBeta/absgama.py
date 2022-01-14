import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def LinearFit(x, k, n):
    return k*x + n


def split(word):
    return [char for char in word]


letter_s = {"Q": "1230",
            "R": "1890",
            "S": "3632",
            "T": "7435"}


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

# Data in
rho = 11340
x_import = np.genfromtxt("naloga04_abs_gama.txt", usecols=0, dtype=str)
n = np.genfromtxt("naloga04_abs_gama.txt", usecols=1)
x = decode(x_import)
a = [item/500 for item in n]
y = [np.log(value/a[0]) for value in a]


# Data sort and fit computation
combine = zip(x, y)
combine_s = sorted(list(combine))
x_s = [i for (i, s) in combine_s]
y_s = [s for (i, s) in combine_s]

r = 20  # Linear fit first r points
fitpar, fitcov = curve_fit(LinearFit, xdata=x_s[:r], ydata=y_s[:r])
yfit = LinearFit(np.array(x_s[:r]), fitpar[0], fitpar[1])
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))

# Error computation
yerr = [value * 0.05 for value in y_s]

# Graph plot
fix, ax = plt.subplots()
plt.text(0.54, 0.75, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#ed9de8", alpha=0.5))
plt.errorbar(x_s, y_s, yerr=yerr, label="Data", c="#88fc03", linestyle='None', marker="o", capsize=1)
plt.plot(x_s[:r], yfit, label="Linear Fit", c="#24C7F0")

plt.title("Dolocanje ekstinkcijskega koeficienta Pb")
plt.xlabel(r"x [mm]")
plt.ylabel(r"$\ln{\left(\phi/\phi_0\right)}$")
plt.legend()
plt.show()