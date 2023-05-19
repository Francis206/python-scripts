# IT 280 –  Lab #9: File Modification Instructions by Francis

from os import path
lineFormat = "{0:2d}. {1} Sample\n"


def readFile():
    lines = []
    if path.exists('./value.txt'):
        with open('./value.txt') as file:
            lines = file.read().splitlines()
        file.close()
    return lines


def createFile(lines):
    file = open("./value2.txt", "w+")
    file.writelines(lines)
    file.close()


def main():
    lines = readFile()
    for i in range(len(lines)):
        lines[i] = lineFormat.format(i, lines[i])
    createFile(lines)


main() 
