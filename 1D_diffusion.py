import numpy as np
import matplotlib.pyplot as plt

D = 100
Lx = 300

dx = 0.5
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)

z = np.zeros_like(x)
z_hi = 500.0
z_lo = 0.0
z[x <= Lx/2] = z_hi
z[x > Lx/2] = z_lo

plt.figure()
plt.plot(x, z, "r")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Initial hillslope profile")

nt = 5000
dt = 0.5 * dx**2 / D

for _ in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])

plt.figure()
plt.plot(x, z, "b")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Final hillslope profile")

