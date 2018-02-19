
import project2_functions as p2f

amino_acids = p2f.read_file("Proteins.fa")
amino_labels = p2f.read_file("Proteins.sa")

acid_train, acid_test, label_train, label_test = p2f.split_data(amino_acids, amino_labels)

feature_matrix = p2f.build_feature_matrix()

decision_tree = p2f.build_decision_tree(feature_matrix, acid_train, label_train)

result_sequence = p2f.traverse_tree(decision_tree, acid_test, label_test)

p2f.evaluate(label_test, result_sequence)
