text = input("Введіть текст: ")
rechenya = 0

for char in text:
    if char in ".!?":
        rechenya += 1

print(f"У введенному тексті {rechenya} реченнь")