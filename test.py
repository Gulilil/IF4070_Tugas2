from query import Query
from node import Node
from rdr import RDR

if __name__ == "__main__":

  tests = [
    "word1, word2? ",
    "123, test_1? aaa",
    "hello?",
    "one, two, three?",
    "word1, word2 > result",
    "123, test_1 > final_output",
    "hello world > goodbye",
    " , hehe > hasil",
    ' > hasil 2',
    " ? ",
    'hehe'
  ]
  
  for test in tests:
    q = Query(test)
    q.display()
