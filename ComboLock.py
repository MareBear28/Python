num = ['first', 'second', 'third']
combo = []
user_combo = []
direction = ['clockwise', 'counterclockwise', 'clockwise']
for i in num:
    ans = int(input('What is the {} number in the combination? '.format(i)))
    combo.append(ans)

correct = False
while not correct:
    print()
    start = 0
    user_combo = []
    for x in direction:
        user_ans = int(input('Turn the lock {} by how much? '.format(x)))
        if x == 'clockwise':
            user_ans = 40 - user_ans
            start += user_ans
        if x == 'counterclockwise':
            start += user_ans
            if start > 39:
                start - 39
        user_combo.append(start)
    print()
    for f in range(3):
        if combo[f] != user_combo[f]:
            print('Sorry, that sequence was incorrect')
            correct = False
            break
    else:
        print('Correct!')
        break
