import re

class Query:
  type : str
  conditions : list
  result : str | None
  '''
    Input Format:
    -> Ask : [CONDITIONS] ?
      Example => A, B, C ?
    -> Add : [CONDITIONS] > [RESULT]
      Example => A, B, C > D
  '''
  def __init__ (self, input: str):
    try:
      assert "?" in input or ">" in input
      ask_pattern = r'^([\s\S]+(,\s?[\s\S]+)*)\?$'
      add_pattern = r'^([\s\S]*(,\s?[\s\S]+)*)\s?>\s?[\s\S]+$'
      input = input.strip()

      if (bool(re.match(ask_pattern, input))):
        self.type = "ask"
        self.conditions = input.split("?")[0].split(",")
        self.conditions = [condition.strip() for condition in self.conditions]
        self.result = None
        
      elif (bool(re.match(add_pattern, input))):
        self.type = "add"
        self.conditions = input.split(">")[0].split(",")
        self.conditions = [condition.strip() for condition in self.conditions if len(condition) > 0]
        self.result = input.split(">")[1].strip()
        assert self.result is not None, "None result value"

      else:
        raise ValueError("Invalid string pattern")
      
    except Exception as e:
      print(f"[ERROR] Error in parsing the input {input} : {e}")

  @classmethod
  def from_properties(cls, type: str, conditions: list, result: str | None = None):
    """Alternative constructor to initialize properties directly."""
    obj = cls.__new__(cls)
    obj.type = type
    obj.conditions = conditions
    obj.result = result
    return obj
  
  def is_valid(self):
    return 'type' in self.__dict__

  def display(self):
    if (not self.is_valid()):
      print("[ERROR] Cannot display invalid Query")
    else:
      print(f"Type : {self.type}")
      print(f"Conditions : {self.conditions}")
      if (self.result is not None) : print(f"Result : {self.result}")