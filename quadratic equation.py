# Квадратное уравнение

a = int(input('Введите коэфиц x**2: '))
b= int(input('Введите коэфиц x: '))
c = int(input('Введите свобод член квадр уравнения: '))

def solution(a,b,c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x_1 = (- b + d ** 0.5)/(2 * a)
        x_2 = (- b - d ** 0.5)/(2 * a)
        return x_1, x_2
    else:
        x_1 = complex((-b / 2 * a), abs(d) ** 0.5 / (2*a))

        x_2 = complex((-b / 2 * a), abs(d) ** 0.5 / (2*a))
        return x_1, x_2
print(solution(a,b,c))
