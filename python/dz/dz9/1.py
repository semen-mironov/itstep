string = input("Введіть рядок: ")

leters = 0
nums = 0

for char in string:
    if char in "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmMйцукенгшщзхїфівапролджєячсмитьбюЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ":
        leters += 1
    elif char in "123456789":
        nums += 1

print(f"У рядку {leters} букв та {nums} цифр")