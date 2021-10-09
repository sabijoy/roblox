import random
from random import randint
import time
import os
import sys
import pyfiglet
import requests
from pathlib import Path
gentype = '0123456789'
ascii_banner = pyfiglet.figlet_format("Roblox Giftcard Generator")
print(ascii_banner)
os.system("title Thank you for using R.G.G Roblox Giftcard Generator Developer: Danko")

mode = input("""          
   \033[1;37;40m┌──────┐
   │ Main │\033[1;37;40m
\033[1;36;40m╔═\033[1;36;40m═══════════════╗
\033[1;36;40m║\033[1;35;40m \033[1;32;40m1 \033[1;33;40m: \033[1;37;40mGenerator  \033[1;36;40m║\033[1;36;40m
\033[1;36;40m║\033[1;35;40m \033[1;32;40m2 \033[1;33;40m: \033[1;37;40mHelp       \033[1;36;40m║
\033[1;36;40m║\033[1;35;40m \033[1;32;40m3 \033[1;33;40m: \033[1;37;40mCredits    \033[1;36;40m║\033[1;36;40m
\033[1;36;40m╚\033[1;35;40m\033[1;36;40m═══\033[1;36;40m═════════════╝\n\n[+] Choice: """)

# generator #################
if(mode == "1"):
  os.system("title [Option] [1] [Generator]")
  os.system('cls')
  ascii_banner = pyfiglet.figlet_format("Number To Generate")
  print(ascii_banner)
  total = input("\033[1;34;40mHow Many Would You Like To Generate?\n\n[>] Number To Generate: ")
  number = int(total)
  for x in range(number):
      generate1 = random.choice(gentype) 
      generate2 = random.choice(gentype) 
      generate3 = random.choice(gentype) 
      generate4 = random.choice(gentype) 
      generate5 = random.choice(gentype) 
      generate6 = random.choice(gentype) 
      generate7 = random.choice(gentype) 
      generate8 = random.choice(gentype) 
      generate9 = random.choice(gentype) 
      generate10 = random.choice(gentype) 
      subtodanko = "\n"
      file = (total + " Roblox Giftcards.txt")
      with open(file, 'a') as out:
        out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+subtodanko)
### HELP
if(mode == "2"):
    os.system("title [Option] [2] [Help]")
    os.system("cls")
    ascii_banner = pyfiglet.figlet_format("[>] Help")
    print(ascii_banner)
    print("\033[1;37;40mHey There! I've Heard that you need \033[1;37;40mHELP! well am here to help you, so first of all this program generates \033[1;37;40mUNCHECKED Roblox Giftcards whuich could be worth \033[1;37;40m5$/10$/25$/50$ & 100$! But \033[1;37;40mNOT All giftcards work, they are basiclly \033[1;37;40mmrandom numbers putten together, if you would like to check if your gift card works then go to \033[1;37;40mhttps://roblox.com/redeem/ Dont forget to join our discord server for more help! \033[1;35;40mdisc\033[1;37;40mord.gg/hacks, \033[1;35;40manyways Click Enter to quit")
    input("\n\n[>] Click Enter to exist the program:-")
### CREDITS
if(mode == "3"):
    os.system("title [Option] [3] [Credits]")
    os.system("cls")
    ascii_banner = pyfiglet.figlet_format("Credits")
    print(ascii_banner)
    print("\033[1;33;40m[>] \033[1;31;40mProgram Creator: \033[1;36;40mDanko")
    print("\033[1;33;40m[>] \033[1;31;40mYoutube Channel: \033[1;36;40mhttps://www.youtube.com/c/DankoYT/")
    print("\033[1;33;40m[>] \033[1;31;40mDiscord Server: \033[1;36;40mdiscord.gg/hacks")
    print("\033[1;33;40m[>] \033[1;31;40mMore Crazy Videos: \033[1;36;40mhttps://www.youtube.com/watch?v=ANGR4cCh8gw")
    print("\033[1;33;40m[>] \033[1;31;40mNitro Generator & Checker: \033[1;36;40mhttps://www.youtube.com/watch?v=Wlvonr8JPrU&t")
    print("\033[1;33;40m[>] \033[1;31;40mDiscord User: \033[1;36;40mDanko#0002")
    print("\033[1;33;40m[>] \033[1;31;40mPress Enter to \033[1;36;40mExist")
    input("\033[1;33;40m[>] \033[1;31;40mEnter\n\n")
