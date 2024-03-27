import numpy as np
import matplotlib.pyplot as plt

N = 23
x = np.linspace(0, 1, 1000)
y = np.sin(np.pi * x / N)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'N = {N}')
plt.title('Графік функції $f(x) = \sin(\\frac{\\pi x}{N})$ на проміжку [0, 1]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
