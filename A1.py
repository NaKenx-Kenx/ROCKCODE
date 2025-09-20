import sys
import time
from getpass import getpass

def countdown(duration: int,stronga : str):
    for a in range(duration):
        for i in [' | ',' / ',' - ',' \\ ']:
            sys.stdout.write(f"\r{stronga}"+i+str(duration-a-1))
            sys.stdout.flush
            time.sleep(0.25)
    sys.stdout.write("\r")
    sys.stdout.flush

loadingres = [
    "|...............||||",
    "||...............|||",
    "|||...............||",
    "||||...............|",
    "|||||...............",
    ".|||||..............",
    "..|||||.............",
    "...|||||............",
    "....|||||...........",
    ".....|||||..........",
    "......|||||.........",
    ".......|||||........",
    "........|||||.......",
    ".........|||||......",
    "..........|||||.....",
    "...........|||||....",
    "............|||||...",
    ".............|||||..",
    "..............|||||.",
    "...............|||||"
]

loadframe = 0
print(r"""   ___  ____  _______ ___________  ___  ____
  / _ \/ __ \/ ___/ //_/ ___/ __ \/ _ \/ __/
 / , _/ /_/ / /__/ ,< / /__/ /_/ / // / _/  
/_/|_|\____/\___/_/|_|\___/\____/____/___/  
  / __/ _ \/ __/ __/ / __/  _/ _ \/ __/     
 / _// , _/ _// _/  / _/_/ // , _/ _/       
/_/ /_/|_/___/___/ /_/ /___/_/|_/___/       """)
print("V0.0.1 by NaKenx\n")
countdown(5, "Prepare")
print('Enter the passkey')
paskey = getpass("passkey: ")

def fake_process():
    for a in range(20):
       for s in [".","..","...",".."]:
            sys.stdout.write(f"\rprocessing"+s)
            sys.stdout.flush
            time.sleep(0.2)
    sys.stdout.write("\r")
    sys.stdout.flush

def create_Menu():
    print("\n\n")
    print("ILLEGAL BOOM:\n" \
    "   HACK ACCOUNT -> [1]\n" \
    "   BAN ACCOUNT -> [2]\n" \
    "   DELETE ACCOUNT -> [3]\n" \
    "   FREE TOP UP -> [4]\n" \
    "   SET RANK BATTLE ROYALE -> [5]\n" \
    "   SET RANK CLASH SQUAD -> [6]\n" \
    "   CLOSE -> [0]\n" \
    "\n#If anything happens, it's not our fault\n")
    modetype = input("CODE: ")
    match modetype:
        case "1":
            print("------<ACCOUNT HACKING>-------")
            uid = input("\nenter, free fire id: ")
            nick = input("enter, free fire nickname: ")
            print("\nEnter your email to send hacked account.")
            email = input("your email: ")
            while not "@" in email:
                email = input("wrong email, please enter email: ")
            fake_process()
            print("\n\naccount in hack proccessing. hacked account will sent to your email")
            countdown(10,"Back to boom in")
            create_Menu()
        case "2":
            comeson()
        case "3":
            comeson()
        case "4":
            comeson()
        case "5":
            comeson()
        case "6":
            comeson()
        case "0":
            countdown(30,"this tools closed in")
            print("V0.0.1 NaKenx/Kenx Real uip: 12.80.8325.18 "+str(time.ctime))

def comeson():
    print("coming soon")
    countdown(15,"Back to boom in")
    create_Menu()

if paskey == "672011":
    print("\n")
    for percentage in range(45):
        for frame in loadingres:
            sys.stdout.write(f"\rprocessing [-{frame}-] { int(float(float(percentage)/44.0)*100) }%")
            sys.stdout.flush
            time.sleep(0.0025)
        loadframe += 1
    sys.stdout.write("\r")
    sys.stdout.flush
    create_Menu()
else:
    print("\n")
    for percentage in range(15):
        for frame in loadingres:
            sys.stdout.write(f"\rprocessing [-{frame}-] { int(float(float(percentage)/200.0)*100) }%")
            sys.stdout.flush
            time.sleep(0.0105)
        loadframe += 1
    sys.stdout.write("\r")
    sys.stdout.flush
    print("\033[31mWRONG PASSKEY\033[37m, ERROR : 2120-3\n")
    print("\033[31mACCESS DENIED\033[37m")
