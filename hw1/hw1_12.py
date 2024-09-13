import numpy as np
import matplotlib.pyplot as plt
import random 

def load_data():
    file_path = 'hw1_train.dat'
    data = np.loadtxt(file_path, delimiter=' ', dtype=float)
    return data

data = load_data()

data_train = []
for i in range(256):
    l1 = []
    l2 = [1]
    for  n in range(13):
        if n != 12:
            l2.append(data[i][n])
        else: 
            t2 = tuple(l2)
            l1.append(t2)
            l1.append(data[i][n])
    t1 = tuple(l1)
    data_train.append(t1)

def check_error(w, dataset, index):
    result = None
    x, s = dataset[index]
    x = np.array(x)
    if (w.T.dot(x) == 0) & (int(s) == -1):
        return result
    if int(np.sign(w.T.dot(x))) != s:                              
        result =  x, s
    return result

def pla(dataset):
    w = np.zeros(13)
    num_error = 0
    num_update = 0
    next = True
    while num_error < 1280:                                         # checking 5N(=1280) randomly-picked examples
        if next == True:
            index_random = random.randint(0,255)
        if check_error(w, dataset, index_random) != None:
            x, s = check_error(w, dataset, index_random)
            w += int(s) * x
            num_error = 0
            num_update += 1
            next = False
        else: 
            num_error += 1
            next = True
    return w, num_update

i = 0
nums_update = []
while i < 1000:                                                      # repeating 1000 times
    random.seed(i)
    w, num_update = pla(data_train)
    nums_update.append(num_update)
    i += 1
    
plt.hist(nums_update, bins=50, edgecolor='blue')
plt.xlabel('Number of Updates')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

median = np.median(nums_update)
print(median)