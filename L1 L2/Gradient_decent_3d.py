import numpy as np
import matplotlib.pyplot as plt

def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5

def gradient_decent(x, y):
    """Return the derivative of z_function (Product Rule)"""
    return np.cos(5 * x) * np.cos(5 * y), np.sin(5 * x) * -np.sin(5 * y)

x = np.arange(start=-1, stop=1, step=0.05)
y = np.arange(start=-1, stop=1, step=0.05)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

current_position = (0.7, 0.4, z_function(0.7, 0.4))
learning_rate = 0.001

ax = plt.subplot(projection= "3d", computed_zorder=False)  # Corrected the `projection` placement

for _ in range(1000):
    X_derivative, y_derivative = gradient_decent(current_position[0], current_position[1])
    new_x, new_y = current_position[0] - learning_rate * X_derivative , current_position[1] - learning_rate * y_derivative
    current_position = (new_x, new_y, z_function(new_x, new_y))
    
    ax.plot_surface(X, Y, Z, cmap='viridis')  # Use `cmap` instead of `color`
    ax.scatter(current_position[0], current_position[1], current_position[2], color="magenta")
    plt.pause(0.001)
    ax.clear()
