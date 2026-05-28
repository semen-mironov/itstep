def linia(char, direction, length):
    for i in range(length):
        if direction == 1:
            print(char, end="\n")
        elif direction == 2:
            print(char, end="")


linia(input("Введіть символ для лінії: "), int(input("Введіть напрямок лінії(1 - вертикаль, 2 - горизонталь): ")), int(input("Введіть довжину лінії у символах: ")))