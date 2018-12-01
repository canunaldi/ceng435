class Route:
    def __init__(self, ip, incoming_port, outgoing_port):
        self._ip = ip
        self._iport = incoming_port
        self._oport = outgoing_port

    def get_listener(self):
        return self._ip, self._iport

    def get_sender(self):
        return self._ip, self._oport


LOCALHOST = "127.0.0.1"
SOURCE_TO_BROKER = Route(10.10.1.2,3000,3001)
BROKER_TO_R1 = Route(10.10.2.2,3002,3003)
BROKER_TO_R2 = Route(10.10.4.2,3004,3005)
R1_TO_DEST = Route(10.10.3.2,3006,3007)
R2_TO_DEST = Route(10.10.5.2,3008,3009)
SOURCE = Route(LOCALHOST, 3001, 3002)
BROKER = Route(LOCALHOST, 3003, 3004)
ROUTER_1 = Route(LOCALHOST, 3005, 3006)
ROUTER_2 = Route(LOCALHOST, 3007, 3008)
DESTINATION = Route(LOCALHOST, 3009, 3010)
DESTINATION2 = Route(LOCALHOST, 3011, 3012)


PACKET_SIZE = 18