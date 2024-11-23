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
          lines = file.readlines()  # Read all lines once
          self.tree = self._load_subtree(lines, 0)[0]

  def _load_subtree(self, lines: list[str], indent_level: int) -> tuple[Node, int]:
    if not lines:
        return None, 0

    node = None
    i = 0  # Start from the current line in the list

    while i < len(lines):
        line = lines[i].rstrip()
        current_indent = self._get_indent_level(line)

        # Debug: Print the current processing line and indentation details
        print(f"Processing line: {line}")
        print(f"Current indent level: {current_indent}, Expected indent level: {indent_level}")

        if current_indent < indent_level:
            # If we encounter a line with less indentation, return to the previous level
            print(f"Breaking out of loop. Line's indent level {current_indent} < expected {indent_level}.")
            break

        if current_indent == indent_level:
            # Parse the current node
            try:
                conditions, result = line.split(" -> ")
                print(f"Conditions: {conditions}, Result: {result.strip()}")
                # conditions = eval(conditions.strip())  # Safely convert string representation of list to actual list
            except Exception as e:
                raise ValueError(f"Failed to parse line: {line}. Error: {e}")

            # Debug: Print parsed node details
            print(f"Node conditions: {conditions}, Node result: {result.strip()}")

            node = Node(conditions, result.strip())
            i += 1

        # Parse child nodes
        while i < len(lines) and self._get_indent_level(lines[i]) > indent_level:
            branch_line = lines[i].strip()

            if branch_line.startswith("|- next node:"):
                branch_conditions, branch_result = branch_line[len("|- next node:"):].split(" -> ")
            elif branch_line.startswith("|- false node:"):
                branch_conditions, branch_result = branch_line[len("|- false node:"):].split(" -> ")
            else:
                branch_conditions, branch_result = None, None

            if branch_conditions is not None:
                try:
                    branch_conditions = eval(branch_conditions.strip())  # Convert to list
                except Exception as e:
                    raise ValueError(f"Failed to parse branch line: {branch_line}. Error: {e}")

                # Debug: Print extracted branch details
                print(f"Processing branch: {branch_conditions} -> {branch_result.strip()}")

            if branch_line.startswith("|- next node:"):
                print("Parsing next node...")
                child_node, offset = self._load_subtree(lines[i + 1:], indent_level + 2)
                node.next_node = child_node
                i += offset + 1
            elif branch_line.startswith("|- false node:"):
                print("Parsing false node...")
                child_node, offset = self._load_subtree(lines[i + 1:], indent_level + 2)
                node.false_node = child_node
                i += offset + 1
            else:
                # Debug: Print unrecognized line
                print(f"Unrecognized branch line: {lines[i]}")
                i += 1

        break  # Exit after parsing the main node and its children

    return node, i

  def _get_indent_level(self, line: str) -> int:
      return len(line) - len(line.lstrip())