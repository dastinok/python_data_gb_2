# Бинарное, строчное и восьмеричное

def get_next(number, system):
    result = 0
    ost = 0
    rezString = ''
    while True:
        result = number // system
        ost = number % system
        if result < system:
            rezString = rezString + str(ost) + str(result)
            break
        else:
            number = result
            rezString = rezString + str(ost)
    return rezString[::-1]

integer = int(input('Введите целое: '))

print(get_next(integer,2))
print(get_next(integer,8))