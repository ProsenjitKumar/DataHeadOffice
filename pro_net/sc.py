# An example script to connect to Google using socket
# programming in Python
# import socket  # for socket
# import sys
#
# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket successfully created")
# except socket.error as err:
#     print("socket creation failed with error %s" % (err))
#
# # default port for socket
# port = 80
#
# try:
#     host_ip = socket.gethostbyname('www.prosenjit-das.herokuapp.com.com')
# except socket.gaierror:
#
#     # this means could not resolve the host
#     print("there was an error resolving the host")
#     sys.exit()
#
# # connecting to the server
# s.connect((host_ip, port))
#
# print("the socket has successfully connected to google \
# on port == %s" % (host_ip) )

# 54.175.179.21
# 74.125.130.104
# 79.124.78.120 78.142.29.210


# first of all import the socket library
# import socket
#
# # next create a socket object
# s = socket.socket()
# print("Socket successfully created")
#
# # reserve a port on your computer in our
# # case it is 12345 but it can be anything
# port = 12345
#
# # Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests
# # coming from other computers on the network
# s.bind(('', port))
# print("socket binded to %s" % (port))
#
# # put the socket into listening mode
# s.listen(5)
# print("socket is listening")
#
# # a forever loop until we interrupt it or
# # an error occurs
# while True:
#     # Establish connection with client.
#     c, addr = s.accept()
#     print('Got connection from', addr)
#
#     # send a thank you message to the client.
#     c.send(4)
#
#     # Close the connection with the client
#     c.close()

# ------------------------------------- find local ip ----------------------
# import socket
# ip_addr = socket.gethostbyname(socket.gethostname()) # localhost
# print(ip_addr)



# --------------------------------- find ip address ethernet -----------
import ipaddress
import socket, subprocess
from subprocess import PIPE, Popen
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
print("ip address",s.getsockname())
s.close()

# try:
#     network = ipaddress.IPv4Network(ip_address)
#     print(network)
# except ValueError:
#     print('address/netmask is invalid for IPv4:', ip_address)
#


# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
# print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])


from netifaces import interfaces, ifaddresses, AF_INET
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    #addr_with_port = (ifaceName, ', '.join(addresses)
    print('%s: %s' % (ifaceName, ', '.join(addresses)))

# ------------------------------ Local Ip or Localhost ----------------
import socket, os

if os.name != "nt":
    import fcntl
    import struct
    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', bytes(ifname[:15], 'utf-8'))
                # Python 2.7: remove the second argument for the bytes call
            )[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break;
            except IOError:
                pass
    return ip


print(get_lan_ip())


# -----------------------------  - Get MAC address of only the connected local NIC
# network = ipaddress.ip_network('192.168.100.0/24')
# for i in network.hosts():
#     i=str(i)
#     toping = Popen(['ping', '-c', '3', i], stdout=PIPE)
#     output = toping.communicate()[0]
#     hostalive = toping.returncode
#     if hostalive == 0:
#         print(i, "is reachable")
#     else:
#         print(i, "is unreachable")


'''
# ------------------------------------------- mapping my own network area

import os
import socket
import multiprocessing
import subprocess
import os


def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """

    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


if __name__ == '__main__':

    print('Mapping...')
    lst = map_network()
    print(lst)
    
'''

'''
# import scanip.scanip
#
# scanip.scanip.start_scan()

# import requests
# url = 'http://messi-fan.org/post'
# files = {'file': open('image.png', 'rb')}
# r = requests.post(url, files=files)
'''
# find out mac address or something where i can send data by ip address ----------------------------------------------

























