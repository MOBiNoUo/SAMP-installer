#libs : 
import ctypes
import platform
import psutil
import requests
import sys
from zipfile import ZipFile
import os
import time
#defs : 
def print_green(text):
    STD_OUTPUT_HANDLE = -11
    GREEN = 0x02
    
    std_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_handle, GREEN)
    print(text)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_handle, 7)
def print_green_atr(text, atr):
    STD_OUTPUT_HANDLE = -11
    GREEN = 0x02
    
    std_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_handle, GREEN)
    print(text, atr)
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_handle, 7)

#Var : 
cpu_cores = psutil.cpu_count(logical=False)
version = "Beta"

#Codes : 
if platform.system() != "Windows":
    print("This Script For Windows!!!!!")

print_green("Welcome To SA-MP Server Installer v." + version)
print("------------------")
print_green("GitHub.com/MobinOuo")
print_green("OuoMen.ir")
print_green("t.me/OuoMen")
print("------------------")
print_green("OS: " + platform.system())
ram = psutil.virtual_memory()
ram_total = ram.total / (1024.0 ** 3)
print_green("RAM: {:.2f} GB".format(ram_total))
print_green_atr("CPU cores:", cpu_cores)
print("\n")
print_green("Enter Server Name(Default = SA-MP 0.3.7 Server): ")
NameSv = input()
if NameSv == "": 
    NameSv = "SA-MP 0.3.7 Server"
print_green("Enter Server MaxPlayers(Default = 50): ")
MaxPlayerSv = input()
if MaxPlayerSv == "":
    MaxPlayerSv = "50"
print_green("Enter Server Port(Default = 7777): ")
PortSv = input()
if PortSv == "":
    PortSv = "7777"
print_green("Enter Server WebSite(Default = SA-MP.com): ")
SiteSv = input()
if SiteSv == "":
    SiteSv = "SA-MP.com"

print_green("Enter Server Rcon(REQUID): ")
while True:
    RconSv = input()
    if RconSv == "":
        print_green("Enter Server Rcon(REQUID): ")
    else:
        break
    
print_green("Enter Server GameMode: \n 1.FreeRoam \n")
while True:
    GmSv = input()
    if GmSv != 1:
        print_green("Enter Server GameMode: \n 1.FreeRoam \n")
    elif GmSv == 1:
        break
    link = "http://files.sa-mp.com/samp037_svr_R2-1-1_win32.zip"
    file_name = "server-win.zip"
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: 
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
            print_green("\n 1.Download Completed!")
            
        zip_file = "server-win.zip"
        extract_folder = "server"
        if not os.path.exists(extract_folder):
            os.makedirs(extract_folder)
    ZipFile("server-win.zip").extractall("server")
    os.remove("server/server.cfg")
    os.remove("server-win.zip")
    file_path = "server/server.cfg"
    text = "lanmode 0 \nrcon_password " + RconSv + "\nmaxplayers " + MaxPlayerSv + "\nport " + PortSv + "\nhostname " + NameSv + "\ngamemode0 grandlarc 1" + "\nfilterscripts gl_actions gl_realtime gl_property gl_mapicon ls_elevator attachments skinchanger vspawner ls_mall ls_beachside" + "\nannounce 0" + "\nchatlogging 0" + "\nweburl " + SiteSv + "\nonfoot_rate 40" + "\nincar_rate 40" + "\nweapon_rate 40" + "\nstream_distance 300.0" + "\nstream_rate 1000" + "\nmaxnpc 0" + "\nlogtimeformat [%H:%M:%S]" + "\nlanguage English"
    with open(file_path, "w") as f:
        f.write(text)
        print_green(" 2.Configuration Updated!")

    print_green("\n \n 3.Install Finished!!!")

    print_green("\n Start SA-MP Server? (yes or no) :")
    while True:
        run = input()
        if run == "yes":
            print_green("Please Wait 3s")
            time.sleep(3)
            os.system("cd server && samp-server.exe")
        elif run == "no":
            print_green("Ok, Have a Good Day")
            time.sleep(1)
            os.system("taskkill /f /im samp-setup.exe") 
        elif run != "yes" or run != "no":
            print_green("\n Start SA-MP Server? (yes or no) :")
   
    
