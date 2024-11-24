from query import Query
from node import Node
from rdr import RDR

if __name__ == "__main__":

  tests = [
    "word1, word2? ",
    "hello?",
    "one, two, three?",
    "word1, word2 > result",
    "123, test_1 > final_output",
    "hello world > goodbye",
    " , hehe > hasil",
    ' > hasil 2'
  ]
  
  for test in tests:
    q = Query(test)
    q.display()

  # rdr = RDR()
  # rdr.load_tree('rdr_tree')
  # rdr.tree.print_subtree()