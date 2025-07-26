# simulator.py
import numpy as np

class ProjectileSimulator:
    def __init__(self, dt=0.1, total_time=10.0, noise_std=1.0):
        self.dt = dt
        self.total_time = total_time
        self.noise_std = noise_std

        self.g = -9.81  # gravity
        self.reset()

    def reset(self):
        self.t = 0
        self.position = np.array([0.0, 0.0])         # x, y
        self.velocity = np.array([10.0, 20.0])        # vx, vy
        self.trajectory = []
        self.measurements = []

    def step(self):
        # Update true position using simple physics
        self.velocity[1] += self.g * self.dt
        self.position += self.velocity * self.dt

        # Simulate noisy measurement (only position)
        measurement = self.position + np.random.normal(0, self.noise_std, size=2)

        self.t += self.dt
        self.trajectory.append(self.position.copy())
        self.measurements.append(measurement)

        return self.position.copy(), measurement.copy()

    def run(self):
        self.reset()
        steps = int(self.total_time / self.dt)
        for _ in range(steps):
            self.step()
        return np.array(self.trajectory), np.array(self.measurements)
