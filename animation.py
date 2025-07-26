# animation.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from simulator import ProjectileSimulator
from kalman_filter import KalmanFilter2D

def animate_kalman(dt=0.1, total_time=10.0, save_path="exports/kalman_tracking.gif"):
    os.makedirs("exports", exist_ok=True)

    sim = ProjectileSimulator(dt=dt, total_time=total_time, noise_std=2.0)
    true_positions, measurements = sim.run()

    kf = KalmanFilter2D(dt=dt, measurement_noise_std=2.0, process_noise_std=0.5)

    est_positions = []
    for z in measurements:
        kf.predict()
        kf.update(z)
        est_positions.append(kf.get_state()[:2])
    est_positions = np.array(est_positions)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, np.max(true_positions[:, 0]) + 10)
    ax.set_ylim(np.min(true_positions[:, 1]) - 50, np.max(true_positions[:, 1]) + 50)

    true_line, = ax.plot([], [], 'b-', label='True')
    meas_scatter, = ax.plot([], [], 'rx', alpha=0.5, label='Measured')
    est_line, = ax.plot([], [], 'g--', label='Estimated')
    ax.set_title("Kalman Filter Tracking Animation")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.legend()
    ax.grid(True)

    def update(i):
        true_line.set_data(true_positions[:i+1, 0], true_positions[:i+1, 1])
        meas_scatter.set_data(measurements[:i+1, 0], measurements[:i+1, 1])
        est_line.set_data(est_positions[:i+1, 0], est_positions[:i+1, 1])
        return true_line, meas_scatter, est_line

    ani = animation.FuncAnimation(fig, update, frames=len(true_positions), interval=50, blit=True)

    if save_path:
        ani.save(save_path, fps=20, dpi=150)
        print(f"✅ GIF saved to {save_path}")
    else:
        plt.show()

if __name__ == "__main__":
    animate_kalman()
