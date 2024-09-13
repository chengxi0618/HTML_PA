import numpy as np
import matplotlib.pyplot as plt
import random

class TreeNode:
    def __init__(self, feature_index=None, threshold=None, prediction=None):
        self.feature_index = feature_index
        self.threshold = threshold
        self.prediction = prediction
        self.left = None
        self.right = None

def calculate_squared_error(labels):
    if len(labels) != 0:
        mean = np.mean(labels)
        er = np.sum((labels - mean) ** 2)
        er = er / len(labels)
        return er # 
    else: return 0

def find_allsegment_theta(values):
    theta_values = []
    theta_values.append(values[0]-1)
    for n in range(len(values)-1):
        theta_values.append((values[n]+values[n+1])/2)
    theta_values.append(values[-1]+1)
    return theta_values

def find_best_split(data, labels, indices):
    num_features = data.shape[1]
    best_error = float('inf')
    best_feature_index = None
    best_threshold = None

    for feature_index in range(num_features):
        feature_values = data[indices, feature_index]
        unique_values = np.unique(feature_values)
        theta_values = find_allsegment_theta(unique_values)

        for threshold in theta_values:
            left_indices = indices[feature_values <= threshold]
            right_indices = indices[feature_values > threshold]

            left_error = calculate_squared_error(labels[left_indices])
            right_error = calculate_squared_error(labels[right_indices])

            total_error = len(left_indices)*left_error + len(right_indices)*right_error

            if total_error < best_error:
                best_error = total_error
                best_feature_index = feature_index
                best_threshold = threshold

    return best_feature_index, best_threshold

def build_tree(data, labels, indices):
    if calculate_squared_error(labels[indices]) == 0 or len(indices) == 1: # 
        prediction = np.mean(labels[indices])
        return TreeNode(prediction=prediction)

    feature_index, threshold = find_best_split(data, labels, indices)

    if feature_index is None:
        prediction = np.mean(labels[indices])
        return TreeNode(prediction=prediction)

    left_indices = indices[data[indices, feature_index] <= threshold]
    right_indices = indices[data[indices, feature_index] > threshold]

    node = TreeNode(feature_index=feature_index, threshold=threshold)
    node.left = build_tree(data, labels, left_indices)
    node.right = build_tree(data, labels, right_indices)

    return node

def predict_single_data_point(node, features):
    if node.prediction is not None:
        return node.prediction
    if features[node.feature_index] <= node.threshold:
        return predict_single_data_point(node.left, features)
    else:
        return predict_single_data_point(node.right, features)
    
def squared_error(predict_y, y):
    e_sq = 0
    for i in range(len(y)):
        e_sq += (predict_y[i] - y[i]) ** 2
    e_sq = e_sq / len(y)
    return e_sq

def sample_with_replacement(x, y):
    x_train = []
    y_train = []
    indices = np.arange(3200)
    sample = np.random.choice(indices, size=1600, replace=True)
    for n in range(len(sample)):
        x_train.append(x[sample[n]])
        y_train.append(y[sample[n]])
    return x_train, y_train

file_path = 'hw6_train.dat'
file2_path = 'hw6_test.dat'

x_train = []
y_train = []

x_test = []
y_test = []

with open(file_path, 'r') as file:
    for line in file:
        y_train.append(int(line.strip().split()[0]))
        pairs = line.strip().split()[1:]
        features = [float(pair.split(':')[1]) for pair in pairs]
        x_train.append(features)
        
with open(file2_path, 'r') as file2:
    for line in file2:
        y_test.append(int(line.strip().split()[0]))
        pairs = line.strip().split()[1:]
        features = [float(pair.split(':')[1]) for pair in pairs]
        x_test.append(features)
        
list_error = []
tree_root = []
label_t = np.arange(1,2001)

for t in range(2000):
    np.random.seed(t)
    xs_train, ys_train = sample_with_replacement(x_train, y_train)
    all_indices = np.arange(len(ys_train))
    root = build_tree(np.array(xs_train), np.array(ys_train), all_indices)
    tree_root.append(root)

    y_predict = []
    for j in range(len(y_test)):
        y_predict.append(predict_single_data_point(root, x_test[j]))
    e_sq = squared_error(y_predict, y_test)
    print(t)
    # print(f"Eout using squared error: {e_sq}")
    list_error.append(e_sq)
    
y_Gpredict_out = []
for k in range(len(y_test)):
    y_Gpredict = 0
    y_Gpredict_list = []
    for n in range(len(tree_root)):
        y_Gpredict += predict_single_data_point(tree_root[n], x_test[k])
        y_Gpredict_list.append(y_Gpredict/(n+1))
    y_Gpredict_out.append(y_Gpredict_list)
    
errorG_out = []
for d in range(len(y_Gpredict_out[0])):
    y_Gpredict_one_out = []
    for f in range(len(y_Gpredict_out)):
        y_Gpredict_one_out.append(y_Gpredict_out[f][d])
    errorG_out.append(squared_error(y_Gpredict_one_out, y_test))

plt.plot(label_t, list_error, label='Eout(gt)')
plt.plot(label_t, errorG_out, label='Eout(Gt)')
plt.xlabel('t')
plt.ylabel('Function Value')
plt.title('Eout(gt) vs Eout(Gt)')
# Add a legend
plt.legend()

plt.show()