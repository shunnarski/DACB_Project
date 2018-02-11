import utils as utils

class NeedlemanWunsch:

  # assume strings of sequences
  def __init__(self, s1, s2, match):
    self.s1 = [""] + list(s1)
    self.s2 = [""] + list(s2)
    self.match = match[0]
    self.mismatch = match[1]
    self.indel = match[2]
    self.adj_matrix = utils.init_matrix(len(self.s1), len(self.s2))
    self.scr_matrix = self.build_scr_matrix()
    # utils.print_2d(self.scr_matrix)
    # print()
    # utils.print_2d(self.adj_matrix)

  @classmethod
  def fromfilenames(self, s1_filename, s2_filename, match):
    NeedlemanWunsch(utils.fasta_to_seq(s1_filename), utils.fasta_to_seq(s2_filename), match)

  def score(self):
    return self.scr_matrix[len(self.s2)-1][len(self.s1)-1]

  def build_scr_matrix(self):
    w = len(self.s1)
    h = len(self.s2)
    m = utils.init_matrix(w, h)
    for col in range(w-1):
      m[0][col+1] = (col+1)*self.indel
    for row in range(h-1):
      m[row+1][0] = (row+1)*self.indel


    for row in range(h-1):
      for col in range(w-1):
        match = self.match if self.s1[col+1] == self.s2[row+1] else self.mismatch
        fromtopleft = m[row][col]+match
        fromtop = self.indel+m[row][col+1]
        fromleft = self.indel+m[row+1][col]
        max_val = max(fromtopleft, fromtop, fromleft)
        m[row+1][col+1] = max_val

        if fromtopleft == max_val:
          self.adj_matrix[row+1][col+1] = "D"
        if fromtop == max_val:
          self.adj_matrix[row+1][col+1] = "V"
        if fromleft == max_val:
          self.adj_matrix[row+1][col+1] = "H"

    return m


  def traceback(self):
    ss1 = ""
    ss2 = ""
    row = len(self.s2)-1
    col = len(self.s1)-1
    while row > 0 or col > 0:
      # print(row, col)
      if row > 0 and col > 0 and self.adj_matrix[row][col] == "D":
        ss1 = self.s1[col] + ss1
        ss2 = self.s2[row] + ss2
        row = row-1
        col = col-1
      elif col > 0 and self.adj_matrix[row][col] == "H":
        ss1 = self.s1[col] + ss1
        ss2 = "-" + ss2
        col = col-1
      else:
        ss1 = "-" + ss1
        ss2 = self.s2[row] + ss2
        row = row-1
    # print(ss1, ss2)
    return ss1, ss2





nw = NeedlemanWunsch("CAAGAC", "GAAC",(1, -1, -1))
nw.traceback()
print(nw.score())
# print(nw.match, nw.mismatch, nw.indel)
# m = nw.build_matrix("GCATGCU"), list(" GATTACA"))
# utils.print_2d(nw.build_scr_matrix())
# utils.print_2d(nw.adj_matrix)