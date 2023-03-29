from pytube import YouTube
from time import sleep
from youtubeServices import download_video
import color as colors

def print_menu():
    print("")
    print(colors.Color.Red+"┌"+"".center(104, "─")+"┐")
    print("│"+colors.Color.Bold+colors.Color.RANDOM+"YouTube Services Menu".center(104," ").replace("YouTube", f"{colors.Color.White}You{colors.Color.Red}Tube{colors.Color.RANDOM}")+colors.Color.NoBold+colors.Color.Red+"│")
    print("│"+"".center(104," ")+"│")
    print(colors.Color.Red+"│"+colors.Color.White+"Here where you can download and get info of YouTube videos that you want for free!".center(104," ")+colors.Color.Red+"│")
    print(colors.Color.Red+"│"+colors.Color.White+"And you can do same with Thumbnails.".center(104," ")+colors.Color.Red+"│")
    print("│"+"".center(104," ")+"│")
    print("│"+"REMEMBER: Downloading copyrighted YouTube videos is ILLEGAL! I'm NOT responsible for your downloads.".center(104," ")+"│")
    print("│"+"You must know how, why and where to use copyrighted items.".center(104," ")+"│")
    print(colors.Color.Red+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
    print("")
    numbers = ["1","2","0"]
    Services = ["Download a Yotube video","Download a thumbnail of a video","Back to main menu"]
    for number,Service in zip(numbers, Services):
        print(f"[{number}] {Service}")
    print("")

def youtube_menu():
    while True:
        
        from main import clear_console, main_menu
        clear_console()
        print_menu()
        colors.window.addToTitle("Youtube")
        choice = input(f"{colors.Color.White}Pick an option:{colors.Color.reset} ")

        if choice == '0':
            clear_console()
            colors.window.restoreTitle()
            main_menu()
        elif choice == '1':
            clear_console()
            url = input(f"{colors.Color.white}Enter video URL:{colors.Color.reset} ")
            try:
                yt = YouTube(url)
            except:
                print(f"{colors.Color.Red}Invalid video URL. Please try again.{colors.Color.reset}")
                sleep(2)
                continue

            video_info = {'title': yt.title,
                          'description': yt.description,
                          'duration': yt.length,
                          'formats': [{'qualityLabel': f'{stream.resolution}', 'url': stream.url}
                                      for stream in yt.streams.filter(progressive=True)]
                         }
            print(f"Title: {video_info['title']}")
            print(f"Description: {video_info['description']}")
            print(f"Duration: {video_info['duration']} seconds")
            formats = video_info['formats']
            if not formats:
                print(f"{colors.Color.Red}No video formats available. Please try another video.{colors.Color.reset}")
                sleep(2)
                continue

            print(f"{colors.Color.White}\nAvailable Resolutions:{colors.Color.reset}")
            for i, format in enumerate(formats):
                print(f"{i+1}. {format['qualityLabel']}")

            while True:
                selection = input("Enter resolution number to download (0 to go back): ")
                if selection == '0':
                    break
                try:
                    selection = int(selection)
                    if selection < 1 or selection > len(formats):
                        print(f"{colors.Color.Red}Invalid resolution choice. Please enter a number between 1 and", len(formats),colors.Color.reset)
                    else:
                        break
                except ValueError:
                    print(f"{colors.Color.Red}Invalid input. Please enter a number.{colors.Color.reset}")
            
            if selection == 0:
                continue
            
            selected_format = formats[selection-1]
            if 'url' not in selected_format:
                print(f"{colors.Color.red}Invalid video format. Please try another resolution.{colors.Color.reset}")
                sleep(2)
                continue

            url = selected_format['url']
            filename = f"./youtube/{video_info['title']}_{selected_format['qualityLabel']}.mp4"
            download_video(url, filename)

            print(f"{colors.Color.Green}Video downloaded & saved to {filename}{colors.Color.reset}")
        elif choice == "2":
            from youtubeServices import download_thumbnail
            url = input(f"{colors.Color.white}Enter video URL:{colors.Color.reset} ")
            try:
                yt = YouTube(url)
            except:
                print(f"{colors.Color.red}Invalid URL. Please try again{colors.Color.reset} ")
                sleep(2)
                continue
            try:
                download_thumbnail(url)
                print(f"{colors.Color.Green}Download succesfully completed.{colors.Color.reset}")
                sleep(5)
            except Exception as e:
                print("An error occured please report")
                print(e)
                sleep(5)
        else:
            print(f"{colors.Color.red}Invalid choice. Try again.{colors.Color.reset}")
            sleep(2)