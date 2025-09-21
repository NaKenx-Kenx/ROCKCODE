import sys , time , os , random , string , socket , platform
from getpass import getpass

#DOnt STeAl My Script
#YOU StupId If YoU SteaL It

menu_dict = {
    "MAIN":[],
    "GAMES":[],
    "VIRUS":[],
}
menu_game_dict = {
    "FF":[],
    "ML":[],
    "PUBG":[],
    "GI":[],
    "SS":[],
}
scene_index = 0
game_index = 0
premium_mode = False
virus_att = {
    "num":"08119909786",
    "virus":0
}
RESET = "\033[0m"
colors = [
    "\033[31m",  # merah
    "\033[32m",  # hijau
    "\033[33m",  # kuning
    "\033[34m",  # biru
    "\033[35m",  # magenta
    "\033[36m",  # cyan
    "\033[91m",  # bright red
    "\033[92m",  # bright green
]

def fakeloadrand(prefix:str,max:float=0.5,maxstep:int=3):
    progress = 0
    while progress < 101:
        print(f"\033[93m{prefix} \033[32m[{"■"*progress}{"☐"*(100-progress)}] {progress}%\033[0m")
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        progress += random.randint(1,maxstep)
        time.sleep(random.uniform(0.001,max/(((progress+50)/100)*3)))

def get_local_ip() -> any:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_size() -> dict:
    size = {
        "x":0.0,
        "y":0.0
        }
    terminalS = os.get_terminal_size()
    size["x"] = terminalS.columns
    size["y"] = terminalS.lines
    return size

def create_menuinlist(NAME:str,index:int) -> str:
    return f"\033[38;5;15;48;5;236m> {NAME} -> [{index}]\033[0m\n   \033[90m{random_string(50)}\n {random_string(50)}{RESET}"

def create_minlist(pc1:str,pc2:str) -> str:
    return f"\033[38;5;15;48;5;236m> {pc1} => {pc2}\033[0m\n   \033[90m{random_string(50)}\n {random_string(50)}{RESET}"

def animated_text(duration:float,text:str):
    for dar in text:
        print(dar,end="",flush=True)
        time.sleep((duration)/len(text))

def animated_countdown(duration:int,perspin_time:float=0.125,prefix:str=""):
    animtext = ['-','\\','|','/']
    for dur in range(duration*int(1/perspin_time),0,-1):
        for text in animtext:
            sys.stdout.write("\r"+text+" "+str(dur)+prefix)
            sys.stdout.flush
            time.sleep(0.125)
    sys.stdout.write("\r")
    sys.stdout.flush

def center_text(text:str,fillchart:str=" ") -> str:
    return text.center(get_size()["x"],fillchart)

