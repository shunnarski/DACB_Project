import Data_Utils
from LinearRegression import LinearRegression


if __name__ == "__main__":
    print "Loading Data ..."
    X, Y = Data_Utils.Load_Dataset("labels.csv")
    print "Splitting Data ..."
    train_x, test_x, train_y, test_y = Data_Utils.Split_Data(X, Y)
    print "Total: {}".format(len(train_x))
    print "Train split: {}".format(len(train_x))
    print "Test split: {}".format(len(test_x))
    clf = LinearRegression(batch_size=64, max_iter=10000, learning_rate=1e-5, reg_strength=1e-4, convergence_threshold=1e-4)
    clf.fit(train_x, train_y, test_x, test_y, verbose=True)
    clf.save_weights("test.mdl")
