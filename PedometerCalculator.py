#Mariel Urbano
#October 10th, 2019
#This program will be able to ask the user to input data, such as, the day of
#the week and the number of steps they took throughout the day, where the steps
#would be used to calculate the distance(in miles) walked and the calories lost
#from walking.
DayofWeek = input("Enter the day of the week. ")
steps = float(input("Enter the number of steps taken thoughout the day. "))
distanceWalked = steps/2000
caloriesLost = distanceWalked*65
print("Day of the week: ", DayofWeek)
print("The distance walked: ", distanceWalked, " miles")
print("The calories lost: ", caloriesLost, " calories")
