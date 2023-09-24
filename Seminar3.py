# Task 12
# s = int(input("Введите сумму элементов: "))
# p = int(input("Введите произведение элементов: "))
# D = s ** 2 - 4 * p
# y1 = (s - D  ** 0.5) / 2
# y2 = (s + D ** 0.5) / 2
# x1 = s - y1
# x2 = s - y2
# print(x1, y1)
# print(x2, y2)


# Task 10
# n = int(input("Введите кол-во монет: "))
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input("Введите сторону монеты(1 или 0): "))
#     if x == 1:
#         count_one += 1
#     else:
#         count_zero += 1
# if count_zero > count_one:
#     print(count_one)
# else:
#     print(count_zero)


# array - массив содержит только один тип данных
# list - список может содержать разные типы данных
# example = [1, 2.0, "IVAN", True]
#          0   1     2      3
# import array <-
# import numpy <- pip install numpy
# print(*example)
# set_1 = set()
# for i in 3, 56, 13, 26, 18, 9, 23:
#     set_1.add(i)

# print(set_1)
# print(int("07"))

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# #                              -1
# print(list_1[-1])
# print(tuple(list_1))
# print(len(set(list_1)))
# print(list((4, 2, 3, 1, 5)))
# # len -> Length
# for i in range(-1, -len(list_1), -1):
#     print(list_1[i])

# Task 19
# list_1 = [45, 23, 1, 5, 31] # len()
# k = int(input("Введите кол-во сдвигов: ")) % len(list_1)
# # int.Parse(Console.ReadLine()!) % array.Length;
# # print(list_1[begin=0:end=обязательный_парамет:step=+1])
# if k == 0:
#     print(list_1)
# else:
#     print(list_1[-k:] + list_1[:len(list_1) - k])


# Dictionary
# data = {}
# data_second = dict()
# # key: value
# data['Кирилл'] = 23
# data['Марина'] = 20
# # print(data["Кирилл"])
# # print(list(data.keys()))
# # print(list(data.values()))
# for i in data: # <-> data.keys()
#     print(i)
# for i in data.values():
#     print(i)

# Task 21
# data = [{"V": "S001"}, {"V": "S002"},
#          {"VI": "S001"}, {"VI": "S005"},
#            {"VII": "S005"}, {"V":"S009"},
#              {"VIII":"S007"}]
# set_values = set() 
# # print(data[1])
# for i in data:
#     print(i)
#     set_values.add(list(i.values())[0])
# print(set_values)

# Task 23
# data = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(data)):
#     if data[i - 1] < data[i]:
#         count += 1
# print(count)