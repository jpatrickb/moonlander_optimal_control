import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation

animation.writer = animation.writers['ffmpeg']


def moving_obstacle(t, x, y, W1=1, r=(1, 1), c=(0, 0), lam=20):
    """
    Define the area that represents a 2-D obstacle moving through space

    Parameters:
        t (float): time
        x (float): x position in space
        y (float): y position in space
        W1 (float): weight of cost
        r (tuple): radius in x and y direction
        c (tuple of functions): center of the ellipse
    """

    ellipse = ((x - c[0](t)) ** 2 / r[0] + (y - c[1](t)) ** 2 / r[1]) ** lam + 1

    return W1 / ellipse


def moving_obstacle_dx(t, x, y, W1=1, r=(1, 1,), c=(0, 0), lam=20):
    """
    Calculates the x derivative of the moving obstacle

    Parameters:
        t (float): time
        x (float): x position in space
        y (float): y position in space
        W (float): weight of cost
        r (tuple): radius in x and y direction
        c (tuple): center of the ellipse
    """

    circle = (x - c[0](t)) ** 2 / r[0] + (y - c[1](t)) ** 2 / r[1]
    numer = -2 * lam * W1 * (x - c[0](t)) * (circle) ** (lam - 1)
    denom = r[0] * ((circle) ** lam + 1) ** 2

    return numer / denom


def moving_obstacle_dy(t, x, y, W1=1, r=(1, 1,), c=(0, 0), lam=20):
    """
    y derivative of the obstacle

    Parameters:
        t (float): time
        x (float): x position in space
        y (float): y position in space
        W1 (float): weight of cost
        r (tuple): radius in x and y direction
        c (tuple): center of the ellipse
    """

    circle = (x - c[0](t)) ** 2 / r[0] + (y - c[1](t)) ** 2 / r[1]
    numer = -2 * lam * W1 * (y - c[1](t)) * (circle) ** (lam - 1)
    denom = r[1] * ((circle) ** lam + 1) ** 2

    return numer / denom

def avoid_many_moving_obstacle(r, c, W1=500, W2=10, ani_name="avoiding_many_moving_object.mp4"):
    """
    Finds the fastest path through

    Parameters:

    """
    # Define the parameters for the system
    W1 = 500
    W2 = 10

    # Define the ODE for the system
    def ode(t, y, p):
        return p[0] * np.array([
            y[2],
            y[3],
            y[6] / (2 * W2),
            y[7] / (2 * W2),
            sum(moving_obstacle_dx(t, y[0], y[1], W1, r[i], c[i]) for i in range(len(c))),  # Sums over all the ellipses
            sum(moving_obstacle_dy(t, y[0], y[1], W1, r[i], c[i]) for i in range(len(c))),
            -y[4],
            -y[5]
        ])

    # Define the boundary conditions
    def bc(ya, yb, p):
        utf = yb[6:] / (2 * W2)
        return np.array([
            ya[0] - 6,
            ya[1],
            ya[2],
            ya[3],
            yb[0],
            yb[1],
            yb[2],
            yb[3],
            yb[2:4] @ yb[4:6] + yb[6:] @ utf - (
                        1 + sum(moving_obstacle(p[0], yb[0], yb[1], W1, r[i], c[i]) for i in range(len(c))) + W2 * (
                            utf ** 2).sum())
        ])

    # Define the initial guess
    t_steps = 200
    t_eval = np.linspace(0, 1, t_steps)
    y0 = np.zeros((8, t_steps))
    x = np.linspace(0, 6, t_steps)
    y1 = (1.75 / 3) * x[:int(t_steps / 2)]
    y2 = (- 1.75) / 3 * (x[int(t_steps / 2):] - 3) + 1.75
    y_init = np.concatenate((y1, y2))
    y0[0, :] = x[::-1]
    y0[1, :] = y_init[::-1]
    y0[2, :] = -1 * np.ones(t_steps)

    p0 = np.array([6.0])

    # Solve the ODE
    sol = solve_bvp(ode, bc, t_eval, y0, p0, max_nodes=30000)

    # Plot the obstacle
    fig, ax = plt.subplots()
    x = np.linspace(0, 7, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)

    ax.plot(y0[1], y0[2], label='Initial Guess')

    def animate(t):
        ax.clear()
        contour = []
        for i in range(len(c)):
            contour.append(ax.contour(X, Y, moving_obstacle(t, X, Y, r=r[i], c=c[i])))
        line = ax.plot(*sol.sol(np.linspace(0, t / sol.p[0], 200))[:2, :], c='blue')
        dot = ax.plot(*sol.sol(t / sol.p[0])[:2], 'o', c='blue')
        return *contour, line, dot

    ani = FuncAnimation(fig, animate, frames=np.linspace(0, sol.p[0], 20 * np.ceil(sol.p[0]).astype(int)), interval=50)

    ani.save(ani_name)
    plt.show()

    plt.plot(sol.x, sol.y[2], label="$x'(t)$")
    plt.plot(sol.x, sol.y[3], label="$y'(t)$")
    plt.legend()
    plt.show()

    plt.plot(sol.x, sol.y[4], label='$u_1$')
    plt.plot(sol.x, sol.y[5], label='$u_2$')
    plt.legend()
    plt.show()

    plt.plot(*sol.y[:2, :])
    plt.show()

    print("Time taken to reach the end:", sol.p[0])