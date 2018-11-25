import dpkt
import socket
import sys
from collections import defaultdict

SYN_dict=defaultdict(int)
SYN_ACK_dict=defaultdict(int)
ip_list=[]
#f = open('samples/lbl-internal.20050107-0456.port025.dump.anon.pcap')
f=open(sys.argv[1])
pcap = dpkt.pcap.Reader(f)
for ts, buf in pcap:
    try:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        try:

            if ip.p==dpkt.ip.IP_PROTO_TCP:
                tcp=ip.data

                src_add=socket.inet_ntoa(ip.src)
                dst_add=socket.inet_ntoa(ip.dst)
                SYN_flag=(tcp.flags&dpkt.tcp.TH_SYN )!=0
                ACK_flag=(tcp.flags&dpkt.tcp.TH_ACK )!=0


                if SYN_flag:

                    if ACK_flag:

                        SYN_ACK_dict[dst_add]+=1
                    else:
                        SYN_dict[src_add]+=1
        except:

            pass

    except:
        pass

for each in SYN_dict:
    if SYN_dict[each]>=3*SYN_ACK_dict[each]:
        ip_list.append(each)
        print(each)
