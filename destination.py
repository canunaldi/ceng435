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
        starttime = data[5:]
        print(data[:4])
        starttime = str (starttime)
        starttime = int (starttime)
        end_to_end = currenttime - starttime
        print (end_to_end)
        ack = "OK!"
        sock.sendto(ack, DEST_TO_R1.get_sender())
        print("ACK SENT!")

def receive_r2():
    while True:
        data,addr = sock2.recvfrom(18)
        currenttime = time.time()
        currenttime = currenttime * 1000
        currenttime = int (currenttime)
        starttime = data[:13]
        print(data[:4])
        starttime = str (starttime)
        starttime = int (starttime)
        end_to_end = currenttime - starttime
        print (end_to_end)
        ack = "OK!"
        sock.sendto(ack, DEST_TO_R2.get_sender())
    

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(R1_TO_DEST.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R2_TO_DEST.get_listener())

th1 = threading.Thread(target= receive_r1, args=())
th2 = threading.Thread(target= receive_r2, args=())

th1.start()
th2.start()



