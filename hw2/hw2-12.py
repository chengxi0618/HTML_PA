import numpy as np
import matplotlib.pyplot as plt
import random

def generate_x_y():
    data = []
    for i in range(8):
        d = []
        x = random.uniform(-1, 1)
        noise = random.uniform(0,1)
        if x > 0:
            if noise > 0.1:
                y = 1
            else: 
                y = -1
        else:
            if noise > 0.1:
                y = -1
            else:
                y = 1
        d.append(x)
        d.append(y)
        data.append(d)
    return data

def Ein(data_sorted):
    error = 0
    hypothesis = [random.uniform(-1, 1), random.choice([-1, 1])]
    for n in range(len(data_sorted)):
        if ((data_sorted[n][0] - hypothesis[0]) == 0):
            if(data_sorted[n][1] == 1):
                error += 1
        else:
            if(hypothesis[1] * np.sign(data_sorted[n][0] - hypothesis[0]) != data_sorted[n][1]):
                error += 1
    return error, hypothesis

          
Ein_g = []
Eout_g = []

for i in range(2000):
    data = generate_x_y()
    data_sorted = sorted(data, key=lambda x: x[0])
    error, hypothesis = Ein(data_sorted)
    Ein_g.append(error/8)
    Eout_g.append(0.5-(0.4*hypothesis[1])+(0.4*hypothesis[1]*abs(hypothesis[0])))

print(np.median(np.array(Eout_g) - np.array(Ein_g)))

plt.scatter(Ein_g, Eout_g)
plt.xlabel('Ein(g)')
plt.ylabel('Eout(g)')
plt.show()