import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

f = np.genfromtxt("Data_export.txt", usecols=0)
u = np.genfromtxt("Data_export.txt", usecols=1)

def LinearFit(x, k, n):
    return k*x + n

fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(LinearFit, xdata=f, ydata=u)
yfit = LinearFit(f, fitpar[0], fitpar[1])
yerr = [0.01 * value for value in u]

plt.errorbar(f, u, yerr=yerr, markersize=4, color="#C44BC4", linestyle='None',
             marker="o", capsize=3, label="Data")
plt.plot(f, yfit, "r-", label="Linear Fit", c="#24C7F0")
plt.title("Dolocitev koeficienta keramike")
plt.xlabel("F [N]")
plt.ylabel(r"U [V]")
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend()
plt.show()

