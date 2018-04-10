import os
import random
import sys

def Get_Data(feature_dir):
    X = []
    y = []
    for file in os.listdir(feature_dir):
        if ".features" not in file:
            continue
        with open(feature_dir + file, "r") as feature_file:
            for line in feature_file:
                line = line.strip().split(",")
                label = float(line[0])
                features = [int(x) for x in line[1:]]
                features.append(1)
                y.append(label)
                X.append(features)
    return X, y

def Split_Data(X, Y, test_split=.25):
    train_X = []
    test_X = []
    train_Y = []
    test_Y = []
    test_indices = random.sample(range(len(X)), int(len(X)*test_split))
    index_counter = 0
    for x, y in zip(X, Y):
        if index_counter in test_indices:
            test_X.append(x)
            test_Y.append(y)
        else:
            train_X.append(x)
            train_Y.append(y)
        index_counter += 1
    return train_X, test_X, train_Y, test_Y
                
