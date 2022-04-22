import pyshark
import json
import re
from arp import arp_search

server = {

    "id": "Server",
    "height": 70,
    "fill": {
        "src": "static/main/img/server_icon.png"
    }
}

listarp = arp_search()
print(listarp)
print(len(listarp))


def pc_data(ip_points, check_point, pcnum, src):
    pc = {
        "id": "PC_1_" + str(pcnum),
        "status": str(check_point),
        "ip": str(ip_points),
        "mac": "28:E9:46:6C:58:EF",
        "height": 60,
        "fill": {
            "src": "static/main/img/device_" + src + "icon.png"
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

    with open('main/static/main/js/nodes.json', 'w', encoding='utf-8') as outfile:
        json.dump(nodes, outfile, indent=2, ensure_ascii=False)
    with open('main/static/main/js/edges.json', 'w', encoding='utf-8') as file:
        json.dump(edges, file, indent=2, ensure_ascii=False)


def write_itog():
    try:
        nodes = json.load(open('main/static/main/js/nodes.json'))
        edges = json.load(open('main/static/main/js/edges.json'))
    except:
        nodes = []
        edges = []
    nodes.append(server)
    itog = {
        'nodes': nodes,
        'edges': edges
    }
    with open('main/static/main/js/data1.json', 'w', encoding='utf-8') as file:
        json.dump(itog, file, indent=4, ensure_ascii=False)


def scan():
    sh = 0
    f = open('main/static/main/js/data1.json', 'w', encoding='utf-8')
    f.close()
    f = open('main/static/main/js/nodes.json', 'w', encoding='utf-8')
    f.close()
    f = open('main/static/main/js/edges.json', 'w', encoding='utf-8')
    f.close()
    networkInterface = "5"
    pcnum = 0
    # define capture object
    print("listening on %s" % networkInterface)
    capture = pyshark.LiveCapture(interface=networkInterface, bpf_filter='tcp')
    for packet in capture.sniff_continuously(packet_count=50):
        # adjusted output
        try:
            # get packet content
            sh += 1
            src_addr = packet.ip.src  # source address
            dst_addr = packet.ip.dst  # destination address
            pkt_info = packet.tcp.payload
            hex_split = pkt_info.replace(':', '')
            # mining = '6d696e696e67'
            mining = '17'

            for i in range(len(listarp)):
                if listarp[i] == src_addr or listarp[i] == dst_addr:
                    if re.search(mining, hex_split, flags=0):
                        pcnum += 1
                        check_point = 'Обнаружен майнинг!'
                        src = 'infected_'
                        listarp[i] = 0
                        pc_data(str(listarp[i]), check_point, pcnum, src)
                    elif sh == 40:
                        pcnum += 1
                        check_point = 'Всё тихо!'
                        src = ''
                        pc_data(str(listarp[i]), check_point, pcnum, src)
                        listarp[i] = 0
            if len(pkt_info) > 5:
                print("IP %s <-> %s" % (
                    src_addr, dst_addr))
        except AttributeError as e:
            # ignore packets other than TCP, UDP and IPv4
            pass
    write_itog()


"""
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
"""
