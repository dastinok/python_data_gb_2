# Угадай число


num = float(input('Загадывайте число от 1 до 1000: '))
LOW = 1
HIGH = 1000
effort = 0

if num < 1 or num > 1000:
    print('Заново')
else:
    print(f'Вы загадали {num} число')
    print('Компьютер начинает отгадывать')
    num_comp = HIGH
    print(f'Комп предполагает число {num_comp}')
    while num < num_comp:
        num_comp = num_comp / 2
        print(f'Комп предполаг {num_comp}')
        if num == num_comp:
            print('Угадал')
    else:





