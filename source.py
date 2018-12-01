import random
import string
from socket import socket, AF_INET, SOCK_STREAM
import time
import threading
from const import BROKER


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
print(BROKER.get_listener())
sock.connect(BROKER.get_listener())
print("fasasd")
while True:
    message = generate_random_message()
    print(message)
    sock.send(message.encode())  # TODO: Maybe send parts instead of whole message?
    time.sleep(0.2)