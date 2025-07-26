# utils.py
import csv
import os

def save_results_to_csv(true, measurements, estimates, velocities, path="exports/results.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["step", "true_x", "true_y", "meas_x", "meas_y", "est_x", "est_y", "vel_x", "vel_y"])
        for i, (t, m, e, v) in enumerate(zip(true, measurements, estimates, velocities)):
            writer.writerow([i, *t, *m, *e, *v])
