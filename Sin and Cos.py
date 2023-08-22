from math import *

def factorial(num):
    start = 1
    for i in range(num, 1, -1):
        start *= i
    return start

def sine(rads):
    other = 0
    n = 1
    go = True
    while go:
        bottom = factorial((2*n) + 1)
        top_pt1 = (rads**((2*n)+1))
        top_pt2 = (-1)**n
        top = top_pt1 * top_pt2
        value = top/bottom
        if abs(value) < (10**-10):
            break
        else:
            other += value
            n += 1
            go = True
    return (rads + other)

def cosine(rads):
    other = 0
    n = 1
    go = True
    while go:
        bottom = factorial(2*n)
        top_pt1 = (rads ** (2*n))
        top_pt2 = (-1) ** n
        top = top_pt1 * top_pt2
        value = top / bottom
        if abs(value) < (10**-10):
            break
        else:
            other += value
            n += 1
            go = True
    return 1 + other

def main():
    q1 = input('Do you want the sin or cos?\n')
    q2 = int(input('What angle do you want?\n'))
    rads = radians(q2)
    if q2 == 'sin':
        ans = sine(rads)
        real = sin(rads)
        print('{} ; Theirs: {}'.format(ans, real))
    else:
        ans = cosine(rads)
        real = cos(rads)
        print('{} ; Theirs: {}'.format(ans, real))

main()