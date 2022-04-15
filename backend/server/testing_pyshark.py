import pyshark
import json
import re

data_json={}

def gen_data(ip_points, check_point):
    id = ''
    status = ''
    ip = ''
    mac = ''
    height = 0
    fill = ''

    pc = {
        "id": "PC_1_1",
        "status": check_point,
        "ip": ip_points,
        "mac": "28:E9:46:6C:58:EF",
        "height": 60,
        "fill": {
            "src": "static/main/img/device_icon.png"
        }
    }
    return pc

def write_json(pc_data):
    try:
        data = json.load(open('persons.json'))
    except:
        data = []

    data.append(pc_data)

    with open('persons.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)






def scan():
    global check_point
    networkInterface = "5"
    ip_points = ''
    ip_points_1 = ''
    check_point = 0
    # define capture object
    print("listening on %s" % networkInterface)
    capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter='tcp')
    for packet in capture.sniff_continuously(packet_count=50):
        # adjusted output
        try:
            # get packet content
            src_addr = packet.ip.src  # source address
            dst_addr = packet.ip.dst  # destination address
            pkt_info = packet.tcp.payload
            # hex to utf
            hex_split = pkt_info.replace(':', '')

            # mining = '6d696e696e67'
            mining = '6d'

            if re.search(mining, hex_split, flags=0):
                check_point = 'Майнинг'
                ip_points += src_addr
                #ip_points_1 += dst_addr



            # output packet info
            if len(pkt_info) > 5:
                print("IP %s <-> %s (%s)" % (
                    src_addr, dst_addr, hex_split))

        except AttributeError as e:
            # ignore packets other than TCP, UDP and IPv4
            pass
        write_json(gen_data(ip_points,check_point))
    return check_point, ip_points


