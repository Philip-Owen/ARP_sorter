from operator import itemgetter

file_path = 'arp.txt'

f = open(file_path)
lines = f.readlines()

addresses = []

for line in lines:
    if "Internet" in line:
        line = line.split()
        print(line)
        ip = line[1].split('.')
        ip[3] = int(ip[3])
        addresses.append(ip)

arp_list = sorted(addresses, key=itemgetter(3))

with open('arp_list.txt', 'w') as file:
    for ip in arp_list:
        ip[3] = str(ip[3])
        line = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + ip[3] + '\n'
        file.write(line)