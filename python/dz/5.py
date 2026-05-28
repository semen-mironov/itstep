num1 = float(input("Перше число: "))
num2 = float(input("Друге число: "))
op = input("Операція (+, -, *, /, %, **): ")

if op == "+": 
    num = num1 + num2
elif op == "-": 
    num = num1 - num2
elif op == "*": 
    num = num1 * num2
elif op == "/": 
    num = num1 / num2
elif op == "%": 
    num = num1 % num2
elif op == "**": 
    num = num1 ** num2
else:
    print("Невірна дія")

print(f"Результат: {num}")