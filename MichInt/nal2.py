import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

delta_p = np.genfromtxt("nal2_data.txt", usecols=0)
N = np.genfromtxt("nal2_data.txt", usecols=1)
y = [(i * 633 * 10**-9)/(100*10**-3) for i in N]
init_vals = [0.5, 20]
Nerr = [1/item for item in N]
yerr = [Nerr[Nerr.index(i)]*y[y.index(j)] for i,j in zip(Nerr, y)]


def LinearFit(x, k, n):
    return k*x + n

fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(LinearFit, xdata=delta_p, ydata=y)
yfit = LinearFit(delta_p, fitpar[0], fitpar[1])

plt.errorbar(delta_p+1, y, yerr=yerr, markersize=4, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data")
plt.plot(delta_p+1, yfit, "r-", label="Linear Fit", c="#24C7F0")
plt.title("Sprememba lomnega kolicnika kot funkcija absolutnega tlaka")
plt.xlabel("p [bar]")
plt.ylabel(r"$n_0 - 1$")
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend()
plt.show()

