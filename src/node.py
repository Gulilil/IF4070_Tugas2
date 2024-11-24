import json

class Node:
  def __init__ (self, conditions : list = [], result : str = None):
    self.rule_conditions = conditions
    self.rule_result = result
    self.next_node = None
    self.false_node = None

  def check_rule(self, input: list):
    # If self.rule_conditions = [] (empty list) => that means if TRUE (always True)
    for cond in self.rule_conditions:
      if (cond not in input):
        return False
    return True

  def display_node(self):
    print(f"Rule Conditions : {self.rule_conditions}")
    print(f"Rule Result : {self.rule_result}" )
    print(f"Next Node : {self.next_node is not None}")
    print(f"False Node : {self.false_node is not None}")

  def get_final_result(self, conditions: list, newest_result: str):
    if self.check_rule(conditions):
      remaining_cond = [cond for cond in conditions if cond not in self.rule_conditions]
      newest_result = self.rule_result
      if self.next_node is not None:
        return self.next_node.get_final_result(remaining_cond, newest_result)
    else:
      if self.false_node is not None:
        return self.false_node.get_final_result(conditions, newest_result)
    
    return newest_result

  def add_node(self, conditions: list, result: str):
    if self.check_rule(conditions):
      remaining_cond = [cond for cond in conditions if cond not in self.rule_conditions]
      if self.next_node is None:
        self.next_node = Node(remaining_cond, result)
      else:
        self.next_node.add_node(remaining_cond, result)
    else:
      if self.false_node is None:
        self.false_node = Node(conditions, result)
      else:
        self.false_node.add_node(conditions, result)

  def print_subtree(self, prefix: str = ""):
    rule_conditions_str = "TRUE" if not self.rule_conditions else self.rule_conditions
    print(f"{rule_conditions_str} -> {self.rule_result}")
      
    prefix = prefix + "  |"
    if self.next_node != None:
      print(f"{prefix}- next node: ", end="")
      self.next_node.print_subtree(prefix)
    
    if self.false_node != None:
      print(f"{prefix}- false node: ", end="")
      self.false_node.print_subtree(prefix)
      
  def save_subtree(self, file, prefix: str = ""):
      # Write the current node's details
      rule_conditions_str = "TRUE" if not self.rule_conditions else self.rule_conditions
      file.write(f"{rule_conditions_str} -> {self.rule_result}\n")
      
      # Update the prefix for child nodes
      child_prefix = prefix + "  |"
      if self.next_node is not None:
          # Write the "next node" label and recursively save the next node
          file.write(f"{child_prefix}- next node: ")
          self.next_node.save_subtree(file, child_prefix)
      
      if self.false_node is not None:
          # Write the "false node" label and recursively save the false node
          file.write(f"{child_prefix}- false node: ")
          self.false_node.save_subtree(file, child_prefix)
          
  def to_json(self):
    json_dict = {}
    json_dict["rule_conditions"] = self.rule_conditions
    json_dict["rule_result"] = self.rule_result
    
    if self.next_node is not None:
      json_dict["next_node"] = self.next_node.to_json()
      
    if self.false_node is not None:
      json_dict["false_node"] = self.false_node.to_json()
      
    return json.dumps(json_dict, indent=2)
  
  def from_json(json_str: str):
    json_dict = json.loads(json_str)
    node = Node(json_dict["rule_conditions"], json_dict["rule_result"])
    
    if "next_node" in json_dict:
      node.next_node = Node.from_json(json_dict["next_node"])
      
    if "false_node" in json_dict:
      node.false_node = Node.from_json(json_dict["false_node"])
      
    return node