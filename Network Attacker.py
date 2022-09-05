from scapy.all import *
from scapy.layers.inet import TCP, IP

target = input("Type target: ")

Registered_Ports = range(1, 1023)

open_ports = []


def scanport(port):
    source_rand_port = RandShort()
    conf.verb = 0
    synchronization_packet = sr1(IP(dst=target) / TCP(sport=source_rand_port,
                                                      dport=port, flags="S"), timeout=0.5)

    if str(type(synchronization_packet)) != "class <'NoneType'>":
        pass
    else:
        return False
