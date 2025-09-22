import sys , time , os , random , string , socket , platform , requests , math , json , uuid , hashlib
from getpass import getpass

BASE_URL = "https://talksupsoc-default-rtdb.firebaseio.com/"
# Warna teks (foreground)
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
# Warna terang (bright)
BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"
# Warna background
BG_BLACK   = "\033[40m"
BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN    = "\033[46m"
BG_WHITE   = "\033[47m"
# Background terang (bright)
BG_BRIGHT_BLACK   = "\033[100m"
BG_BRIGHT_RED     = "\033[101m"
BG_BRIGHT_GREEN   = "\033[102m"
BG_BRIGHT_YELLOW  = "\033[103m"
BG_BRIGHT_BLUE    = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN    = "\033[106m"
BG_BRIGHT_WHITE   = "\033[107m"
# Reset (balikin ke default)
RESET = "\033[0m"
# Abu-abu
DARK_GRAY  = "\033[90m"  # abu gelap
LIGHT_GRAY = "\033[37m"  # abu terang
BG_DARK_GRAY  = "\033[100m"
BG_LIGHT_GRAY = "\033[47m"
USERNAME :str = "anonymous312"

JUDUL_MAINMENU = """    __  ___ __       __                   __                  
   / / / (_) /______/ /_  ___  __________/ /   ___  __________
  / /_/ / / __/ ___/ __ \/ _ \/ ___/ ___/ /   / _ \/ ___/ ___/
 / __  / / /_/ /__/ / / /  __(__  |__  ) /___/  __(__  |__  ) 
/_/ /_/_/\__/\___/_/ /_/\___/____/____/_____/\___/____/____/  
                                                              """
JUDUL_ABTMENU = """    ___    __                __ 
   /   |  / /_  ____  __  __/ /_
  / /| | / __ \/ __ \/ / / / __/
 / ___ |/ /_/ / /_/ / /_/ / /_  
/_/  |_/_.___/\____/\__,_/\__/  
                                """
JUDUL_GMEMENU = """   _________    __  ___________  _____   ________ __
  / ____/   |  /  |/  / ____/ / / /   | / ____/ //_/
 / / __/ /| | / /|_/ / __/ / /_/ / /| |/ /   / ,<   
/ /_/ / ___ |/ /  / / /___/ __  / ___ / /___/ /| |  
\____/_/  |_/_/  /_/_____/_/ /_/_/  |_\____/_/ |_|  
                                                    """
JUDUL_VIRUS = """ _    __________  __  _______ ___________
| |  / /  _/ __ \/ / / / ___// ____/ ___/
| | / // // /_/ / / / /\__ \/ __/  \__ \ 
| |/ // // _, _/ /_/ /___/ / /___ ___/ / 
|___/___/_/ |_|\____//____/_____//____/  
                                         """
JUDUL_FIREBASE = """    ______________  __________  ___   _____ ______
   / ____/  _/ __ \/ ____/ __ )/   | / ___// ____/
  / /_   / // /_/ / __/ / __  / /| | \__ \/ __/   
 / __/ _/ // _, _/ /___/ /_/ / ___ |___/ / /___   
/_/   /___/_/ |_/_____/_____/_/  |_/____/_____/   
                                                  """
JUDUL_HACK = """    __  _____   ________ __ __    ________________
   / / / /   | / ____/ //_// /   / ____/ ___/ ___/
  / /_/ / /| |/ /   / ,<  / /   / __/  \__ \\__ \ 
 / __  / ___ / /___/ /| |/ /___/ /___ ___/ /__/ / 
/_/ /_/_/  |_\____/_/ |_/_____/_____//____/____/  
                                                  """

def clamp(x, lo, hi):
    if lo > hi:
        raise ValueError("lo tidak boleh lebih besar dari hi")
    return max(lo, min(x, hi))

def fake_load(prefix:str,max_rndtime:float=0.3, max_rndvalue:float=0.75,is_idle:bool=True):
    progress = 0.0
    while progress <= 25.0:
        progress += random.uniform(0,max_rndvalue)
        print(f"\033[93m{prefix} \033[32m[{"■"*int(progress)}{"☐"*int(25.0-progress)}] {clamp(int(progress*4),0,100)}%\033[0m")
        if is_idle:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
        time.sleep(random.uniform(0.0001,max_rndtime/clamp((progress/25.0)*1.5,1,1.5)))

def get_size() -> dict:
    vaenge = os.get_terminal_size()
    return {
        "X":vaenge.columns,
        "Y":vaenge.lines
    }

