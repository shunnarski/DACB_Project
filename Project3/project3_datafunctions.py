import os
from subprocess import call

def extract_features(X):
    fasta_dir = "Data/tmp/fasta_files"
    pssm_dir = "Data/tmp/pssm_files"
    call(["mkdir", fasta_dir])
    call(["mkdir", pssm_dir])
    create_fasta_files(X, fasta_dir)
    create_pssm_files(fasta_dir)
    X =  extract_features_dataset(pssm_dir, len(X))
    call(["rm -r", "Data/tmp"])
    return X


def create_fasta_files(sequences, fasta_dir):
    """
    Creates fasta files for a list of sequences to be analyzed with Blast

    :param sequences: list of protein sequences
    """
    for i in range(len(sequences)):
        with open("{}/{}.fa".format(fasta_dir, i), "w") as fasta_file:
            fasta_file.write(">sequence {}\n".format(i))
            fasta_file.write("{}\n".format("".join(sequences[i])))

def create_pssm_files(fasta_dir):
    for filename in os.listdir(fasta_dir):
        pssm_filename = filename[:-3] + ".pssm"
        call(["blast/bin", "-d", "nr/nr", "-j", "3"
              "-b", "1", "-a", "4", "-i", filename,
              "-Q", pssm_filename])


def generate_training_data_file(num_instances):
    """
    Generates the compiled dataset form the .fa and corresponding .pssm files. 

    :param num_instances: the number of sequences to use for the training data file
    """
    Labels = read_file("Data/Proteins.ss")
    Data = extract_features_dataset("Data/pssm_files", num_instances)
    with open("protein_dataset.csv", "w") as ds_file:
        for data, labels in zip(Data, Labels):
            for instance, label in zip(data, labels):
                ds_file.write("{},{}\n".format(label,",".join([str(x) for x in instance])))


def extract_features_dataset(pssm_dir, num_instances):
    """
    Helper function for generating the dataset file

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
    
        with open("{}/{}.pssm".format(pssm_dir, i), 'r') as pssm_file: # "Data/pssm_files"
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
    
    return all_feature_vectors

def read_dataset(filename):
    """
    Reads training data from the dataset file

    :param filename: filename of datast file
    :return: the feature vectors and labels
    """
    X = []
    y = []
    with open(filename, "r") as data_file:
        for line in data_file:
            line = line.strip().split(",")
            y.append([line[0]])
            X.append([[int(x) for x in line[1:]]])
    return X, y