import json


with open('rdpscan_414.json', 'r') as f:
    data = json.load(f)
    rdp_ip_list = []
    for host in data :
        rdp_ip_list.append(host['ip'])
    print(rdp_ip_list)
    print("ip_num:{}".format(len(rdp_ip_list)))


with open('rdp_ip_414.txt', 'w') as f:
    for ip in rdp_ip_list:
        f.write(ip + '  ')
