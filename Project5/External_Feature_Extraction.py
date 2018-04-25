import project2_functions as p2f
import sys
from ID3 import Deserialize_Tree


def Extract_Decision_Tree_Features(fasta_file):
    amino_acids = p2f.read_file(fasta_file)
    amino_acids, _ = p2f.extract_features(amino_acids)
    s_tree = Deserialize_Tree("Decision_Tree")

    result_sequence = p2f.traverse_tree(s_tree, amino_acids)

    exposed_count = 0
    buried_count = 0
    for i in result_sequence:
        if i == 'e':
            exposed_count += 1
        else:
            buried_count += 1

    result_length = len(result_sequence)
    exposed_percent = float(exposed_count) / result_length
    buried_percent = float(buried_count) / result_length

    project2_features = [exposed_percent, buried_percent]

    return project2_features



def Extract_GNB_Features(pssm_features):
    pass