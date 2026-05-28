a = int(input("Введіть число: "))
n = int(input("Введіть ступінь: "))

result = 1

if n == 0:
    result = 1
else:
    for i in range(n):
        result *= a

print(f"Число {a} у степені {n} дорівнює: {result}")