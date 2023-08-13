#✔ Начальная сумма равна нулю
#✔ Допустимые действия: пополнить, снять, выйти
#✔ Сумма пополнения и снятия кратны 50 у.е.
#✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
#✔ Нельзя снять больше, чем на счёте
#✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
#✔ Любое действие выводит сумму денег


def main():
    def get_menu():
        print('Вас приветствует программа "Банкомат"\n'
              '1. Пополнить\n'
              '2. Снять\n'
              '3. Выйти')
        while True:
            action = input('Выберите ф-цию (цифру) меню: ')
            if action.isdigit() and 0 < int(action) < 4:
                return action
    num = get_menu()
    print(num)


    if int(num) == 3:
        exit()

    elif int(num) == 1:
        def put_money():
            with open('wallet.txt', 'r') as f:
                sum_account = sum(int(line) for line in f)
                print(f'Ваша сумма счета составляет - {sum_account}')

            while True:
                number = input('Введите сумму, которую хотите положить: ')
                if number.isdigit() and 0 < int(number):
                    sum_account = sum_account + int(number)
                    print(sum_account)

                with open('wallet.txt', 'w') as file:
                    new_summ = file.write(str(sum_account))
                    return new_summ


        put_money()
        main()



    elif int(num) == 2:

        def take_money():
            with open('wallet.txt', 'r') as f:
                sum_account = sum(int(line) for line in f)
                print(f'Ваша сумма счета составляет - {sum_account}')

            while True:
                number = input('Введите сумму, которую хотите снять, но не более счета: ')
                if number.isdigit() and 0 < int(number) <= sum_account:
                    sum_account = sum_account - int(number)

                    print(sum_account)

                    with open('wallet.txt', 'w') as file:
                        new_summ = file.write(str(sum_account))

                        return new_summ
        take_money()
        main()


main()







