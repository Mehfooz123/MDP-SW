import os
import sys 
import platform
from github_menu import github_downloader
from youtube_menu import youtube_menu
import version
import color as colors
import credit
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
            
def main_menu():
    while True:
        OSplatformVersion = "Unknown!"
        if(sys.platform.lower() == "win32"):
            OSplatformVersion = f"Windows {sys.getwindowsversion().major}"
        elif(sys.platform.lower() in ["linux", "linux2"]):
            OSplatformVersion = "Linux"
        elif(sys.platform.lower() == "darwin"):
            OSplatformVersion = "Mac OS"
        else:
            OSplatformVersion = "Unknown!"
            CWD = os.getcwd()

        ConsoleTitle = f"{version.name} ({version.version}) - {version.fullname}"

        try:
            os.system(f"title {ConsoleTitle}")
        except:
            actlikenothinghappened = ""
        ColorOfTitle = colors.Color.RANDOM

        print("\r", end="\r")    
        print(colors.Color.Yellow+"┌"+"".center(78, "─")+"┐"+colors.Color.reset)
        print(colors.Color.Yellow+"│"+"".center(78, " ")+"│"+colors.Color.reset)
        print(colors.Color.Yellow+"│"+ColorOfTitle+"$$___$$_ ____ $$$$$___ ____ $$$$$$__ -_$$$$$__ $$___$$_".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+ColorOfTitle+"$$$_$$$_ ____ $$__$$__ ____ $$___$$_ -$$___$$_ $$___$$_".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+ColorOfTitle+"$$$$$$$_ ____ $$___$$_ ____ $$___$$_ -_$$$____ $$_$_$$_".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+ColorOfTitle+"$$_$_$$_ ____ $$___$$_ ____ $$$$$$__ -___$$$__ $$$$$$$_".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+ColorOfTitle+"$$___$$_ _$$_ $$__$$__ _$$_ $$______ -$$___$$_ $$$_$$$_".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+ColorOfTitle+"$$___$$_ _$$_ $$$$$___ _$$_ $$______ -_$$$$$__ $$___$$_".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+"".center(78, " ")+"│"+colors.Color.reset)
        print(colors.Color.Yellow+"│"+ColorOfTitle+f"{version.fullname} ({version.version})".center(78, " ").replace(f"{version.fullname} ({version.version})", f"{colors.Color.bold}{version.fullname} ({version.version}){colors.Color.nobold}")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+colors.Color.Cyan+f"{OSplatformVersion}".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"│"+"".center(78, " ")+"│"+colors.Color.reset)
        print(colors.Color.Yellow+"│"+colors.Color.White+f"{version.CopyrightText}".center(78, " ")+colors.Color.Yellow+"│")
        print(colors.Color.Yellow+"└"+"".center(78, "─")+"┘"+colors.Color.reset)

        colors.window.setTitle(ConsoleTitle) #Trying to change terminal title in every OS' console
        print(f"{colors.Color.White}Welcome to {version.name} Menu.({version.version}){colors.Color.reset}")
        print(f"{colors.Color.White}What service do you want to use?{colors.Color.reset}")
        numbers = ["1","2","3","0"]
        services =["Github ","Youtube","Credit","Exit"]
        for number,Service in zip(numbers, services):
            print(f"[{number}] {Service}")
        tab = input(f"{colors.Color.White}Choose a service:{colors.Color.reset}")
        if tab == "1":
            github_downloader()
        elif tab == "2":
            youtube_menu()
        elif tab == "3":
            credit.credit()
        elif tab.lower() in ("exit", "0", "quit"):
            break
        else:
            clear_console()
            print(f"{colors.Color.Red}Invalid input. Please try again.{colors.Color.reset}")


if __name__ == '__main__':
    main_menu()
