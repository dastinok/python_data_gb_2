# Длина площади круга и окружности
import math
from decimal import Decimal, getcontext
#getcontext().prec = 42

def circle(diametr):


    result = Decimal(diametr*math.pi)
    area = Decimal (((diametr / 2)** 2) * math.pi)
    return result, area

diametr = float(input('Введите диаметр: '))
print(circle(diametr))
str(circle(diametr))

print(len(str(math.pi)))