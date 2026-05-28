string = input("Введіть рядок: ")
char = input("Введіть символ для пошуку: ")
count = 0


for i in string:
    if i == char:
        count += 1

print(f"Символ {char} звустрічається у рядку {count} разів")