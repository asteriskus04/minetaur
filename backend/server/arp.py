import os
import pandas
import re


def arp_search():
    os.system('arp -a > arp.csv')
    data = pandas.read_csv('arp.csv', encoding='cp866')
    data_prom = data.values.tolist()
    data_result = []
    for i in data_prom:
        if re.search('Интерфейс:', str(*i), flags=1):
            data_result += re.findall(r'[0-9]+(?:\.[0-9]+){3}', *i)

    return (data_result)
print(arp_search())
