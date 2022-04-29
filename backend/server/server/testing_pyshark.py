import pyshark
import json
import re
import arp
from arp import arp_search
import numpy as np
from keras.models import model_from_json

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def RGB(hex_split):
    res = np.zeros((30, 30, 3)).astype(int)
    s = 0
    k = 0
    for i in range(0, len(hex_split) - 6, 6):
        a = hex_split[i:i + 6]
        RGB = hex_to_rgb(a)
        r = RGB[0]
        g = RGB[1]
        b = RGB[2]
        res[k, s] = [r, g, b]
        s += 1
        if s == 30:
            k += 1
            s = 0
    return res




def pc_data(ip_points, check_point, pcnum, src):
    if check_point == 1:
        status = 'Опасность'
    else:
        status = 'Все хорошо'
    pc = {
        "id": "PC_1_" + str(pcnum),
        "status": status,
        "ip": str(ip_points),
        "mac": "28:E9:46:6C:58:EF",
        "height": 60,
        "fill": {
            "src": "static/main/img/device_" + src + "icon.png"
        }
    }
    edg = {
        "from": "Switch_1",
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


def write_itog(server, switch):
    try:
        nodes = json.load(open('main/static/main/js/nodes.json', encoding='utf-8'))
        edges = json.load(open('main/static/main/js/edges.json', encoding='utf-8'))
    except:
        nodes = []
        edges = []
    nodes.append(server)
    nodes.append(switch)
    sw_edg = {
        "from": "Server",
        "to": "Switch_1"
    }
    edges.append(sw_edg)
    itog = {
        'nodes': nodes,
        'edges': edges
    }
    with open('main/static/main/js/data1.json', 'w', encoding='utf-8') as file:
        json.dump(itog, file, indent=4, ensure_ascii=False)


def scan():
    listarp = arp_search()
    print(listarp)
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
    for packet in capture.sniff_continuously(packet_count=100):
        # adjusted output
        try:
            # get packet content
            src_addr = packet.ip.src  # source address
            dst_addr = packet.ip.dst  # destination address
            pkt_info = packet.tcp.payload
            hex_split = pkt_info.replace(':', '')
            # mining = '6d696e696e67'

            for i in range(len(listarp)):
                print("IP Отправки: %s <-> IP Назначения:%s ====== IP Из АРП:%s" % (src_addr, dst_addr, listarp[i]))
                if listarp[i] == src_addr or listarp[i] == dst_addr:
                    if len(hex_split) > 5:
                        if len(hex_split) < 5400:
                            for n in range(len(hex_split) + 1, 5400 + 1):
                                hex_split += "0"
                        x_train = []
                        x_train.append(RGB(hex_split))
                        x_train = np.array(x_train)
                        x_train = np.expand_dims(x_train, axis=0)
                        x_train = x_train / 255

                        jfile = open("model.json", "r")
                        loaded_json = jfile.read()
                        jfile.close()
                        loaded_model = model_from_json(loaded_json)

                        loaded_model.load_weights("weights.hdf5")

                        loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
                        check_point = loaded_model.predict(x_train[0])
                        check_point = np.argmax(check_point)

                        if check_point == 1:
                            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                            print(hex_split)
                            pcnum += 1
                            src = 'infected_'
                            pc_data(listarp[i], check_point, pcnum, src)
                            listarp[i] = 0
                    #if len(pkt_info) > 5:


            check_point = 0
        except AttributeError as e:
            # ignore packets other than TCP, UDP and IPv4
            pass
    for i in range(len(listarp)):
        if listarp[i] != 0 and i != 0:
            pcnum += 1
            check_point = 0
            src = ''
            pc_data(listarp[i], check_point, pcnum, src)
            listarp[i] = 0
    server = {
        "id": "Server",
        "height": 70,
        "fill": {
            "src": "static/main/img/server_icon.png"
        }
    }
    switch = {
        "id": "Switch_1",
        "ip": "192.168.0.1",
        "mac": "7c-39-53-c3-9c-41",
        "height": 70,
        "fill": {
            "src": "static/main/img/switch_icon.png"
        }
    }
    write_itog(server, switch)