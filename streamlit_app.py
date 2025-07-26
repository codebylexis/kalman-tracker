# streamlit_app.py
import streamlit as st
import numpy as np
from simulator import ProjectileSimulator
from kalman_filter import KalmanFilter2D
from visualize import plot_trajectory, plot_velocity
from animation import animate_kalman
import tempfile

st.set_page_config(page_title="Kalman Tracker", layout="wide")
st.title("🧭 Kalman Filter 2D Tracker")

with st.sidebar:
    st.header("Simulation Controls")
    dt = st.slider("Time Step (dt)", 0.01, 0.5, 0.1)
    total_time = st.slider("Total Time", 1.0, 20.0, 10.0)
    measurement_noise_std = st.slider("Measurement Noise", 0.1, 5.0, 2.0)
    process_noise_std = st.slider("Process Noise", 0.01, 2.0, 0.5)
    show_velocity = st.checkbox("Show Velocity Plot", value=True)
    export_gif = st.checkbox("Export GIF Animation", value=False)

if st.button("🚀 Run Simulation"):
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

    # Plot trajectory
    fig1 = plot_trajectory(true_positions, measurements, estimated_positions)
    st.pyplot(fig1)

    # Plot velocity
    if show_velocity:
        fig2 = plot_velocity(estimated_velocities)
        st.pyplot(fig2)

    if export_gif:
        with st.spinner("Generating animation..."):
            tmp_path = tempfile.NamedTemporaryFile(suffix=".gif", delete=False).name
            animate_kalman(dt=dt, total_time=total_time, save_path=tmp_path)
            st.success("✅ GIF exported")
            with open(tmp_path, "rb") as f:
                st.download_button("⬇ Download GIF", data=f, file_name="kalman_tracking.gif", mime="image/gif")
