def DisplayMenu():
    selection = 0
    print('Geometry Calculator')
    print('')
    print('-------------------------------------')
    print('| Calculate Area of Circle      [1] |')
    print('|                                   |')
    print('| Calculate Area of Rectangle   [2] |')
    print('|                                   |')
    print('| Calculate Area of Triangle    [3] |')
    print('|                                   |')
    print('| Cancel                        [4] |')
    print('-------------------------------------')
    selection = input('Please choose calculator or type 4 to cancel:\t')
    ask = True
    while ask:
        if ((not(selection.isdigit()))or((int(selection)<1)or(int(selection)>4))):
            print('Input was not a number or it was less than 1 or greater than 4, try again!')
            selection = input('Please choose calculator or type 4 to cancel:\t')
            ask = True
        else:
            ask = False
    selection = int(selection)
    return selection
def cancelScreen():
    print('Thanks for using our calculator!')
def dimensions():
    num = 0
    num = input('Enter here: \t')
    ask = True
    while ask:
        if not(num.isdigit()):
            print('Input was not a number, try again!')
            num = input('Enter again: \t')
            ask = True
        else:
            ask = False
    num = float(num)
    return num
def calcAreaCircle():
    PI = 3.14
    radius = 0
    print('Enter a radius')
    radius = dimensions()
    areaCircle = (PI*(radius*radius))
    print()
    print('Your radius is', radius,' and the area of your circle is', areaCircle)
def calcAreaRectangle():
    length = 0
    width = 0
    print('Enter a length')
    length = dimensions()
    print('Enter a width')
    width = dimensions()
    area = length * width
    print()
    print('The length was', length,' and the width was', width)
    print('The area of the rectangle is', area)
def calcAreaTriangle():
    HALF = 0.5
    base = 0
    height = 0
    print('Enter a base length')
    base = dimensions()
    print('Enter a height')
    height = dimensions()
    area = HALF * base * height
    print()
    print('The base was', base, 'and the height was', height)
    print("The area of the triangle is",area)
def choice(selection):
    if (selection==1):
        calcAreaCircle()
    elif (selection==2):
        calcAreaRectangle()
    elif (selection==3):
        calcAreaTriangle()
def main():
    selection = 0
    ans = True
    while ans:
        selection = DisplayMenu()
        if (selection != 4):
            choice(selection)
        else:
            print()
            cancelScreen()
            ans = False
    return 0
main()
