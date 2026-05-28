num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

choice = input("Оберіть дію (max/min/avg): ")

if choice == "max":
    if num1 >= num2 and num1 >= num3:
        num = num1
    elif num2 >= num1 and num2 >= num3:
        num = num2
    else:
        num = num3
    print(f"Максимум: {num}")

elif choice == "min":
    if num1 <= num2 and num1 <= num3:
        num = num1
    elif num2 <= num1 and num2 <= num3:
        num = num2
    else:
        num = num3
    print(f"Мінімум: {num}")

elif choice == "avg":
    num = (num1 + num2 + num3) / 3
    print(f"Середнє: {num}")


else:
    print("Невідома операція!")