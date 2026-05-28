text = input("Введіть текст: ")

words = 0

for char in text:
    if char == " " or char == ",":
        words += 1

print(f"У введеному тексті {words} слів")