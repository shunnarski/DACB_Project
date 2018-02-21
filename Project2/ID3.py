from Tree import Node
import math

def ID3(Attributes, X, Y):

    # Handle base cases
    num_positive, num_negative = Calculate_Proportions(Y)
    # All labels are positive
    if num_positive == len(Y):
        return Node(label='e')
    # All labels are negative
    elif num_negative == len(Y):
        return Node(label='-')
    # No attributes left to test (Choose the most common label amongst the remaining examples)
    if len(Attributes) == 0:
        if num_positive > num_negative:
            return Node(label='e')
        else:
            return Node(label='-')

    # Determine the best attribute
    max_gain = 0
    max_attribute = 0
    max_index = 0
    max_positive_split = []
    max_negative_split = []
    gains = []
    for i in range(len(Attributes)):
        gain, positive_split, negative_split = Gain(Attributes[i], X, Y)
        gains.append(gain)
        if gain > max_gain:
            max_gain = gain
            max_attribute = Attributes[i]
            max_index = i
            max_positive_split = positive_split
            max_negative_split = negative_split

    
    # Remove the attribute from the list of attributes (Attrubutes - {A})
    Attributes = Attributes[:max_index] + Attributes[max_index+1:]

    # Set Attribute of the decision node to the one with the max gain
    current_node = Node(attribute=max_attribute)

    if len(positive_split[0]) > 0:
        current_node.Positive_Branch = ID3(Attributes, positive_split[0], positive_split[1])
    else:
        num_positive, num_negative = Calculate_Proportions(positive_split[1])
        if num_positive >= num_negative:
            current_node.Positive_Branch = Node(label='e')
        else:
            current_node.Positive_Branch = Node(label='-')

    if len(negative_split[0]) > 0:
        current_node.Negative_Branch = ID3(Attributes, negative_split[0], negative_split[1])
    else:
        num_positive, num_negative = Calculate_Proportions(negative_split[1])
        if num_positive >= num_negative:
            current_node.Negative_Branch = Node(label='e')
        else:
            current_node.Negative_Branch = Node(label='-')
    return current_node

def H(proportion_pos, proportion_neg):
    if proportion_pos == 0 or proportion_pos == 1:
        return 0
    return -(proportion_pos*math.log(proportion_pos, 2)) - (proportion_neg*math.log(proportion_neg, 2))

def Attribute_Split(Attribute, X, Y):
    """
    """
    # Initialize variables
    positive_X = []
    negative_X = []
    positive_Y = []
    negative_Y = []
    split1_num_pos = 0
    split1_num_total = 0
    split2_num_pos = 0
    split2_num_total = 0

    for i in range(len(X)):
        # The attribute is positive so place it in the positive split
        if X[i][Attribute] == 1:
            positive_X.append(X[i])
            positive_Y.append(Y[i])
            # Calculating the proportion positive in the positive attribute split
            if Y[i] == 'e':
                split1_num_pos += 1
            split1_num_total += 1
        # The attribute is negative so place it in the negative split
        else:
            negative_X.append(X[i])
            negative_Y.append(Y[i])
            # Calculating the proportion positive in the negative attribute split
            if Y[i] == 'e':
                split2_num_pos += 1
            split2_num_total += 1
    # Calculate the proportions
    split1_proportion_pos = 0
    split2_proportion_pos = 0
    if split1_num_total > 0:
        split1_proportion_pos = split1_num_pos/float(split1_num_total)
    if split2_num_total > 0:
        split2_proportion_pos = split2_num_pos/float(split2_num_total)

    return (positive_X, positive_Y), (negative_X, negative_Y), (split1_proportion_pos, split2_proportion_pos)

def Gain(Attribute, X, Y):
    pos_split, neg_split, proportions = Attribute_Split(Attribute, X, Y)
    num_pos_examples = len(pos_split[0])
    num_neg_examples = len(neg_split[0])
    pos_split_weight = num_pos_examples/float(num_pos_examples + num_neg_examples)
    neg_split_weight = num_neg_examples/float(num_pos_examples + num_neg_examples)
    num_total_examples = num_pos_examples + num_neg_examples
    num_pos_labels, num_neg_labels = Calculate_Proportions(Y)
    proportion_pos_labels = num_pos_labels/float(num_pos_labels + num_neg_labels)
    gain = H(proportion_pos_labels, 1 - proportion_pos_labels) - (pos_split_weight*H(proportions[0], 1 - proportions[0]) + neg_split_weight*H(proportions[1], 1 - proportions[1]))
    return gain, pos_split, neg_split

def Calculate_Proportions(Y):
    num_positive = 0
    num_negative = 0
    for label in Y:
        if label == "e":
            num_positive += 1
        else:
            num_negative += 1
    return num_positive, num_negative
