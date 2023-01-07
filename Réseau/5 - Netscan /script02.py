from scapy.all import arping
import re


def SendReq(IP):
    scan = arping(IP)
    print(scan)


while True:
    adress = input("Enter address: ")
    if not re.match("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,3}$", adress):
        print("Invalid format")
    else:
        SendReq(adress)
        print("Done")
        break
