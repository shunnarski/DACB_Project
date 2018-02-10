import abc
from AlignmentAlgorithmABC import AlignmentAlgorithmABC

class AlignmentAlgorithm(AlignmentAlgorithmABC):
  def __init__(self, match, mismatch, indel):
    self.match = match
    self.mismatch = mismatch
    self.indel = indel

  def match(self):
    return self.match

  def mismatch(self):
    return self.mismatch

  def indel(self):
    return self.indel