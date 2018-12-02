# ceng435 Term Project Part 1

This project constists of 6 python scripts:
* broker.py
* const.py
* destination.py
* r1.py
* r2.py
* source.py

The detailed explanations of each script can be found inside their comments.

# source.py

The source file connects to the "s" node in our slice. The main object of this script is to send the packet to the broker(aim = is to send to the destination). Waits for the acknowledge and sends another packet after gets the acknowledge.

# const.py

This file consists of the constants that we use always. The constants are IP and port numbers represented as a class called Route.

# broker.py

This file connects to the "b" node in our slice. The main object of this file is to send the packet coming from the source (get the packet) and by choosing between r1 and r2 send the incoming packet to one of them. And get the acknowledge from the r1 or r2 and send it to the source

# r1.py

This file connects to the "r1" node in our slice. This file gets the packet coming from the broker and redirects it to the destination. And get the acknowledge from the destination and send to the broker.

# r2.py

This file connects to the "r2" node in our slice. And does exactly same things with r1.

# destination.py

This file connects to the "destination" node in our slice. By using threading, gets the packet from the r1 and r2 and calculates the end_to_end delay. The result stored into a csv file and used for experiments. After calculations sends the acknowledge to r1/r2 (from which the packet came).