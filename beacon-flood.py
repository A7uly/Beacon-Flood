#!/usr/bin/python
# python3
# Writer: Subin Jo

from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap
import sys


# 비콘 패킷 생성해서 전송
def sendBeacon(interface, ssid):
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=str(RandMAC()), addr3=str(RandMAC()))  # 랜덤한 bssid 생성
    beacon = Dot11Beacon(cap='ESS+privacy')  # pw 필요한 ap인 것처럼 설정
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/beacon/essid
    # frame.show()
    sendp(frame, iface=interface, count=3, inter=0.01)  # 각 ssid당 패킷 3번씩 전송


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Insufficient arguments")
        sys.exit()
    interface = sys.argv[1]
    fname = sys.argv[2]

    # ssid-list.txt 읽어오기
    f = open(fname, 'r')
    ssid_list = f.readlines()
    f.close()

    bssid = '112233000000'

    for i, ssid in enumerate(ssid_list):
        ssid = ssid.strip('\n')
        sendBeacon(interface, ssid)

