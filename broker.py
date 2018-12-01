import random
import string
import socket
import time
import threading
from const import *


random = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(BROKER.get_listener())
sock.listen(5)
print("AFSADFSAD")
print(ROUTER_1.get_listener())
conn, addr = sock.accept()
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(ROUTER_1.get_sender())
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3.bind(ROUTER_2.get_sender())
print("2")
while 1:
    data = conn.recv(18).decode()
    print "received data:", data
    if random == 0:
        sock2.sendto(data, ROUTER_1.get_listener())
        data,addr = sock2.recvfrom(21)
        print "R1 Response", data
        random = 1
    elif random == 1:
        sock3.sendto(data, ROUTER_2.get_listener())
        data,addr = sock3.recvfrom(21)
        print "R1 Response", data
        random = 0



    
conn.close()