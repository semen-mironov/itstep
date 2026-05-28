age = int(input("Введіть вік авто (роки): "))
probeg = int(input("Введіть пробіг (км): "))

if age < 3 and probeg <= 30000:
    print("Автомобіль у відмінному стані")
elif age < 10 and probeg <= 100000:
    print("Автомобіль у хорошому стані")
else:
    print("Автомобіль потребує перевірки")