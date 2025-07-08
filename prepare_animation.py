from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_system(trajectory, interval=50, point_size=2, save_path=None):
    """
    u_log: list of (xs, ys) tuples
    interval: milliseconds between frames
    point_size: scatter point size
    save_path: if set (e.g., 'animation.gif'), saves to that path
    """
    trajectory = trajectory[::interval,:,:]

    fig, ax = plt.subplots()
    #fig.patch.set_facecolor('black')
    #ax.set_facecolor('black')      
    xs, ys = trajectory[0, 0, 0], trajectory[0, 0, 1]
    scat_1 = ax.scatter(xs, ys, s=point_size)
    
    xs, ys = trajectory[0, 1, 0], trajectory[0, 1, 1]
    scat_2 = ax.scatter(xs, ys, s=point_size)

    xs, ys = trajectory[0, 2, 0], trajectory[0, 2, 1]
    scat_3 = ax.scatter(xs, ys, s=point_size)

    ax.set_xlim(np.min(trajectory[:, :, 0]), np.max(trajectory[:, :, 0]))
    ax.set_ylim(np.min(trajectory[:, :, 1]), np.max(trajectory[:, :, 1]))
    ax.set_aspect('equal')

    def update(i):
        
        n_bodies = 3
        
        for j in range(n_bodies):
            x , y = trajectory[i, j, 0], trajectory[i, j, 1]

            data = np.array([x, y])  # or .T if stacking on axis=0
            if j==0:
                scat_1.set_offsets(data)
            if j==1:
                scat_2.set_offsets(data)
            if j==2:
                scat_3.set_offsets(data)
                
        return scat_1, scat_2, scat_3


    ani = animation.FuncAnimation(
    fig, update, frames=len(trajectory), interval=interval, blit=False
    )

    if save_path:
        ani.save(save_path, writer="ffmpeg", fps=50)
        #ani.save(save_path, writer='pillow', fps=1000 // interval)
    else:
        plt.show()