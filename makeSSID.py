# 임의의 ssid (TEST0~TEST299) 담긴 파일 생성
if __name__ == "__main__":
    f = open('ssid-list.txt', 'w')
    ssid = ['TEST'+str(x)+'\n' for x in range(300)]
    f.writelines(ssid)
    f.close()
