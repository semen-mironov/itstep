text = input("введіть текст: ")

new_text = ""
capitalize_next = True

for char in text:
    if capitalize_next and char.isalpha():
        new_text += char.upper()
        capitalize_next = False
    else:
        new_text += char
    
    if char == "." or char == "!" or char == "?":
        capitalize_next = True

print("Текст:", new_text)


znaki = ".,!?-:;()\"'"
znaki_count = 0
for char in text:
    if char in znaki:
        znaki_count += 1

print("Кількість розділових знаків:", znaki_count)

znaki_okliku_count = 0
for char in text:
    if char == "!":
        znaki_okliku_count += 1

print("Кількість знаків оклику:", znaki_okliku_count)