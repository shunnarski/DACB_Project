import random
import math
from Data_Utils import Get_Data

def sigmoid_forward(x):
    return 1/(1+math.exp(-x))

def sigmoid_backward(x):
    return x*(1-x)

def _get_batches(X, Y, batch_size=32):
    data_combined = list(zip(X, Y))
    random.shuffle(data_combined)
    for i in range(0, len(X), batch_size):
        batch = data_combined[i:i+batch_size]
        batch_x, batch_y = zip(*batch)
        yield batch_x, batch_y
        
def get_batch(X, Y, batch_size=32):
    batch_indices = random.sample(range(len(X)), batch_size)
    batch_x = []
    batch_y = []
    index_counter = 0
    for index in batch_indices:
        batch_x.append(X[index])
        batch_y.append(Y[index])
    return batch_x, batch_y

def get_batch_index(indices, batch_size=32):
    batch_index = random.sample(indices, batch_size)
    return batch_index

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
        probs = self.predict(X)
        error = [a - p for a, p in zip(Y, probs)]
        grads = [sigmoid_backward(x) for x in probs]
        return error, grads
        
        
    def fit(self, X, Y, train_index, test_index, verbose=False):
        train_x, train_y = Get_Data(X, Y, train_index)
        test_x, test_y = Get_Data(X, Y, test_index)
        self._init_weights(len(X[0]))
        for t in range(self.max_iter):
            if verbose and t % 5 == 0:
                train_error, _ = self.loss(train_x, train_y)
                test_error, _ = self.loss(test_x, test_y)
                train_error = sum([math.pow(x, 2) for x in train_error])/float(len(train_index))
                test_error = sum([math.pow(x, 2) for x in test_error])/float(len(test_index))
                print "Training Data MSE: {}".format(train_error)
                print "Testinng Data MSE: {}".format(test_error)
                with open("loss.32.log", "a") as log_file:
                    log_file.write("{},{},{}\n".format(t,train_error, test_error))
            batch_index = get_batch_index(train_index, self.batch_size)
            batch_X, batch_Y = Get_Data(X, Y, batch_index)
            error, grads = self.loss(batch_X, batch_Y)
            weight_delta = [e*g for e, g in zip(error,grads)]
            weight_update = [0 for _ in range(len(batch_X[0]))]
            for i in range(len(batch_X[0])):
                for j in range(len(batch_X)):
                    weight_update[i] += batch_X[j][i]*weight_delta[j]
                self.weights[i] += self.learning_rate*(- self.reg_strength*self.weights[i] + weight_update[i]/float(len(batch_X)))

        if verbose:
            train_error, _ = self.loss(train_x, train_y)
            test_error, _ = self.loss(test_x, test_y)
            train_error = sum([math.pow(x, 2) for x in train_error])/float(len(train_index))
            test_error = sum([math.pow(x, 2) for x in test_error])/float(len(test_index))
            print "Training Data MSE: {}".format(train_error)
            print "Testinng Data MSE: {}".format(test_error)
            with open("loss.32.log", "a") as log_file:
               log_file.write("{},{},{}\n".format(t,train_error, test_error))                   
            

    def predict(self, X):
        predictions = []
        for x in X:
            prediction = 0
            for feature, weight in zip(x, self.weights):
                prediction += feature*weight
            predictions.append(sigmoid_forward(prediction))
        return predictions
            
    
    def _init_weights(self, num_weights):
        self.weights = [random.random()*1e-3 for _ in range(num_weights)]
    
    def save_weights(self, filename):
        with open(filename, "w") as weight_file:
            for weight in self.weights:
                weight_file.write("{}\n".format(weight))          
