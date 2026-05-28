cost_per_minute = float(input("Введіть базову вартість хвилини: "))
minutes = float(input("Введіть тривалість розмови (хв): "))

print("Виберіть оператора:")
print("1. Kyivstar -> Kyivstar (коефіцієнт 0.5)")
print("2. Kyivstar -> Vodafone (коефіцієнт 1.2)")
print("3. Vodafone -> Lifecell (коефіцієнт 1.5)")

choice = input("Ваш вибір (1-3): ")

if choice == "1":
    total_cost = (cost_per_minute * 0.5) * minutes
    print(f"Тариф: Внутрімережевий")
elif choice == "2":
    total_cost = (cost_per_minute * 1.2) * minutes
    print(f"Тариф: Міжмережевий (Kyivstar/Vodafone)")
elif choice == "3":
    total_cost = (cost_per_minute * 1.5) * minutes
    print(f"Тариф: Міжмережевий (Vodafone/Lifecell)")
else:
    total_cost = cost_per_minute * minutes
    print("Оператора не обрано, розрахунок за базовим тарифом")

print(f"Загальна вартість розмови: {total_cost:.2f} грн")