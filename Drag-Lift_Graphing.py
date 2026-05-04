import numpy as np
import matplotlib.pyplot as plt

# Constants
rho = 1.225  # air density (kg/m^3)
S = 0.1     # wing area (m^2)

# Lift coefficient function
def lift_coefficient(alpha):
    return 2 * np.pi * alpha  # alpha in radians

# Drag coefficient function
def drag_coefficient(alpha):
    return 0.02 + alpha**2

# Velocity range
velocities = np.linspace(1, 400000, 1000000)

# Angle of attack
alpha = np.radians(10)

# Calculate lift and drag
lift = 0.5 * rho * velocities**2 * S * lift_coefficient(alpha)
drag = 0.5 * rho * velocities**2 * S * drag_coefficient(alpha)

# Plot results
plt.plot(velocities, lift, label="Lift")
plt.plot(velocities, drag, label="Drag")

plt.xlabel("Velocity (m/s)")
plt.ylabel("Force (N)")
plt.title("Lift and Drag vs Velocity")
plt.legend()

plt.savefig("lift_drag_graph.png")

plt.show()
