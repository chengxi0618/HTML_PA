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
    if((int(y_train[i])) == 3):
        y_train[i] = 1
    else:
        y_train[i] = -1
        
prob  = svm_problem(y_train, x_train)
# 有 -r 1?
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
list_cq =  [0.01, 0.1, 1, 10, 100]
svs = []
sv_coeffs = []

for i in range(len(m)):
    sv = []
    sv_coeff = []
    sv = m[i].get_SV()
    sv_coeff = m[i].get_sv_coef()
    svs.append(sv)
    sv_coeffs.append(sv_coeff)

w_norm = []
array = list(svs[0][0].values())
print(array)

for i in range(5):
    w = np.zeros(36)
    # print(len(svs[i]))
    for n in range(len(svs[i])):
        print(sv_coeffs[i][n][0])
        if(len(svs[i][n]) == 36):
            w += sv_coeffs[i][n][0]*np.array(list(svs[i][n].values()))
        else:
            w_fixed = []
            for j in range(1,37):
                if j in svs[i][n]:
                    w_fixed.append(svs[i][n][j])
                else: w_fixed.append(0)
            w += sv_coeffs[i][n][0]*np.array(w_fixed)
    w_norm.append(np.linalg.norm(w))

for i in range(5):
    print(w_norm[i])
categories = np.log10(list_cq)

plt.plot(categories, w_norm)
plt.xlabel('selected C (log10)')
plt.ylabel('w_norm')
plt.show()