amount = float(input("Введіть суму кредиту (грн): "))
years = int(input("Введіть термін (роки): "))

if amount > 50000:
    rate = 0.20
elif amount > 10000:
    if years <= 3:
        rate = 0.12
    else:
        rate = 0.15
else:
    if years <= 3:
        rate = 0.08
    else:
        rate = 0.10

total_to_pay = amount * (1 + rate)
monthly_payment = total_to_pay / (years * 12)

print(f"Ставка: {int(rate * 100)}%")
print(f"Загальна сума: {total_to_pay} грн")
print(f"Щомісячний платіж: {monthly_payment} грн")