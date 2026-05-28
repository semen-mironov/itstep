n = int(input("Введіть ціле число N: "))

a, b = 0, 1
is_fibonachi = False

if n == 0 or n == 1:
    is_fibonacci = True
else:
    while b < n:
        a, b = b, a + b
        if b == n:
            is_fibonacci = True
            break

if is_fibonachi:
    print(f"Число {n} належить послідовності Фібоначчі")
else:
    print(f"Число {n} не належить послідовності Фібоначчі")