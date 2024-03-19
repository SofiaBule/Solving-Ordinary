import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the differential equation
def damped_oscillator(t, y, omega0, gamma):
    return [y[1], -omega0**2 * y[0] - gamma * y[1]]

# Define initial conditions
y0 = [1, 0]

# Define time points for integration
t_span = (0, 10)
t_eval = np.linspace(*t_span, 100)

# Solve the ODE
solution = solve_ivp(damped_oscillator, t_span, y0, args=(1, 0.1), t_eval=t_eval)

# Plot the solution
plt.plot(solution.t, solution.y[0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Solution of Damped Oscillator ODE')
plt.grid(True)
plt.show()
