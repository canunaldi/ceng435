import random
import string
import socket
import time
import threading
from const import *
import csv


result_datas = []

def receive_r1():
    while True:
        data,addr = sock.recvfrom(18)
        print(data)
        currenttime = time.time()
        currenttime = currenttime * 1000
        currenttime = int (currenttime)
        starttime = data[5:]
        print(data[:4])
        print(starttime)
        starttime = int (starttime)
        end_to_end = currenttime - starttime
        result_datas.append(end_to_end)

        ack = "OK!"
        sock.sendto(ack, DEST_TO_R1.get_sender())
        if data[:4] == '3999':
            print("GIRDIM")
            with open('result.csv', 'wb') as csvfile:
                patcher = csv.writer(csvfile, dialect='excel')
                patcher.writerow(result_datas)             


# Same work done for R1 at receive_r1 but this time for the data coming from the R2
def receive_r2():
    while True:
        data,addr = sock2.recvfrom(18)
        print(data)
        currenttime = time.time()
        currenttime = currenttime * 1000
        currenttime = int (currenttime)
        starttime = data[5:]
        print(data[:4])
        print(starttime)
        starttime = str (starttime)
        starttime = int (starttime)
        end_to_end = currenttime - starttime
        result_datas.append(end_to_end)
        ack = "OK!"
        sock2.sendto(ack, DEST_TO_R2.get_sender())
        if data[:4] == '3999':
            with open('result.csv', 'wb') as csvfile:
                patcher = csv.writer(csvfile, dialect='excel')
                patcher.writerow(result_datas)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(R1_TO_DEST.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R2_TO_DEST.get_listener())

th1 = threading.Thread(target= receive_r1, args=())
th2 = threading.Thread(target= receive_r2, args=())

th1.start()
th2.start()



