#✔ Напишите программу, которая решает
#квадратные уравнения даже если
#дискриминант отрицательный.
#✔ Используйте комплексные числа
#для извлечения квадратного корня.
from typing import Any


def get_number():
    while True:
        a = input('Введите значение a: ')
        b = input('Введите значение b: ')
        c = input('Введите значение c: ')
        if a.isdigit() and b.isdigit() and c.isdigit():
            return a, b, c

num_1, num_2, num_3 = get_number()

print(num_1, num_2, num_3)

def get_discr(a: str, b: str, c: str):
    a = int(a)
    b = int(b)
    c = int(c)
    discr = b**2 - 4 * a * c
    return discr
D = get_discr(num_1, num_2, num_3)
print(D)


def get_quadratic(a: str, b: str, disc: int) -> int|Any:
    a = int(a)
    b = int(b)

    if disc == 0:
        x = -b / 2 * a
        return int(x), None

    elif disc < 0:
        disc = disc * (-1)
        c = complex(a, b)
        x1 = (-b + c * disc**0.5) / (2 * a)
        x2 = (-b - c * disc**0.5) / (2 * a)

        return x1, x2

    else:
        x1 = (-b + disc**0.5) / (2 * a)
        x2 = (-b - disc**0.5) / (2 * a)

        return x1, x2


x1, x2 = get_quadratic(num_1, num_2, D)


print(f'Первый корень {x1:.1f}')
print(f'Второй корень {x2:.1f}')



