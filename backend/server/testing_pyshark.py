import pyshark
import time
import re



def scan(check_point):
    networkInterface = "4"

    # define capture object
    print("listening on %s" % networkInterface)
    capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter='tcp')
    for packet in capture.sniff_continuously(packet_count=50):
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
            # hex to utf

            hex_split = pkt_info.replace(':', '')

            mining = '6d696e696e67'
            check_point = 0
            if re.search(mining, hex_split, flags=0):
                print('УРА')
                check_point = 1

            # output packet info
            if len(pkt_info) > 5:
                print("%s IP %s:%s <-> %s:%s (%s)     %s" % (
                    localtime, src_addr, src_port, dst_addr, dst_port, protocol, hex_split))

            ##pkt_info = bytes.fromhex(pkt_info)
            ##print(pkt_info.decode('utf-8'))
            """
            dir(packet)  # for entire packet
            dir(packet.ip)  # for ip layer
            dir(packet.tcp)  # for tcp layer
            print(packet.tcp)  # one way
            packet.tcp.pretty_print()
            """

        except AttributeError as e:
            # ignore packets other than TCP, UDP and IPv4
            pass
    return check_point
    """
    
    cap = pyshark.LiveCapture(interface='4', bpf_filter='tcp')
    
    cap.sniff(packet_count=10)
    
    
    def print_dns_info(pkt):
        print('DNS Request from %s: %s' % (pkt.ip.src, pkt.tcp.payload))
    
    
    cap.apply_on_packets(print_dns_info, timeout=100)
    """
