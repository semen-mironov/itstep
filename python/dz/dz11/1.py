nums = []
num_of_nums = int(input("Введіть кількість чисел: "))
temp = 0
odd = 0
even = 0


for i in range(num_of_nums):
    temp = int(input("Введіть число: "))
    nums = nums + [temp]
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(nums)
print("Непарних: ", odd)
print("Парних: ", even)
