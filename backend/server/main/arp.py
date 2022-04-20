import os
import pandas
import re

os.system('arp -a > arp.csv')
data = pandas.read_csv('arp.csv', encoding='cp866')
# print(data.loc[:,'Интерфейс: 192.168.56.1 --- 0x9'])
data_prom = data.values.tolist()
print(data_prom)
data_result = []
print()
for i in data_prom:
    print(i)
    if re.search('динамический', str(*i), flags=1):
        print(i)
        data_result += re.findall(r'[0-9]+(?:\.[0-9]+){3}', *i)
print(data_result)
