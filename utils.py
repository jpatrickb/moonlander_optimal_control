import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.image as mpimg
from scipy.ndimage import rotate
from itertools import product
from tqdm import tqdm

animation.writer = animation.writers['ffmpeg']


def lunar_lander(pos_init, v_init, tf_guess=20, y0_guess=1, alpha=10., beta=25., gamma=3., nu=0., G=2., t_steps=200, animate_file=None):
    '''Find the optimal control and trajectory for the lunar lander.

        Parameters:
            pos_init (tuple) : x and y coordinates defining the starting position of the lunar lander
            v_init (float) : the lander's starting velocity in the x direction
            alpha (float) : the weight on the magnitude of the lander's acceleration over time
            beta (float) : the weight on the magnitude of the lander's final velocity (both x and y directions)
            gamma (float) : the weight on the final time
            nu (float): the weight of the y_position being negative
            G (float) : acceleration due to gravity on the moon
            t_steps : number of time steps to evaluate
            animate_file : if a string filename is passed in, an animation will be created and saved in the 
                specified file name. If no filename is passed in, the function will return without creating an
                animation
        
        Returns: 
            t_vals (ndarray) : the time values corresponding with the solution values
            x (ndarray) : the lander's trajectory (position) in the x direction
            y (ndarray) : the lander's trajectory (position) in the y direction
            xp (ndarray) : the lander's velocity in the x direction
            yp (ndarray) : the lander's velocity in the y direction
            ux (ndarray) : the optimal control (acceleration) in the x direction
            uy (ndarray) : the optimal control (acceleration) in the y direction
            tf (float) : the optimal landing time
    '''

    x_init, y_init = pos_init

    # Define the ODE's associated with state and costate evolution
    def ode(t, y, p):
        tf = p[0]
        return tf * np.array([
            y[2],
            y[3],
            y[6] / (2*alpha),
            y[7] / (2*alpha) - G,
            np.zeros_like(y[0]), 
            nu*(1-np.heaviside(y[1], 0)), 
            -y[4],
            -y[5]
        ])
    
    # Define the boundary conditions
    # BC's 1-5 come from known initial and final conditions
    # BC's 6-8 come from conditions on the costate
    # BC 9 comes from the final condition on the Hamiltonian relating to variable final time
    def bc(ya, yb, p):
        tf = p[0]
        uxf = yb[6] / (2*alpha)
        uyf = yb[7] / (2*alpha)
        return np.array([
            ya[0] - x_init,
            ya[1] - y_init,
            ya[2] - v_init,
            ya[3],
            yb[1],
            yb[4],
            yb[6] - 2*beta*yb[2],
            yb[7] - 2*beta*yb[3],
            yb[4]*yb[2] + yb[5]*yb[3] + yb[6]*uxf + yb[7]*(uyf - G) - alpha*(uxf**2 + uyf**2) - gamma + nu*(np.minimum(0, yb[1]))
        ])
    
    # Define the initial guess
    tf_0 = tf_guess
    t_eval = np.linspace(0, 1, t_steps) 
    y0 = y0_guess * np.ones((8, t_steps))
    y0[0] = np.ones((1, t_steps))


    y0[0] *= x_init                            # x constant
    y0[1] = np.linspace(y_init, 0, t_steps)    # y goes to 0
    y0[2] = np.linspace(v_init, 0, t_steps)    # vx goes to 0
    

    # Solve the ODE
    sol = solve_bvp(ode, bc, t_eval, y0, p=np.array([tf_0]), max_nodes=30000)
    tf = sol.p[0]

    # Extract the different elements of the solution
    x = sol.y[0]
    y = sol.y[1]
    xp = sol.y[2]
    yp = sol.y[3]
    ux = sol.y[6] / (2*alpha)       # compute controls from costates
    uy = sol.y[7] / (2*alpha)
    t_vals = sol.x * tf

    return t_vals, x, y, xp, yp, ux, uy, tf


