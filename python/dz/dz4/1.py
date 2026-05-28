num = float(input("Введіть число: "))
pow_choice = int(input("Введіть ступінь (0-7): "))

if 0 <= pow_choice <= 7:
    result = num ** pow_choice
    print(f"Результат: {result}")
else:
    print("Помилка: ступінь має бути від 0 до 7.")