from random import sample, seed
from math import sqrt

def read_dataset(filename):
    X = []
    y = []
    with open(filename, "r") as data_file:
        for line in data_file:
            line = line.strip().split(",")
            y.append([line[0]])
            X.append([[int(x) for x in line[1:]]])
    return X, y

def read_file(filename):
    """
    :param filename: Gets the sequences from the Proteins.fa and Proteins.ss files
    :return: A list of sequences of amino acids and their results in the files
    """
    Data = []
    print "reading file {} ...".format(filename)
    with open(filename, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if len(line) == 0:
                continue
            if ">" not in line: 
                Data.append(list(line))

    return Data


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
    print "Calculating splits ..."
    # Initialize data
    seed(0)
    acid_train = []
    acid_test = []
    label_train = []
    label_test = []
    num_total = len(acids)

    # Determine test set indices
    test_indicies = sample(range(num_total), int(num_total*.5))

    # Split the data based on test indices
    for i in range(num_total):
        # Add to test set
        if i in test_indicies:
            acid_test.append(acids[i])
            label_test.append(labels[i])
        # Add to training set
        else:
            acid_train.append(acids[i])
            label_train.append(labels[i])

    return acid_train, acid_test, label_train, label_test


def extract_features(sequences, labels, num_instances):
    """
    Get PSSM values from a given set of sequences

    :param sequences: list of proten sequences
    :return: return the extracted features from the sequences
    """
    all_feature_vectors = []
    for i in range(num_instances):
        print i
        feature_vectors = []
        pssm = []
        pssm.append([-1 for _ in range(20)])
        pssm.append([-1 for _ in range(20)])
    
        with open("Data/pssm_files/{}.pssm".format(i), 'r') as pssm_file:
            start_read = False
            for line in pssm_file:
                if "Lambda" in line:
                    break
                line = line.strip()
                if line == "":
                    continue
                line = line.split()
                if line[0] == "1":
                    start_read = True
                if start_read:
                    scores = [int(x) for x in line[2:22]]
                    pssm.append(scores)
    
        pssm.append([-1 for _ in range(20)])
        pssm.append([-1 for _ in range(20)])
        for i in range(2,len(pssm)-2):
            features = []
            for j in range(i-2,i+3):
                features.extend(pssm[j])
            feature_vectors.append(features)
        all_feature_vectors.append(feature_vectors)
    
    return [all_feature_vectors, labels]


            

def evaluate(predictions, y):
    """
    Calculate Q3 Accuracy

    :param predictions: Predicted Labels
    :param y: Acutal Labels
    :return: Q3 Accuracy
    """

    print "Evaluating results ...\n"

    correct = 0.0
    num_total = float(len(y[0]))

    for pred, actual in zip(predictions, y[0]):
        if pred == actual:
            correct += 1.0
    return correct/num_total


def create_fasta_files(sequences):
    """
    Creates fasta files for a list of sequences to be analyzed with Blast

    :param sequences: list of protein sequences
    """
    for i in range(len(sequences)):
        with open("Data/fasta_files/{}.fa".format(i)) as fasta_file:
            fasta_file.write(">sequence {}\n".format(i))
            fasta_file.write("{}\n".format("".join(sequences[i])))

def generate_training_data_file(num_instances):
    """
    """
    Labels = read_file("Data/Proteins.ss")
    Data, _ = extract_features(None,None,num_instances)
    with open("protein_dataset.csv", "w") as ds_file:
        for data, labels in zip(Data, Labels):
            for instance, label in zip(data, labels):
                ds_file.write("{},{}\n".format(label,",".join([str(x) for x in instance])))

    
