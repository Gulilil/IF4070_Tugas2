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
      return self.get_result(query)
    
    else: # query.type == "add"
      self.add_rule(query)
    
  def add_rule(self, query: Query):
    conditions = query.conditions
    result = query.result

    if self.tree is None:
      self.tree = Node(conditions, result)
    else:
      self.tree.add_node(conditions, result)

  def get_result(self, query: Query) -> str | None :
    conditions = query.conditions
    result = "Not mapped"

    if self.tree is None:
      print("Tree is empty")
    else:
      result = self.tree.get_final_result(conditions, result)
    return result

  def print_tree(self):
    if self.tree is None:
      print("Tree is empty")
    else:
      self.tree.print_subtree("")