#!/usr/bin/python
# -*- coding: utf-8 -*
#Phoenix Cyber Team
#Just_Tobi
#Rev Ip 000
import os
import requests
import socket
from colorama import Fore, init
from multiprocessing import Pool 
from multiprocessing.dummy import Pool as ThreadPool
from re import findall as reg

init(autoreset=True)

tmp = []
count=0
print '\x1b[91m[\x1b[92m+\x1b[91m]\x1b[92mTOTAL WEBLIST=',count
def repip(url):
    if url.startswith("http://"): url = url.replace("http://", "")
    elif url.startswith("https://"): url = url.replace("https://", "")

    try:
        ip = socket.gethostbyname(url)
        if ip in tmp: print("("+ url + ")" + "\033[31;1m Same Ip Detected \033[32;1m> Deleted...")
        else: 
            tmp.append(ip)
            grab = requests.get('https://soulapizy.000webhostapp.com/zerorev/?ip='+ip).content
            if 'null' in grab: print "{}[Bad IP] {}".format(Fore.RED, str(url))
            else:
                print(url + ' ' +'\033[32;1mGrab : '),len(grab)
                open('phoenixgrab.txt', 'a').write(grab+'\n')
    except: print("("+ url + ")" + "\033[31;1m Error")

spiner ="\033[31;1m++++++++++++++++++++++++++++++++++++++++++++++++++++"
instruksi ="\033[31;1m                 Cara Penggunaan "
first="\033[37;1m    Buat List Berupa .txt Dan Berisi List Web \n    Yang Mau Di Mass Rev Ip Di Folder Rev\n"
banner =  """
\033[31;1m██████╗░██╗░░██╗░█████╗░███████╗███╗░░██╗██╗██╗░░██╗
\033[31;1m██╔══██╗██║░░██║██╔══██╗██╔════╝████╗░██║██║╚██╗██╔╝
\033[37;1m██████╔╝███████║██║░░██║█████╗░░██╔██╗██║██║░╚███╔╝░
\033[37;1m██╔═══╝░██╔══██║██║░░██║██╔══╝░░██║╚████║██║░██╔██╗░
\033[31;1m██║░░░░░██║░░██║╚█████╔╝███████╗██║░╚███║██║██╔╝╚██╗
\033[31;1m╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝

\033[37;1m Author    : \033[31;1mMr.T0B1
\033[31;1m Team      : \033[37;1mPhoenix Cyber Team
\033[37;1m Date      : \033[31;1mOktober 03 2021
\033[31;1m Version   : \033[37;1m1.0
\033[31;1m Tools     : \033[37;1m000Priv8 Big Rev Ip
""".format(Fore.YELLOW)

os.system('clear')
print banner
print spiner
print instruksi
print first
url = raw_input(Fore.WHITE+'\033[31;1m[\033[32;1m>\033[31;1m]\033[37;1m List : \033[31;1m')

if os.path.exists(url): url = open(url, "r").read().splitlines()
else:  
    print("\033[31;1mError \033[37;1mList tidak ada di dalam folder")
    exit()

print spiner
Thread = raw_input(Fore.WHITE+'\033[31;1m[\033[32;1m>\033[31;1m]\033[37;1m Thread : \033[31;1m')
pool = ThreadPool(int(Thread))
pool.map(repip, url)
print('\033[32;1mTersimpan \033[37;1mDi File phoenixgrab.txt')
pool.close()
pool.join()
