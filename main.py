import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import simple_simulation
from infinity import infinity_principle
import pickle


length = 40_000.0 #[s]

steps_list = [int(20_000*7 + 30000*n) for n in range(55)]
dt_list = [length / steps for steps in steps_list]

result = []    
for i, (steps, dt) in enumerate(zip(steps_list,dt_list)):
    print(f"iteracjai {i}")
    n_bodies = 3
    positions = np.array([[0, 0], [1e7, 0], [0, 1e7]], dtype = float)
    velocities = np.array([[50, 50], [-30, 350], [-100, 0]], dtype = float)
    masses = np.array([5e21, 1e22, 1e22])
    
    print(f"ilosc krokow: {steps}")
    result.append(simple_simulation.simulate_return_end_only(positions, velocities, masses, dt = dt, steps = steps))

result = np.array(result)
for n in range(3):
    body_x = result[:, n, 0]
    body_y = result[:, n, 1] 

    pickle.dump((body_x,body_y,steps_list), open(f'fitting_test_{n}.pkl', 'wb'))

#trajectory = simple_simulation.simulate(positions, velocities, masses, dt = 1e-2, steps = 1_000_000)

# Plotting
"""
for i in range(n_bodies):
    plt.plot(trajectory[:, i, 0], trajectory[:, i, 1])
plt.gca().set_aspect('equal')

plt.show()
"""

#animate_system(trajectory, 80, 2, 'animacja.mp4')


