from ping3 import ping
from pypresence import Presence
import time, pyautogui

def ganyu():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="Jogando de Ganyu", state="Ranque de Aventura: 56", large_image='ganyu', large_text="Ganyu")
            time.sleep(15)
        except Exception:
            print ("Deu erro")

def xiao():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="Jogando de Xiao", state="Ranque de Aventura: 56", large_image='xiao', large_text="Xiao")
            time.sleep(15)
        except Exception:
            print ("Deu erro")

def razor():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="Jogando de Razor", state="Ranque de Aventura: 56", large_image='razor', large_text="Menino Lobo")
            time.sleep(15)
        except Exception:
            print ("Deu erro")

def eula():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="Jogando de Eula", state="Ranque de Aventura: 56", large_image='eula', large_text="Eula")
            time.sleep(15)
        except Exception:
            print ("Deu erro")            

jogo = pyautogui.prompt(text="Com quem você está jogando?\n ganyu, xiao, razor ou eula\n", title="Personagem", default='')
if jogo == 'ganyu':
    ganyu()
elif jogo == 'xiao':
    xiao()
elif jogo == 'razor':
    razor()
elif jogo == 'eula':
    eula()
