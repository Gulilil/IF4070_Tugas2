from query import Query
from node import Node
import re

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
      print("Printing the RDR tree:")
      self.tree.print_subtree("")
      
  def save_tree(self, filename: str):
      if self.tree is None:
          print("Tree is empty")
      else:
          print(f"Saving tree to {filename}.txt")
          with open(filename + ".txt", "w") as file:
              self.tree.save_subtree(file)
              
  def load_tree(self, filename: str):
    print(f"\nLoading tree from {filename}.txt\n")
    with open(filename + ".txt", "r") as file:
        lines = file.readlines()  # Read all lines
        self.tree = self.load_subtree(lines, 0, len(lines), 0)

  def load_subtree(self, lines: list[str], start_index: int, end_index: int, depth: int) -> tuple[Node, int]:
    # Extract the current line and determine the level of indentation
    current_line = lines[start_index]

    # Remove unnecessary substr
    list_to_replace = ["|-", "|", "next node:", "false node:"]
    for str_to_replace in list_to_replace:
        current_line = current_line.replace(str_to_replace, "")
    current_line = current_line.strip()
    
    # Extract conditions and result from the line
    rule_conditions_str, rule_result = current_line.split("->")
    rule_conditions_str = rule_conditions_str.strip()
    rule_result = rule_result.strip()

    if rule_conditions_str == "TRUE":
        rule_conditions = []
    else:
        # Convert conditions string to list
        try:
            rule_conditions = re.findall(r"'(.*?)'", rule_conditions_str)
            # Debug: print the parsed conditions
        except Exception as e:
            rule_conditions = []

    current_node = Node(rule_conditions, rule_result)

    next_depth = depth + 1
    next_node_index_range = [None, None]
    false_node_index_range = [None, None]
  
    # Search for children node
    for i in range(start_index, end_index):
      line = lines[i]
      if (line.count("|") == next_depth):
          if ("next node:" in line):
            next_node_index_range[0] = i
          elif ("false node:" in line):
            false_node_index_range[0] = i

    if (next_node_index_range[0] is not None):
      next_node_index_range[1] = false_node_index_range[0] if (false_node_index_range[0] is not None) else end_index
      current_node.next_node = self.load_subtree(lines, next_node_index_range[0], next_node_index_range[1], next_depth)
    if (false_node_index_range[0] is not None):
      false_node_index_range[1] = end_index 
      current_node.false_node = self.load_subtree(lines, false_node_index_range[0], false_node_index_range[1], next_depth)
    
    return current_node

      

