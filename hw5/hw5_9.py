import numpy as np
import matplotlib.pyplot as plt
import random
from libsvm.svmutil import *

file_path = 'hw5_train.dat'

x_train = []
y_train = []

with open(file_path, 'r') as file:
    for line in file:
        y_train.append(line.strip().split()[0])
        pairs = line.strip().split()[1:]
        features = {int(pair.split(':')[0]): float(pair.split(':')[1]) for pair in pairs}
        x_train.append(features)

for i in range(len(y_train)):
    if((int(y_train[i])) == 4):
        y_train[i] = 1
    else:
        y_train[i] = -1
        
prob  = svm_problem(y_train, x_train)
# 有 -r 1?
param1 = svm_parameter('-s 0 -t 1 -d 2 -g 1 -r 1 -c 0.1')
param2 = svm_parameter('-s 0 -t 1 -d 3 -g 1 -r 1 -c 0.1 -q')
param3 = svm_parameter('-s 0 -t 1 -d 4 -g 1 -r 1 -c 0.1 -q')
param4 = svm_parameter('-s 0 -t 1 -d 2 -g 1 -r 1 -c 1 -q')
param5 = svm_parameter('-s 0 -t 1 -d 3 -g 1 -r 1 -c 1 -q')
param6 = svm_parameter('-s 0 -t 1 -d 4 -g 1 -r 1 -c 1 -q')
param7 = svm_parameter('-s 0 -t 1 -d 2 -g 1 -r 1 -c 10 -q')
param8 = svm_parameter('-s 0 -t 1 -d 3 -g 1 -r 1 -c 10 -q')
param9 = svm_parameter('-s 0 -t 1 -d 4 -g 1 -r 1 -c 10 -q')

m1 = svm_train(prob, param1)
m2 = svm_train(prob, param2)
m3 = svm_train(prob, param3)
m4 = svm_train(prob, param4)
m5 = svm_train(prob, param5)
m6 = svm_train(prob, param6)
m7 = svm_train(prob, param7)
m8 = svm_train(prob, param8)
m9 = svm_train(prob, param9)
m = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
list_cq = ["2 0.1", "3 0.1", "4 0.1", "2 1", "3 1", "4 1", "2 10", "3 10", "4 10"]
svs = []
leastsv = 0
num_sv = 5000
for i in range(len(m)):
    sv = []
    sv = m[i].get_SV()
    svs.append(len(sv))
    print(len(sv))
    if len(sv) < num_sv:
        print(i)
        leastsv = i
        num_sv = len(sv)
print(list_cq[leastsv])  