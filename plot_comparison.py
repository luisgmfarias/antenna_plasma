import numpy as np
import matplotlib.pyplot as plt

com_plasma = np.load("com_plasma.npy")
sem_plasma = np.load("sem_plasma.npy")

plt.plot(com_plasma)
plt.plot(sem_plasma)
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.show()