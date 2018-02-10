import utils as utils

# s1 and s2 arrays (1 index)
# 2d scr_matrix
# 2d adj_matrix

class Blosum62Alignment:
  def __init__(self, s1_filename, s2_filename, alg):
    self.s1 = [""] + utils.fasta_to_seq(s1_filename)
    self.s2 = [""] + utils.fasta_to_seq(s2_filename)
    print(self.s1)
    print(self.s2)
    self.alg = alg
    self.scr_matrix = self.__init_scr_matrix(self.s1, self.s2, self.alg)

  def __init_scr_matrix(s1, s2, alg):


Blosum62Alignment("mouse_hemoglobin_alpha.fasta.txt", "human_hemoglobin_alpha.fasta.txt", "")