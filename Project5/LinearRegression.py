import random
import math
from Data_Utils import Get_Data
        
def get_batch(X, Y, batch_size=32):
    batch_indices = random.sample(range(len(X)), batch_size)
    batch_x = []
    batch_y = []
    index_counter = 0
    for index in batch_indices:
        batch_x.append(X[index])
        batch_y.append(Y[index])
    return batch_x, batch_y

class LogisticRegression:

    def __init__(self, num_weights=201, max_iter=200, batch_size=64,
                    learning_rate=1e-3, reg_strength=1e-4, convergence_threshold=1e-4):
        self._init_weights(num_weights)
        self.max_iter = max_iter
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.reg_strength = reg_strength
        self.convergence_threshold = convergence_threshold
    
    def loss(self, X, Y):
        predictions = self.predict(X)
        error = [actual - predicted for actual, predicted in zip(Y, predictions)]
        return error
        
        
    def fit(self, X, Y, verbose=False, log_filename="test.log"):
        self._init_weights(len(X[0]))
        acc_train_error = 0
        for t in range(self.max_iter):
            if verbose and t % 5 == 0 and t != 0:
                avg_train_error = acc_train_error/(self.batch_size*5.0)
                acc_train_error = 0
                print "Train Error: {}".format(avg_train_error)
                with open(log_filename, "a") as log_file:
                    log_file.write("{},{}\n".format(t,avg_train_error))

            batch_X, batch_Y = get_batch(X, Y, batch_index)

            error = self.loss(batch_X, batch_Y)

            acc_train_error += sum([e**2 for e in error])

            
            for i in range(len(batch_X[0])):
                weight_update = 0
                for j in range(len(batch_X)):
                    weight_update += batch_X[j][i]*error[j]
                weight_update /= float(len(batch_X))
                self.weights[i] -= self.learning_rate*(2*weight_update[i]) - 2*self.reg_strength*self.weights[i])

        if verbose:
            avg_train_error = acc_train_error/(self.batch_size*5.0)
            acc_train_error = 0
            print "Train Error: {}".format(avg_train_error)
            with open(log_filename, "a") as log_file:
                log_file.write("{},{}\n".format(t,avg_train_error))

                 
            

    def predict(self, X):
        predictions = []
        for x in X:
            prediction = 0
            for feature, weight in zip(x, self.weights):
                prediction += feature*weight
            predictions.append(prediction)
        return predictions
            
    
    def _init_weights(self, num_weights):
        self.weights = [random.random()*1e-3 for _ in range(num_weights)]
    
    def save_weights(self, filename):
        with open(filename, "w") as weight_file:
            for weight in self.weights:
                weight_file.write("{}\n".format(weight))          
