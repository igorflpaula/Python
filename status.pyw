import psutil
from ping3 import ping
from pypresence import Presence
import time

RPC = Presence('816474128831479888',pipe=0)
RPC.connect()

while 1:
    try:
        cpu_per = round(psutil.cpu_percent(),1) 
        mem_per = round(psutil.virtual_memory().percent,1)
        ping1 = round(ping('google.com', unit='ms'))
    
        print("CPU: " + str(cpu_per) + "% RAM: " + str(mem_per) + "% PING: " + str(ping1) + "ms")
        RPC.update(details="Meu PC: PING: "+str(ping1)+" ms", state="RAM: "+str(mem_per)+"% CPU: "+str(cpu_per)+"%" , large_image='logo-flamengo-512', large_text="Seu cu é meu!", buttons=[{"label":"#SacyDay", "url":"https://www.twitch.tv/valorant_br"}])
        time.sleep(15)
    except Exception:
        print ("Deu erro")