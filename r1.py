import random
import string
import socket
import time
import threading
from const import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(BROKER_TO_R1.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R1_TO_DEST.get_sender())
print("ASFFSADFSAD")
while True:
    data,addr = sock.recvfrom(18)
    print(data)
    sock2.sendto(data,R1_TO_DEST.get_listener())