def make_plots(t, x, y, xp, yp, ux, uy, tf):  
    plt.style.use('dark_background')
    print("Final Time:", tf)
    print("Final Position:", (np.round(x[-1], 3), np.round(y[-1], 3)))

    # make a huge figure
    plt.figure(figsize=(12, 18))
    plt.subplot(421)
    plt.plot(t, x)
    plt.title("x Position")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")

    plt.subplot(422)
    plt.plot(t, y)
    plt.title("y Position")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")

    # plt.subplot(423)
    # plt.plot(x, y)
    # plt.title("Lander Trajectory")
    # plt.tight_layout()
    # plt.show()

    # plt.figure(figsize=(10, 4))
    plt.subplot(423)
    plt.plot(t, xp)
    plt.title("Velocity $V_x$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Velocity ($\frac{m}{s}$)")
    
    plt.subplot(424)
    plt.plot(t, yp)
    plt.title("Velocity $V_y$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Velocity ($\frac{m}{s}$)")
 
    plt.subplot(425)
    plt.plot(t, ux)
    plt.title("Control $U_x$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Acceleration ($\frac{m}{s^2}$)")

    plt.subplot(426)
    plt.plot(t, uy)
    plt.title("Control $U_y$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Acceleration ($\frac{m}{s^2}$)")
 
    plt.subplot(427)
    plt.plot(t, np.arctan2(-ux, uy))
    plt.title(r"Lander Angle ($\theta$)")
    plt.yticks([-np.pi/2, -np.pi/4, 0, np.pi / 4, np.pi/2], [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", "0", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$"])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (radians)")

    plt.subplot(428)
    plt.plot(t, (ux**2 + uy**2)**0.5)
    plt.title(r"Thrust Magnitude ($\tau$)")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Magnitude ($\frac{m}{s^2}$)")

    # finish the plotting
    plt.tight_layout()
    plt.show()

