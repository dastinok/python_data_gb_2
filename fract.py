'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''


try:
    first_str_numerator = input('Введите числитель: ')
    print(first_str_numerator)

    a = int(first_str_numerator)
    print(type(a))
except ValueError:
    print('Вы ввели не число')

try:
    first_str_denom = input('Введите знаменатель: ')
    print(first_str_denom)

    b = int(first_str_denom)
    print(type(b))
except ValueError:
    print('Вы ввели не число')
print(f'{first_str_numerator}/{first_str_denom}')

try:
    second_str_numerator = input('Введите числитель: ')
    print(second_str_numerator)

    c = int(second_str_numerator)
    print(type(c))
except ValueError:
    print('Вы ввели не число')

try:
    second_str_denom = input('Введите знаменатель: ')
    print(second_str_denom)

    d = int(second_str_denom)
    print(type(d))
except ValueError:
    print('Вы ввели не число')

print(f'{second_str_numerator}/{second_str_denom}')

try:
    denominator = b * d
    numerator_1 = (denominator / b * a)
    numerator_2 = (denominator / d * c)
    numerator = numerator_1 + numerator_2
    result = numerator / denominator
    print('Сложение дроби')
    print(f'{first_str_numerator}/{first_str_denom} + {second_str_numerator}/{second_str_denom} = {result:.1f}')
except ZeroDivisionError:
    print('Деление на ноль')
except TypeError:
    print("Вы сложили значения несовместимых типов")
except NameError:
    print('Ошибка, несовместимы тип')

try:
    numerator = a * c
    denominator = b * d
    result = numerator / denominator
    print('Произведение дроби')
    print(f'{first_str_numerator}/{first_str_denom} * {second_str_numerator}/{second_str_denom} = {result:.1f}')
except ZeroDivisionError:
    print('Деление на ноль')
except TypeError:
    print("Вы сложили значения несовместимых типов")
except NameError:
    print('Ошибка, несовместимы тип')


