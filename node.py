class Node:
  def __init__ (self):
    self.rule_conditions = []
    self.rule_result = None
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

