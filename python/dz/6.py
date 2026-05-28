num = int(input("Введіть тризначне число: "))

num1 = num // 100
num2 = (num // 10) % 10
num3 = num % 10

if num1 == num2 == num3:
    print("Всі цифри однакові")
else:
    print("Цифри різні")