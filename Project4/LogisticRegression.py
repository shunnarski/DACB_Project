import random
import math

class LogisticRegression:

    def __init__(self, num_weights=201):
        self._init_weights(num_weights)

    def fit(self, X, Y):
        self._init_weights(len(X))

    def predict(self, X):
        predictions = []
        for x in X:
            prediction = 0
            for feature, weight in zip(x, self.weights):
                prediction += feature*weight
            predictions.append(prediction)
        return predictions
            
    
    def _init_weights(self, num_weights):
        self.weights = [random.random()*math.sqrt(2.0/num_weights) for _ in range(num_weights)]            
