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
        self.tree = self._load_subtree(lines, 0)[0]

    """
    Load the subtree from the file, for example condition of subtree:
      TRUE -> b (basis level 0, conditions: TRUE/"", result: b)
    |- next node: TRUE -> c (next node level 1, conditions: TRUE/"", result: c)
    |  |- next node: ['a'] -> c (next node level 2, conditions: a, result: c)
    |  |  |- false node: ['c'] -> d (false node level 3, conditions: c, result: d)
    |  |  |  |- next node: ['b'] -> d (next node level 4, conditions: b, result: d)
    |  |  |  |- false node: ['d'] -> a (false node level 4, conditions: d, result: a)
    |  |  |  |  |- false node: TRUE -> a (false node level 5, conditions: TRUE/"", result a)
    |  |  |  |  |  |- next node: ['b'] -> e (false node level 6, conditions: b, result: e)
    """
    
  def _load_subtree(self, lines: list[str], index: int) -> tuple[Node, int]:
      # Extract the current line and determine the level of indentation
      current_line = lines[index].strip()
      prefix_level = len(lines[index]) - len(current_line)
      
      # Debug: print the current line and prefix level
      print(f"Parsing line: '{current_line}', Prefix level: {prefix_level}")
      
      # Extract conditions and result from the line
      rule_conditions_str, rule_result = current_line.split("->")
      rule_conditions_str = rule_conditions_str.strip()
      rule_result = rule_result.strip()
      
      # Debug: print extracted conditions and result
      print(f"Conditions: {rule_conditions_str}, Result: {rule_result}")
      
      # Parse the rule conditions
      if rule_conditions_str == "TRUE":
          rule_conditions = []
      else:
          # Convert conditions string to list
          try:
              rule_conditions = re.findall(r"'(.*?)'", rule_conditions_str)
              # Debug: print the parsed conditions
              print(f"Parsed conditions: {rule_conditions}")
          except Exception as e:
              print(f"Error parsing conditions: {e}")
              rule_conditions = []
      
      # Create the current node
      current_node = Node(rule_conditions, rule_result)
      print(f"Created Node with Conditions: {rule_conditions}, Result: {rule_result}")
      
      # Move to the next line
      index += 1
      
      # Parse child nodes
      while index < len(lines):
          next_line = lines[index].strip()
          prefix_count = len(lines[index]) - len(next_line)
          
          # Debug: print the next line and prefix count
          print(f"Parsing next line: '{next_line}', Prefix count: {prefix_count}")

          # If prefix count is 0, we have reached the same or higher level (end of current subtree)
          if prefix_count <= prefix_level:
              break

          # If prefix count is greater than the current prefix level, determine next node or false node
          if "next node:" in next_line:
              print(f"Parsing next node")
              current_node.next_node, index = self._load_subtree(lines, index)
          elif "false node:" in next_line:
              print(f"Parsing false node")
              current_node.false_node, index = self._load_subtree(lines, index)
          else:
              print(f"Line does not match expected 'next node' or 'false node', breaking")
              break

      # Debug: print the returning node
      print(f"Returning node with Conditions: {current_node.rule_conditions}, Result: {current_node.rule_result}")
      
      return current_node, index