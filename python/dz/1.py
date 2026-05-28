num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

choice = input("Що ви хочете знайти? (+ *): ")

if choice == "+":
    print(f"Результат: {num1 + num2 + num3}")
elif choice == "*":
    print(f"Результат: {num1 * num2 * num3}")
else:
    print("Ви обрали неправильну дію")