def open_title_menu():
    clean_screen()
    judul = r""" ____  __.__                    .____                         
|    |/ _|__|__________    _____|    |    ____   ______ ______
|      < |  \____ \__  \  /  ___/    |  _/ __ \ /  ___//  ___/
|    |  \|  |  |_> > __ \_\___ \|    |__\  ___/ \___ \ \___ \ 
|____|__ \__|   __(____  /____  >_______ \___  >____  >____  >
        \/  |__|       \/     \/        \/   \/     \/     \/ """
    for line in judul.strip("\n").split("\n"):
        animated_text(0.0125,center_text(line))
    print(center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"))
    print("")
    print(center_text("<[ MAIN SCX ]>","-"))
    print_array(menu_dict["MAIN"])
    print(center_text("<?>","-"))
    scene_index = int(input("\r S: "))
    while scene_index > len(menu_dict["MAIN"]) or scene_index < 0:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        scene_index = int(input("\r S: "))
    match scene_index:
        case 0:
            open_game_menu()
        case 1:
            open_virus_menu()
        case 2:
            open_about_menu()
        case 3:
            if premium_mode:
                pass
            else:
                fakeloadrand("Checking Premium",0.8,8)
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("PREMIUM FALSE")
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                open_title_menu()
    
    
def open_game_menu():
    clean_screen()
    judul = r""" ____  __.__                    .____                         
|    |/ _|__|__________    _____|    |    ____   ______ ______
|      < |  \____ \__  \  /  ___/    |  _/ __ \ /  ___//  ___/
|    |  \|  |  |_> > __ \_\___ \|    |__\  ___/ \___ \ \___ \ 
|____|__ \__|   __(____  /____  >_______ \___  >____  >____  >
        \/  |__|       \/     \/        \/   \/     \/     \/ """
    for line in judul.strip("\n").split("\n"):
        print(center_text(line))
    print(center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"))
    print("")
    print(center_text("<[ GAME HACK ]>","-"))
    print_array(menu_dict["GAMES"])
    print(center_text("<?>","-"))
    game_index = int(input("\r S (close -> -1): "))
    if game_index == -1:
        open_title_menu()
    while game_index > len(menu_dict["GAMES"]):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        game_index = int(input("\r S (close -> -1): "))
    open_gametools_menu(game_index)

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_array(array:list):
    for a in array:
        print(a)

def print_center_array(array:list,fillcahart:str=" "):
    for a in array:
        print(center_text(a,fillcahart))

def load_all():
    listname = {
    "MAIN":[
        "Game Hack",
        "Virus",
        "About",
        "Premium menu"
        ],
    "GAMES":[
        "Free fire",
        "Mobile legends",
        "PUBG",
        "Genshin impact",
        "Super sus"
        ],
    "VIRUS":[
        "Set target number",
        "Set virus",
        "Send"
    ]
}
    listgamne = {
    "FF":[
        "Top up free Diamonds",
        "Ban account",
        "Delete account",
        "Set Rank"
    ],
    "ML":[
        "Top up free Diamonds",
        "Ban account",
        "Delete account",
        "Set Rank",
        "Unlock skin"
    ],
    "PUBG":[
        "Top up free G-coins & UC",
        "Ban account",
        "Delete account",
        "Set Rank"
    ],
    "GI":[
        "Top up free Primogems",
        "Ban account",
        "Delete account",
    ],
    "SS":[
        "Top up free Goldstars",
        "Ban account",
        "Delete account",
        "Set Rank"
        "unlock role"
    ],
}
    for a in listname.keys():
        for b in range(len(listname[a])):
            menu_dict[a].append(create_menuinlist(listname[a][b],b))
    for a in listgamne.keys():
        for b in range(len(listgamne[a])):
            menu_game_dict[a].append(create_menuinlist(listgamne[a][b],b))

def intro():
    ascciart = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⠶⠶⠶⠶⠶⠶⠶⢖⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠈⠹⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⢀⣤⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣦⣀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⣠⡾⢁⣾⡿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣆⠹⣦⠀⠀⢻⣆⠀⠀⠀⠀
⠀⠀⢀⡾⠁⢀⢰⣿⠃⠾⢋⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⠀⢹⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡌⠻⠆⢿⣧⢀⠀⢻⣆⠀⠀⠀
⠀⠀⣾⠁⢠⡆⢸⡟⣠⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡸⣿⠀⣆⠀⢿⡄⠀⠀
⠀⢸⡇⠀⣽⡇⢸⣿⠟⢡⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠙⢿⣿⠀⣿⡀⠘⣿⠀⠀
⡀⣿⠁⠀⣿⡇⠘⣡⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣦⡙⠀⣿⡇⠀⢻⡇⠀
⢸⡟⠀⡄⢻⣧⣾⡿⢋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣴⣿⠉⡄⢸⣿⠀
⢾⡇⢰⣧⠸⣿⡏⢠⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠓⢶⠶⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠙⣿⡟⢰⡧⠀⣿⠀
⣸⡇⠰⣿⡆⠹⣠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣿⡏⠀⠠⢺⠢⠀⠀⣿⣷⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠸⠁⣾⡇⠀⣿⠀
⣿⡇⠀⢻⣷⠀⣿⡿⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡅⠀⠀⢸⡄⠀⠀⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡆⣰⣿⠁⠀⣿⠀
⢸⣧⠀⡈⢿⣷⣿⠃⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣇⠀⢀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⢿⣧⣿⠃⡀⢸⣿⠀
⠀⣿⡀⢷⣄⠹⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⡟⢁⣴⠇⣼⡇⠀
⠀⢸⡇⠘⣿⣷⡈⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢰⣿⡧⠈⣴⣿⠏⢠⣿⠀⠀
⠀⠀⢿⡄⠘⢿⣿⣦⣿⣯⠘⣆⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⡎⢸⣿⣣⣾⡿⠏⠀⣾⠇⠀⠀
⠀⠀⠈⢷⡀⢦⣌⠛⠿⣿⡀⢿⣆⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢀⣿⡁⣼⡿⠟⣉⣴⠂⣼⠏⠀⠀⠀
⠀⠀⠀⠈⢷⡈⠻⣿⣶⣤⡁⠸⣿⣆⠡⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣾⡟⠀⣡⣴⣾⡿⠁⣴⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣄⠈⢙⠿⢿⣷⣼⣿⣦⠹⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢡⣾⣿⣶⣿⠿⢛⠉⢀⣾⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣧⡀⠳⣦⣌⣉⣙⠛⠃⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠐⠛⠋⣉⣉⣤⡶⠁⣰⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠙⠛⠿⠿⠿⠿⠟⠛⠛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠙⠟⠛⠿⠿⠿⠿⠟⠛⠁⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠙⠶⣦⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⡶⠖⣁⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⡉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠉⠉⠉⠉⣡⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⢦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣠⣴⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    for line in ascciart.strip("\n").split("\n"):
        animated_text(0.0125,center_text(line))
    fress = r"""  _  __             ___          _ 
 | |/ /___ _ _ __ _| _ \___ __ _| |
 | ' </ -_) ' \\ \ /   / -_) _` | |
 |_|\_\___|_||_/_\_\_|_\___\__,_|_|
                                   """
    for line in fress.strip("\n").split("\n"):
        animated_text(0.0125,center_text(line))
    time.sleep(4)
    clean_screen()
    words = ["DEBUG", "INIT", "LOAD", "SUCCESS", "KIPASLESS", "TOOLS", "RUNNING", "PROCESS", "MEMORY"]
    print(r""" _   _       _   __                  _____           _     
| \ | |     | | / /                 |_   _|         | |    
|  \| | __ _| |/ /  ___ _ __ __  __   | | ___   ___ | |___ 
| . ` |/ _` |    \ / _ \ '_ \\ \/ /   | |/ _ \ / _ \| / __|
| |\  | (_| | |\  \  __/ | | |>  <    | | (_) | (_) | \__ \
\_| \_/\__,_\_| \_/\___|_| |_/_/\_\   \_/\___/ \___/|_|___/
                                                           """)
    animated_countdown(1,0.25," Keanu el | Tools   ")
    premium_mode = getpass("Enter premium code or start free mode [X]: ") == "nakenxfr"
    if premium_mode:
        print(center_text("<[HAS ENTERED PREMIUM MODE]>","~"))
        fakeloadrand("activate all premium mode",0.25,5)
        print(center_text("<[PREMIUM MODE]>","~"))
    for a in range(100):
        word = random.choice(words)
        if random.random() <= 0.02:
            word = "ERROR"
        stringcase = random_string(random.randint(4,45))
        print(f"{random.choice(colors)}[{word}] -{stringcase}{RESET}")
        if word == "ERROR":
            stafs = input("Select Y/N to return error phrase: ")
            while stafs != "y" and stafs != "Y" and stafs != "N" and stafs != "n":
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                stafs = input("Please select Y/N to return error phrase!: ")
            print(colors[0])
            print(center_text("|FIXING ERROR|","-"))
            print(RESET)
            if stafs == "Y" or stafs == "y":
                for d in range(random.randint(3,15)):
                    wird = "[KIPASLESS-REPAIR] "+random.choice(words)
                    strcase = random_string(8)
                    print(f"{wird}-{strcase}")
                    time.sleep(random.uniform(0.005,0.05))
                fakeloadrand("fix \033[31mError ",0.2,6)
            else:
                print("INSTALL \033[31m[TOOLFIXING]\033[0m RUNNING -"+random_string())
                fakeloadrand("instaling.. ",0.4,9)
                print("TOOLFIXING Installing Complete..")
        time.sleep(random.uniform(0.006,0.01))
    print(center_text("|>Installing complete<|","~"))

def open_virus_menu():
    clean_screen()
    all_prefixes = [
    "0811","0812","0813","0821","0822","0823","0851","0852","0853",  # Telkomsel
    "0817","0818","0819","0859","0877","0878",                       # XL
    "0814","0815","0816","0855","0856","0857","0858",                # Indosat
    "0895","0896","0897","0898","0899",                               # Tri
    "0881","0882","0883","0884","0885","0886","0887","0888","0889"    # Smartfren
]
    viruses = ["Trojan","Malware","Spyware","Adware"]
    judul = r"""____   ____._____________ ____ ___  ____________________ _________
\   \ /   /|   \______   \    |   \/   _____/\_   _____//   _____/
 \   Y   / |   ||       _/    |   /\_____  \  |    __)_ \_____  \ 
  \     /  |   ||    |   \    |  / /        \ |        \/        \
   \___/   |___||____|_  /______/ /_______  //_______  /_______  /
                       \/                 \/         \/        \/ """
    for line in judul.strip("\n").split("\n"):
        print(center_text(line))
    print(center_text("|>VMENO<|","-"))
    print_array(menu_dict["VIRUS"])
    print(center_text(f"<[Virus name: {viruses[virus_att['virus']]},Phone number: {virus_att['num']}]>","-"))
    index_numpad = int(input("\r S (Close -> -1): "))
    while index_numpad > len(menu_dict["VIRUS"]) or index_numpad < -1:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        index_numpad = int(input("\r S (Close -> -1): "))
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    match index_numpad:
        case -1:open_title_menu()
        case 0:
            virus_att["num"] = input_number("enter the phone number of target. Virus will be sent to the phone with that phone number [BACK]: ")
            open_virus_menu()
        case 1:
            virus_att["virus"] = int(input_number("set virus (Trojan[0], Malware[1], Spyware[2], Adware[3]) [BACK]: ",1))
            open_virus_menu()
        case 2:
            statm = input(f"Are you sure? you will send {viruses[virus_att['virus']]} to {virus_att['num']} [Y/N]: ")
            vasta = statm.capitalize() == "Y"
            if not vasta:
                animated_countdown(2,0.25," Back to main menu in")
                open_title_menu()
            if any(virus_att["num"].startswith(p) for p in all_prefixes):
                fakeloadrand("Processing Api",0.2)
                fakeloadrand(f"Sending to {virus_att['num']}")
                animated_text(0.2,f"{viruses[virus_att['virus']]} was sent to {virus_att['num']} succesfully")
                animated_countdown(2,0.25," Back to main menu in")
                open_title_menu()
            else:
                animated_countdown(1,0.025," Sending failed. error number invalid")
                open_virus_menu()

def open_about_menu():
    clean_screen()
    judul = """          :::     :::::::::   ::::::::  :::    ::: ::::::::::: 
       :+: :+:   :+:    :+: :+:    :+: :+:    :+:     :+:      
     +:+   +:+  +:+    +:+ +:+    +:+ +:+    +:+     +:+       
   +#++:++#++: +#++:++#+  +#+    +:+ +#+    +:+     +#+        
  +#+     +#+ +#+    +#+ +#+    +#+ +#+    +#+     +#+         
 #+#     #+# #+#    #+# #+#    #+# #+#    #+#     #+#          
###     ### #########   ########   ########      ###           """
    for line in judul.strip("\n").split("\n"):
        print(center_text(line))
    print(center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"))
    print("")
    print(center_text("|>Dev<|","-"))
    vrass = []
    vrass.append(create_minlist("Developer","Nakenx/Kenx [Keanu el jabar naga putra]"))
    vrass.append(create_minlist("Version","V0.1.21"))
    vrass.append(create_minlist("LinkTree","https://heylink.me/fredick.xdevs/"))
    print_array(vrass)
    print(center_text("|>You<|","-"))
    vresx = []
    vresx.append(create_minlist("IPV4/Local IP",str(get_local_ip()))) 
    vresx.append(create_minlist("Operation System",platform.system()))
    vresx.append(create_minlist("OS version",platform.version()))
    vresx.append(create_minlist("Release",platform.release()))
    vresx.append(create_minlist("Python version",str(sys.version)))
    vresx.append(create_minlist("Platform",str(sys.platform)))
    vresx.append(create_minlist("Home dir",os.path.expanduser("~"))) 
    print_array(vresx)
    print(center_text("<?>","-"))
    varse = input("Close [-1]: ")
    while varse != "-1":
        varse = input("Close [-1]: ")
    if varse:
        open_title_menu()
    

def open_gametools_menu(game:int):
    clean_screen()
    juduls = [
        """ ____  ____  ____  ____    ____  __  ____  ____ 
(  __)(  _ \(  __)(  __)  (  __)(  )(  _ \(  __)
 ) _)  )   / ) _)  ) _)    ) _)  )(  )   / ) _) 
(__)  (__\_)(____)(____)  (__)  (__)(__\_)(____)""",
        """  __  __     _    _ _            
 |  \/  |___| |__(_) |___        
 | |\/| / _ \ '_ \ | / -_)       
 |_|  |_\___/_.__/_|_\___|  _    
 | |   ___ __ _ ___ _ _  __| |___
 | |__/ -_) _` / -_) ' \/ _` (_-<
 |____\___\__, \___|_||_\__,_/__/
          |___/                  """,
        """ ____  _  _  ____   ___ 
(  _ \/ )( \(  _ \ / __)
 ) __/) \/ ( ) _ (( (_ \
(__)  \____/(____/ \___/""",
        """  ___  ____  __ _  ____  _  _  __  __ _       
 / __)(  __)(  ( \/ ___)/ )( \(  )(  ( \      
( (_ \ ) _) /    /\___ \) __ ( )( /    /      
 \___/(____)\_)__)(____/\_)(_/(__)\_)__)      
  __  _  _  ____   __    ___  ____            
 (  )( \/ )(  _ \ / _\  / __)(_  _)           
  )( / \/ \ ) __//    \( (__   )(             
 (__)\_)(_/(__)  \_/\_/ \___) (__)            """,
        """  ___                    ___         
 / __|_  _ _ __  ___ _ _/ __|_  _ ___
 \__ \ || | '_ \/ -_) '_\__ \ || (_-<
 |___/\_,_| .__/\___|_| |___/\_,_/__/
          |_|                        """,
        ]
    judul = juduls[game]
    for line in judul.strip("\n").split("\n"):
        print(center_text(line))
    print(center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"))
    print("")
    keysgame = list(menu_game_dict.keys())[game]
    print(center_text(f"<[ {keysgame} ]>","-"))
    print_array(menu_game_dict[keysgame])
    print(center_text("<?>","-"))
    picked_index = int(input("\r S : (close -> -1)"))
    if picked_index == -1:
        open_game_menu()
    while picked_index > len(menu_dict["MAIN"]) or picked_index < 0:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        picked_index = int(input("\r S : (close -> -1)"))
    open_title_menu()
    

def input_number(prompt:str,minimum_length:int=10) -> str:
    iniput = input(prompt)
    while not iniput.isdigit and len(iniput)>10 and len(iniput)==0:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        iniput = input(prompt)
    return iniput

def random_string(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

clean_screen()
intro()
fakeloadrand("Loading Resources")
fakeloadrand("Loading Lufrax Engine",0.7,2)
fakeloadrand("Finishing",0.3,5)
load_all()
open_title_menu()
