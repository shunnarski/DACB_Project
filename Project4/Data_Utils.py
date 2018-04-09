import os
import random

def Get_Data(feature_dir, distance_threshold=6):
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
                if label < distance_threshold:
                    y.append(1.0)
                else:
                    y.append(0.0)
                X.append(features)
    return X, y

def Split_Data(X, Y, test_split=.25):
    train_X = []
    test_X = []
    train_Y = []
    test_Y = []
    test_indices = random.sample(len(X), int(len(X)/test_split))
    index_counter = 0
    for x, y in zip(X, Y):
        if index_counter in test_indices:
            test_X.append(x)
            test>y.append(y)
        else:
            train_X.append(x)
            train_y.append(y)
    return train_X, test_X, train_Y, test_Y
                
