import  socket, time, json, os
from binascii import unhexlify
from tqdm import tqdm

def rdp_ip_load():
    ip_list = []
    with open("rdp_ip_414.txt","r") as f:
        #for line in f.readlines():
        data = f.read()
        ip = data.split()
        ip_list.append(ip)
        ip_list = ip_list[0]
        #print(len(ip_list))
    return ip_list

def write_list_to_json(list, json_file_name):
    #os.chdir(json_file_save_path)
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)
def write_list_to_txt(list, txt_file_name):
    with open(txt_file_name, 'w') as  f:
        f.write(str(list))

#print(ip_list)
#'35.201.103.233', '45.223.176.180', '103.43.11.117', '168.221.186.221', '45.60.48.141'
def probe_rdp_seurityset(ip_list):

    NativeRDP0 = unhexlify(b"030000130ee000000000000100080000000000")
    tls1 = unhexlify(b"030000130ee000000000000100080001000000")
    HYBRID3 = unhexlify(b"030000130ee000000000000100080003000000")
    RDSTLS4 = unhexlify(b"030000130ee000000000000100080004000000")
    HYBRID_EX8 = unhexlify(b"030000130ee000000000000100080008000000")
    x224ConnReqPDU = [ NativeRDP0, tls1,  HYBRID3, RDSTLS4, HYBRID_EX8]

    ips_seurity_set_list = []
    ip_bar = tqdm(ip_list)
    for dest_ip in ip_bar :
        ip_bar.set_description('Processing')
        ip_dict={}
        ip_seurity_set_response = ""
        ip_dict['ip'] = dest_ip
        #print("ip:{}".format(dest_ip))
        for reqPDU in x224ConnReqPDU:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.settimeout(2)
                s.connect((dest_ip,3389))
                s.send(reqPDU)
                msg = s.recv(1024)
                #print(msg)
                if msg == b'':
                    ip_seurity_set_response = "Empty message"
                    #print("Empty message")
                    break
                elif msg[:2] != b'\x03\x00':
                    ip_seurity_set_response = "not rdp protocol"
                    break
                else:
                    ip_seurity_set_response= ip_seurity_set_response+","+ str(msg[11])
                #ip_seurity_set.append(msg[11])
                s.shutdown(socket.SHUT_RDWR)
                s.close()
            except Exception as e:
                ip_seurity_set_response = str(e) #time out \ [WinError 10054] 远程主机强迫关闭了一个现有的连接。
                #print(e)
                break
        ip_dict['response'] =ip_seurity_set_response
        ips_seurity_set_list.append(ip_dict)
        #print(ip_dict)
    return ips_seurity_set_list

ip_list = rdp_ip_load()

# start_time = time.time()
ips_seurity_set_list = probe_rdp_seurityset(ip_list)
# perf = time.time()-start_time

write_list_to_json(ips_seurity_set_list, 'ips_seurity_set_list_0416.json ')
