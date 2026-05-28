age = int(input("Тобі скількі років?: "))

if age > 0 and age < 100:
    if 0 <= age < 3:
        print("ти бєйбік")
    elif 4 <= age < 6:
        print("Ти хотіш у садік")
    elif 6 <= age < 10:
        print("Ти школьнік")
    elif 11 <= age < 17:
        print("ти школьнік-подросток")
    elif 18 <= age < 25:
        print("ти молодой")
    elif 25 <= age < 35:
        print("ти взрослий чєловєк")
    elif 35 <= age < 55:
        print("ти уже очєнь взрослий")
    elif 55 <= age < 100:
        print("ти уже на пєнсії")
elif age > 100:
    print("Ти долгожитєль")
else:
    print("ти ще не родився")

