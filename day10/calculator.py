import art



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

operation = " ".join(operations.keys())

def calculator():
  print(art.logo)        
  # Get user inputs
  num1 = float(input("What's the first number?: "))
  operation_symbol = input(f"What type of operation ( {operation} ) do you want:\n")

  more_operations = True
  choice = ""
  previous_answer = 0 
  while more_operations:
    if choice == 'y':
      operation_symbol = input(f"What type of operation ( {operation} ) do you want:\n")
      num1 = previous_answer     
    num2 = float(input("What's the next number?: "))

    calculation_function = operations.get(operation_symbol)
    # if we have valid operation
    if calculation_function:
        answer = calculation_function(num1, num2)
        previous_answer = answer
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    else:
        print("Invalid operation symbol. Please choose from: +, -, *, /")
        more_operations = False
        break
    choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit.")
    if choice == "n":
        more_operations = False
        calculator()

calculator()
      