import random
import string
import socket
import time
import threading
from const import *

  
BROKERLIST = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new Socket
BROKERLIST.bind(BROKER_TO_R1.get_listener()) # Socket listens Broker
DEST_RECVSOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new Socket
DEST_RECVSOCK.bind(DEST_TO_R1.get_sender()) # Socket listens Destination for acknowledge and send data to the destination
print("ASFFSADFSAD") # Test issues
while True:
    data,addr = BROKERLIST.recvfrom(18)  # Receive data coming from the Broker and store into the variable data
    print(data) # Test issues
    DEST_RECVSOCK.sendto(data,R1_TO_DEST.get_listener()) # Send the incoming data to the Destionation
    ack,addr = DEST_RECVSOCK.recvfrom(3) # Wait for the acknowledge coming from the destination
    print(ack) # Test issues
    BROKERLIST.sendto(ack,R1_TO_BROKER.get_sender()) # Send the acknowledge back to the Broker