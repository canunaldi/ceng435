import random
import string
import socket
import time
import threading
from const import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(R1_TO_DEST.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R2_TO_DEST.get_listener())

th1 = threading.Thread(target= receive_r1, args=())
th2 = threading.Thread(target= receive_r2, args=())




def receive_r1():
    data,addr = sock.recvfrom(18)
    print(data)

def receive_r2():
    data,addr = sock2.recvfrom(18)
    print(data)
    