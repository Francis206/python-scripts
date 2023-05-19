# IT 280 – Lab #4: List Manipulation Lab by Frfancis

# define the type of list
def sort(list):
    list.sort(key=int)


# add to list and remove the duplicate
def removeDuplicate(list):
    addlist = []
    for i in list:
        if i not in addlist:
            addlist.append(i)
    return addlist


# Main method to add number
option = ''
list = []
while option != '0':
    # The main manu output
    print()
    print('Menu:')
    print('\t1. Add number to a list')
    print('\t0. Exit')
    option = input('Option: ')
    print()
    # Option's conditions
    if option == '1':
        value = int(input('Enter a number: '))
        list.append(value)
        for i in range(len(list)):
            print('Index: ' + str(i) + ', Value: ' + str(list[i]))
    while len(list) == 0 and option == '0':
        print('\nInvalid, please enter a number.')
        option = ''
    #print the list output
sort(list)
list = removeDuplicate(list)
print('Here is the list: ' + str(list))

