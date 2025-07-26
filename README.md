```
# Kalman Tracker

A real-time Kalman filter system built in Python for tracking a 2D projectile using noisy sensor data. The project includes a physics simulator, filtering engine, matplotlib-based plotting, GIF export, and an interactive Streamlit UI.

## Features

- Custom Kalman filter implementation for 2D position and velocity tracking
- Simulated physical system (projectile motion under gravity)
- Noisy sensor measurement simulation
- Visualizations of:
  - True vs measured vs filtered trajectories
  - Estimated velocity over time
- Real-time animation using matplotlib
- Export filtered tracking animation to GIF
- Interactive Streamlit dashboard with parameter controls
- Automatically saves filter results (true state, measurements, estimates, velocities) to `results.csv`


## Directory Structure

```
kalman_tracker/
├── animation.py              # Animation and GIF export logic
├── config.py                 # Default simulation parameters
├── kalman_filter.py          # Kalman filter implementation (2D position + velocity)
├── main.py                   # CLI runner with static plots
├── requirements.txt          # Project dependencies
├── simulator.py              # Physics + noisy measurement simulation
├── streamlit_app.py          # Interactive UI using Streamlit
├── utils.py                  # Export helpers (CSV, folders)
├── visualize.py              # Matplotlib-based plotting functions
├── exports/                  # Output folder (GIFs, CSVs, images)
│   ├── kalman_tracking.gif
│   ├── results.csv
│   └── *.png
└── README.md
```

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run: Basic CLI

Run the simulation and view static trajectory and velocity plots:

```bash
python main.py
```

This will also export plots to the `exports/` directory.

## Run: Animated Tracking

Create a frame-by-frame animated Kalman tracking GIF:

```bash
python animation.py
```

Outputs a GIF to `exports/kalman_tracking.gif`.

## Run: Interactive Streamlit App

Launch an interactive app with sliders for tuning:

```bash
streamlit run streamlit_app.py
```

In the app, you can:
- Tune time step, simulation duration, noise levels
- Enable velocity plots
- Export GIFs with one click
- Download results as CSV

## Example

Simulation of a projectile with noisy 2D position readings:

- Red crosses: sensor measurements
- Blue line: true position
- Green dashed line: Kalman filter estimate

Velocity plots show how the filter converges on smoothed estimates for `vx` and `vy`.

## Future Work

- Extend to 3D tracking
- Support for mouse-controlled target input
- Interactive uncertainty ellipses
- Model-based switching (e.g. constant turn, acceleration)
- Web-hosted version using Streamlit Cloud or Hugging Face Spaces
```
