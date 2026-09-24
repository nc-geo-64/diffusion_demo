import numpy as np
import matplotlib.pyplot as plt


def calculate_stable_time_step(grid_spacing, diffusivity):
    return 0.5 * grid_spacing**2 / diffusivity


def plot_profile(xvals, yvals, color="r", title=None, outfile=None):
    plt.figure()
    plt.plot(xvals, yvals, color)
    plt.xlabel("distance")
    plt.ylabel("elevation")
    plt.title(title)
    plt.savefig(outfile)


if __name__ == "__main__":

    D = 100
    Lx = 300

    dx = 0.5
    x = np.arange(start=0, stop=Lx, step=dx)
    nx = len(x)

    z = np.zeros_like(x)
    z_hi = 500.0
    z_lo = 0.0
    z[x <= Lx / 2] = z_hi
    z[x > Lx / 2] = z_lo

    plot_profile(
        x,
        z,
        color="r",
        title="Initial hillslope profile",
        outfile="initial_profile.png",
    )

    nt = 5000
    dt = calculate_stable_time_step(dx, D)

    for _ in range(0, nt):
        z[1:-1] += D * dt / dx**2 * (z[:-2] - 2 * z[1:-1] + z[2:])

    plot_profile(
        x,
        z,
        color="b",
        title="Final hillslope profile",
        outfile="final_profile.png",
    )
