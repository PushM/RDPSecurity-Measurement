import json,re
#[ NativeRDP0, tls1,  HYBRID3, RDSTLS4, HYBRID_EX8]


with open('ips_seurity_set_list_0416.json', 'r') as f:
    ips_list = json.load(f)
    print(len(ips_list) )
    onlyNativeRDP0 = 0
    onlytls1 = 0
    onlyHYBRID3 = 0
    onlyRDSTLS4 = 0
    onlyHYBRID_EX8 = 0
    analyse_list = [0]*33
    #analyse_list)
    #
    for ip_dic in ips_list:
        if ip_dic["response"] == ",2,2,2,2,2":
            analyse_list[0]=analyse_list[0]+1
        elif ip_dic["response"] == ",2,2,2,2,3":
            analyse_list[1]=analyse_list[1]+1
        elif ip_dic["response"] == ",2,2,2,3,2":
            analyse_list[2]=analyse_list[2]+1
        elif ip_dic["response"] == ",2,2,2,3,3":
            analyse_list[3]=analyse_list[3]+1
        elif ip_dic["response"] == ",2,2,3,2,2":
            analyse_list[4]=analyse_list[4]+1
        elif ip_dic["response"] == ",2,2,3,2,3":
            analyse_list[5]=analyse_list[5]+1
        elif ip_dic["response"] == ",2,2,3,3,2":
            analyse_list[6]=analyse_list[6]+1
        elif ip_dic["response"] == ",2,2,3,3,3":
            analyse_list[7]=analyse_list[7]+1
        elif ip_dic["response"] == ",2,3,2,2,2":
            analyse_list[8]=analyse_list[8]+1
        elif ip_dic["response"] == ",2,3,2,2,3":
            analyse_list[9]=analyse_list[9]+1
        elif ip_dic["response"] == ",2,3,2,3,2":
            analyse_list[10]=analyse_list[10]+1
        elif ip_dic["response"] == ",2,3,2,3,3":
            analyse_list[11]=analyse_list[11]+1
        elif ip_dic["response"] == ",2,3,3,2,2":
            analyse_list[12]=analyse_list[12]+1
        elif ip_dic["response"] == ",2,3,3,2,3":
            analyse_list[13]=analyse_list[13]+1
        elif ip_dic["response"] == ",2,3,3,3,2":
            analyse_list[14]=analyse_list[14]+1
        elif ip_dic["response"] == ",2,3,3,3,3":
            analyse_list[15]=analyse_list[15]+1
        elif ip_dic["response"] == ",3,2,2,2,2":
            analyse_list[16]=analyse_list[16]+1
        elif ip_dic["response"] == ",3,2,2,2,3":
            analyse_list[17]=analyse_list[17]+1
        elif ip_dic["response"] == ",3,2,2,3,2":
            analyse_list[18]=analyse_list[18]+1
        elif ip_dic["response"] == ",3,2,2,3,3":
            analyse_list[19]=analyse_list[19]+1
        elif ip_dic["response"] == ",3,2,3,2,2":
            analyse_list[20]=analyse_list[20]+1
        elif ip_dic["response"] == ",3,2,3,2,3":
            analyse_list[21]=analyse_list[21]+1
        elif ip_dic["response"] == ",3,2,3,3,2":
            analyse_list[22]=analyse_list[22]+1
        elif ip_dic["response"] == ",3,2,3,3,3":
            analyse_list[23]=analyse_list[23]+1
        elif ip_dic["response"] == ",3,3,2,2,2":
            analyse_list[24]=analyse_list[24]+1
        elif ip_dic["response"] == ",3,3,2,2,3":
            analyse_list[25]=analyse_list[25]+1
        elif ip_dic["response"] == ",3,3,2,3,2":
            analyse_list[26]=analyse_list[26]+1
        elif ip_dic["response"] == ",3,3,2,3,3":
            analyse_list[27]=analyse_list[27]+1
        elif ip_dic["response"] == ",3,3,3,2,2":
            analyse_list[28]=analyse_list[28]+1
        elif ip_dic["response"] == ",3,3,3,2,3":
            analyse_list[29]=analyse_list[29]+1
        elif ip_dic["response"] == ",3,3,3,3,2":
            analyse_list[30]=analyse_list[30]+1
        elif ip_dic["response"] == ",3,3,3,3,3":
            analyse_list[31]=analyse_list[31]+1
        else:
            analyse_list[32]=analyse_list[32]+1
num = 0
print(analyse_list)
# for i in analyse_list:
#     print(num)
#     num = num + 1
#     print(i)