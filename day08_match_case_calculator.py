# Day 8 - Simple Calculator using match-case (Python 3.10+)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation: +, -, *, /,%")
operator = input("Enter operator: ")

match operator:
    case "+":
        result = num1 + num2
    case "%":
        result = num1 % num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    case _:
        result = "Invalid operator"

print(f"Result: {result}")
