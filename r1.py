import random
import string
import socket
import time
import threading
from const import *


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new Socket
sock.bind(BROKER_TO_R1.get_listener()) # Socket listens Broker
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new Socket
sock2.bind(DEST_TO_R1.get_sender()) # Socket listens Destination for acknowledge and send data to the destination
print("ASFFSADFSAD") # Test issues
while True:
    data,addr = sock.recvfrom(18)  # Receive data coming from the Broker and store into the variable data
    print(data) # Test issues
    sock2.sendto(data,R1_TO_DEST.get_listener()) # Send the incoming data to the Destionation
    ack,addr = sock2.recvfrom(3) # Wait for the acknowledge coming from the destination
    print(ack) # Test issues
    sock.sendto(ack,R1_TO_BROKER.get_sender()) # Send the acknowledge back to the Broker