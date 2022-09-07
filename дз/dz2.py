
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# num = float(input('Введите число'))
# sum = 0
# num = num * 10 ** 15
# while num > 0:
#     sum = sum + num % 10
#     num = num // 10
# print(int(sum))


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input("Введите число"))
# arr = []
# mult = 1
# for i in range (1, num + 1):
#     mult *= i
#     arr.append(mult)
# print(arr)


# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# num = int(input("Введите число"))
# def sum_seq(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += round((1 + 1 / i) ** i, 3)
#     return sum
# print(sum_seq(num))


# 5. Реализуйте алгоритм перемешивания списка.


# import random
# spisok = [1,2,3,4,5]
# for i in range(len(spisok)):
#     a = random.randint(0, len(spisok)-1)
#     b = random.randint(0, len(spisok)-1)
#     spisok[a],spisok[b] = spisok[b],spisok[a]
# print(spisok)