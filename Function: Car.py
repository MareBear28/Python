def menu():
    print('')
    print('Main Menu:')
    print(' {}'.format('1. Cost of Gas'))
    print(' {}'.format('2. Used Value'))
    print(' {}'.format('3. Stopping Distance'))
    print(' {}'.format('4. Quit'))
    selection = raw_input('Choose a function from the list:\n')
    ask = True
    while ask:
        if (not(selection.isdigit())) or (int(selection) < 1 or int(selection) > 4 or int(selection) == 0):
            print('Error: Invalid input. Please try again.')
            print('')
            selection = raw_input('Choose a function from the list:\n')
            ask = True
        else:
            break
    selection = int(selection)
    return selection

def user_inputs(word):
    num = 0
    num = raw_input('Enter {}: \t'.format(word))
    ask = True
    while ask:
        if ((float(num) < 1) or (float(num) == 0)):
            print('Invalid input. Input either not an integer or not a positive number. Try again')
            print('')
            num = raw_input('Enter {}: \t'.format(word))
            ask = True
        else:
            break
    num = float(num)
    return num

def Cost_Gas():
    mileage_1 = user_inputs('car 1\'s mileage')
    mileage_2 = user_inputs('car 2\'s mileage')
    cost_1 = user_inputs('car 1\'s average gas cost per gallon')
    cost_2 = user_inputs('car 2\'s average gas cost per gallon')
    miles_per_month = user_inputs('how many miles you drive a month')

    total_1 = ((miles_per_month * 12) / mileage_1) * cost_1
    #print(total_1)
    total_2 = ((miles_per_month * 12) / mileage_2) * cost_2
    #print(total_2)
    
    if total_1 > total_2:
        diff = total_1 - total_2
        print('Car 2 will save ${:.2f} in a year'.format(diff))
    elif total_2 > total_1:
        diff = total_2 - total_1
        print('Car 1 will save ${:.2f} in a year'.format(diff))
    else:
        print('Both cars will cost the same')

def Used_Value():
    original = user_inputs('original car price')
    years = user_inputs('number of years')
    new_price = original
    for i in range(1,int(years) + 1):
        new_price = new_price - (new_price * .18)
        print('Year {} value: ${:.2f}'.format(i, new_price))

def Stopiing_Dist():
    speed = user_inputs('initial speed')
    tire_condition = int(user_inputs('tire condition (1 = new, 2 = good, 3 = poor'))
    speed = (speed * 5280) / 3600
    if tire_condition == 1:
        mew = 0.8
        condition = 'new'
    elif tire_condition == 2:
        mew = 0.6
        condition = 'good'
    elif tire_condition == 3:
        mew = 0.5
        condition = 'poor'

    top = speed ** 2
    bottom = 2 * mew * 32.174
    distance = top / bottom
    print('At {:.1f} miles per hour with {} tires, the car will stop in {:.2f} feet away '.format(speed, condition ,distance))

def main():
    selection = 0
    while True:
        selection = menu()
        if selection == 1:
            Cost_Gas()
        elif selection == 2:
            Used_Value()
        elif selection == 3:
            Stopiing_Dist()
        else:
            break

main()