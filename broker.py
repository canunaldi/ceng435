import random
import string
import socket
import time
import threading
from const import *

random = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SOURCE_TO_BROKER.get_listener())
sock.listen(5)
conn, addr = sock.accept()
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R1_TO_BROKER.get_sender())
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3.bind(R2_TO_BROKER.get_sender())
print("2")
while 1:
    data = conn.recv(18).decode()
    print "received data:", data
    if random == 0:
        sock2.sendto(data, BROKER_TO_R1.get_listener())
        random = 1
    elif random == 1:
        sock3.sendto(data, BROKER_TO_R2.get_listener())
        random = 0



    
conn.close()