# app/calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple CLI Calculator")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = sub(a, b)
        elif op == "*":
            result = mul(a, b)
        elif op == "/":
            result = div(a, b)
        else:
            print("Unsupported operation.")
            return

        print(f"Result: {result}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
