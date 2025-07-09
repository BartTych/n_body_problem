import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import simple_simulation
from infinity import infinity_principle
import pickle
import prepare_animation

length = 40_000.0 #[s]

positions = np.array([[0, 0], [1e7, 0], [0, 1e7]], dtype = float)
velocities = np.array([[50, 50], [-30, 350], [-100, 0]], dtype = float)
masses = np.array([5e21, 1e22, 1e22])

steps = int(20_000*7 + 30000*30)
dt = length / steps 

print(f"steps: {steps}, dt: {dt}")

result = []    
    
trajectory = simple_simulation.simulate(positions, velocities, masses, dt = dt, steps = steps)

# Plotting
"""
for i in range(n_bodies):
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1])
plt.gca().set_aspect('equal')

plt.show()
"""

prepare_animation.animate_system(trajectory, 80, 2, 'animacja.mp4')