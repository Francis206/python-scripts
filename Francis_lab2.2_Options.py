# IT280 Lab2.2
import sys
# Area of Circle
def areacircle(radius):
    return 3.14159 * (radius * radius)


# Area of square.
def areasquare(side):
    return side * side

# MPG for a vehicle
def mpg(miles, gallons):
    return miles / gallons

# Hourly work per week
def totalhour(hours):
    return sum(hours)


def main():
    # Control variable to quit the program/loop
    option = ''
    while option != '0':
        # Print the menu
        print()
        print('Menu:')
        print('\t1. Calculate Area of a Circle')
        print('\t2. Calculate Area of a Square')
        print('\t3. Calculate MPG for a vehicle')
        print('\t4. Calculate Total Hour Worked in a Week')
        print('\t0. Exit')
        option = input('Option: ')

        result = ''
        if option == '1':
            value = int(input('Input radius of a circle: '))
            result = areacircle(value)
        elif option == '2':
            value = int(input('Input length side of a square: '))
            result = areasquare(value)
        elif option == '3':
            value1 = int(input('Total miles driven per tank: '))
            value2 = int(input('Tank capacity (gallon): '))
            result = mpg(value1, value2)
        elif option == '4':
            values = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
            listHours = []
            for i in range(7):
                listHours.append(int(input('Input the total hour you work this day ' + values.get(i) + ': ')))
            result = totalhour(listHours)
        elif option == '0':
            sys.exit('Thank you for using my program!')

        print('The operation result is: ' + str(result))

main()
