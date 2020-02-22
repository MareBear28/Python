car_milage1 = int(input('Enter car 1\'s milage: '))
validate1 = True
while validate1:
    if car_milage1 < 0:
        validate1 = True
        print('Car milage entered was invalid.')
        car_milage1 = int(input('Enter car 1\'s milage: '))
        print()
    else:
        validate1 = False

car_milage2 = int(input('Enter car 2\'s milage: '))
print()
validate2 = True
while validate2:
    if car_milage2 < 0:
        validate2 = True
        print('Car milage entered was invalid.')
        car_milage2 = int(input('Enter car 2\'s milage: '))
        print()
    else:
        validate2 = False

car_cost_gallon1 = float(input('Enter car 1\'s average gas cost per gallon: '))
check = True
while check:
    if car_cost_gallon1 < 0:
        check = True
        print('Car cost per gallon entered was invalid.')
        car_cost_gallon1 = int(input('Enter car 1\'s average gas cost per gallon: '))
        print()
    else:
        check = False

car_cost_gallon2 = float(input('Enter car 2\'s average gas cost per gallon: '))
check2 = True
while check2:
    if car_cost_gallon1 < 0:
        check2 = True
        print('Car cost per gallon entered was invalid.')
        car_cost_gallon2 = int(input('Enter car 2\'s average gas cost per gallon: '))
        print()
    else:
        check2 = False

miles_month = int(input('How many miles do you drive a month?: '))
check3 = True
while check3:
    if car_cost_gallon1 < 0:
        check3 = True
        print('Miles driven in a month entered was invalid.')
        miles_month = int(input('How many miles do you drive a month?: '))
        print()
    else:
        check3 = False

total_car1 = ((miles_month * 12) * car_cost_gallon1) / car_milage1
total_car2 = ((miles_month * 12) * car_cost_gallon2) / car_milage2
difference = 0

if total_car1 > total_car2:
    difference = total_car1 - total_car2
    print('Car 2 will save ${:.2f} in a year'.format(difference))
elif total_car2 == total_car1:
    print('The two cars cost the same')
else:
    difference = total_car2 - total_car1
    print('Car 1 will save ${:.2f} in a year'.format(difference))