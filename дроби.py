#Напишите программу, которая принимает две строки
#вида “a/b” — дробь с числителем и знаменателем.
#Программа должна возвращать сумму
#и *произведение дробей. Для проверки своего
#кода используйте модуль fractions.

from fractions import Fraction


def get_num():
    while True:

        numerator_1 = input('Введите числитель: ')
        denominator_1 = input('Введите знаменатель: ')

        numerator_2 = input('Введите числитель: ')
        denominator_2 = input('Введите знаменатель: ')

        if numerator_1.isdigit() and denominator_1.isdigit() and numerator_2.isdigit() and denominator_2.isdigit():
            return numerator_1, denominator_1, numerator_2, denominator_2

num_1, num_2, num_3, num_4 = get_num()

print(num_1, '/', num_2)

print(num_3, '/', num_4)

denominator = int(num_2) * int(num_4)
numerator = int(num_4)*int(num_1) + int(num_2)*int(num_3)

res_sum = numerator / denominator
print(num_1, '/', num_2, '+', num_3, '/', num_4, '=', res_sum)

x = Fraction(int(num_1), int(num_2))
y = Fraction(int(num_3), int(num_4))
print(x+y)

numerator = int(num_1)*int(num_3)
denominator = int(num_2)*int(num_4)

res_add = numerator / denominator
print(num_1, '/', num_2, '*', num_3, '/', num_4, '=', res_add)

x = Fraction(int(num_1), int(num_2))
y = Fraction(int(num_3), int(num_4))
print(x*y)
