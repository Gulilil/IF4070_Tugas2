from query import Query
from node import Node
from rdr import RDR
import random

WORD_POOL_FEW = [   
    "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india",
    "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo"]
WORD_POOL = [
    "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india",
    "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo",
    "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu",
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "iguana", "jaguar", "koala", "lemur", "mongoose", "narwhal", "octopus", "penguin",
    "quokka", "raven", "sparrow", "turtle", "umbrella", "vulture"
]

# Function to create queries matching the patterns
def generate_queries(list_of_word: list = WORD_POOL, type :str = 'ask'):
    queries = []
    for _ in range(100): 
        if (type == 'ask' or type == 'mix'):
          # Matching the 'ask_pattern'
          ask_words = random.sample(list_of_word, random.randint(1, 4))  # Select 1-4 words
          query_ask = ', '.join(ask_words) + '?'
          queries.append(query_ask)
          

        elif (type == 'add' or type == 'mix'):
          # Matching the 'add_pattern'
          add_words = random.sample(list_of_word, random.randint(0, 3))  # Select 1-3 words
          result_word = random.choice(list_of_word)
          query_add = ', '.join(add_words) + ' > ' + result_word
          queries.append(query_add)

    return queries

if __name__ == "__main__":

  # Test Load from file
  # rdr = RDR()
  # rdr.load_tree('rdr_tree')
  # rdr.tree.print_subtree()

  # Test from random query generation
  rdr = RDR()
  queries = generate_queries(WORD_POOL_FEW, "add")
  for query in queries:
    rdr.execute_query(Query(query))

  rdr.save_tree("random_query_tree")
  rdr.load_tree("random_query_tree")
  rdr.save_tree("random_query_tree_check") # Print lagi biar bisa check

  queries_ask = generate_queries(WORD_POOL_FEW, 'mix')
  for query in queries_ask:
    result = rdr.execute_query(Query(query))
    print(f"{query} -> {result}")

  


