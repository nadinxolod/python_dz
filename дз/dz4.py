# 1.Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$ Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

# P = 62.8318530717
# d = 20

# pi = P/d

# f = int(input("введите число знаков после запятой"))

# if f == 0:
#     print(int(pi))
# else:
#     print(round(pi, f))




#2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def prime_num(n):
#     lst=[]
#     for i in range(2, (n//4)):
#         for j in lst:
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
#     return lst

# flag = True
# lst = []

# n = 66

# summ = n
# list_prime_number = prime_num(n)

# while flag:
#     if summ == 1:
#         flag = False
#     else:
#         for i in list_prime_number:
#             if summ % i == 0:
#                 lst.append(i)
#                 summ /= i
# print(lst)





#3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# a = [int(i) for i in input('Enter numbers: ').split()]

# for i in a:
#     if a.count(i) == 1:
#         print(i)





# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 

# k = 2

# a,b,c = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
# print((a,b,c), max(a,b,c))
# max_n = max(a,b,c)