def center_text(text:str,fillchart:str=" ") -> str:
    return text.center(get_size()["X"],fillchart)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_output(count:int=50):
    words = ["DEBUG", "INIT", "LOAD", "SUCCESS", "KIPASLESS", "TOOLS", "RUNNING", "PROCESS", "MEMORY" , "FIX"]
    virds = [
        f" ran {GREEN}succesfully with no errors {RESET}[lufrax]\n{YELLOW}programs was scaned;{RESET}",
        "",
        f" ran {RED}failed{RESET}\nrerunning programs...\n{BLUE}fixxed, run normally;{RESET}",
    ]
    for ran in range(count):
        word = random.choice(words)
        strings = random_string(random.randint(45,100))
        strings += "\n"+word.lower()+random.choice(virds)
        if random.random() <= 0.025:
            word = "ERROR"
            strings += f", CODE -{random.randint(100,200)}"
        print(f"[{word}] => {strings};")
        if word == "ERROR":
            print(RED+center_text(" -<FIX ERROR>- ","-"))
            print(f"Fixing errors phrase, {strings}\nrequest repairing error -u --y\nrequest accepted fix -{strings}")
            fake_load(f"Fixing error [-u --y sorx, plyteu, dcireg]",0.05,0.95)
            print(f"{RED}error fixxed dirs...\n{strings} fixxed -u --y;")
            fake_load("Reloading <[ HITCHLESS ]>",0.1,0.65)
            print(RED+center_text(" -<!>- ","-")+RESET)
        time.sleep(random.uniform(0.001,0.125))

def logos(duration:float):
    print(GREEN)
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
        animated_text(0.0025,center_text(line))
    fress = r"""  _  __             ___          _ 
 | |/ /___ _ _ __ _| _ \___ __ _| |
 | ' </ -_) ' \\ \ /   / -_) _` | |
 |_|\_\___|_||_/_\_\_|_\___\__,_|_|
                                   """
    for line in fress.strip("\n").split("\n"):
        animated_text(0.0025,center_text(line))
    time.sleep(duration)
    for ass in range(len(fress.strip("\n").split("\n"))+len(ascciart.strip("\n").split("\n"))):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()
        time.sleep(0.025)

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

def print_array(array:list):
    for a in array:
        print(a)

def print_center_array(array:list,fillcahart:str=" "):
    for a in array:
        print(center_text(a,fillcahart))

def random_string(length=8):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def introduce():
    fake_load("Launching file [S1.py]",0.125,1.5)
    clear()

def makelistray(namelist:list) -> list:
    lisall = []
    for a in range(len(namelist)):
        lisall.append(create_menuinlist(namelist[a],a))
    return lisall

def create_minlist(pc1:str,pc2:str) -> str:
    return f"\033[38;5;15;48;5;236m> {pc1} => {pc2}\033[0m\n   \033[90m{random_string(50)}\n {random_string(50)}{RESET}"

def create_menuinlist(NAME:str,index:int) -> str:
    return f"\033[38;5;15;48;5;236m> {NAME} -> [{index}]\033[0m\n   \033[90m{random_string(50)}\n {random_string(50)}{RESET}"


def open_custom_menu(title:str,subtitle:str,prompt:str,openstr:str,closestr:str,dictionaryoption:dict,backmenu):
    clear()
    for line in title.strip("\n").split("\n"):
        print(center_text(line))
    print(subtitle)
    print(openstr)
    print_array(makelistray(list(dictionaryoption.keys())))
    print(closestr)
    option:int = inputnum(prompt,-1,len(list(dictionaryoption.keys())))
    if option == -1:
        backmenu()
    else:
        dictionaryoption[list(dictionaryoption.keys())[option]]()

def open_custom_static_menu(title:str,subtitle:str,prompt:str,openstr:str,closestr:str,listoption:list,backmenu):
    clear()
    for line in title.strip("\n").split("\n"):
        print(center_text(line))
    print(subtitle)
    print(openstr)
    print_array(makelistray(listoption))
    print(closestr)
    option:int = inputnum(prompt,-1,0)
    if option == -1:
        backmenu()

def inputnum(prompt:str,minnum:int=-1,maxnum:int=0) -> int:
    while True:
        num:str = input(prompt)
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        if num.isdigit:
            if int(num) >= minnum and int(num) < maxnum:
                return int(num)

