# Преобразование строки в число и проверка на кодировку ASCII

text = input('Введите текст: ')
print(f'Вы ввели {text}')
print(f'Содержит ли строка число - {text.isdigit()}')

if text.isdigit():
    print(f'Преобразуем в число строку {int(text)}')
else:
    print(f'Входит ли строка в ASCII - {text.isascii()}')
