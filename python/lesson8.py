num = int(input("Введи додатне число: "))

if num <= 0:
    print("Число має буть больше нуля.")
else:
    count = 0
    print(f"Дільники числа {num}:")
    
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
            count += 1
            
    print(f"Кількість дільників: {count}")