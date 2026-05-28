#задача 5 з рестораном та чайовими

price = float(input("Введіть суму рахунку: "))
peoples = int(input("Введіть кількість людей: "))

chayovi = price / 100 * 15

print(f"Сума з чайовими: {chayovi+price}грн")
print(f"Кожна людина повинна заплатити: {((chayovi+price)/peoples)}грн")