

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))
print(f'Вы ввели {num} число')

num2 = hex(num)
print(f'Функция hex - {num2}')

if num <= 9:
    print(f'0x{num}')
elif num == 10:
    print(f'0xa')
elif num == 11:
    print(f'0xb')
elif num == 12:
    print(f'0xc')
elif num == 13:
    print(f'0xd')
elif num == 14:
    print(f'0xe')
elif num == 15:
    print(f'0xf')
else:
    lst = []
    while num != 0: # Цикл до тех пор пока
        remain = num % 16 # Остаток от деления
        num = num // 16
        #print(remain)
        if remain == 10:
            remain = 'a'
        elif remain == 11:
            remain = 'b'
        elif remain == 12:
            remain = 'c'
        elif remain == 13:
            remain = 'd'
        elif remain == 14:
            remain = 'e'
        elif remain == 15:
            remain = 'f'
        lst.append(remain)

        print(f'0x{lst[::-1]}'.replace('[','').replace(',','').replace(']','').replace(' ','').replace("'",""))

    else:
        print('')






