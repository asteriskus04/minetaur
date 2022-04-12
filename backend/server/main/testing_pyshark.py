import pyshark
import time


networkInterface = "4"

# define capture object
capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter='tcp')

print("listening on %s" % networkInterface)

for packet in capture.sniff_continuously(packet_count=300):
    # adjusted output
    try:
        # get timestamp
        localtime = time.asctime(time.localtime(time.time()))

        # get packet content
        protocol = packet.transport_layer  # protocol type
        src_addr = packet.ip.src  # source address
        src_port = packet[protocol].srcport  # source port
        dst_addr = packet.ip.dst  # destination address
        dst_port = packet[protocol].dstport  # destination port
        pkt_info = packet.tcp.payload
        # output packet info
        print("%s IP %s:%s <-> %s:%s (%s)     %s" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol, pkt_info))

    except AttributeError as e:
        # ignore packets other than TCP, UDP and IPv4
        pass
    print(" ")
"""

cap = pyshark.LiveCapture(interface='4', bpf_filter='tcp')

cap.sniff(packet_count=10)


def print_dns_info(pkt):
    print('DNS Request from %s: %s' % (pkt.ip.src, pkt.tcp.payload))


cap.apply_on_packets(print_dns_info, timeout=100)
"""