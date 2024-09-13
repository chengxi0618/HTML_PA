import numpy as np
import matplotlib.pyplot as plt
import random
from libsvm.svmutil import *

file_path = 'hw5_train.dat'
file_test_path = 'hw5_test.dat'

x_train = []
y_train = []
x_test = []
y_test = []

with open(file_path, 'r') as file:
    for line in file:
        y_train.append(line.strip().split()[0])
        pairs = line.strip().split()[1:]
        features = {int(pair.split(':')[0]): float(pair.split(':')[1]) for pair in pairs}
        x_train.append(features)
        
with open(file_test_path, 'r') as file:
    for line in file:
        y_test.append(line.strip().split()[0])
        pairs = line.strip().split()[1:]
        features = {int(pair.split(':')[0]): float(pair.split(':')[1]) for pair in pairs}
        x_test.append(features)

for i in range(len(y_train)):
    if((int(y_train[i])) == 1):
        y_train[i] = 1
    else:
        y_train[i] = -1
        
for i in range(len(y_test)):
    if((int(y_test[i])) == 1):
        y_test[i] = 1
    else:
        y_test[i] = -1
        
prob  = svm_problem(y_train, x_train)

param1 = svm_parameter('-s 0 -t 2 -g 1 -c 0.01')
param2 = svm_parameter('-s 0 -t 2 -g 1 -c 0.1 -q')
param3 = svm_parameter('-s 0 -t 2 -g 1 -c 1 -q')
param4 = svm_parameter('-s 0 -t 2 -g 1 -c 10 -q')
param5 = svm_parameter('-s 0 -t 2 -g 1 -c 100 -q')

m1 = svm_train(prob, param1)
m2 = svm_train(prob, param2)
m3 = svm_train(prob, param3)
m4 = svm_train(prob, param4)
m5 = svm_train(prob, param5)

m = [m1, m2, m3, m4, m5]
list_cq = [0.01, 0.1, 1, 10, 100]
c_best = 0
Pacc_best = 0
for i in range(len(m)):
    p_label, p_acc, p_val = svm_predict(y_test, x_test, m[i])
    if p_acc[0] > Pacc_best:
        c_best = i
        Pacc_best = p_acc[0]
        print(i)
        print(p_acc[0])
print(list_cq[c_best])