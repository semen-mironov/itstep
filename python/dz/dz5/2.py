start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

print("Усі числа діапазону:")
for i in range(start, end + 1):
    print(i, end=" ")
print()

print("Усі числа в спадающому порядку:")
for i in range(end, start - 1, -1):
    print(i, end=" ")
print()

print("Усі числа, кратні 7:")
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()

count = 0
for i in range(start, end + 1):
    if i % 5 == 0:
        count += 1
print(f"Кількість чисел кратних 5: {count}")