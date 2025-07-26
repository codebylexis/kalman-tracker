# kalman_filter.py
import numpy as np

class KalmanFilter2D:
    def __init__(self, dt, measurement_noise_std=1.0, process_noise_std=1.0):
        self.dt = dt

        # State vector: [x, y, vx, vy]
        self.x = np.zeros((4, 1))

        # State covariance
        self.P = np.eye(4) * 500.0

        # State transition matrix
        self.F = np.array([
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1,  0],
            [0, 0, 0,  1]
        ])

        # Observation matrix: we only observe position (x, y)
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])

        # Measurement noise covariance
        self.R = np.eye(2) * measurement_noise_std**2

        # Process noise covariance (acceleration uncertainty)
        q = process_noise_std**2
        self.Q = np.array([
            [dt**4/4, 0, dt**3/2, 0],
            [0, dt**4/4, 0, dt**3/2],
            [dt**3/2, 0, dt**2, 0],
            [0, dt**3/2, 0, dt**2]
        ]) * q

    def predict(self):
        # x_k = F x_{k-1}
        self.x = self.F @ self.x

        # P_k = F P F^T + Q
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        z = np.reshape(z, (2, 1))
        y = z - self.H @ self.x  # innovation
        S = self.H @ self.P @ self.H.T + self.R  # innovation covariance
        K = self.P @ self.H.T @ np.linalg.inv(S)  # Kalman gain

        self.x = self.x + K @ y
        I = np.eye(4)
        self.P = (I - K @ self.H) @ self.P

    def get_state(self):
        return self.x.flatten()
