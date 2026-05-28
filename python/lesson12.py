import random

password = ""
lengh = int(input("Введіть довжину бажаного пароля: "))

for i in range(lengh):
    password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~")

print(password)