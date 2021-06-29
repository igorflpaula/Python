from ping3 import ping
from pypresence import Presence
import time, pyautogui

def espinha():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="Na Montanha Nevada", state="Ranque de Aventura: 56", large_image='dragon', large_text="Espinha do Dragão")
            time.sleep(15)
        except Exception:
            print ("Deu erro")

def liyue():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="No Porto de Liyue", state="Ranque de Aventura: 56", large_image='liyue', large_text="Liyue")
            time.sleep(15)
        except Exception:
            print ("Deu erro")

def mondstadt():

    RPC = Presence('816474128831479888',pipe=0)
    RPC.connect()

    while 1:
        try:
        
            #print("CPU: " "% RAM: " "% PING: " "ms")
            RPC.update(details="Na Cidade da Liberdade", state="Ranque de Aventura: 56", large_image='mond', large_text="Mondstadt")
            time.sleep(15)
        except Exception:
            print ("Deu erro")

jogo = pyautogui.prompt(text="Onde voce esta explorando?\n espinha, liyue ou mond\n", title="Região", default='')
if jogo == 'espinha':
    espinha()
elif jogo == 'liyue':
    liyue()
elif jogo == 'mond':
    mondstadt()

