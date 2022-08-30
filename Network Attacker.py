from scapy.all import *

target = input("Type target: ")

Registered_Ports = []
for i in range(1, 1024):
    Registered_Ports.append(i)

open_ports = []

def scanport(port):
    source_rand_port = RandShort()
    return rand_port
    conf.verb = 0
    synchronization_packet = sr1(IP(dst=target) / TCP(sport=source_rand_port,
                                dport=port, flags = "S"), timeout=0.5)

