import pyshark
import json
import re
import os

data_json = {}
server = {

        "id": "Server",
        "height": 70,
        "fill": {
            "src": "static/main/img/server_icon.png"
        }
    }




def pc_data(ip_points, check_point, pcnum):
    id = ''
    status = ''
    ip = ''
    mac = ''
    height = 0
    fill = ''
    pc = {
        "id": "PC_1_" + str(pcnum),
        "status": check_point,
        "ip": ip_points,
        "mac": "28:E9:46:6C:58:EF",
        "height": 60,
        "fill": {
            "src": "static/main/img/device_suspect_icon.png"
        }
    }
    edg = {
        "from": "Server",
        "to": "PC_1_" + str(pcnum),
    }
    write_nodes_edges(pc, edg)


def write_nodes_edges(pc_data, edg):
    try:
        nodes = json.load(open('main/static/main/js/nodes.json'))
        edges = json.load(open('main/static/main/js/edges.json'))
    except:
        nodes = []
        edges = []

    nodes.append(pc_data)
    edges.append(edg)

    with open('main/static/main/js/nodes.json', 'w') as file:
        json.dump(nodes, file, indent=2, ensure_ascii=False)
    with open('main/static/main/js/edges.json', 'w') as file:
        json.dump(edges, file, indent=2, ensure_ascii=False)


def write_itog():

    try:
        nodes = json.load(open('main/static/main/js/nodes.json'))
        edges = json.load(open('main/static/main/js/edges.json'))
    except:
        nodes = []
        edges = []

    itog = {
        'nodes': nodes,
        'edges': edges
    }
    with open('main/static/main/js/data1.json', 'w') as file:
        json.dump(itog, file, indent=4, ensure_ascii=False)

    



def scan():
    global check_point
    networkInterface = "5"
    pcnum = 0
    ip_points = ''
    ip_points_1 = ''
    check_point = 0
    # define capture object
    print("listening on %s" % networkInterface)
    capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter='tcp')
    with open('main/static/main/js/nodes.json', 'w') as file:
        json.dump(server, file, indent=4, ensure_ascii=False)
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
                pcnum += 1
                check_point = 'Возможен майнинг!'
                pc_data(src_addr, check_point, pcnum)
                # ip_points_1 += dst_addr

            # output packet info
            if len(pkt_info) > 5:
                print("IP %s <-> %s" % (
                    src_addr, dst_addr))

        except AttributeError as e:
            # ignore packets other than TCP, UDP and IPv4
            pass
        write_itog()
    return check_point, ip_points
