#Задача 3 з зарплатою, кредитом та комуналкою

zp = float(input("Введіть вашу зарплату: "))
kredit_v_mesyats = float(input("Введіть суму місячної виплати по кредиту: "))
komunalka_za_mesyats = float(input("Введіть суму комунальних послуг за місяць: "))

print(f"У вас залишиться з зарплати {zp-(kredit_v_mesyats+komunalka_za_mesyats)}грн")
