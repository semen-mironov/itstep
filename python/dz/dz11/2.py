nums = []
num_of_nums = int(input("Введіть кількість чисел: "))
temp = 0




for i in range(num_of_nums):
    temp = int(input("Введіть число: "))
    nums = nums + [temp]

minim = nums[0]
maxim = nums[0]

for num in nums:
    if num < minim:
        minim = num
    elif num > maxim:
        maxim = num
print("Max: ", maxim)
print("Min: ", minim)

