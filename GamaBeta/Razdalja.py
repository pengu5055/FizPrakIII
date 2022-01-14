import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def LinearFit(x, k, n):
    return k*x + n

# Import data
dist = np.genfromtxt("Razdalja_Export.txt", usecols=0)
inversesquareA = np.genfromtxt("Razdalja_Export.txt", usecols=1)

# Fit data
fitpar, fitcov = curve_fit(LinearFit, xdata=dist, ydata=inversesquareA)
yfit = LinearFit(dist, fitpar[0], fitpar[1])
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
print(fitcov)
# Error calculation
xerr = [item * 0.0004 for item in dist]
yerr = [item * 0.02 for item in inversesquareA]

err = np.sqrt(np.diag(fitcov))
print(err)

# Plot graph
fig, ax = plt.subplots()
plt.text(0.5, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#ed9de8", alpha=0.5))
plt.errorbar(dist, inversesquareA, label="Data", c="#88fc03", xerr=xerr, yerr=yerr, linestyle='None', marker="o", capsize=1)
plt.plot(dist, yfit, "r-", label="Linear Fit", c="#24C7F0")

plt.title("Aktivnost v odvisnosti od oddaljenosti od izvora")
plt.xlabel("d [cm]")
plt.ylabel(r'$\sqrt{A}^{-1}$')

plt.legend()
plt.show()
