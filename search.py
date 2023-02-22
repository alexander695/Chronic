import os
import time
import random
import sys
from colorama import Fore
from googlesearch import search
import signal

colorama.init()
def signal_handler(signal,frame):
   global Interrupted
   interrupted = True
# MAIN CODE #
def main():
 print(Fore.LIGHTGREEN_EX + " / ___| |__  _ __ ___  _ __ (_) ___")
 print(Fore.LIGHTGREEN_EX + "| |   | '_ \| '__/ _ \| '_ \| |/ __|")
 print(Fore.LIGHTGREEN_EX + "| |___| | | | | | (_) | | | | | (__")
 print(Fore.LIGHTGREEN_EX + " \____|_| |_|_|  \___/|_| |_|_|\___|")
 print(Fore.LIGHTYELLOW_EX + "Search in? 1. specific page 2. everything in web")
 sel = input("[?] >>")
 interrupted = False
 signal.signal(signal.SIGINT, signal_handler)
 if sel =="1" or sel=="specific page":
   page = input("\nWhat do you want to search?:")
   print(Fore.LIGHTBLUE_EX + "\n[!] Searching for:" + page)
   resul = search(page, pause=2.0, num=10, stop=10)
   for r in resul:
      print(r)
   input("press enter to back")
   main()
 elif sel =="2" or sel=="everything in web":
      page = input("\nWhat do you want to search?:")
      print(Fore.LIGHTBLUE_EX + "\n[!] Searching infinitely for:" + page)
      time.sleep(1)
      resul = search(page, pause=2.0, stop=None)
      for r in resul:
        print(r)
        if interrupted:
          print("Exiting")
          time.sleep(0.7)
          main()

 else:
    print(Fore.LIGHTRED_EX + "an error was ocurred. Possible errors:")
    print(Fore.LIGHTRED_EX + "[!] Are you connected to internet?")
    print(Fore.LIGHTRED_EX + "[!] you selected right the options?")
 




# START ANIMATION
def anim():
    print(Fore.LIGHTGREEN_EX + " / ___| |__  _ __ ___  _ __ (_) ___")
    time.sleep(0.7)
    print(Fore.LIGHTGREEN_EX + "| |   | '_ \| '__/ _ \| '_ \| |/ __|")
    time.sleep(0.7)
    print(Fore.LIGHTGREEN_EX + "| |___| | | | | | (_) | | | | | (__")
    time.sleep(0.7)
    print(Fore.LIGHTGREEN_EX + " \____|_| |_|_|  \___/|_| |_|_|\___|")
    time.sleep(0.7) 
      # String to be displayed when the application is loading
    load_str = "starting..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1

      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
        main()
          
    # for linux / Mac OS
    else:
        os.system("clear")
        main()

   
anim()
     
