import sys

if len(sys.argv) < 4:
    print(f"Usage: Python {sys.argv[0]} <operator> <num1> <num2>")
    sys.exit(1)

operator = sys.argv[1]

if operator not in ['add', 'subtract', 'multiply', 'divide']:
    print(f"Error: Unsupported operator '{operator}'.Supported operators are: add, subtract, multiply, divide.")
    sys.exit(1)

ValueErrormsg = "Error: Both operands must be numbers."

if operator == "add":
    try:
        result = float(sys.argv[2]) + float(sys.argv[3])
        print(result)
    except ValueError:
       print(ValueErrormsg)
    sys.exit(1)
       
elif operator == "subtract":
    try:
        result = float(sys.argv[2]) - float(sys.argv[3])
        print(result)
    except ValueError:
       print(ValueErrormsg)
       sys.exit(1) 
elif operator == "multiply":
    try:
        result = float(sys.argv[2]) * float(sys.argv[3])
        print(result)
    except ValueError:
       print(ValueErrormsg)
       sys.exit(1) 
elif operator == "divide":
    try:
        denominator = float(sys.argv[3])
        if denominator == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit(1)
        result = float(sys.argv[2]) / denominator
        print(result)
    except ValueError:
       print(ValueErrormsg)
       sys.exit(1)  