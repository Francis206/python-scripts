# IT 280 – Lab #12: File Search using Regular Expressions Instructions by Francis @ 2022

from os import path
import re

ssnRegex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"
zipCode = "^(\d{5})([-])?(\d{4})?"
phoneRegex = re.compile('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}')


def readFile():
    lines = []
    if path.exists('./numbers.txt'):
        with open('./numbers.txt') as file:
            lines = file.read().splitlines()
        file.close()
    return lines


def isPhoneValid(value):
    if re.search(phoneRegex, value):
        return True
    else:
        return False


def isZipCodeValid(value):
    if re.search(zipCode, value):
        return True
    else:
        return False


def isSSNValid(value):
    if re.search(ssnRegex, value):
        return True
    else:
        return False


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
