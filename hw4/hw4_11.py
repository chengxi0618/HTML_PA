import numpy as np
import matplotlib.pyplot as plt
import random
from liblinear.liblinearutil import *

file_path = 'hw4_train.dat'
data = np.loadtxt(file_path, delimiter=' ', dtype=float)

x_train = []
y_train = []

for i in range(200):
    l = []
    for  n in range(7):
        if n != 6:
            l.append(data[i][n])
        else:
            y_train.append(data[i][n])
    x_train.append(l)

transform = []
for i in range(6):
    transform.append([i])
for i in range(6):
    for j in range(i, 6):
        transform.append([i, j])
for i in range(6):
    for j in range(i, 6):
        for n in range(j, 6):
            transform.append([i, j, n])

z_train = []
for i in range(200):
    z_dat = [1]
    for j in range(len(transform)):
        z = 1
        for n in range(len(transform[j])):
            z = z * x_train[i][transform[j][n]]
        z_dat.append(z)
    z_train.append(z_dat)
    
def random_split(z, y):
    data = []
    for i in range(200):
        data.append([z[i], y[i]])
    data_train = random.sample(data, 120)
    data_val = [element for element in data if element not in data_train]    
    z_train = []
    y_train = []
    z_val = []
    y_val = []
    for j in range(120):
        z_train.append(data_train[j][0])
        y_train.append(data_train[j][1])
    for n in range(80):
        z_val.append(data_val[n][0])
        y_val.append(data_val[n][1])
    return z_train, y_train, z_val, y_val

best_list = []

for n in range(128):
    random.seed(n)  
    z_tra, y_tra, z_val, y_val = random_split(z_train, y_train)

    ## train C = 1/2lambda where log10(lambda)={-6,-4,-2,0,2} <> lambda={10^-6, 10^-4, 10^-2, 1, 10^2}
    w = []
    prob = problem(y_tra, z_tra)
    param = parameter('-s 0 -c 500000 -e  0.000001')
    w_m6 = train(prob, param)
    w.append(w_m6)
    prob = problem(y_tra, z_tra)
    param = parameter('-s 0 -c 5000 -e  0.000001')
    w_m4 = train(prob, param)
    w.append(w_m4)
    prob = problem(y_tra, z_tra)
    param = parameter('-s 0 -c 500 -e  0.000001')
    w_m2 = train(prob, param)
    w.append(w_m2)
    prob = problem(y_tra, z_tra)
    param = parameter('-s 0 -c 0.5 -e  0.000001')
    w_0 = train(prob, param)
    w.append(w_0)
    prob = problem(y_tra, z_tra)
    param = parameter('-s 0 -c 0.005 -e  0.000001')
    w_2 = train(prob, param)
    w.append(w_2)

    # p_labels, p_acc, p_vals = predict(y_train, z_train, w[0])
    # print(p_acc[0])
    l = [-6, -4, -2, 0, 2]
    best = -7
    best_acc = 0

    for i in range(5):
        p_labels, p_acc, p_vals = predict(y_val, z_val, w[i])
        if p_acc[0] >= best_acc:
            if p_acc[0] == best_acc:
                if l[i] > best:
                    best = l[i]
            else:
                best = l[i]
                best_acc = p_acc[0]
    best_list.append(best)
    
plt.hist(best_list, bins=20, edgecolor='blue')
plt.xlabel('log10(lambda*)')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()