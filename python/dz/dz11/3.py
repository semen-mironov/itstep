import random

nums = []
nums_len = int(input("Введіть довжину списку: "))
num = int(input("Введіть число: "))
new_spisok = []

for i in range(nums_len):
    random_num = random.randint(0, 10)
    nums += [random_num]
print(nums)
for j in nums:
    if j > num:
        new_spisok += [j]

print(new_spisok)
