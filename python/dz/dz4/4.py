max_total_salary = 0
best_manager_id = 0

s1 = 0
s2 = 0
s3 = 0

for i in range(1, 4):
    sales = float(input(f"Введіть продажі менеджера {i}: "))

    if sales < 500:
        bonus_percent = 0.03
    elif sales <= 1000:
        bonus_percent = 0.05
    else:
        bonus_percent = 0.08
    
    current_salary = 200 + (sales * bonus_percent)

    if i == 1:
        s1 = current_salary
    elif i == 2:
        s2 = current_salary
    elif i == 3:
        s3 = current_salary

    if current_salary > max_total_salary:
        max_total_salary = current_salary
        best_manager_id = i

if best_manager_id == 1:
    s1 += 200
elif best_manager_id == 2:
    s2 += 200
elif best_manager_id == 3:
    s3 += 200

print(f"Менеджер 1: {s1}$", "(Найкращий!)" if best_manager_id == 1 else "")
print(f"Менеджер 2: {s2}$", "(Найкращий!)" if best_manager_id == 2 else "")
print(f"Менеджер 3: {s3}$", "(Найкращий!)" if best_manager_id == 3 else "")