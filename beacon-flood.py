#!/usr/bin/python
# python3
# Writer: Subin Jo

from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap
import sys


# 비콘 패킷 생성해서 전송
def sendBeacon(interface, bssid, ssid):
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=bssid, addr3=bssid)
    beacon = Dot11Beacon(cap='ESS+privacy')  # pw 필요한 ap인 것처럼 설정
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    rsn = Dot11Elt(ID='RSNinfo', info=(
        '\x01\x00'
        '\x00\x0f\xac\x02'
        '\x02\x00'
        '\x00\x0f\xac\x04'
        '\x00\x0f\xac\x02'
        '\x01\x00'
        '\x00\x0f\xac\x02'
        '\x00\x00'))
    frame = RadioTap()/dot11/beacon/essid/rsn
    frame.show()
    sendp(frame, iface=interface, count=3, inter=0.001)  # 각 ssid당 패킷 3번씩 전송


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

    # ssid와 일대일 대응되도록 임의의 bssid 생성
    # 20씩 증가되는 bssid
    bssid = '112233000000'

    for i, ssid in enumerate(ssid_list):
        ssid = ssid.strip('\n')
        bssid = format(int(bssid, 16) + 20, "#014x").replace("0x", "")
        addr3 = bssid[0:2] + ":" + bssid[2:4] + ":" + bssid[4:6] + ":" + bssid[6:8] + ":" + bssid[8:10] + ":" + bssid[10:12]
        sendBeacon(interface, addr3, ssid)

