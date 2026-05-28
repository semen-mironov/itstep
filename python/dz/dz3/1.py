day = int(input("Введіть номер дня тижня (1-7): "))

if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П'ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")
else:
    print("Помилка: введіть число від 1 до 7")