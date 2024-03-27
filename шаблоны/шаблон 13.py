# 183
from ipaddress import *
li = []
for i in range(63, 256):
    for j in range(256):
        for k in range(256):
            try:
                if IPv4Network(f'99.{i}.{j}.{k}') in ip_network(f'99.64.0.0/255.192.0.0'):
                    li.append(IPv4Network(f'99.{i}.{j}.{k}'))
            except:
                pass
print(li)                                                                                                                                                                            k