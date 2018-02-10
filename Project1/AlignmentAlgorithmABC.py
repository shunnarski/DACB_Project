import abc

class AlignmentAlgorithmABC(abc.ABC):
  @abc.abstractproperty
  def match(self):
    pass

  @abc.abstractproperty
  def mismatch(self):
    pass

  @abc.abstractproperty
  def indel(self):
    pass

  # Returns a matrix appropriately initialized for the alg
  @abc.abstractmethod
  def build_matrix(self, cols, rows):
    pass

  # Smith-Waterman doesn't allow negative scores
  @abc.abstractmethod
  def normalize_score(self, scr):
    pass

  @abc.abstractmethod
  def traceback(self, scr_matrix, adj_matrix, s1, s2):
    pass