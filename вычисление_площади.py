#Напишите программу, которая вычисляет площадь
#круга и длину окружности по введённому диаметру.
#✔ Диаметр не превышает 1000 у.е.
#✔ Точность вычислений должна составлять
#не менее 42 знаков после запятой.


import decimal

MAX = 1000

def get_diametr(maxim: int) -> str:
    while True:
        number = input(f'Введите диаметр до {maxim}: ')
        if number.isdigit() and int(number) <= maxim:
            return number

diametr = get_diametr(MAX)
print(diametr)

def get_area_of_circle_len(diam: str) -> decimal:
    diam = int(diam)
    pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
    decimal.getcontext().prec = 42
    area_circle = pi / 4 * decimal.Decimal(diam)**2

    circ_len = pi * decimal.Decimal(diam)

    return area_circle, circ_len


circle_area, len_circ = get_area_of_circle_len(diametr)

print('Площадь круга',  circle_area)
print('Длина окружности',  len_circ)




