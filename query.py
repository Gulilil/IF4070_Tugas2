class Query:
  '''
    Input Format:
    -> Ask : [CONDITIONS] ?
      Example => A, B, C ?
    -> Add : [CONDITIONS] > [RESULT]
      Example => A, B, C > D
  '''
  def __init__ (self, input):
    try:
      if ("?" in input):
        self.type = "ask"
        self.conditions = input.split("?")[0].split(",")
        self.conditions = [condition.strip() for condition in self.conditions]
        self.result = None
        
      elif (">" in input):
        self.type = "add"
        self.conditions = input.split(">")[0].split(",")
        self.conditions = [condition.strip() for condition in self.conditions]
        self.result = input.split(">")[1].strip()
        assert self.result is not None
    except Exception as e:
      print(f"Error in parsing the input {input} : {e}")

  def display_input(self):
    print(f"Type : {self.type}")
    print(f"Conditions : {self.conditions}")
    if (self.result is not None) : print(f"Result : {self.result}")