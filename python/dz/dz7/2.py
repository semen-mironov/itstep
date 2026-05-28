import random


d1 = random.randint(0, 9)

d2 = random.randint(0, 9)
while d2 == d1:
    d2 = random.randint(0, 9)

d3 = random.randint(0, 9)
while d3 == d1 or d3 == d2:
    d3 = random.randint(0, 9)

d4 = random.randint(0, 9)
while d4 == d1 or d4 == d2 or d4 == d3:
    d4 = random.randint(0, 9)


s1, s2, s3, s4 = str(d1), str(d2), str(d3), str(d4)

print("Гра Бики та Корови. Вгадайте 4 цифри.")

while True:
    user_input = input("Введіть 4 цифри: ")
    
    bulls = 0
    cows = 0
    
    pos = 1
    for char in user_input:
        if pos == 1 and char == s1:
            bulls += 1
        elif pos == 2 and char == s2:
            bulls += 1
        elif pos == 3 and char == s3:
            bulls += 1
        elif pos == 4 and char == s4:
            bulls += 1
        
        else:
            if char == s1 or char == s2 or char == s3 or char == s4:
                cows += 1
        
        pos += 1
            
    print("Бики:", bulls, "Корови:", cows)
    
    if bulls == 4:
        print("Перемога!")
        break