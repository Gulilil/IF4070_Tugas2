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
      result = None
      result = self.get_result(query)
      return None
    
    else: # query.type == "add"
      self.add_node(query)
    
  def add_node(self, query: Query):
    conditions = query.conditions
    result = query.result
    new_node = Node(conditions, result)

    # TO DO
    # recursive to add node
    # terminate/ base condition => (node.check_rule() and node.next_node is None) or (not node.check_rule() and node.false_node is None)


  def get_result(self, query: Query) -> str | None :
    conditions = query.conditions

    # TO DO 
    # recursive to return 
    # terminate/ base condition => (node.check_rule() and node.next_node is None) or (not node.check_rule() and node.false_node is None)
    # only update the return result if not None
    # if true -> get node.rule_result as result and then traverse to node.next_node
    # else -> traverse to node.false_node
    


