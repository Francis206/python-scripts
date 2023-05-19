import os
import subprocess

# Function that defines the Nikto scan
   
def nikto(host):

    # Stores the open text file into the 'out' var

    out = open('NiktoScan.txt', 'a')
   
    # Stores the terminal command into thee 'cmd' var

    cmd = ['nikto', '-h',  host]

    # Returns varibles

    return subprocess.call(cmd, stdout = out)
     
    return subprocess.call(cmd)
   
    # close txt file

    out.close()
     
host = input('What IP would you like to scan?\nTarget IP: ')

print ('Results will be scored in NiktoScan.txt')

print(nikto(host))

