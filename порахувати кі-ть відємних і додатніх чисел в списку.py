# Завдання 214. Напишіть програму, яка підраховує додатні і від’ємні числа, 
# а також нулі, введені користувачем, і виводить їхню кількість в один рядок з одним пропуском між ними.
#Вхідні дані: 5, 12, -45, 0, 14, 0

list_of_numbers = [5, 12, -45, 0, 14, 0]

# Ініціалізуємо лічильники для додатних, від'ємних і нулів
positive_count = 0
negative_count = 0
zero_count = 0

# Перебираємо числа зі списку і рахуємо кожну категорію
for num in list_of_numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Виводимо кількість у потрібному форматі
print(positive_count, negative_count, zero_count)

    

    