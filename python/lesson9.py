size = int(input("Висота трикутника: "))

for y in range(size):
    for x in range(size - y - 1):
        print(' ', end=' ')
        
    for x in range(2 * y + 1):
        print('*', end=' ')
        
    print()