def open_menu(menu_index:int):
    listofmenu:list = [
        create_menu_lister(JUDUL_MAINMENU,center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"),"S (-1 => Close): ",center_text("<|MAIN MENU|>","-"),center_text("<?>","-"),{"[+] HACKERMODES":open_hackmenu,"[+] ONLINEMODES":open_onlinemenu,"[+] ABOUT":open_abtmenu,"[X] EXIT":exit_pls},open_mainmenu),
        create_menu_lister(JUDUL_HACK,center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"),"S (-1 => Close): ",center_text("<|HACKERS|>","-"),center_text("<?>","-"),{"[-] GAMES":open_gamemenu,"[-] VIRUS":open_virusmenu,"[-] DDOS":open_ddosmenu},open_mainmenu),
        create_menu_lister(JUDUL_FIREBASE,center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"),"S (-1 => Close): ",center_text("<|FIREBASE ONLINE|>","-"),center_text(f"< username: {USERNAME} >","-"),{"[-] SET USERNAME":set_usn,"[-] CHAT":open_chatmenu,"[-] ABOUT":open_frabtmenu},open_mainmenu),
    ]
    menudict:dict = listofmenu[menu_index]
    open_custom_menu(menudict["title"],menudict["subtitle"],menudict["prompt"],menudict["openstr"],menudict["closestr"],menudict["dict"],menudict["backmenu"])

def open_frabtmenu():
    pass

def open_chatmenu():
    pass

def set_usn():
    clear()
    print(center_text("<|change your username|>","-"))
    stats = input("change [Y/N: ]")
    while stats.capitalize() != "Y" and stats.capitalize() != "N":
      stats =input("change [Y/N: ]")
    value = stats.capitalize()
    if value == "Y":
      global USERNAME
      USERNAME = input("enter username: ")
      send_data({"name":USERNAME},f"/user/{get_device_code()}.json")
      open_onlinemenu()
    else:
      animated_countdown(1,0.25," Back to OnlineMenu")
      open_onlinemenu()

def open_gamemenu():
    pass

def open_hackmenu():
    open_menu(1)

def open_ddosmenu():
    pass

def open_virusmenu():
    pass

def get_local_ip() -> any:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def open_abtmenu():
    vrass = []
    vrass.append(center_text("|>Dev<|","-"))
    vrass.append(create_minlist("Developer","Nakenx/Kenx [Keanu el jabar naga putra]"))
    vrass.append(create_minlist("Version","V0.1.21"))
    vrass.append(create_minlist("LinkTree","https://heylink.me/fredick.xdevs/"))
    vrass.append(center_text("|>You<|","-"))
    vrass.append(create_minlist("IPV4/Local IP",str(get_local_ip()))) 
    vrass.append(create_minlist("Operation System",platform.system()))
    vrass.append(create_minlist("OS version",platform.version()))
    vrass.append(create_minlist("Release",platform.release()))
    vrass.append(create_minlist("Python version",str(sys.version)))
    vrass.append(create_minlist("Platform",str(sys.platform)))
    vrass.append(create_minlist("Home dir",os.path.expanduser("~"))) 
    open_custom_static_menu(JUDUL_ABTMENU,center_text("V0.1.21 | By Nakenx/Kenx | PassEncryptKey : uOFeIdQIQXEkqLXocUw49Q== , N4K3NX"),"S (-1 => Close): ",center_text("<|ABOUT..|>","-"),center_text("<?>","-"),vrass,open_mainmenu)

def open_mainmenu():
    open_menu(0)

def open_onlinemenu():
    open_menu(2)

def exit_pls():
    clear()
    animated_countdown(1,0.25," EXITING PROGRAM..")

def send_data(data: dict,url:str):
    url = f"{BASE_URL}{url}.json"
    r = requests.put(url, data=json.dumps(data))

def create_menu_lister(title:str,subtitle:str,prompt:str,openstr:str,closestr:str,dictionaryoption:dict,backmenu) -> dict:
    return{
            "title":title,
            "subtitle":subtitle,
            "prompt":prompt,
            "openstr":openstr,
            "closestr":closestr,
            "dict":dictionaryoption,
            "backmenu":backmenu
        }

def get_device_code() -> str:
    mac_num = uuid.getnode()

    raw = str(mac_num).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]

def loads():
    loadata = get_data(f"/user/{get_device_code()}/name")
    if not loadata is None:
        global USERNAME
        USERNAME = loadata
    else:
        send_data({"name":USERNAME},f"/user/{get_device_code()}.json")



def get_data(path: str) -> dict | None:
    url = f"{BASE_URL}{path}.json"
    resp = requests.get(url)

    if resp.status_code == 200:
        data = resp.json()
        if data is None:
            return None
        return data
    else:
        raise Exception(f"Gagal ambil data: {resp.status_code} - {resp.text}")

clear()
logos(1.5)
loads()
clear()
introduce()
fake_output(125)
clear()
print(DARK_GRAY+center_text(" -<HITCHLESS>- ","-")+RESET)
ilim = getpass("press [Enter] button to continue...")
animated_countdown(1,0.125," FINISHING...")
clear()
open_menu(0)