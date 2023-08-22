from math import *

pi_list = [pi]
print(pi, end='')
for i in range(2,6):
    num = pi ** i
    pi_list.append(num)
    if i == 5:
        print(num)
    else:
        print(num, end='')

border = '.' *16
print(border, end = '')
print('{line:>32}'.format(line = border), end = '')
print('{line:>32}'.format(line = border))

for pos in range(5):
    pi_list[pos] = '{:.6f}'.format(pi_list[pos])
    print('{:^16}'.format(pi_list[pos]), end = '')
    pi_list[pos] = '{:.6f}'.format(pi * (2** pos))
print()
for pos in range(5):
    print('{:^16}'.format(pi_list[pos]), end = '')
