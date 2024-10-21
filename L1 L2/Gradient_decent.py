import numpy as np
import matplotlib.pyplot as plt

from numpy._typing._array_like import NDArray
from typing import Literal


def y_function(x: int | float) -> int | float:return np.sin(x)
def y_derivative(x: int | float) -> int | float: return np.cos(x)

x: NDArray[np.float64] = np.arange(start=-5, stop=5, step=0.1)
y: int | float = y_function(x=x)

print("X - axis\n:", x)
print("\n\nY - axis\n", y)

current_position: tuple[float, int | float] = (-2, y_function(x=-2))
learning_rate= 0.1

for _ in range(1000):
    new_x: float = current_position[0] + learning_rate * y_derivative(x=current_position[0])
    new_y: int | float = y_function(x=new_x)
    
    current_position = (new_x, new_y)
    
    plt.plot(x, y)
    plt.scatter(x=current_position[0], y=current_position[1], color="red")
    plt.pause(interval=0.001)
    plt.clf()
    plt.tight_layout()

