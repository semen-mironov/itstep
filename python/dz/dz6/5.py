start = int(input())
end = int(input())
for num in range(start, end + 1):
    if num < 2:
        continue
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        print(num)