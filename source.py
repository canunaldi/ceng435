import random
import string
from socket import socket, AF_INET, SOCK_STREAM
import time
import threading
from const import *


id = 999
def generate_random_message():
    # TODO: Maybe meaningful stuff
    global id
    currtime = time.time()
    currtime = currtime * 1000
    currtime = int (currtime)
    id +=1
    return "".join(str(id)+ " " + str(currtime))


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(SOURCE_TO_BROKER.get_listener())
while id<1040:
    message = generate_random_message()
    print(message)
    sock.send(message.encode())  # TODO: Maybe send parts instead of whole message?
    time.sleep(0.2)
    ack = sock.recv(3)
    print(ack)