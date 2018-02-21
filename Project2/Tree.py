class Node:
    """
    Args:
        attribute (int): Index of the attribute to be test. (None if this is a leaf node)
        label (int): Label of leaf node. (None if this is a decision node)

    Attributes:
        Attribute (int): Index of the attribute to be test. (None if this is a leaf node)
        Label (int): Label of leaf node. (None if this is a decision node)
        Positive_Branch (Node): The branch taken if the instance's attribute being tested is positive.
        Negative_Branch (Node): The branch taken if the instance's attribute being tested is negative.

    """
    def __init__(self, attribute=None, label=None):
        self.Attribute = attribute
        self.Label = label
        self.Positive_Branch = None
        self.Negative_Branch = None

def Display_Tree(root_node):
    tree_dict = {}
    queue = []
    queue.append((root_node,0))
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node[0].Attribute != None:
            if current_node[1] in tree_dict:
                tree_dict[current_node[1]] += str(current_node[0].Attribute)
            else:
                tree_dict[current_node[1]] = str(current_node[0].Attribute)
        if current_node[0].Label != None:
            if current_node[1] in tree_dict:
                tree_dict[current_node[1]] += str(current_node[0].Label)
            else:
                tree_dict[current_node[1]] = str(current_node[0].Label)
        if current_node[0].Positive_Branch != None:
            queue.append((current_node[0].Positive_Branch,current_node[1]+1))
        if current_node[0].Negative_Branch != None:
            queue.append((current_node[0].Negative_Branch,current_node[1]+1))

    for key in tree_dict:
        print "{}\n".format(tree_dict[key])
        