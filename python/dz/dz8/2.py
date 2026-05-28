import random

score = 0

for i in range(1, 5):
    if i == 1:
        n1, n2, n3 = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        mode = random.randint(0, 1)
        if mode == 1:
            print("Числа:", n1, n2, n3)
            print("Знайдіть максимум: ")
            correct = max(n1, n2, n3)
        else:
            print("Числа:", n1, n2, n3)
            print("Знайдіть мінімум: ")
            correct = min(n1, n2, n3)
            
    elif i == 2:
        a, b = random.randint(1, 100), random.randint(1, 100)
        print(a, "+", b, "=")
        correct = a + b
        
    elif i == 3:
        a, b = random.randint(1, 10), random.randint(1, 10)
        print(a, "*", b, "=")
        correct = a * b
        
    elif i == 4:
        num, pwr = random.randint(1, 5), random.randint(2, 5)
        print(num, "у степені", pwr, "=")
        correct = num ** pwr

    answer = int(input())
    if answer == correct:
        score += 1

print("Ваш результат:", score)