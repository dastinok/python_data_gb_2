# Программа которая запрашивает типы данных

name = input('Введите текст: ')

print(f'Вы ввели {name}')

print(f'Тип объекта - {type(name)}')
print(f'Адрес объекта - {id(name)}')
print(f'Хэш объекта - {hash(name)}')

data = [4, 6.0, 'String', False, False, 6.0]
num = 1
for i in data:
    if isinstance(i, int):
        integer = 'integer'
    if isinstance(i, str):
        string = 'string'
    print('number:', num, 'var:', i, 'Type is:', type(i), 'id:', id(i), 'hash:', hash(i),\
          'is integer:', integer, )
    num += 1
    integer = ''