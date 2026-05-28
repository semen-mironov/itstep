import random

nums = [random.randint(-100, 100) for i in range(20)]
print(nums)

parni = []

for num in nums:
    if num % 2 == 0:
        parni.append(num)
print(parni)
dodatni = []

for num2 in nums:
    if num2 > 0:
        dodatni.append(num2)

print(dodatni)