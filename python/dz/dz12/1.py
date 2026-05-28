import random
 
nums = [random.randint(-100, 100) for i in range(20)]
print(nums)
 
sum_neg = 0
 
for num1 in nums:
    if num1 < 0:
        sum_neg += num1
print("Сума негативних: ", sum_neg)
 
sum_pos = 0
 
for num2 in nums:
    if num2 > 0:
        sum_pos += num2
print("Сума позитивних: ", sum_pos)
 
dob_krat = 1
 
for i in nums:
    if nums.index(i) % 3 == 0:
        dob_krat *= i
 
print("Добуток елементів з індексами кратними 3: ", dob_krat)