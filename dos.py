import socket
import threading
import os,sys
from colorama import Fore,init

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
