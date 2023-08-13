
num = 17

num2 = hex(num)
print(num2)

while num != 0:
    remain_1 = num % 16
    num = num // 16
    print(remain_1)
    print(num)

else:
    print('stop')

