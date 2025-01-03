from numpy import np
import matplotlib.pyplot as plt

def flux_surface(A = 2.2, kappa = 1.5, delta = 0.3, R0 = 2.5, theta = np.linspace(0, 2 * np.pi)):

    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)
    return R_s, Z_s

def plot_surface(R_s, Z_s):
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    plt.savefig("miller.png")

def main():
    R_s, Z_s = flux_surface()
    plot_surface(R_s, Z_s)

if __name__ == "__main__":
    main()