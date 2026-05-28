num = float(input("Введіть кількість метрів: "))
print("1 - милі/дюйми/ярди, 2 - все разом, 3 - км/см")
choice = input(": ")

if choice == "1":
    unit = input("Оберіть (милі/дюйми/ярди): ")
    if unit == "милі": print(f"{num * 0.000621}")
    elif unit == "дюйми": print(f"{num * 39.37}")
    elif unit == "ярди": print(f"{num * 1.093}")
elif choice == "2":
    print(f"Милі: {num * 0.000621}, Дюйми: {num * 39.37}, Ярди: {num * 1.093}")
elif choice == "3":
    print(f"Км: {num / 1000}, См: {num * 100}")