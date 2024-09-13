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
    random.shuffle(data)
    z_1 = []
    y_1 = []
    z_2 = []
    y_2 = []
    z_3 = []
    y_3 = []
    z_4 = []
    y_4 = []
    z_5 = []
    y_5 = []
    for j in range(40):
        z_1.append(data[j][0])
        y_1.append(data[j][1])
        z_2.append(data[40+j][0])
        y_2.append(data[40+j][1])
        z_3.append(data[80+j][0])
        y_3.append(data[80+j][1])
        z_4.append(data[120+j][0])
        y_4.append(data[120+j][1])
        z_5.append(data[160+j][0])
        y_5.append(data[160+j][1])
    return z_1, y_1, z_2, y_2, z_3, y_3, z_4, y_4, z_5, y_5

best_list = []

for n in range(128):
    random.seed(n)  
    z_1, y_1, z_2, y_2, z_3, y_3, z_4, y_4, z_5, y_5 = random_split(z_train, y_train)
    z1_train = z_2 + z_3 + z_4 + z_5  # leave z_1 for validation
    y1_train = y_2 + y_3 + y_4 + y_5
    z1_val = z_1
    y1_val = y_1
    z2_train = z_1 + z_3 + z_4 + z_5  # leave z_2 for validation
    y2_train = y_1 + y_3 + y_4 + y_5
    z2_val = z_2
    y2_val = y_2
    z3_train = z_1 + z_2 + z_4 + z_5  # leave z_3 for validation
    y3_train = y_1 + y_2 + y_4 + y_5
    z3_val = z_3
    y3_val = y_3
    z4_train = z_1 + z_2 + z_3 + z_5  # leave z_4 for validation
    y4_train = y_1 + y_2 + y_3 + y_5
    z4_val = z_4
    y4_val = y_4
    z5_train = z_1 + z_2 + z_3 + z_4  # leave z_5 for validation
    y5_train = y_1 + y_2 + y_3 + y_4
    z5_val = z_5
    y5_val = y_5
    ## train C = 1/2lambda where log10(lambda)={-6,-4,-2,0,2} <> lambda={10^-6, 10^-4, 10^-2, 1, 10^2}
    w = []
    prob1 = problem(y1_train, z1_train)
    prob2 = problem(y2_train, z2_train)
    prob3 = problem(y3_train, z3_train)
    prob4 = problem(y4_train, z4_train)
    prob5 = problem(y5_train, z5_train)
    param1 = parameter('-s 0 -c 500000 -e  0.000001')
    param2 = parameter('-s 0 -c 5000 -e  0.000001')
    param3 = parameter('-s 0 -c 500 -e  0.000001')
    param4 = parameter('-s 0 -c 0.5 -e  0.000001')
    param5 = parameter('-s 0 -c 0.005 -e  0.000001')
    w_m6_1 = train(prob1, param1)
    w.append(w_m6_1)
    w_m6_2 = train(prob2, param1)
    w.append(w_m6_2)
    w_m6_3 = train(prob3, param1)
    w.append(w_m6_3)
    w_m6_4 = train(prob4, param1)
    w.append(w_m6_4)
    w_m6_5 = train(prob5, param1)
    w.append(w_m6_5)
    w_m4_1 = train(prob1, param2)
    w.append(w_m4_1)
    w_m4_2 = train(prob2, param2)
    w.append(w_m4_2)
    w_m4_3 = train(prob3, param2)
    w.append(w_m4_3)
    w_m4_4 = train(prob4, param2)
    w.append(w_m4_4)
    w_m4_5 = train(prob5, param2)
    w.append(w_m4_5)
    w_m2_1 = train(prob1, param3)
    w.append(w_m2_1)
    w_m2_2 = train(prob2, param3)
    w.append(w_m2_2)
    w_m2_3 = train(prob3, param3)
    w.append(w_m2_3)
    w_m2_4 = train(prob4, param3)
    w.append(w_m2_4)
    w_m2_5 = train(prob5, param3)
    w.append(w_m2_5)
    w_0_1 = train(prob1, param4)
    w.append(w_0_1)
    w_0_2 = train(prob2, param4)
    w.append(w_0_2)
    w_0_3 = train(prob3, param4)
    w.append(w_0_3)
    w_0_4 = train(prob4, param4)
    w.append(w_0_4)
    w_0_5 = train(prob5, param4)
    w.append(w_0_5)
    w_2_1 = train(prob1, param5)
    w.append(w_2_1)
    w_2_2 = train(prob2, param5)
    w.append(w_2_2)
    w_2_3 = train(prob3, param5)
    w.append(w_2_3)
    w_2_4 = train(prob4, param5)
    w.append(w_2_4)
    w_2_5 = train(prob5, param5)
    w.append(w_2_5)

    # p_labels, p_acc, p_vals = predict(y_train, z_train, w[0])
    # print(p_acc[0])
    l = [-6, -4, -2, 0, 2]
    best = -7
    best_Ecv = 1

    for i in range(5):
        p1_labels, p1_acc, p1_vals = predict(y1_val, z1_val, w[5*i])
        p2_labels, p2_acc, p2_vals = predict(y2_val, z2_val, w[5*i+1])
        p3_labels, p3_acc, p3_vals = predict(y3_val, z3_val, w[5*i+2])
        p4_labels, p4_acc, p4_vals = predict(y4_val, z4_val, w[5*i+3])
        p5_labels, p5_acc, p5_vals = predict(y5_val, z5_val, w[5*i+4])
        Ecv = 1-(p1_acc[0] + p2_acc[0] + p3_acc[0] + p4_acc[0] + p5_acc[0])/500
        if Ecv <= best_Ecv:
            if Ecv == best_Ecv:
                if l[i] > best:
                    best = l[i]
            else:
                best = l[i]
                best_Ecv = Ecv
    best_list.append(best)
    
plt.hist(best_list, bins=20, edgecolor='blue')
plt.xlabel('log10(lambda*)')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()