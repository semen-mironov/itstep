import random

nums = [random.randint(-100, 100) for i in range(20)]
print(nums)

count = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        count += 1

print("Кількість елементів які більші за попередній: ", count)
