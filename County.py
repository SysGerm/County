import time
import colorama
from colorama import Fore
colorama.init() 

print("""
_________  ________    ____ ___ _______ ________________.___. 
\_   ___ \ \_____  \  |    |   \\      \\__    ___/\__  |   | 
/    \  \/  /   |   \ |    |   //   |   \ |    |    /   |   | 
\     \____/    |    \|    |  //    |    \|    |    \____   | 
 \______  /\_______  /|______/ \____|__  /|____|    / ______| 
        \/         \/                  \/           \/        
                                                              """)
def countdown(tme):

    while tme:
        mins, secs = divmod(tme, 60)
        timer = Fore.GREEN + '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tme -= 1


    print(Fore.RED + "Time is over!")


tme = input(Fore.BLUE + "Put in your time (s): ")

countdown(int(tme))