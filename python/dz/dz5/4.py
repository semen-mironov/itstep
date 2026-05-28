start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
step = int(input("Введіть крок: "))
direction = input("Оберіть послідовність (1 - звичайна, 2 - зворотня): ")

if direction == "1":
    for i in range(start, end + 1, step):
        print(i)
elif direction == "2":
    for i in range(end, start - 1, -step):
        print(i)
else:
    print("Помилка вибору послідовності")