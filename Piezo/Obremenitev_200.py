import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def theta(t, t_0):
    if t.all() >= t_0:
        return 1
    else:
        return 0


def theoreticalfit(t, u_b, u_0, t_0, tau, s=1):
    return u_b + s * u_0 * np.exp(-(t - t_0) / tau) * np.heaviside(t-t_0, 1)


x = np.genfromtxt("SDS00005.txt", usecols=0)
y = np.genfromtxt("SDS00005.txt", usecols=1)

fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(theoreticalfit, xdata=x, ydata=y, p0=[-0.0013, 0.27, -0, 7.6])
yfit = theoreticalfit(x, fitpar[0], fitpar[1], fitpar[2], fitpar[3])
perr = np.sqrt(np.diag(fitcov))
print(perr)
fittext= "Model fit:\nU_b = {} ± {}\nU_0 = {} ± {}\nt_0 = {} ± {}\ntau = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                                                   format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"),
                                                                                                   format(fitpar[2], ".4e"), format(fitcov[2][2]**0.5, ".4e"),
                                                                                                   format(fitpar[3], ".4e"), format(fitcov[3][3]**0.5, ".4e"))

plt.scatter(x, y, s=0.5, label="Data")
plt.plot(x, yfit, c="#f542e9", label="Fit")


plt.title("Obremenitev z maso 195g")
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.text(0.49, 0.72, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.legend(loc=0)
plt.show()
