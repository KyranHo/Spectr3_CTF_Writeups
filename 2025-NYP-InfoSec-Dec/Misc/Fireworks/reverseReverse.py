from random import seed , randint
seed(914)
wheel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}'
EncryptedFlag ="OELXFGQPYRI}C}DPKGOCASGPZVNJ"
flag = ""
for i in EncryptedFlag:
    flag += wheel[(wheel.find(i) - randint(0,len(wheel)-1))%(len(wheel))]
print(flag)
