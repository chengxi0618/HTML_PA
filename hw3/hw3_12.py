import numpy as np
import matplotlib.pyplot as plt
import random

def generate_train_test():
    data_train_x = []
    data_train_y = []
    for i in range(256):
        y = random.choice([+1, -1])
        x = [1]
        if y == +1:
            mean = np.array([3, 2])
            cov_matrix = np.array([[0.4, 0], [0, 0.4]])
            x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
            x.append(x1_x2[0][0])
            x.append(x1_x2[0][1])
            data_train_x.append(x)
            data_train_y.append(y)
        else:
            mean = np.array([5, 0])
            cov_matrix = np.array([[0.6, 0], [0, 0.6]])
            x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
            x.append(x1_x2[0][0])
            x.append(x1_x2[0][1])
            data_train_x.append(x)
            data_train_y.append(y)
    for i in range(16):
        y = 1
        x = [1]
        mean = np.array([0, 6])
        cov_matrix = np.array([[0.1, 0], [0, 0.3]])
        x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
        x.append(x1_x2[0][0])
        x.append(x1_x2[0][1])
        data_train_x.append(x)
        data_train_y.append(y)
    data_test_x = []
    data_test_y = []
    for i in range(4096):
        y = random.choice([+1, -1])
        x = [1]
        if y == +1:
            mean = np.array([3, 2])
            cov_matrix = np.array([[0.4, 0], [0, 0.4]])
            x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
            x.append(x1_x2[0][0])
            x.append(x1_x2[0][1])
            data_test_x.append(x)
            data_test_y.append(y)
        else:
            mean = np.array([5, 0])
            cov_matrix = np.array([[0.6, 0], [0, 0.6]])
            x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
            x.append(x1_x2[0][0])
            x.append(x1_x2[0][1])
            data_test_x.append(x)
            data_test_y.append(y)
    return data_train_x, data_train_y, data_test_x, data_test_y

def linear_regression(x, y):
    x_pinv = np.linalg.pinv(x)
    w_LIN = np.dot(x_pinv, y)
    return w_LIN

def logistic_regression(x, y):
    w = np.zeros(len(x[0]))
    for i in range(500):
        s = np.zeros(len(x[0]))
        for n in range(len(y)):
            s += -np.exp(-y[n]*np.dot(w.T, x[n]))/(1 + np.exp(-y[n]*np.dot(w.T, x[n]))) * np.dot(np.array(y[n]),np.array(x[n]))
        s /= len(y)
        w = w - 0.1 * s / np.linalg.norm(s)
    return w

def Ein_linearclassification(w, x, y):
    error = 0
    for i in range(len(y)):
        if int(np.sign(w.T.dot(x[i]))) != y[i]:                              
            error += 1
    error /=  len(y)
    return error

E_linear = []
E_logistic = []

for i in range(128):
    random.seed(i)
    x_train, y_train, x_test, y_test = generate_train_test()
    w_LIN = linear_regression(x_train, y_train)
    w_LOG = logistic_regression(x_train, y_train)
    Ein1 = Ein_linearclassification(w_LIN, x_test, y_test)
    E_linear.append(Ein1)
    Ein2 = Ein_linearclassification(w_LOG, x_test, y_test)
    E_logistic.append(Ein2)
    
median_lin = np.median(E_linear)
print(median_lin)
median_log = np.median(E_logistic)
print(median_log)

plt.scatter(E_linear, E_logistic)
plt.xlabel('Eout(A(D\'))')
plt.ylabel('Eout(B(D\'))')
plt.show()