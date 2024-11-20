from query import Query
from node import Node

class RDR:
  tree : Node | None

  def __init__ (self):
    self.tree = None

  def execute_query(self, query: Query) -> str | None:
    # Additional handling
    if (not query.is_valid()):
      print(f"[ERROR] Cannot execute invalid query")
      return None
    
    if (query.type == "ask"):
      # TO DO
      return
    else: # query.type == "add"
      # TO DO 
      return None # add does not return anything
