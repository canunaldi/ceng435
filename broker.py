import random
import string
import socket
import time
import threading
from const import *

print("2")

random = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SOURCE_TO_BROKER.get_listener())
sock.listen(5)
conn, addr = sock.accept()
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R1_TO_BROKER.get_sender())
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3.bind(R2_TO_BROKER.get_sender())
while 1:
    data = conn.recv(18).decode()
    if not data:
        break
    print "received data:", data
    if random == 0:
        sock2.sendto(data, BROKER_TO_R1.get_listener())
        random = 1
        ack,addr = sock2.recvfrom(3)
        conn.send(ack)
        print(ack)

    elif random == 1:
        sock3.sendto(data, BROKER_TO_R2.get_listener())
        random = 0
        ack,addr = sock3.recvfrom(3)
        conn.send(ack)
        print(ack)


    
conn.close()