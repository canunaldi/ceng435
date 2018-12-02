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
        result_datas.append(data)
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
        if data[:4] == 2999:
            with open('names.csv', 'w') as csvfile:
                fieldnames = ['id', 'time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for var in result_datas:
                    writer.writerow({'id': var[:4], 'time': var[5:]})


def receive_r2():
    while True:
        data,addr = sock2.recvfrom(18)
        result_datas.append(data)
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
        sock2.sendto(ack, DEST_TO_R2.get_sender())
        if data[:4] == 2999:
            with open('names.csv', 'w') as csvfile:
                fieldnames = ['id', 'time']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for var in result_datas:
                    writer.writerow({'id': var[:4], 'time': var[5:]})

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(R1_TO_DEST.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(R2_TO_DEST.get_listener())

th1 = threading.Thread(target= receive_r1, args=())
th2 = threading.Thread(target= receive_r2, args=())

th1.start()
th2.start()



