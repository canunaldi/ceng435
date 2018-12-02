import random
import string
import socket
import time
import threading
from const import *


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new socket that gets data from the broker
sock.bind(BROKER_TO_R2.get_listener()) # Socket listens from the Broker 
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # new socket will be used to send the data to the destination and get the acknowledge from the destination
sock2.bind(DEST_TO_R2.get_sender()) # Socket listens from the Destination in order to get the acknowlege
print("ASFFSADFSAD") # Test issues
while True:
    data,addr = sock.recvfrom(18) # Get the data coming from the Broker and store it to the data
    print(data) # Test issues
    sock2.sendto(data,R2_TO_DEST.get_listener()) # Send the incoming data to the destination.
    ack,addr = sock2.recvfrom(3) # Get the acknowledge from the destination
    print(ack) # Test issues
    sock.sendto(ack,R2_TO_BROKER.get_sender()) # Send the acknowledge to the Broker
