# visualize.py
import matplotlib.pyplot as plt
import numpy as np

def plot_trajectory(true_positions, measurements, estimates):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(true_positions[:, 0], true_positions[:, 1], label='True Position', linewidth=2)
    ax.plot(measurements[:, 0], measurements[:, 1], 'rx', label='Noisy Measurements', alpha=0.5)
    ax.plot(estimates[:, 0], estimates[:, 1], 'g--', label='Kalman Filter Estimate', linewidth=2)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title('2D Kalman Filter Tracking')
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    return fig

def plot_velocity(velocities):
    vx = velocities[:, 0]
    vy = velocities[:, 1]
    time = np.arange(len(vx))

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, vx, label='vx (X Velocity)', linewidth=2)
    ax.plot(time, vy, label='vy (Y Velocity)', linewidth=2)
    ax.set_title('Estimated Velocities Over Time')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Velocity')
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    return fig
