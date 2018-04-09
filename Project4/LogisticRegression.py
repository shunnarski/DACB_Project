import random
import math

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
    for x, y in zip(X, Y):
        if index_counter in batch_indices:
            batch_x.append(x)
            batch_y.append(y)
        if len(batch_x) == batch_size:
            break
        index_counter += 1
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
        probs = self.predict(X)
        error = [a - p for a, p in zip(Y, probs)]
        grads = [sigmoid_backward(x) for x in probs]
        return error, grads
        
        
    def fit(self, X, Y, X_test=None, Y_test=None, verbose=False):
        self._init_weights(len(X))
        for t in range(self.max_iter):
            if verbose:
                train_error, _ = self.loss(X, Y)
                test_error, _ = self.loss(X_test, Y_test)
                train_error = sum([math.pow(x, 2) for x in train_error])/float(len(X))
                test_error = sum([math.pow(x, 2) for x in test_error])/float(len(X_test))
                print "Training Data MSE: {}".format(train_error)
                print "Testinng Data MSE: {}".format(test_error)
                with open("loss.32.log", "a") as log_file:
                    log_file.write("{},{},{}\n".format(t,train_error, test_error))
            batch_X, batch_Y = get_batch(X, Y, self.batch_size)
            error, grads = self.loss(batch_X, batch_Y)
            weight_delta = [e*g for e, g in zip(error,grads)]
            weight_update = [0 for _ in range(len(batch_X[0]))]
            for i in range(len(batch_X[0])):
                for j in range(len(batch_X)):
                    weight_update[i] += batch_X[j][i]*weight_delta[j]
                self.weights[i] += self.learning_rate*(- self.reg_strength*self.weights[i] + weight_update[i]/float(len(batch_X)))

        if verbose:
            train_error, _ = self.loss(X, Y)
            test_error, _ = self.loss(X_test, Y_test)
            train_error = sum([math.pow(x, 2) for x in train_error])/float(len(X))
            test_error = sum([math.pow(x, 2) for x in test_error])/float(len(X_test))
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
        self.weights = [random.random()*math.sqrt(2.0/num_weights) for _ in range(num_weights)]            
