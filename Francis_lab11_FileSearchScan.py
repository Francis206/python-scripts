# IT 280 - IT 280 – Lab #11: File Search using Strings Instructions by Francis @ 2022

from os import path


def readFile():
    lines = []
    if path.exists('./numbers.txt'):
        with open('./numbers.txt') as file:
            lines = file.read().splitlines()
        file.close()
    return lines


def isPhoneValid(value):
    value = value.replace('1.', '', 1)
    value = value.replace('1-', '', 1)
    value = value.replace('(', '')
    value = value.replace(')', '')
    if len(value) != 12:
        return False
    for i in range(0, 2):
        if not value[i].isdecimal():
            return False
    if value[3] != '.' and value[3] != '-':
        return False
    for i in range(4, 6):
        if not value[i].isdecimal():
            return False
    if value[7] != '.' and value[3] != '-':
        return False
    for i in range(8, 11):
        if not value[i].isdecimal():
            return False
    return True


def isZipCodeValid(value):
    if len(value) != 5:
        return False
    for i in range(0, 5):
        if not value[i].isdecimal():
            return False
    return True


def isSSNValid(value):
    if len(value) != 11:
        return False
    for i in range(0, 2):
        if not value[i].isdecimal():
            return False
    if value[3] != '.' and value [3] != '-':
        return False
    for i in range(4, 5):
        if not value[i].isdecimal():
            return False
    if value[6] != '.' and value[6] != '-':
        return False
    for i in range(7, 10):
        if not value[i].isdecimal():
            return False
    return True


def main():
    lines = readFile()
    for line in lines:
        if isPhoneValid(line):
            print('{0:20} is a Phone Number'.format(line))
        elif isSSNValid(line):
            print('{0:20} is a Social Security Number'.format(line))
        elif isZipCodeValid(line):
            print('{0:20} is a Zip Code Number'.format(line))
        else:
            print('{0:20} is Undefined'.format(line))

main()
