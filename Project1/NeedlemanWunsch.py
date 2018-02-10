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
    # self.adj_matrix[len(s2)][len(s1)] = 1 #temp, might start from the end later
    self.scr_matrix = self.build_scr_matrix()
    utils.print_2d(self.scr_matrix)
    print()
    utils.print_2d(self.adj_matrix)

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

  # def traceback(self):
  #   (score, s1, s2) = self.traceback0(self.s1, self.s2, self.adj_matrix, self.scr_matrix, 0, "", "", 0, 0)
  #   print("FINAL", score, s1, s2)

  # def traceback0(self, s1, s2, adj_matrix, scr_matrix, score, ss1, ss2, row, col):
  #   print(score, ss1, ss2)
  #   if len(ss1) > len(s1)-1 or len(ss2) > len(s2)-1:
  #     return (-999999, ss1, ss2)
  #   if row == len(s2)-1 and col == len(s1)-1:
  #     return (score, ss1, ss2)
  #   # if row > len(s2)-1 or col > len(s1)-1:
  #   #   return (-999999, ss1, ss2)
  #   # EDIT: change to "if nowhere to go in adj_matrix"
  #   # if adj_matrix[row+1][col] < 1 and adj_matrix[row][col+1] < 1 and adj_matrix[row+1][col+1] < 1:
  #   #   return (-999999, ss1, ss2)

  #   # new_score = score + scr_matrix[row][col]

  #   if col+1 <= len(s1)-1 and adj_matrix[row][col+1] > 0:
  #     (r_score, r_ss1, r_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, score+scr_matrix[row][col+1], ss1+s1[col+1], ss2+"-", row, col+1)
  #   else:
  #     r_score, r_ss1, r_ss2 = -999999, ss1, ss2
  #   if row+1 <= len(s2)-1 and adj_matrix[row+1][col] > 0:
  #     (b_score, b_ss1, b_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, score+scr_matrix[row+1][col], ss1+"-", ss2+s2[row+1], row+1, col)
  #   else:
  #     b_score, b_ss1, b_ss2 = -999999, ss1, ss2
  #   if col+1 <= len(s1)-1 and row+1 <= len(s2)-1 and adj_matrix[row+1][col+1] > 0:
  #     (br_score, br_ss1, br_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, score+scr_matrix[row+1][col+1], ss1+s1[col+1], ss2+s2[row+1], row+1, col+1)
  #   else:
  #     br_score, br_ss1, br_ss2 = -999999, ss1, ss2

  #   # (r_score, r_ss1, r_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, new_score, ss1+s1[col+1], ss2+"-", row, col+1) if col+1 < len(s1) and adj_matrix[row][col+1] > 0 else (-999999, ss1, ss2)
  #   # (b_score, b_ss1, b_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, new_score, ss1+"-", ss2+s2[row+1], row+1, col) if row+1 < len(s2) and adj_matrix[row+1][col] > 0 else (-999999, ss1, ss2)
  #   # (br_score, br_ss1, br_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, new_score, ss1+s1[col+1], ss2+s2[row+1], row+1, col+1) if col+1 < len(s1) and row+1 < len(s2) and adj_matrix[row+1][col+1] > 0 else (-999999, ss1, ss2)

  #   max_val = max(r_score, b_score, br_score)
  #   if r_score == max_val:
  #     return (r_score, r_ss1, r_ss2)
  #   elif b_score == max_val:
  #     return (b_score, b_ss1, b_ss2)
  #   else:
  #     return (br_score, br_ss1, br_ss2)





  # def traceback(self):
  #   (score, ss1, ss2) = self.traceback0(self.s1, self.s2, self.adj_matrix, self.scr_matrix, 0, "", "", len(self.s2)-1, len(self.s1)-1, 0)
  #   print("FINAL", score, ss1, ss2)

  # def traceback0(self, s1, s2, adj_matrix, scr_matrix, score, ss1, ss2, row, col, depth):
  #   print(score, ss1, ss2)
  #   # if depth >
  #   if row == 0 and col == 0 and depth == max():
  #     return (score, ss1, ss2)









  #   if len(ss1) > len(s1)-1 or len(ss2) > len(s2)-1:
  #     return (-999999, ss1, ss2)
  #   if row == len(s2)-1 and col == len(s1)-1:
  #     return (score, ss1, ss2)
  #   # if row > len(s2)-1 or col > len(s1)-1:
  #   #   return (-999999, ss1, ss2)
  #   # EDIT: change to "if nowhere to go in adj_matrix"
  #   # if adj_matrix[row+1][col] < 1 and adj_matrix[row][col+1] < 1 and adj_matrix[row+1][col+1] < 1:
  #   #   return (-999999, ss1, ss2)

  #   # new_score = score + scr_matrix[row][col]

  #   if col+1 <= len(s1)-1 and adj_matrix[row][col+1] > 0:
  #     (r_score, r_ss1, r_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, score+scr_matrix[row][col+1], ss1+s1[col+1], ss2+"-", row, col+1)
  #   else:
  #     r_score, r_ss1, r_ss2 = -999999, ss1, ss2
  #   if row+1 <= len(s2)-1 and adj_matrix[row+1][col] > 0:
  #     (b_score, b_ss1, b_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, score+scr_matrix[row+1][col], ss1+"-", ss2+s2[row+1], row+1, col)
  #   else:
  #     b_score, b_ss1, b_ss2 = -999999, ss1, ss2
  #   if col+1 <= len(s1)-1 and row+1 <= len(s2)-1 and adj_matrix[row+1][col+1] > 0:
  #     (br_score, br_ss1, br_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, score+scr_matrix[row+1][col+1], ss1+s1[col+1], ss2+s2[row+1], row+1, col+1)
  #   else:
  #     br_score, br_ss1, br_ss2 = -999999, ss1, ss2

  #   # (r_score, r_ss1, r_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, new_score, ss1+s1[col+1], ss2+"-", row, col+1) if col+1 < len(s1) and adj_matrix[row][col+1] > 0 else (-999999, ss1, ss2)
  #   # (b_score, b_ss1, b_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, new_score, ss1+"-", ss2+s2[row+1], row+1, col) if row+1 < len(s2) and adj_matrix[row+1][col] > 0 else (-999999, ss1, ss2)
  #   # (br_score, br_ss1, br_ss2) = self.traceback0(s1, s2, adj_matrix, scr_matrix, new_score, ss1+s1[col+1], ss2+s2[row+1], row+1, col+1) if col+1 < len(s1) and row+1 < len(s2) and adj_matrix[row+1][col+1] > 0 else (-999999, ss1, ss2)

  #   max_val = max(r_score, b_score, br_score)
  #   if r_score == max_val:
  #     return (r_score, r_ss1, r_ss2)
  #   elif b_score == max_val:
  #     return (b_score, b_ss1, b_ss2)
  #   else:
  #     return (br_score, br_ss1, br_ss2)







  def traceback(self):
    ss1 = ""
    ss2 = ""
    row = len(self.s2)-1
    col = len(self.s1)-1
    while row > 0 or col > 0:
      print(row, col)
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
    print(ss1, ss2)





nw = NeedlemanWunsch("CAAGAC", "GAAC",(1, -1, -2))
nw.traceback()
print(nw.score())
# print(nw.match, nw.mismatch, nw.indel)
# m = nw.build_matrix("GCATGCU"), list(" GATTACA"))
# utils.print_2d(nw.build_scr_matrix())
# utils.print_2d(nw.adj_matrix)