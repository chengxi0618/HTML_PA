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
    data_test = []
    for i in range(4096):
        y = random.choice([+1, -1])
        x = [1]
        if y == +1:
            mean = np.array([3, 2])
            cov_matrix = np.array([[0.4, 0], [0, 0.4]])
            x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
            x.append(x1_x2[0][0])
            x.append(x1_x2[0][1])
            data_test.append([x, y])
        else:
            mean = np.array([5, 0])
            cov_matrix = np.array([[0.6, 0], [0, 0.6]])
            x1_x2 = np.random.multivariate_normal(mean, cov_matrix, 1)
            x.append(x1_x2[0][0])
            x.append(x1_x2[0][1])
            data_test.append([x, y])
    return data_train_x, data_train_y, data_test

def linear_regression(x, y):
    x_pinv = np.linalg.pinv(x)
    w_LIN = np.dot(x_pinv, y)
    return w_LIN

def E_in(w_LIN, x, y):
    Ein = 0
    for i in range(len(y)):
        Ein += (np.dot(w_LIN.T, x[i]) - y[i]) ** 2
    Ein /= len(y)
    return Ein

E = []
for i in range(128):
    random.seed(i)
    x_train, y_train, data_test = generate_train_test()
    w_LIN = linear_regression(x_train, y_train)
    Ein = E_in(w_LIN, x_train, y_train)
    E.append(Ein)
    
median = np.median(E)
print(median)

plt.hist(E, bins=20, edgecolor='blue')
plt.xlabel('Ein(wLIN)')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()    