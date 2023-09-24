
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a(i) ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# result = []
# i = 0
# sum = 0

# print(berryes)

# while (i < kust):
#     if (i == kust - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1

# print(f"максимальное число ягод за одну итерацию {result[-1]}")


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# def newset(num):
#     new_set = set()
#     for i in range(num):
#         new_set.add(int(input("Введите число для множества: ")))
#     return new_set

# n = int(input("Введите кол-во элементов первого множества: "))
# n_set = newset(n)

# m = int(input("Введите кол-во элементов второго множества: "))
# m_set = newset(m)

# print(*n_set)
# print(*m_set)

# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)
