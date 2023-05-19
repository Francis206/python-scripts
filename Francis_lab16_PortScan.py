# IT 280 – Lab #16: Extended Hello World Instructions by Francis @ 2022
import re
import socket
from datetime import datetime

import pyfiglet


def is_valid_ip(ip):
    isValid = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    return isValid


def askIPAddress():
    ip = input('Please, inform the host ip address: ')
    while True:
        if is_valid_ip(ip):
            break
        else:
            ip = input('Invalid IP Address. Please, inform a valid ip address: ')
    return ip


def askFileAddress():
    filePath = input('Please, inform the file output address: ')
    while True:
        if filePath:
            break
        else:
            filePath = input('Invalid File Address. Please, inform a valid file address: ')
    return filePath


def scanning(ip):
    list = []
    try:
        for port in range(1, 500):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((ip, port))
            status = ''
            if result == 0:
                status = 'Open'
            else:
                status = 'Closed'
            print("{}:{} is {}".format(ip, port, status))
            list.append("{}:{} is {}".format(ip, port, status))
            s.close()
    except socket.gaierror:
        print("Hostname cannot be resolved.")
    except socket.error:
        print("Server cannot respond.")
    return list


def write(path, lines):
    with open(path, "w") as file:
        file.writelines('\n'.join(lines))


def main():
    pyfiglet.print_figlet('Port Scanner', 'big', 'GREEN')

    ip = askIPAddress()
    file = askFileAddress()
    # file = './test.txt'
    # ip = '127.0.0.1'

    print(' ')
    print('-' * 50)
    print("Scanning Target: " + ip)
    print("Scanning started at: " + str(datetime.now()))
    result = scanning(ip)
    write(file, result)
    print('-' * 50)


main()
