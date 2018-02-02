def Get_Sequences(file_1, file_2):
	"""
	Reads sequences from the two input files

	Args:
		file_1: The name of the file containing the first sequence
		file_2: The name of the file containing the second sequence

	Returns:
		Returns the two sequences in a tuple of the form (str, str)

	"""
	pass
	
def Build_Scoring_Matrix(file_1):
	"""
	Builds the BLOSUM scoring matrix from the input file

	Args:
		file_1: The name of the file containing the BLOSUM matrix

	Returns:
		Returns a dictionary of the form BLOSUM_dict[(str, str)] = int

	"""
	pass
	
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
	pass