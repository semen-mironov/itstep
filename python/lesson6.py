number = int(input("введи шестизначне число: "))
 
if number < 100000 or number > 999999:
    print("некоректні дані")
else:
    sum1_3 = 0
    sum4_6 = 0
    k = 1
 
    for i in range(1, 7):
        if i <= 3:
            sum1_3 += number // k % 10
            k *= 10
        else:
            sum4_6 += number // k % 10
            k *= 10
 
    if sum1_3 == sum4_6:
        print("Число \"щасливе\"")
    else:
        print("Число \"нещасливе\"")