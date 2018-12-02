import random
import string
import socket
import time
import threading
from const import *


BROKER_LIST = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new socket that gets data from the broker
BROKER_LIST.bind(BROKER_TO_R2.get_listener()) # Socket listens from the Broker 
DEST_RECV_R2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new socket will be used to send the data to the destination and get the acknowledge from the destination
DEST_RECV_R2.bind(DEST_TO_R2.get_sender()) # Socket listens from the Destination in order to get the acknowlege
print("ASFFSADFSAD") # Test issues
while True:
    data,addr = BROKER_LIST.recvfrom(18) # Get the data coming from the Broker and store it to the data
    print(data) # Test issues
    DEST_RECV_R2.sendto(data,R2_TO_DEST.get_listener()) # Send the incoming data to the destination.
    ack,addr = DEST_RECV_R2.recvfrom(3) # Get the acknowledge from the destination
    print(ack) # Test issues
    BROKER_LIST.sendto(ack,R2_TO_BROKER.get_sender()) # Send the acknowledge to the Broker
