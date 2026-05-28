n = int(input("Введіть ціле число N: "))

if n <= 1:
    print("Число має бути більшим за 1")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Число ", n, " є простим")
    else:
        print("Число ", n, " не є простим")