def make_control_plot(t, ux, uy):
    plt.style.use('dark_background')
    plt.subplot(211)
    plt.plot(t, np.arctan2(-ux, uy))
    plt.title(r"Lander Angle ($\theta$)")
    plt.yticks([0, np.pi / 8, np.pi / 4, 3*np.pi / 8], ["0", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$", r"$\frac{3\pi}{8}$"])#, r"$\frac{\pi}{2}$"])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (radians)")

    plt.subplot(212)
    plt.plot(t, (ux**2 + uy**2)**0.5)
    plt.title(r"Acceleration Magnitude ($\tau$)")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Magnitude ($m/s^2$)")

    plt.tight_layout()
    plt.show()

def make_trajectory_plot(x, y, obstacles=None, xlim=None, guess=None, title=None, save_file=None):
    plt.style.use('dark_background')

    if obstacles is not None:
        for obstacle in obstacles:
            # x_vals = np.linspace(np.min(x)-2*obstacle.r[0], np.max(x)+2*obstacle.r[1], 150)
            # y_vals = np.linspace(np.min(y)-.25, np.max(y)+.25, 150)
            x_vals = np.linspace(-10., 10., 150)
            y_vals = np.linspace(-10., 10., 150)
            X, Y = np.meshgrid(x_vals, y_vals)
            Z = obstacle.obstacle(X, Y)
            plt.contour(X, Y, Z, linewidths=5, cmap='Greys')
    
    if guess is not None:
        guess_x, guess_y = guess 
        plt.plot(guess_x, guess_y)

    
    if guess is not None:
        guess_x, guess_y = guess 
        plt.plot(guess_x, guess_y, label="Initial Guess")
    
    plt.plot(x, y, color='#8dd3c7', label="Optimal Trajectory")

    if guess is not None:
        plt.legend()
    
    if title is not None:
        plt.title(title)
    else:
        plt.title("Lander Trajectory")

    
    if xlim is not None:
        plt.xlim(*xlim)
    plt.ylim(0, np.max(y)+0.5)
    plt.xlabel("Horizontal Position (meters)")
    plt.ylabel("Vertical Position (meters)")
    
    plt.tight_layout()

    if save_file is not None:
        plt.savefig(save_file, dpi=300)

    plt.show()


def lunar_lander_final_angle(pos_init, v_init, tf_guess=20, y0_guess=1, alpha=10., beta=25., gamma=3., nu=0., G=2., t_steps=200, rho=.01, final_angle_on=True, animate_file=None):
    '''Find the optimal control and trajectory for the lunar lander.

        Parameters:
            pos_init (tuple) : x and y coordinates defining the starting position of the lunar lander
            v_init (float) : the lander's starting velocity in the x direction
            alpha (float) : the weight on the magnitude of the lander's acceleration over time
            beta (float) : the weight on the magnitude of the lander's final velocity (both x and y directions)
            gamma (float) : the weight on the final time
            nu (float): the weight of the y_position being negative
            G (float) : acceleration due to gravity on the moon
            t_steps : number of time steps to evaluate
            animate_file : if a string filename is passed in, an animation will be created and saved in the 
                specified file name. If no filename is passed in, the function will return without creating an
                animation
        
        Returns: 
            t_vals (ndarray) : the time values corresponding with the solution values
            x (ndarray) : the lander's trajectory (position) in the x direction
            y (ndarray) : the lander's trajectory (position) in the y direction
            xp (ndarray) : the lander's velocity in the x direction
            yp (ndarray) : the lander's velocity in the y direction
            ux (ndarray) : the optimal control (acceleration) in the x direction
            uy (ndarray) : the optimal control (acceleration) in the y direction
            tf (float) : the optimal landing time
    '''

    x_init, y_init = pos_init

    # Define the ODE's associated with state and costate evolution
    def ode(t, y, p):
        tf = p[0]
        return tf * np.array([
            y[2],
            y[3],
            y[6] / (2*alpha),
            y[7] / (2*alpha) - G,
            np.zeros_like(y[0]), 
            nu*(1-np.heaviside(y[1], 0)) + final_angle_on * 2 * ((y[6] / (2*alpha))**2 / (y[1] + rho)**3), 
            -y[4],
            -y[5]
        ])
    
    # Define the boundary conditions
    # BC's 1-5 come from known initial and final conditions
    # BC's 6-8 come from conditions on the costate
    # BC 9 comes from the final condition on the Hamiltonian relating to variable final time
    def bc(ya, yb, p):
        tf = p[0]
        uxf = yb[6] / (2*alpha)
        uyf = yb[7] / (2*alpha)
        return np.array([
            ya[0] - x_init,
            ya[1] - y_init,
            ya[2] - v_init,
            ya[3],
            yb[1],
            yb[4],
            yb[6] - 2*beta*yb[2],
            yb[7] - 2*beta*yb[3],
            yb[4]*yb[2] + yb[5]*yb[3] + yb[6]*uxf + yb[7]*(uyf - G) - alpha*(uxf**2 + uyf**2) - gamma + nu*(np.minimum(0, yb[1])) - final_angle_on * (uxf / (yb[1] + rho))**2
        ])
    
    # Define the initial guess
    tf_0 = tf_guess
    t_eval = np.linspace(0, 1, t_steps) 
    y0 = y0_guess * np.ones((8, t_steps))
    y0[0] = np.ones((1, t_steps))


    y0[0] *= x_init                            # x constant
    y0[1] = np.linspace(y_init, 0, t_steps)    # y goes to 0
    y0[2] = np.linspace(v_init, 0, t_steps)    # vx goes to 0
    

    # Solve the ODE
    sol = solve_bvp(ode, bc, t_eval, y0, p=np.array([tf_0]), max_nodes=30000)
    tf = sol.p[0]

    # Extract the different elements of the solution
    x = sol.y[0]
    y = sol.y[1]
    xp = sol.y[2]
    yp = sol.y[3]
    ux = sol.y[6] / (2*alpha)       # compute controls from costates
    uy = sol.y[7] / (2*alpha)
    t_vals = sol.x * tf

    return t_vals, x, y, xp, yp, ux, uy, tf



def lunar_lander_final_angle_v2(pos_init, v_init, tf_guess=20, y0_guess=1, alpha=10., beta=25., gamma=3., nu=0., G=2., t_steps=200, zeta=1, eps=.01, final_angle_on=True, animate_file=None):
    '''Find the optimal control and trajectory for the lunar lander.

        Parameters:
            pos_init (tuple) : x and y coordinates defining the starting position of the lunar lander
            v_init (float) : the lander's starting velocity in the x direction
            alpha (float) : the weight on the magnitude of the lander's acceleration over time
            beta (float) : the weight on the magnitude of the lander's final velocity (both x and y directions)
            gamma (float) : the weight on the final time
            nu (float): the weight of the y_position being negative
            G (float) : acceleration due to gravity on the moon
            t_steps : number of time steps to evaluate
            animate_file : if a string filename is passed in, an animation will be created and saved in the 
                specified file name. If no filename is passed in, the function will return without creating an
                animation
        
        Returns: 
            t_vals (ndarray) : the time values corresponding with the solution values
            x (ndarray) : the lander's trajectory (position) in the x direction
            y (ndarray) : the lander's trajectory (position) in the y direction
            xp (ndarray) : the lander's velocity in the x direction
            yp (ndarray) : the lander's velocity in the y direction
            ux (ndarray) : the optimal control (acceleration) in the x direction
            uy (ndarray) : the optimal control (acceleration) in the y direction
            tf (float) : the optimal landing time
    '''

    x_init, y_init = pos_init

    # Define the ODE's associated with state and costate evolution
    def ode(t, y, p):
        tf = p[0]
        return tf * np.array([
            y[2],
            y[3],
            y[6] / (2*alpha),
            np.maximum(0, y[7]) / (2*alpha) - G,
            np.zeros_like(y[0]), 
            nu*(1-np.heaviside(y[1], 0)) + final_angle_on * zeta * np.heaviside(-y[1]+eps, 0), 
            -y[4],
            -y[5]
        ])
    
    # Define the boundary conditions
    # BC's 1-5 come from known initial and final conditions
    # BC's 6-8 come from conditions on the costate
    # BC 9 comes from the final condition on the Hamiltonian relating to variable final time
    def bc(ya, yb, p):
        tf = p[0]
        uxf = yb[6] / (2*alpha)
        uyf = yb[7] / (2*alpha)
        return np.array([
            ya[0] - x_init,
            ya[1] - y_init,
            ya[2] - v_init,
            ya[3],
            yb[1],
            yb[4],
            yb[6] - 2*beta*yb[2],
            yb[7] - 2*beta*yb[3],
            yb[4]*yb[2] + yb[5]*yb[3] + yb[6]*uxf + yb[7]*(np.maximum(0, uyf) - G) - alpha*(uxf**2 + uyf**2) - gamma + nu*(np.minimum(0, yb[1])) - final_angle_on * zeta * np.minimum(0, yb[1]-eps)*uxf**2
        ])
    
    # Define the initial guess
    tf_0 = tf_guess
    t_eval = np.linspace(0, 1, t_steps) 
    y0 = y0_guess * np.ones((8, t_steps))
    y0[0] = np.ones((1, t_steps))


    y0[0] *= x_init                            # x constant
    y0[1] = np.linspace(y_init, 0, t_steps)    # y goes to 0
    y0[2] = np.linspace(v_init, 0, t_steps)    # vx goes to 0
    # y0[2] = np.linspace(v_init, 0, t_steps)    # vx goes to 0
    

    # Solve the ODE
    sol = solve_bvp(ode, bc, t_eval, y0, p=np.array([tf_0]), max_nodes=30000)
    tf = sol.p[0]

    # Extract the different elements of the solution
    x = sol.y[0]
    y = sol.y[1]
    xp = sol.y[2]
    yp = sol.y[3]
    ux = sol.y[6] / (2*alpha)       # compute controls from costates
    uy = sol.y[7] / (2*alpha)
    t_vals = sol.x * tf

    return t_vals, x, y, xp, yp, ux, uy, tf


if __name__=="__main":
    pos = (5., 10.)
    v = 1.
    t, x, y, xp, yp, ux, uy, tf = lunar_lander(pos, v, t_steps=1000)