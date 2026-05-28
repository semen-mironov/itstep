start = int(input("Введіть перше число: "))
end = int(input("Введіть друге число: "))

if start > end:
    start, end = end, start

product = 1
found = False

for i in range(start, end + 1):
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        found = True

if found:
    print(f"Добуток чисел, що діляться на 4 але не діляться на 6: {product}")
else:
    print("У діапазоні нема чисел які діляться на 4 але не діляться на 6")