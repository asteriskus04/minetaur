import os
import pandas
import re


def arp_search():
    data_result = []
    os.system('arp -a > arp.csv')
    data = pandas.read_csv('arp.csv', encoding='cp866')
    head3 = data.columns.tolist()
    # head3 = str(head3)
    # abv = re.findall(r'[0-9]+(?:\.[0-9]+){3}', head3)
    data_prom = data.values.tolist()
    chek = 0
    for i in data_prom:
        if re.search('Интерфейс:', *i, flags=1) and chek == 1:
            break
        if re.search('Интерфейс: 192.168.137.1', *i, flags=1):
            chek = 1
        if re.search('динамический', str(*i), flags=1) and chek == 1:
            data_result += re.findall(r'[0-9]+(?:\.[0-9]+){3}', *i)
    #data_result.append('192.168.137.1')
    return (data_result)
print(arp_search())
