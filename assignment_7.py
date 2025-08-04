#Write functions for add, subtract, multiply with error checks.
#Create a CLI prompt using input() to perform arithmetic.
#Your code should keep running until the user type "bye"

def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError(f"add() requires numeric types, got {type(a)}, {type(b)}")
    return a + b

def subtract(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("subtract() requires numeric types")
    return a - b

def multiply(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("multiply() requires numeric types")
    return a * b

def divide(a,b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("division() requires numeric types")
    return a / b

def main():
    print("Welcome to the Calculator App! (type 'bye' to exit)")
    
    while True:
        op = input("Type 'add', 'subtract', 'multiply' or 'divide': ").strip().lower()
        if op == "bye":
            print("Goodbye!")
            break

        if op not in {"add", "subtract", "multiply", "divide"}:
            print("Unknown command - type add, subtract, or multiply.")
            continue

        try:
            a = int(input("Please enter a number: "))
            b = int(input("Please enter another number: "))
        except ValueError:
            print("Error: Invalid input.")
            continue

        try:
            if op == "add":
                result = add(a, b)
            elif op == "subtract":
                result = subtract(a, b)
            elif op == "multiply":
                result = multiply(a, b)
        except TypeError as err:
            print("Error:", err)
            continue

        print("Result:", result)

if __name__ == "__main__":
    main()