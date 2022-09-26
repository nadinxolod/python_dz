# 1. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Было

# print('Введите число : ')
# n = int(input())
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# list = [factorial(i) for i in range(1, n + 1)] 

# print(list)

# Стало

# from math import factorial

# n = int(input('Введите число: '))
# f = lambda x: 1 if x == 0 else x * factorial(x - 1)
# list2 = list( f(i) for i in range(1, n +1))
# print(list2)


# 2.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Было

# print("Введите число :")
# number = float(input())
# sum = 0
# for i in str(number):
#     if i != ".":
#         sum += int(i)

# print(f'Сумма чисел у введенного числа равна: {sum}.')


# Стало

# my_num = int(input('Введите число: '))
# print(sum(map(int,str(my_num))))

#3. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Было

# n = [i for i in range(1, 10)]
# print(n)
# print(f'Ответ: {sum([n[i] for i in range(1, len(n), 2)])}')


# Стало

# from random import randint
# n = int(input('Введите размер списка: '))
# a = []
# for i in range(n):
#     a.append(randint(1, 10))
# print(f'Первоначальный список {a}')
# new_numb = list(filter(lambda x: (x % 2 == 1) , a))
# print('Сумма четных чисел равна : '+ str(sum(new_numb)))


# Реализуйте алгоритм перемешивания списка.
# Было

# from random import randint
 
# n = int(input('Введите размер списка: '))
# a = []
# for i in range(n):
#     a.append(randint(1, 150))
# print(f'Первоначальный список {a}')
 
 
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
 
# print(f'Отсортированный список методом пузырька {a}')

# Стало

# import random
# my_list = [random.randint(1,10) for i in range(random.randint(3,8))]
# print(f"Наш список: {my_list}")
# random.shuffle(my_list)
# print(f"Наш список после перемешивания: {my_list}")