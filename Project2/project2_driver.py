import project2_functions as p2f
import sys

if len(sys.argv) != 3:
    print "usage: project2_driver.py sequences_file_name labels_file_name"
    sys.exit()

amino_acids = p2f.read_file(sys.argv[1])
amino_labels = p2f.read_file(sys.argv[2])
amino_acids = p2f.extract_features(amino_acids)

acid_train, acid_test, label_train, label_test = p2f.split_data(amino_acids, amino_labels)


decision_tree = p2f.build_decision_tree(acid_train, label_train)

result_sequence = p2f.traverse_tree(decision_tree, acid_test, label_test)

p2f.evaluate(label_test, result_sequence)
