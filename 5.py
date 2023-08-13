
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
            print(number)
            break
        elif number % i == 0:
            save_oct.append(0)
        else:
            save_oct.append(number % i)
    print(save_oct)
    save_last = list(reversed(save_oct))
    print(save_last)

get_oct(6785)


