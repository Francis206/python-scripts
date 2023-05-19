# IT 280 -  Lab #8: Formatted File Creation Instructions by Francis

import random
import string

letters = list(string.ascii_uppercase)
lineFormat = "{0:5s} {1:4d} {2:4.2f}\n"


def randomChar():
    return ''.join(random.sample(letters, 5))


def randomInt():
    return random.randint(0, 999)


def randomFloat():
    return random.uniform(0, 10000)


def createFile(lines):
    file = open("./value1.txt", "w+")
    file.writelines(lines)
    file.close()


def main():
    lines = []
    for i in range(1, 21):
        line = lineFormat.format(randomChar(), randomInt(), randomFloat())
        lines.append(line)

    createFile(lines)


main()
