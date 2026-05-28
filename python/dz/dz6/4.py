total = 0
for n in range(100, 10000):
    if n < 1000:
        a = n // 100
        b = (n // 10) % 10
        c = n % 10
        if a != b and a != c and b != c:
            total += 1
    else:
        a = n // 1000
        b = (n // 100) % 10
        c = (n // 10) % 10
        d = n % 10
        if a != b and a != c and a != d and b != c and b != d and c != d:
            total += 1
print(total)