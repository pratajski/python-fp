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
        if synchronization_packet.haslayer(TCP):
            if synchronization_packet.getlayer(TCP).flags == 0x12:
                print(f'Port: {port} is available')
                sr(IP(dst=target) / TCP(sport=source_rand_port, dport=port, flags='R'), timeout=2)
                return True
            else:
                print(f'Port: {port} is closed')
                return False
        else:
            return False
    else:
        return False


