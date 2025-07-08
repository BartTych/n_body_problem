import numpy as np


G = 6.67430e-11  # gravitational constant



def compute_forces(positions, masses):
    n = len(masses)
    forces = np.zeros_like(positions)
    
    for i in range(n):
        for j in range(i + 1, n):
            r_ij = positions[j] - positions[i]
            distance = np.linalg.norm(r_ij)
            force_magnitude = G * masses[i] * masses[j] / distance**2
            force_direction = r_ij / distance
            force = force_magnitude * force_direction
            forces[i] += force
            forces[j] -= force  # Newton's 3rd law
    return forces

def simulate(positions, velocities, masses, dt, steps):
    pos_log = [positions.copy()]
    vel = velocities.copy()
    
    for step in range(steps):
        forces = compute_forces(positions, masses)
        acc = forces / masses[:, np.newaxis]
        vel += acc * dt
        positions += vel * dt
        if step % 100 == 0:
            pos_log.append(positions.copy())
        if step % 100_000 == 0:
            print(f"Step: {step:,}")
    return np.array(pos_log)

def simulate_return_end_only(positions, velocities, masses, dt, steps):
    #pos_log = [positions.copy()]
    vel = velocities.copy()
    
    for step in range(steps):
        forces = compute_forces(positions, masses)
        acc = forces / masses[:, np.newaxis]
        vel += acc * dt
        positions += vel * dt
        #if step % 100 == 0:
        #    pos_log.append(positions.copy())
        if step % 100_000 == 0:
            print(f"Step: {step:,}")
    return positions