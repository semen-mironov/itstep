number = int(input("Введіть число (1-100): "))

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
else:
    print("Помилка: число поза діапазоном.")