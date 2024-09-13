import numpy as np
import matplotlib.pyplot as plt
import random
from libsvm.svmutil import *

file_path = 'hw5_train.dat'
file_test_path = 'hw5_test.dat'

x_train = []
y_train = []

with open(file_path, 'r') as file:
    for line in file:
        y_train.append(line.strip().split()[0])
        pairs = line.strip().split()[1:]
        features = {int(pair.split(':')[0]): float(pair.split(':')[1]) for pair in pairs}
        x_train.append(features)

for i in range(len(y_train)):
    if((int(y_train[i])) == 1):
        y_train[i] = 1
    else:
        y_train[i] = -1
        
param1 = svm_parameter('-s 0 -t 2 -g 1 -c 0.01')
param2 = svm_parameter('-s 0 -t 2 -g 1 -c 0.1 -q')
param3 = svm_parameter('-s 0 -t 2 -g 1 -c 1 -q')
param4 = svm_parameter('-s 0 -t 2 -g 1 -c 10 -q')
param5 = svm_parameter('-s 0 -t 2 -g 1 -c 100 -q')

def randomSample(x, y):
    data = []
    x_train = []
    y_train = []
    x_val = []
    y_val = []
    for i in range(len(y)):
        data.append([x[i], y[i]])
    random.shuffle(data)
    for i in range(len(data)):
        if(i < 200):
            x_val.append(data[i][0])
            y_val.append(data[i][1])
        else:
            x_train.append(data[i][0])
            y_train.append(data[i][1])
    return x_train, y_train, x_val, y_val

list_c_best = []
list_cq = [0.01, 0.1, 1, 10, 100]
    
for n in range(1000):
    random.seed(n)
    x_train_new, y_train_new, x_val, y_val = randomSample(x_train, y_train)
    prob  = svm_problem(y_train_new, x_train_new)
    m1 = svm_train(prob, param1)
    m2 = svm_train(prob, param2)
    m3 = svm_train(prob, param3)
    m4 = svm_train(prob, param4)
    m5 = svm_train(prob, param5)

    m = [m1, m2, m3, m4, m5]
    
    c_best = -1
    Pacc_best = 0
    for i in range(len(m)):
        p_label, p_acc, p_val = svm_predict(y_val, x_val, m[i])
        if p_acc[0] >= Pacc_best:
            if p_acc[0] == Pacc_best:
                if list_cq[i] < list_cq[c_best]:
                    c_best = i
            else:
                c_best = i
                Pacc_best = p_acc[0]
    list_c_best.append(list_cq[c_best])


categories = np.log10([0.01, 0.1, 1, 10, 100])
values = []
for n in range(len(list_cq)):
    values.append(list_c_best.count(list_cq[n]))
plt.bar(categories, values)
plt.xlabel('selected C (log10)')
plt.ylabel('frequency')
plt.show()
