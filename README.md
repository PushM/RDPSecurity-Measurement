#RDPSecurity-Measurement

测量互联网开启RDP服务的主机安全配置：Standard RDP Security、TLS、RDSTLS 、CredSSP、CredSSP coupled with the Early User Authorization Result PDU这五种安全协议允许哪些？

rdp_ip_414.txt:扫描到互联网开启3389的主机ip

rdp_security_set.py：发送多个指定不同安全等级的x224 connection request PDU探测目标rdp服务端安全等级，将服务端回复保存至json文件

rdp_sec_analyse.py：分析服务端回复