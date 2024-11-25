from query import Query
from node import Node
import os
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
      
  def save_txt_tree(self, filename: str):
      if self.tree is None:
          print("Tree is empty")
      else:
          print(f"Saving tree to {filename}.txt")
          with open(f"../test/txt/{filename}.txt", "w") as file:
              self.tree.save_subtree(file)
              
  def load_txt_tree(self):
    file_name = input("Enter the file name to load: ").strip()
    
    # Construct the full path to the text file in the 'test/txt' directory
    file_path = os.path.join('../test/txt', file_name + ".txt")
        
    # Check if the file exists
    while not os.path.exists(file_path):
        print(f"[ERROR] File {file_path} not found")
        file_name = input("Enter the file name: ").strip()
        file_path = os.path.join('../test/txt', file_name + ".txt")

    print(f"\nLoading tree from {file_path}\n")
        
    # Open the file and process it
    with open(file_path, "r") as file:
      lines = file.readlines()  # Read all lines
      self.tree = self.load_txt_subtree(lines, 0, len(lines), 0)
  
  
    
  def load_txt_subtree(self, lines: list[str], start_index: int, end_index: int, depth: int) -> tuple[Node, int]:

    # Extract the current line and determine the level of indentation
    current_line = lines[start_index]

    # Remove unnecessary substr
    list_to_replace = ["|-", "|", "true node:", "false node:"]
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
    true_node_index_range = [None, None]
    false_node_index_range = [None, None]

    def count_before_character(s, char):
      if char in s:
          return s.index(char)
      else:
          return 0 
      
    # Search for children node
    for i in range(start_index, end_index):
      line = lines[i]
      if (count_before_character(line, "-")//3 == next_depth):
          if ("true node:" in line):
            true_node_index_range[0] = i
          elif ("false node:" in line):
            false_node_index_range[0] = i

    if (true_node_index_range[0] is not None):
      true_node_index_range[1] = false_node_index_range[0] if (false_node_index_range[0] is not None) else end_index
      current_node.true_node = self.load_txt_subtree(lines, true_node_index_range[0], true_node_index_range[1], next_depth)
    if (false_node_index_range[0] is not None):
      false_node_index_range[1] = end_index 
      current_node.false_node = self.load_txt_subtree(lines, false_node_index_range[0], false_node_index_range[1], next_depth)
    
    return current_node
  
  def save_json_tree(self, filename: str):
    if self.tree is None:
      print("Tree is empty")
    else:
      print(f"Saving tree to {filename}.json")
      with open(f"../test/json/{filename}.json", "w") as file:
        file.write(self.tree.to_json())
        
  def load_json_tree(self):
    file_name = input("Enter the file name to load: ").strip()
    file_path = os.path.join('../test/json', file_name + ".json")
    while not os.path.exists(file_path):
      print(f"[ERROR] File {file_path} not found")
      file_name = input("Enter the file name: ").strip()
      file_path = os.path.join('../test/json', file_name + ".json")

    print(f"\nLoading tree from {file_path}\n")
    with open(file_path, "r") as file:
      json_str = file.read()
      self.tree = Node.from_json(json_str)