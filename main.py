# main.py
import numpy as np
from simulator import ProjectileSimulator
from kalman_filter import KalmanFilter2D
from visualize import plot_trajectory, plot_velocity
from utils import save_results_to_csv  # <-- Added import
import matplotlib.pyplot as plt
import os

def main():
    dt = 0.1
    total_time = 10.0
    measurement_noise_std = 2.0
    process_noise_std = 0.5

    sim = ProjectileSimulator(dt=dt, total_time=total_time, noise_std=measurement_noise_std)
    true_positions, measurements = sim.run()

    kf = KalmanFilter2D(dt=dt, measurement_noise_std=measurement_noise_std, process_noise_std=process_noise_std)

    estimated_positions = []
    estimated_velocities = []

    for z in measurements:
        kf.predict()
        kf.update(z)
        state = kf.get_state()
        estimated_positions.append(state[:2])
        estimated_velocities.append(state[2:])

    estimated_positions = np.array(estimated_positions)
    estimated_velocities = np.array(estimated_velocities)

    # Plot and save figures
    fig1 = plot_trajectory(true_positions, measurements, estimated_positions)
    fig2 = plot_velocity(estimated_velocities)

    os.makedirs("exports", exist_ok=True)
    fig1.savefig("exports/trajectory_plot.png")
    fig2.savefig("exports/velocity_plot.png")

    # Save simulation results to CSV
    save_results_to_csv(true_positions, measurements, estimated_positions, estimated_velocities)
    print("✅ Results saved to exports/results.csv")

    # Show plots
    plt.show()

if __name__ == "__main__":
    main()
