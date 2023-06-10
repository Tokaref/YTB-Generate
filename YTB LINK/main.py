import os
import random
import requests
from time import sleep
import threading
from colorama import Fore
import colorama
from datetime import date

colorama.init(autoreset=True) 

os.system("title YOUTUBE INVITE/CHECKER ")


ROOT_PATH = os.chdir(os.path.dirname(os.path.abspath(__file__)))



def getcaractere(length):
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ab = "abcdefghijklmnoparstuvwxyz"
    ba = "0123456789"
    return ''.join(random.choice(str + ab + ba) for i in range(length))

def link_generate_ytb(code):
    url= f"https://youtu.be/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        if "Cette vidéo n'est plus disponible" in response.text:
            return False
        else:
            return True
    else:
        return False    

def verif_bloque_ytb():
    while True:
        today = date.today()
        res = requests.get("https://youtu.be/rTpMFBSf90k")
        if res.status_code == 200:
            if "Cette vidéo n'est plus disponible" in res.text:
                print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTRED_EX +" CONNECTION INTERRUPTED")
                sleep(2)
                while True:
                    print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTRED_EX +" CONNECTION INTERRUPTED")
            else:
                print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTGREEN_EX +" CONNECTION NOT INTERRUPTED")
                sleep(5)
        else:
            print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTRED_EX +" CONNECTION INTERRUPTED")
            sleep(2)
            while True:
                    print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTRED_EX +" CONNECTION INTERRUPTED")


def link_check_ytb():
 while True:
    today = date.today()
    code = getcaractere(11)
    valide_invite = link_generate_ytb(code)
    url = f"https://youtu.be/{code}"
    if valide_invite:
        print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTGREEN_EX +" LIEN VALIDE")
        print(Fore.LIGHTGREEN_EX +    url)
        fichier = open("YOUTUBE VALIDE LINK" +".txt", "w")
        mots = [url]
        for _ in range(1):
            for mot in mots:
                fichier.write("\n"+ mot)
                fichier.close
        break
    else:
        print(Fore.LIGHTYELLOW_EX +" [" + str(today) + "]" + Fore.LIGHTRED_EX +" FALSE LIEN")

class Threading:
    def __init__(self):
        threading.Thread(target=link_check_ytb).start()
        threading.Thread(target=verif_bloque_ytb).start()
Threading()


