import os
import random
import sys

def Load_Data(feature_dir):
    X = []
    y = []
    num_sequences = 0
    for file in os.listdir(feature_dir):
        if ".features" not in file:
            continue
        if num_sequences > 10:
            break
            #pass
        with open(feature_dir + file, "r") as feature_file:
            for line in feature_file:
                line = line.strip().split(",")
                label = float(line[0])
                features = [int(x) for x in line[1:]]
                features.append(1)
                y.append(label)
                X.append(features)
        num_sequences += 1
    return X, y

def Split_Data(num_instances, test_split=.25):
    test_indices = random.sample(range(num_instances), int(num_instances*test_split))
    train_indices = []
    for i in range(num_instances):
        if i not in test_indices:
            train_indices.append(i)
    return train_indices, test_indices

def Get_Data(X, Y, indices):
    x = []
    y = []
    for i in indices:
        x.append(X[i])
        y.append(Y[i])
    return x, y
                
