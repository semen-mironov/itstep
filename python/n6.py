val_day = float(input("Ціна за день в грн: "))
days = int(input("Кількість днів оренди: "))
zastava = int(input("Сума застави: "))

suma = zastava + val_day*days

print(f"Сума: {suma}")

how_many_days = float(input("Скільки людина користувалась: "))
s_mashinay_vsyo_harasho = int(input("Машина ціла? так-1, ні-0: "))
if s_mashinay_vsyo_harasho:
    print(f"Сума повернення: {((days-how_many_days)*val_day)+zastava}")
else:
    print(f"Сума повернення(Машину коцнулі, заставу не повєртаєм): {((days-how_many_days)*val_day)}")

