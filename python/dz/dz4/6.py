print("Меню")
print("Закуски: 1. Салат (5$), 2. Суп (7$)")
print("Основні: 3. Курка (10$), 4. Риба (12$)")
print("Десерти: 5. Морозиво (3$), 6. Фрукти (4$), 0. Без десерту")

starter = int(input("Оберіть закуску (1-2): "))
main = int(input("Оберіть основну страву (3-4): "))
dessert = int(input("Оберіть десерт (5-6 або 0): "))
is_regular = input("Ви постійний клієнт? (так/ні): ")

price = 0
items_count = 0

if starter == 1: 
    price += 5
    items_count += 1
if starter == 2:
    price += 7
    items_count += 1
if main == 3: 
    price += 10
    items_count += 1
if main == 4:
    price += 12 
    items_count += 1

dessert_price = 0
if dessert == 5: 
    dessert_price = 3 
    items_count += 1
if dessert == 6: 
    dessert_price = 4
    items_count += 1

if starter == 2 and main == 4 and dessert != 0:
    dessert_price = max(0, dessert_price - 2)
    print("Отримано знижку 2$ на десерт (Суп + Риба)!")

if main == 3 and dessert == 5:
    print("Бонус: безкоштовний чай!")

price += dessert_price

discount_percent = 0
if items_count == 3:
    discount_percent += 10

if price > 20:
    if discount_percent == 10: 
        discount_percent = 15
    else: 
        discount_percent = 15

if is_regular == "так":
    discount_percent += 5

final_price = price * (1 - discount_percent / 100)
print(f"Ваша знижка: {discount_percent}%")
print(f"Підсумкова вартість: {final_price}$")