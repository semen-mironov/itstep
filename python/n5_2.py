number = int(input())

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

reversed_number = digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
print(reversed_number)