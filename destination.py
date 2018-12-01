import random
import string
import socket
import time
import threading
from const import *


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(DESTINATION.get_listener())
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(DESTINATION2.get_listener())

th = threading.Thread(target= receive_r1, args=(sock))





def receive_r1():
    