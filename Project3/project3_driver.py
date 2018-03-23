from NBClassifier import NBClassifier
import project3_functions
import sys

clf = NBClassifier()

X_raw = project3_functions.read_file(sys.argv[1])
y_raw = project3_functions.read_file(sys.argv[2])

X, y = project3_functions.extract_features(X_raw,y_raw)

X_train, X_test, y_train, y_test = project3_functions.split_data(X,y)

means_and_variances, priors = clf.fit(X_train, y_train)
predictions = clf.predict(X_test, means_and_variances, priors)

accuracy = project3_functions.evaluate(predictions, y_test)
print "Accuracy: {}".format(accuracy)


