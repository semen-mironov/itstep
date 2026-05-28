number = int(input("Введіть чотирицифрове число: "))

n1 = number // 1000 
n2 = (number // 100) % 10 
n3 = (number // 10) % 10  
n4 = number % 10         

dobutok = n1 * n2 * n3 * n4

print(f"Результат добутку: {n1}*{n2}*{n3}*{n4} = {dobutok}")