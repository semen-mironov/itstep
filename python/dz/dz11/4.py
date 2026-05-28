nums = []
num_of_nums = int(input("Введіть кількість чисел: "))
temp = 0
new_nums = []
num = int(input("Введіть число: "))

for i in range(num_of_nums):
    temp = int(input("Введіть число: "))
    nums = nums + [temp]

print(nums)
for j in nums:
    if j > num:
        new_nums += [j]

print(new_nums)
