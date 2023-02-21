import os
import time
import colorama
import random
import sys
from colorama import Fore

colorama.init()

# MAIN CODE #
def main():
 print(Fore.LIGHTGREEN_EX + " / ___| |__  _ __ ___  _ __ (_) ___")
 print(Fore.LIGHTGREEN_EX + "| |   | '_ \| '__/ _ \| '_ \| |/ __|")
 print(Fore.LIGHTGREEN_EX + "| |___| | | | | | (_) | | | | | (__")
 print(Fore.LIGHTGREEN_EX + " \____|_| |_|_|  \___/|_| |_|_|\___|")
 print(Fore.LIGHTYELLOW_EX + "Search in? 1. specific page 2. everything in web")
 select = input(">>")

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

        os.popen("pip install colorama")
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
    
    main()

   

try:
      anim()
except Exception as e:
    print(anim)
    pass

else:
    print("ERROR")
    print("Restarting...")
    time.sleep(1)
    os.system("clear")
    anim()     