import numpy as np
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from scipy.ndimage import rotate
from matplotlib.animation import FuncAnimation
from matplotlib import animation

animation.writer = animation.writers['ffmpeg']
params = {
    "text.usetex" : True,
    "font.family" : "serif",
    "font.serif" : ["Computer Modern Serif"]
    }
plt.rcParams.update(params)


class LunarLander:
    """
    LunarLander class to model the flight of a Lunar Lander

    """
    def __init__(self, initial_position, initial_velocity, alpha=10., beta=25., gamma=2., grav=2., t_steps=200):
        """
        Initializes the Lunar Lander class by creating an ODE for the state and costate evolution

        :param initial_position (arraylike):    The initial position (x0, y0) of the lunar lander
        :param initial_velocity (float):        The initial velocity (v0) of the lunar lander (in the x direction)
        :param alpha (float):                   The weight on the magnitude of the lander's acceleration over time
        :param beta (float):                    The weight on the magnitude of the lander's final velocity (both x and y directions)
        :param gamma (float):                   The weight on the final time
        :param grav (float):                    Gravitational constant for the moon
        :param t_steps (int):                   Number of time steps to evaluate
        :param animate_file (string):           Name of file to write animations to

        Written by Patrick
        """
        # Save the initial position and velocity
        initial_x, initial_y = initial_position
        self.x0 = initial_x
        self.y0 = initial_y
        self.v0 = initial_velocity

        # Initialize solutions as None
        self.state_sol = None
        self.costate_sol = None
        self.controls = None

        # Save weights and solution parameters
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.grav = grav
        self.t_steps = t_steps

        # Creates state and costate evolution and boundary conditions
        self._create_evolution()
        self._create_boundary_condition()



    def _create_evolution(self):
        """
        Creates the state and costate evolution system and saves as class attributes
        :return:

        Written by Tiara
        """
        # Create the State and Costate evolution
        def ode(t, y, p):
            tf = p[0]
            return tf * np.array([
                y[2],
                y[3],
                y[6] / (2*self.alpha),
                y[7] / (2*self.alpha) - self.grav,
                np.zeros_like(y[0]),
                np.zeros_like(y[0]),
                y[4],
                y[5]
            ])

        self.evolution_ode = ode

    def _create_boundary_condition(self):
        """
        Creates the boundary condition and saves as a class attribute

        :return:

        Written by Tiara
        """
        # Create the boundary conditions
        def bc(ya_, yb_, p):
            # Final time
            tf = p[0]

            # Save variables
            x0, y0, xp0, yp0, p1_0, p2_0, p3_0, p4_0 = ya_
            xtf, ytf, xptf, yptf, p1tf, p2tf, p3tf, p4tf = yb_

            # Control variables, constructed from p
            uxf = p3tf / (2 * self.alpha)
            uyf = p4tf / (2 * self.alpha)

            # Hamiltonian, should be zero at the end
            Htf = p1tf * xptf + p2tf * yptf + p3tf * uxf + p4tf * (uyf - self.grav) - self.alpha * (uxf ** 2 + uyf ** 2) + self.gamma

            return np.array([
                x0 - self.x0,
                y0 - self.y0,
                xp0 - self.v0,
                yp0,
                ytf,
                p1tf,
                p3tf - 2 * self.beta * xptf,
                p4tf - 2 * self.beta * yptf,
                Htf
            ])

        self.boundary_condition = bc

    def find_path(self, tf_guess=20, max_nodes=30000):
        """
        Uses the state and costate evolution along with the boundary condition to find the optimal path

        :param tf_guess (float):    Initial guess for the time to take to land
        :param max_nodes (int):     Parameter to be passed to solve_bvp to increase resolution in solving
        :return:                    Solved state, costate, and control values (Dataframes)

        Written by Tiara
        """
        # Convert to array to pass
        tf_guess = np.asarray([tf_guess])

        # Create time steps to evaluate at
        t_eval = np.linspace(0, 1, self.t_steps)

        # Create initial guess for the state and costate
        # TODO: Is there a more intelligent way to make an initial guess?
        init_guess = np.ones((8, self.t_steps))

        init_guess[0] *= self.x0
        init_guess[1] = np.linspace(self.y0, 0, self.t_steps)
        init_guess[2] = np.linspace(self.v0, 0, self.t_steps)

        # Solve the state/costate equation
        sol = solve_bvp(self.evolution_ode, self.boundary_condition, t_eval, init_guess, p=tf_guess, max_nodes=max_nodes)

        # Convert solution into dataframe
        state_vals = pd.DataFrame(sol.y[:4, :].T, columns=['x', 'y', 'xp', 'yp'])
        costate_vals = pd.DataFrame(sol.y[4:, :].T, columns=['p1', 'p2', 'p3', 'p4'])

        # Calculate controls
        controls = pd.DataFrame()
        controls['ux'] = costate_vals['p3'] / (2 * self.alpha)
        controls['uy'] = costate_vals['p4'] / (2 * self.alpha)
        controls['tau'] = (controls['ux']**2 + controls['uy']**2)**0.5
        controls['theta'] = np.arctan(controls['uy'] / controls['ux'])

        # Set index as the time
        state_vals['t'] = sol.x * sol.p[0]
        costate_vals['t'] = sol.x * sol.p[0]
        controls['t'] = sol.x * sol.p[0]

        state_vals = state_vals.set_index('t')
        costate_vals = costate_vals.set_index('t')
        controls = controls.set_index('t')

        # Save solutions as attributes
        self.state_sol = state_vals
        self.costate_sol = costate_vals
        self.controls = controls

        return self.state_sol, self.costate_sol, self.controls

    def plot_state_controls(self, save_file=None, show=True):
        """
        Plots the state and control values

        :return:

        Written by Tiara
        """
        rows = 4
        cols = 3
        # Ensures that the solution has been found
        if self.state_sol is None or self.controls is None:
            self.find_path()

        # Sets plotting parameters
        plt.rcParams['figure.figsize'] = [10, 10]

        # Plots state solution
        plt.subplot(rows, cols, 1)
        self.state_sol['x'].plot()
        plt.title('Position ($x$)')

        plt.subplot(rows, cols, 2)
        self.state_sol['y'].plot()
        plt.title('Position ($y$)')

        plt.subplot(rows, cols, 3)
        plt.plot(self.state_sol['x'], self.state_sol['y'])
        plt.title('Trajectory')

        plt.subplot(rows, cols, 4)
        self.state_sol['xp'].plot()
        plt.title('Velocity ($x$)')

        plt.subplot(rows, cols, 5)
        self.state_sol['yp'].plot()
        plt.title('Velocity ($y$)')

        plt.subplot(rows, cols, 6)
        plt.plot(self.state_sol['xp'], self.state_sol['yp'])
        plt.title('Velocity Phase Plot')

        plt.subplot(rows, cols, 7)
        self.controls['ux'].plot()
        plt.title('Acceleration ($u_x$)')

        plt.subplot(rows, cols, 8)
        self.controls['uy'].plot()
        plt.title('Acceleration ($u_y$)')

        plt.subplot(rows, cols, 9)
        plt.plot(self.controls['ux'], self.controls['uy'])
        plt.title('Acceleration Phase Plot')

        plt.subplot(rows, cols, 10)
        self.controls['tau'].plot()
        plt.title(r'Magnitude of Acceleration ($\sqrt{u_x^2 + u_y^2}$)')

        plt.subplot(rows, cols, 11)
        unit = 0.25
        y_tick = np.arange(-0.5, 0.5 + unit, unit)
        y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$"]
        self.controls['theta'].plot()
        plt.title(r'Angle of Acceleration ($\arctan(u_y / u_x)$)')
        plt.yticks(y_tick * np.pi, y_label)

        plt.tight_layout()

        if save_file is not None:
            plt.savefig(save_file, dpi=300)

        if show:
            plt.show()

    def animate_landing(self, anim_file):
        """
        Function to animate the landing of the Lunar Lander

        :param anim_file:
        :return:

        Written by TJ
        """
        # Ensure valid solution to plot
        if self.state_sol is None or self.controls is None:
            self.find_path()

        # Set up the plotting
        plt.clf()
        Y_PLOT_LIMS = (0, 20)
        PATH_COLOR = "#ffffff"
        plt.title("Lunar Lander Trajectory")
        plt.gcf().set_size_inches(10, 10)
        xlims = (0, 3)
        ylims = (-1, 11)
        plt.xlim(*xlims)
        plt.ylim(*ylims)
        plt.xlabel("$t$")
        plt.ylabel("$y$")

        # Plot the lander
        LANDER_SIZE = 0.3
        # TODO: Get this image from TJ so we can use it
        img = mpimg.imread('./lander.png')

        # Line plot to show the trajectory
        line, = plt.gca().plot([], [], "--", linewidth=1, color=PATH_COLOR)

        # Plot initial position
        lander = plt.imshow(img,
                            extent=[self.state_sol['t'].iloc[0] - LANDER_SIZE,
                                    self.state_sol['y'].iloc[0] - LANDER_SIZE,
                                    self.state_sol['y'].iloc[0] + LANDER_SIZE],
                            aspect='equal',
                            zorder=2
                            )

        def rotate_lander(vel_x, vel_y):
            angle = np.degrees(-np.arctan(vel_x / vel_y))
            rotated_img = rotate(img, angle, reshape=False)
            rotated_img = np.clip(rotated_img, 0, 1)
            return rotated_img

        def update(frame):
            print(frame, "/", len(self.state_sol['t']), end="\r")
            # Update trajectory
            line.set_data(self.state_sol['t'].iloc[:frame], self.state_sol['t'].iloc[:frame])

            # Update lander position and rotation relative to velocity
            vel_x = self.state_sol['xp'].iloc[frame]
            vel_y = self.state_sol['yp'].iloc[frame]
            lander.set_data(rotate_lander(vel_x, vel_y))

            # Update lander position
            lander.set_extent(
                [self.state_sol['t'].iloc[frame] - LANDER_SIZE,
                 self.state_sol['t'].iloc[frame] + LANDER_SIZE,
                 self.state_sol['y'].iloc[frame] - LANDER_SIZE,
                 self.state_sol['x'].iloc[frame] + LANDER_SIZE]
            )

        ani = FuncAnimation(plt.gcf(), update, frames=np.arange(0, len(self.state_sol['t']), 60), interval=60, repeat=False)
        ani.save(anim_file, dpi=300)


if __name__ == "__main__":
    lunarlander = LunarLander([5, 10], 1)
    lunarlander.find_path()
    lunarlander.plot_state_controls()
    lunarlander.animate_landing('test_run1.mp4')







