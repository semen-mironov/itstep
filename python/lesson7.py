start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

if start > end:
    start, end = end, start

product = 1
found = False

for i in range(start, end + 1):
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        found = True
        print(f"Знайдено число: {i}")

if found:
    print(f"Добуток знайдених чисел: {product}")
else:
    print("Чисел, що кратні на 4 і кратні 6, у цьому діапазоні немає")