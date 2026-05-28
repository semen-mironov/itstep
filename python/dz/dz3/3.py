total_sum = float(input("Введіть суму покупки: "))
age = int(input("Введіть ваш вік: "))

if age < 18:
    discount = 0.10
elif 18 <= age <= 60:
    discount = 0.05
else:
    discount = 0.15

final_sum = total_sum * (1 - discount)
print(f"Ваша знижка: {discount * 100}%. Сума до сплати: {final_sum:.2f}")