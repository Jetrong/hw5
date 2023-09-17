# Python, JS
# C#/C/C++, Java
# n = 5 # -> class <'int'> -> []
# int n = 5; -> []
# print(type(n))

# name = input("Введите свое имя: ")
# print(f'Привет, {name}!') # $"{}" char n = '5';
# print(type(name))
# int(), str(), float()

# n = '234'
# print(int(n) - 10) # int() делает перевод из str в int

# n = 2.871
# print(int(n))

# n = int(input("Введите число: "))
# print(f'{n} * 2 = {n * 2}')

# n = float(input("Введите дробное число: "))
# print(f'{n} * 2 = {n * 2}')


# n = int(input("Введите целое число: "))
# print(f'{n} + 5 = {n + 5}')
# print(f'{n} - 7 = {n - 7}')
# print(f'{n} * 3 = {n * 3}')
# # 7 : 3 = 2(ост. 1)
# print(f'{n} : 3 = {n // 3} (ост. {n % 3})')
# # 7 : 3 = 2.3333
# print(f'{n} : 3 = {n / 3}')
# print(f'{n}^0.5 = {n ** 0.5}')



# s
# print(int(n > 8))
# bool(Boolean) - True(1) or False(0)
# and(&&) - конъюнкция(логическое умножение)
# or(||) - дизъюнкция(логическое сложение)
# not - отрицание
# in ???

# print(n % 2 == 0 and n > 10 or n % 12 == 0)


# Task 1

# n = int(input("Введите кол-во километров, которое Вы проезжаете за день: "))
# m = int(input("Введите общий киллометраж: "))
# print((m + n - 1) // n)


# Отрицательное деление
# -7 // 2 = (-4) * 2 + 1
# -12 // 5 = (-3) * 5 + 3 
# print(-12 % 5)


# Task 3

# a = int(input('Введите количество учеников в первом классе:'))
# b = int(input('Введите количество учеников во втором классе:'))
# c = int(input('Введите количество учеников в третьем классе:'))
# sum1 = a//2 + a % 2
# sum2 = b//2 + b % 2
# sum3 = c//2 + c % 2
# print(sum1 + sum2 + sum3)


# Task 5
i = int(input("В какой вагон сел Витя: "))
j = int(input("Какой вагон указан на табличке: "))
if i == j:
    print("Нужна дополнительная информация")
else:
    print(i + j - 1)


# Task 7
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')