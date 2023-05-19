import os
import subprocess

# Function defines the target scan

def nmap(host):

    # Stores results into a text file
    out = open('nmapscan.txt', 'a')

    cmd = ['nmap', '-sV', host]

    return subprocess.call(cmd, stdout = out)
    return subprocess.call(cmd)
    out.close()

host = input('what IP would you like to Scan? ')
print(nmap(host))

