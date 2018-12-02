# ceng435 Term Project Part 1
# Ozan Incesulu, 2099711
# Can Duran Unaldi, 2036523

This project constists of 6 python scripts:
* broker.py
* const.py
* destination.py
* r1.py
* r2.py
* source.py

The detailed explanations of each script can be found inside their comments.

The project cloned into the slices. The running order of the slices in order to minimize(to 0) the packet loss caused by the execution:
* broker.py from b
* destination.py from d 
* r1.py from r1
* r2.py from r2
* source.py from s

The importance is to start the s at final.

The files are doing the following work:

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


# EXPERIMENTS

We take tc qdisc change dev eth0 root netem delay 20ms 5ms distribution normal code as a base for our experiments.

The eth0 changes in each link. We found which eth can be used by using ifconfig.

# Experiment 1

In this experiment we used the following commands:

At b:
sudo tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
sudo tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal

At r1:
sudo tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal

At r2:
sudo tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal

Note: You can use change command instead of add if you already have tc at the slices.

The experiment results comming from the d stored at results.csv

# Experiment 2

In this experiment we used the following commands:

At b:
sudo tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
sudo tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal

At r1:
sudo tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal

At r2:
sudo tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal

Note: change command used since we've already added tc to the slices.


# Experiment 3

In this experiment we used the following commands:

At b:
sudo tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
sudo tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal

At r1:
sudo tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal

At r2:
sudo tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal

Note: change command used since we've already added tc to the slices.


# Usefull Commands

* To close the running python script. (The Ctrl+C does not work for scripts using threads)
ps aux | grep python | grep -v "grep python" | awk '{print $2}' | xargs kill -9 

* To ensure the closing
pkill python

* To get the data from the d slice without pushing it to git.
cat result.csv