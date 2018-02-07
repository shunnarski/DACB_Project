def Get_Sequences(file_1, file_2):
    """
	Reads sequences from the two input files

	Args:
		file_1: The name of the file containing the first sequence
		file_2: The name of the file containing the second sequence

	Returns:
		Returns the two sequences in a tuple of the form (str, str)

	"""

    file1 = open(file_1, "r")
    file2 = open(file_2, "r")

    # get only the sequence letters, initially this will be a list of different sets
    # of letters due to the line breaks in the .txt file
    with file1 as f:
        human = f.read().splitlines()[1::]

    with file2 as f:
        mouse = f.read().splitlines()[1::]

    file1.close()
    file2.close()

    # concatenate the strings of hemoglobin codes to one sequence
    human_sequence = ""
    mouse_sequence = ""

    for s in human:
        human_sequence += s

    for s in mouse:
        mouse_sequence += s

    # set the human and mouse sequences to a tuple called sequences
    sequences = (human_sequence, mouse_sequence)

    # return the tuple of sequences
    return sequences


def Build_Scoring_Matrix(file_1):
    """
	Builds the BLOSUM scoring matrix from the input file

	Args:
		file_1: The name of the file containing the BLOSUM matrix

	Returns:
		Returns a dictionary of the form BLOSUM_dict[(str, str)] = int

	"""
    """
    1. Create list of proteins in matrix in order
    2. Extract BLOSUM62 values in the matrix into a 2x2 int array
    3. Assign a tuple to each value in the matrix in a dictionary
    4. Return the dictionary
    """
    # list of proteins used in the BLOSUM62 matrix
    proteins = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y',
                'V', 'B', 'Z', 'X', '*']

    file = open(file_1, "r")
    with file as f:
        m = f.read().splitlines()[7::]

    file.close()
    # reformat the matrix
    for x in range(len(m)):
        m[x] = m[x].split()[1::]

    # dimensions of blosum62 matrix
    dim = len(proteins)

    # create dictionary we're returning with appropriate key-value pairs
    blosum_dict = {}
    for row in range(dim):
        for column in range(dim):
            tup = (proteins[row], proteins[column])
            val = int(m[row][column])
            blosum_dict[tup] = val

    return blosum_dict


def Smith_Waterman(sequence_1, sequence_2, scoring_matrix):
    """
	Smith-Waterman algorithm

	Args:
		sequence_1: The first sequence
		sequence_2: The second sequence
		scoring_matrix: The matrix to determine the score of alignments

	Returns:
		Returns the two aligned sequences and the score in a tuple of the form (str, str, int)
	"""
    pass


def Needlman_Wunsch(sequence_1, sequence_2, scoring_matrix):
    """
	Needlman-Wunsch algorithm

	Args:
		sequence_1: The first sequence
		sequence_2: The second sequence
		scoring_matrix: The matrix to determine the score of alignments

	Returns:
		Returns the two aligned sequences and the score in a tuple of the form (int, str, str)
	"""
    pass


def Output_Sequences(sequence_1, sequence_2, score):
    """
	Prints (or writes to a file?) the score and two aligned sequences in the format specifed by the project documentation

	Args:
		sequence_1: The first aligned sequence
		sequence_2: The second aligned sequence
		score: the score of the aligned sequences

	"""
    print "Score: %d" % (score)
    print sequence_1
    result = ""
    for c in range(len(sequence_1)):
        if sequence_1[c] == sequence_2[c]:
            result += "|"
        elif sequence_1[c] == "-" or sequence_2[c] == "-":
            result += " "
        else:
            result += "*"
    print result
    print sequence_2
