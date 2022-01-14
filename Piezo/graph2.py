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



x = np.genfromtxt("SDS00002.txt", usecols=0)
y = np.genfromtxt("SDS00002.txt", usecols=1)


fitpar, fitcov = curve_fit(theoreticalfit, xdata=x, ydata=y, p0=[-0.16, 1.32, 0, 5.5])
yfit = theoreticalfit(x, fitpar[0], fitpar[1], fitpar[2], fitpar[3])

plt.scatter(x, y, s=0.5)
plt.plot(x, yfit, c="#f542e9")

plt.title("p0=[-0.16, 1.32, 0, 5.5]")
plt.show()
