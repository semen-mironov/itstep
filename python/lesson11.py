name = input("name: ")
new_name = ""
 
for char in name:
    if char in "аАеЕєЄиИіІїЇоОуУюЮяЯaAeEiIoOuUyY":
        new_name += "*"
    else:
        new_name += char
print(new_name)