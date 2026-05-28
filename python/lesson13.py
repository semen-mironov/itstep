import random
 
n = int(input("введи кількість елементів "))

numbers = []
 
for i in range(n):
    number = random.randint(1, 100)
    numbers += [number]

print(numbers)

found = False

for i in range(n):
    if numbers[i] % 3 == 0 or numbers[i] % 5 == 0:
        print("Чісло кратне 3 або 5 ", numbers[i], "знайдено з індексом", i)
        found = True

if not found:
    print("Чисел кратних 3 або 5 нема")
