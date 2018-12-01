import random
import string
import socket
import time
import threading
from const import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ROUTER_1.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(DESTINATION2.get_sender())
print("ASFFSADFSAD")
while True:
    data,addr = sock.recvfrom(18)
    print(data)
    sock.sendto(data,DESTINATION2.get_listener())