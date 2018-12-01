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
SOURCE = Route(LOCALHOST, 3001, 3002)
BROKER = Route(LOCALHOST, 3003, 3004)
ROUTER_1 = Route(LOCALHOST, 3005, 3006)
ROUTER_2 = Route(LOCALHOST, 3007, 3008)
DESTINATION = Route(LOCALHOST, 3009, 3010)
DESTINATION2 = Route(LOCALHOST, 3011, 3012)


PACKET_SIZE = 18