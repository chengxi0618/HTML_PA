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

def generate_s_theta(data_sorted):
    hypothesis = []
    hypothesis.append([-1, 1])
    hypothesis.append([-1, -1])
    for i in range(7):
        if (data_sorted[i][0] != data[i+1][0]):
            avg = (data_sorted[i][0] + data_sorted[i+1][0]) / 2
            hypothesis.append([avg, 1])
            hypothesis.append([avg, -1])
    return hypothesis

def Ein(data_sorted, hypothesis):
    best_error = 8
    best_hypothesis = [-1, -1]
    for i in range(len(hypothesis)):
        error = 0
        for n in range(len(data_sorted)):
            if ((data_sorted[n][0] - hypothesis[i][0]) == 0):
                if(data_sorted[n][1] == 1):
                    error += 1
            else:
                if(hypothesis[i][1] * np.sign(data_sorted[n][0] - hypothesis[i][0]) != data_sorted[n][1]):
                    error += 1
        if (error < best_error):
            best_error = error
            best_hypothesis = hypothesis[i]
        elif (error == best_error):
            if ((hypothesis[i][0]*hypothesis[i][1]) < (best_hypothesis[0]*best_hypothesis[1])):
                best_hypothesis = hypothesis[i]
    return best_error, best_hypothesis

          
Ein_g = []
Eout_g = []

for i in range(2000):
    data = generate_x_y()
    data_sorted = sorted(data, key=lambda x: x[0])
    hypothesis = generate_s_theta(data_sorted)
    best_error, best_hypothesis = Ein(data_sorted, hypothesis)
    Ein_g.append(best_error/8)
    Eout_g.append(0.5-(0.4*best_hypothesis[1])+(0.4*best_hypothesis[1]*abs(best_hypothesis[0])))

print(np.median(np.array(Eout_g) - np.array(Ein_g)))

plt.scatter(Ein_g, Eout_g)
plt.xlabel('Ein(g)')
plt.ylabel('Eout(g)')
plt.show()