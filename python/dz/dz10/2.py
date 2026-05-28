player_wins = 0
computer_wins = 0

counter = 0

while player_wins < 3 and computer_wins < 3:
    print("\nРахунок: Ви", player_wins, "-", computer_wins, "Комп'ютер")
    user = input("Ваш хід (к, н, п або r, s, p): ").lower()
    
    counter += 7
    comp_num = counter % 3
    if comp_num == 0:
        comp = "r" # камінь
        comp_name = "Камінь"
    elif comp_num == 1:
        comp = "s" # ножиці
        comp_name = "Ножиці"
    else:
        comp = "p" # папір
        comp_name = "Папір"

    if user == "к" or user == "r":
        user_choice = "r"
        user_name = "Камінь"
    elif user == "н" or user == "s":
        user_choice = "s"
        user_name = "Ножиці"
    elif user == "п" or user == "p":
        user_choice = "p"
        user_name = "Папір"
    else:
        print("Неправильне введення!")
        continue

    print("Ви обрали:", user_name)
    print("Комп'ютер обрав:", comp_name)

    if user_choice == comp:
        print("Нічия в раунді!")
    elif (user_choice == "r" and comp == "s") or \
         (user_choice == "s" and comp == "p") or \
         (user_choice == "p" and comp == "r"):
        print("Ви виграли раунд!")
        player_wins += 1
    else:
        print("Комп'ютер виграв раунд!")
        computer_wins += 1

if player_wins == 3:
    print("\nВітаємо! Ви перемогли в грі!")
else:
    print("\nГру закінчено. Переміг комп'ютер.")