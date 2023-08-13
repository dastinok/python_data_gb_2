#Напишите программу, которая получает целое
#число и возвращает его шестнадцатеричное
#строковое представление. Функцию hex
#используйте для проверки своего результата.

def get_num():
    while True:
        number = input('Введите число: ')
        if number.isdigit():
            return number

num = get_num()
print(num)
num_1 = hex(int(num))
print(num_1)

def get_hex(number: str) -> list:
    number = int(number)
    save_oct = []
    num_first = number % 16
    save_oct.append(num_first)

    for i in range(10):
        i = 16
        number = number // 16
        if number % i == 0:
            save_oct.append(0)
        elif number < 16:
            save_oct.append(number)
            break
        else:
            save_oct.append(number % i)

    save_last = list(reversed(save_oct))
    return save_last

my_list = get_hex(num)

my_list = str(my_list).replace('15', 'f').replace('10', 'a').replace('11', 'b').replace('12', 'c').replace('13', 'd').replace('14', 'e')
print('0x' + my_list.replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))




