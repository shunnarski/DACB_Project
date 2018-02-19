
def read_file(filename):
    """
    :param filename: Gets the sequences from the Proteins.fa and Proteins.sa files
    :return: A list of sequences of amino acids and their results in the files
    """
    pass


def split_data(acids, labels):
    """
    Split the data from the Proteins.sa/.fa files into training set data and test data.
    Training set data: ~75% of the total data
    Test set data: ~25% of the total data
    Make sure the two sets aren't overlapping and that the data is selected randomly without replacement
    :param acids: List of the acids from the Proteins.fa file
    :param labels: List of the labels from the Proteins.sa file in respect to the Proteins.fa file
    :return: A tuple containing the training set of data and the test data in the form (acid_train, acid_test,
    label_train, label_test)
    """
    pass

def build_feature_matrix():
    """

    :return: A matrix or vector containing all the features for all 20 amino acids
    """
    pass

def build_decision_tree(feature_matrix, training_data_acids, training_data_labels):
    """
    Based on the feature matrix, the training data, and information gain,
    build a decision tree that can accurately predict if an amino acid
    will be exposed(e) or buried(-)
    :param feature_matrix: feature matrix used to represent nodes in decision tree
    :param training_data_acids: The amino acids in the training data set
    :param training_data_labels: The labels in the training data set
    :return: A binary tree that represents a decision tree based on the given features
    """
    pass

def traverse_tree(decision_tree, test_data_acids, test_data_labels):
    """

    :param decision_tree: Decision tree built from build_decision_tree
    :param test_data_acids: Amino acids from test data set
    :param test_data_labels: The labels in the test data set
    :return: A list of the labels generated from traversing the decision tree
    """
    pass

def evaluate(test_data, results_data):
    """
    Use Precision, Recall, Accuracy, F-1 Score, and MCC to evaluate the accuracy of the decision tree
    and print their values
    :param test_data: test data set
    :param results_data: list of the labels generated in the traverse_tree method
    :return: void
    """
    pass