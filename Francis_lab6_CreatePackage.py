# IT280 - Lab6 Package Creation Lab by Francis

def sortHigh(list):
    list.sort()


# Sort list
def sortLow(list):
    list.sort(reverse=True)


# Remove duplicates
def removeDuplicate(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist


def main():
    # Control variable to quit the program/loop
    option = ''
    list = []
    while option != '0':
        # Print the menu
        print()
        print('Menu:')
        print('\t1. Add an alphabet')
        print('\t2. Show Sorted List')
        print('\t0. Exit')
        option = input('Option: ')
        print()

        if option == '1':
            value = str(input('Please, inform an alphabet: '))
            list.append(value)
            for i in range(len(list)):
                print('Index: ' + str(i) + ', Value: ' + str(list[i]))
        if option == '2':
            sortHigh(list)
            list = removeDuplicate(list)
            print('Here you are your unique ordered listed high: ' + str(list))

            sortLow(list)
            print('Here you are your unique ordered listed low: ' + str(list))

        elif len(list) == 0 and option == '0':
            print('\nEmpty list is not allowed. Please, inform at least one value.')
            option = ''
        


main()
