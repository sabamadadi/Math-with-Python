import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-np.pi, np.pi, 100)
f_t = np.sin(t)
plt.plot(t, f_t, 'r--')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Function f(t) = sin(t)')
plt.show()