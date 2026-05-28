num1 = int(input())
num2 = int(input())

a1 = num1 // 100
a2 = (num1 // 10) % 10
a3 = num1 % 10

b1 = num2 // 100
b2 = (num2 // 10) % 10
b3 = num2 % 10

result = a1 * 100000 + b1 * 10000 + a2 * 1000 + b2 * 100 + a3 * 10 + b3
print(result)