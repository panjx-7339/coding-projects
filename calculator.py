import os 


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def add(a, b):
  return a + b 

def minus(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b


operations = {
  "+": add,
  "-": minus,
  "*": multiply,
  "/": divide
}


def calculator():
  a = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  continue_calc = True
  
  while continue_calc:
    op_symbol = input("Pick an operation from the list above: ") 
    b = float(input("What's the next number?: "))
    calc_function = operations[op_symbol]   #impt! drawing the relevant function from a dictionary
    result = calc_function(a,b)
    
    print(f"{a} {op_symbol} {b} = {result}")
    
    user_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if user_input == 'end':
      break

    elif user_input == 'y':
      a = result
    
    elif user_input == 'n':
      continue_calc = False
      cls()
      calculator()

calculator()