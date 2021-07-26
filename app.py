import time, os, json, zipfile, requests, shutil, ctypes
from os import path
season = 5
ctypes.windll.kernel32.SetConsoleTitleW("Fall Guys Rich Presence")
os.system("cls")
userconfpath = path.expandvars(r'%APPDATA%\FallGuysRichPresence\\')
userconffile = userconfpath + "user_conf.json"
userr = userconfpath.split("\\A")[0]
user = userr.split("s\\")[1]
try:
    os.system("taskkill /IM easyrp.exe")
except:
    print("")
if os.path.isfile(userconffile) == True:
    uconf = open(userconffile, "r")
    uconfjson = json.load(uconf)
    appid = uconfjson["Application_Id"]
    fgname = uconfjson["FallGuysPcName"]
    logoname = uconfjson["LogoImageName"]
else:
    os.system("cls")
    appid = input("Input your Application ID: ")
    fgname = input("Input your Fall Guys PC Name: ")
    logoname = input("Input the name of the logo that you uploaded: ")
    def writeudata():
        uconf = open(userconffile, "w")
        uconf.write('{"Application_Id":"'+appid+'","FallGuysPcName":"'+fgname+'","LogoImageName":"'+logoname+'"}')
    try:
        os.makedirs(userconfpath)
        writeudata()
    except:
        writeudata()
os.chdir(userconfpath)
if os.path.isfile(userconfpath + "easyrp.exe") == True:
    print("")
else:
    print("Downloading required data...")
    erpd = requests.get("https://github.com/Pizzabelly/EasyRP/releases/download/v3.0/EasyRP-v3.0-windows.zip", allow_redirects=True)
    open('easyrp.zip', 'wb').write(erpd.content)
    with zipfile.ZipFile("easyrp.zip","r") as easyrpzip:
        easyrpzip.extractall(userconfpath)
    os.rename(userconfpath + "EasyRP-windows\easyrp.exe", userconfpath + "easyrp.exe")
    shutil.rmtree("EasyRP-windows")
    os.remove("easyrp.zip")
timeplaying = time.time()
os.system('start /min "" "easyrp"')
os.system("cls")
def mainpresence():
    global level
    while True:
        fgLog = open("C:/Users/"+user+"/AppData/LocalLow/Mediatonic/FallGuys_client/Player.log", "r")
        logLines = fgLog.readlines()
        try:
            for line in (logLines):
                if "roundID" in line: levelInfo = line
            levelS = levelInfo.split(' loadingScreen')[0]
            level = levelS.split('roundID=')[1]
            if "round_biggestfan" in level:
                level = "Big Fans"
            elif "round_king_of_the_hill" in level:
                level = "Bubble Trouble"
            elif "round_1v1_button_basher" in level:
                level = "Button Bashers"
            elif "round_door_dash" in level:
                level = "Door Dash"
            elif "round_gauntlet_02" in level:
                level = "Dizzy Heights"
            elif "round_iceclimb" in level:
                level = "Freezy Peak"
            elif "round_fruitpunch" in level:
                level = "Big Shots"
            elif "round_dodge_fall" in level:
                level = "Fruit Chute"
            elif "round_chompchomp" in level:
                level = "Gate Cash"
            elif "round_gauntlet_01" in level:
                level = "Hit Parade"
            elif "round_hoops_blockade_solo" in level:
                level = "Hoopsie Legends"
            elif "round_gauntlet_04" in level:
                level = "Knight Fever"
            elif "round_drumtop" in level:
                level = "Lily Leapers"
            elif "round_penguin_solos" in level:
                level = "Pegwin Pool Party"
            elif "round_tunnel_race" in level:
                level = "Roll On"
            elif "round_see_saw" in level:
                level = "See Saw"
            elif "round_shortcircuit" in level:
                level = "Short Circuit"
            elif "round_skeefall" in level:
                level = "Ski Fall"
            elif "round_gauntlet_06" in level:
                level = "Skyline Stumble"
            elif "round_lava" in level:
                level = "Slime Climb"
            elif "round_slimeclimb_2" in level:
                level = "The Slimescraper"
            elif "round_tip_toe" in level:
                level = "Tip Toe"
            elif "round_gauntlet_07" in level:
                level = "Treetop Tumble"
            elif "round_gauntlet_05" in level:
                level = "Tundra Run"
            elif "round_gauntlet_03" in level:
                level = "Whirlygig"
            elif "round_wall_guys" in level:
                level = "Wall Guys"
            elif "round_block_party" in level:
                level = "Block Party"
            elif "round_hoverboardsurvival" in level:
                level = "Hoverboard Heroes"
            elif "round_jump_club" in level:
                level = "Jump Club"
            elif "round_match_fall" in level:
                level = "Perfect Match"
            elif "round_tunnel" in level:
                level = "Roll Out"
            elif "round_snowballsurvival" in level:
                level = "Snowball Survival"
            elif "round_robotrampage_arena_2" in level:
                level = "Stompin' Ground"
            elif "round_tail_tag" in level:
                level = "Tail Tag"
            elif "round_basketfall" in level:
                level = "Basketfall"
            elif "round_egg_grab" in level:
                level = "Egg Scramble"
            elif "round_egg_grab_02" in level:
                level = "Egg Siege"
            elif "round_fall_ball_60_players" in level:
                level = "Fall Ball"
            elif "round_ballhogs" in level:
                level = "Hoarders"
            elif "round_hoops" in level:
                level = "Hoopsie Daisy"
            elif "round_jinxed" in level:
                level = "Jinxed"
            elif "round_chicken_chase" in level:
                level = "Pegwin Persuit"
            elif "round_territory_control" in level:
                level = "Power Trip"
            elif "round_rocknroll" in level:
                level = "Rock N' Roll"
            elif "round_snowy_scrap" in level:
                level = "Snowy Scrap"
            elif "round_conveyor_arena" in level:
                level = "Team Tail Tag"
            elif "round_fall_mountain_hub_complete" in level:
                level = "Fall Mountain"
            elif "round_floor_fall" in level:
                level = "Hex-A-Gone"
            elif "round_jump_showdown" in level:
                level = "Jump Showdown"
            elif "round_crown_maze" in level:
                level = "Lost Temple"
            elif "round_tunnel_final" in level:
                level = "Roll Off"
            elif "round_royal_rumble" in level:
                level = "Royal Fumble"
            elif "round_thin_ice" in level:
                level = "Thin Ice"
            elif level == "Default":
                level = "Lobby"
        except:
            level = "Lobby"
        writeini()
        time.sleep(10)
        
level = "Lobby"
def writeini():
    global level
    inifile = '[Identifiers]\nClientID='+appid+'\n\n[State]\nState='+fgname+'\nDetails=In '+level+'\nStartTimestamp=' +str(timeplaying)+'\nEndTimestamp=\n[Images]\nLargeImage='+logoname+'\nLargeImageTooltip=Fall Guys: Ultimate Knockout!\nSmallImage=\nSmallImageTooltip=PLACEHOLDER'
    ini = open("config.ini", "w", encoding ='utf-8')
    ini.write(inifile)        
writeini()
os.system("cls")
print("Fall Guys: Ultimate Knockout Rich Presence\n\nCurrent season update: Season "+str(season)+"!\n\nPresence is now online.\n\nTo stop the presence press Ctrl + C.")
try:
    mainpresence()
except:
    os.system("taskkill /IM easyrp.exe")
    exit()
