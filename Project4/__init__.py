import Data_Utils
from LogisticRegression import LogisticRegression


if __name__ == "__main__":
    X, Y = Data_Utils.Get_Data("data/")
    max_dist = max(Y)
    mean_dist = sum(Y)/float(len(Y))
    min_dist = min(Y)
    print "Distance:\n\tMax: {}\n\tMean: {}\n\tMin: {}\n".format(max_dist, mean_dist, min_dist)
    clf = LogisticRegression()
    #print clf.predict(X)
