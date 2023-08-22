def is_list_even(my_list):
    ans = True
    for i in my_list:
        if i % 2 == 0:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        print('all even')
    return ans


def is_list_odd(my_list):
    ans = True
    for i in my_list:
        if i % 2 != 0:
            ans = True
        else:
            ans = False
            break
    if ans == True:
        print('all odd')
    return ans


def getlist(num):
    numbers = []
    for i in range(num):
        ans = int(input())
        numbers.append(ans)
    return numbers


if __name__ == '__main__':
    num = int(input('Rnage'))
    numbers = getlist(num)
    even = is_list_even(numbers)
    if even == False:
        odd = is_list_odd(numbers)
        if odd == False:
            print('not even or odd')
