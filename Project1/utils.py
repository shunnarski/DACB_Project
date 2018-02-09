# Parses a fasta file and returns an array of its sequence
def fasta_to_seq(filename):
  f = open(filename, "r")
  l = [str.strip() for str in f.readlines()[1:]]
  seq = list("".join(l))
  f.close()
  return seq