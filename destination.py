import random
import string
import socket
import time
import threading
from const import *


def receive_r1():
    while True:
        data,addr = sock.recvfrom(18)
        currenttime = time.time()
        currenttime = currenttime * 1000
        currenttime = int (currenttime)
        starttime = data[:13]
        print("START:", starttime)
        print("END:", currenttime)
        starttime = str (starttime)
        starttime = int (starttime)
        end_to_end = currenttime - starttime
        print (end_to_end)

def receive_r2():
    while True:
        data,addr = sock2.recvfrom(18)
        currenttime = time.time()
        currenttime = currenttime * 1000
        currenttime = int (currenttime)
        starttime = data[:13]
        print("START:", starttime)
        print("END:", currenttime)
        starttime = str (starttime)
        starttime = int (starttime)
        end_to_end = currenttime - starttime
        print (end_to_end)
    

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(R1_TO_DEST.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R2_TO_DEST.get_listener())

th1 = threading.Thread(target= receive_r1, args=())
th2 = threading.Thread(target= receive_r2, args=())

th1.start()
th2.start()



