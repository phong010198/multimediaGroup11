import matplotlib.pyplot as plt
import numpy as np

f = 1
fs = 8000
N = 5
A = 5                                                                       
n = 100

t_samplings = np.linspace(0, N/f, (N/f) * fs)

plot1 = A * np.sin(2*np.pi*f*t_samplings)
plt.figure()
plt.plot(t_samplings, plot1)
plt.savefig("image1.png")
plt.close()
