import matplotlib.pyplot as plt
import numpy as np

f = 1
fs = 8000
N = 5
A = 5                                                                       
n = 100

t_samplings = np.linspace(0, N/f, (N/f) * fs)

plot2 = np.zeros(t_samplings.size)
for i in range(2*n+2):
    plot2 += A * np.sin(2*np.pi*(2*i+1)*f*t_samplings) / (2*i+1)**2
plt.figure()
plt.plot(t_samplings, plot2)
plt.savefig("image2.png")
plt.close()
