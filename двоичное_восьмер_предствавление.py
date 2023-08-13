#✔ Напишите программу, которая получает целое число и возвращает
#его двоичное, восьмеричное строковое представление.
#✔ Функции bin и oct используйте для проверки своего
#результата, а не для решения.
#Дополнительно:
#✔ Попробуйте избежать дублирования кода
#в преобразованиях к разным системам счисления
#✔ Избегайте магических чисел
#✔ Добавьте аннотацию типов где это возможно



def get_number():
    while True:
        number: str = input('Введите число: ')
        if number.isdigit():
            return number

num = get_number()
print(num)
print(f'Двоичная система с помощью ф-ции bin() - {bin(int(num))}')


def get_trans(number: int) -> list[str]:
    number = int(number)
    number = number * 2
    save = []
    for i in range(0, 45):
        i = 2
        number = number // i
        if number <= 1:
            save.append('1')
            break
        elif number % i == 0:
            save.append('0')
        else:
            save.append('1')
    save_next = list(reversed(save))
    return save_next


res = get_trans(num)
print('Сам написал код, ляля-траляля', '-', '0b', *res, sep='')


def get_oct(number: str | int):
    number = int(number)
    save_oct = []
    num_first = number % 8
    save_oct.append(num_first)

    for i in range(0, 45):
        i = 8
        number = number // i
        if number < 8:
            save_oct.append(number)
            break
        elif number % i == 0:
            save_oct.append(0)
        else:
            save_oct.append(number % i)

    save_last = list(reversed(save_oct))
    return save_last

result = get_oct(num)
print(f'Восьмиричная система с помощью ф-ции oct() - {oct(int(num))}')
print('Сам написал код, ляля-траляля', '-', '0o', *result, sep='')






