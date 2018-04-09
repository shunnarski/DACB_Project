import Data_Utils
from LogisticRegression import LogisticRegression


if __name__ == "__main__":
    X, Y = Data_Utils.Get_Data("data/")
    Train_X, Test_X, Train_Y, Test_Y = Data_Utils.Split_Data(X, Y)
    max_dist = max(Y)
    mean_dist = sum(Y)/float(len(Y))
    min_dist = min(Y)
    print "Distance:\n\tMax: {}\n\tMean: {}\n\tMin: {}\n".format(max_dist, mean_dist, min_dist)
    print "Train split: {}".format(len(Train_X))
    print "Test split: {}".format(len(Test_X))
    clf = LogisticRegression(batch_size=32, max_iter=100, learning_rate=1e-3, reg_strength=1e-4, convergence_threshold=1e-4)
    clf.fit(Train_X, Train_Y, Test_X, Test_Y, verbose=True)
