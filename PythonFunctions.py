#finds max number in the array
def maximum(array):
    num = 0
    for i in array:
        if i > num:
            num = i
    print(num)

#checks to see that the array is filled with only unique numbers
def UniqueNums(array):
    check = True
    for i in array:
        count = 0
        g = i
        for x in array:
            if g == x:
                count += 1
        if count > 1:
            check = False
            break
    if check:
        print("True")
    else:
        print('False')

#checks to see if the two strings are anagrams
def isAnagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("True")
    else:
        print('False')

#finds if there are 2 numbers in the list that adds up to a given number
def TwoSum(list,x):
    seen = []
    check = False
    for num in list:
        if (x - num) in seen:
            check = True
            print(num, ',',x-num )
        seen.append(num)
    if check:
        print('True')
    else:
        print('False')
    #print(seen)

#checks if a given string is a palindrome
def isPalindrome(s):
    word = s.replace(" ","")
    list = []
    list[:] = word
    new = list[::-1]
    if list == new:
        print('True')
    else:
        print('False')




