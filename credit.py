import color as colors

ORIGINAL_CREATOR_FOUNDER = "Mehfooz123"

DEVELOPERS = [
    "Mehfooz123"
]

TRANSLATORS = []


def credit():
    from main import main_menu,clear_console
    clear_console()
    print("")
    print(colors.Color.Orange+"┌"+"".center(104, "─")+"┐")
    print(colors.Color.Orange+"│"+colors.Color.RANDOM+colors.Color.Bold+"Software credit".center(104, " ")+colors.Color.Orange+"│")
    print(colors.Color.Orange+"│"+"".center(104," ")+"│")
    print(colors.Color.Orange+"│"+colors.Color.Cyan+f"Original Creator and Founder: {ORIGINAL_CREATOR_FOUNDER}.".center(104," ").replace(f"{ORIGINAL_CREATOR_FOUNDER}", f"{colors.Color.White}{ORIGINAL_CREATOR_FOUNDER}{colors.Color.Cyan}")+colors.Color.Orange+"│")
    print(colors.Color.Orange+"│"+"".center(104," ")+"│")
    print(colors.Color.Orange+"│"+colors.Color.White+"+====== Developers ======+".center(104," ").replace("Developers", f"{colors.Color.RANDOM}Developers{colors.Color.White}")+colors.Color.Orange+"│")
    print("│"+"".center(104," ")+"│")
    for developer in DEVELOPERS:
        print(colors.Color.Orange+"│"+colors.Color.Blue+f"• {developer} •".center(104," ").replace(f"{developer}", f"{colors.Color.White}{developer}{colors.Color.Blue}")+colors.Color.Orange+"│")
    print(colors.Color.Orange+"│"+"".center(104," ")+"│")
    print(colors.Color.Orange+"│"+colors.Color.White+"+========================+".center(104," ")+colors.Color.Orange+"│")
    print(colors.Color.Orange+"│"+"".center(104," ")+"│")
    print(colors.Color.Orange+"│"+colors.Color.Yellow+"M.D.P-SW © 2023".center(104," ")+colors.Color.Orange+"│")
    print(colors.Color.Orange+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
    print("")
    PressToContinue = input("Press Enter to continue . . . ")
    print()