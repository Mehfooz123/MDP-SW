import os
import git
from time import sleep
from datetime import datetime
import color as colors
import validators

def github_downloader():
    while True:
        from main import clear_console, main_menu
        clear_console()
        colors.window.addToTitle("GitHub")
        print("Starting GitHub downloader...")
        print("")
        print(colors.Color.purple+"┌"+"".center(104, "─")+"┐")
        print(colors.Color.purple+"│"+colors.Color.RANDOM+"GitHub Service".center(104, " ")+colors.Color.purple+"│")
        print(colors.Color.purple+"│"+"".center(104, " ")+"│")
        print(colors.Color.purple+"│"+colors.Color.white+"Here you can download GitHub repositories and get information about them".center(104, " ")+colors.Color.purple+"│")
        print(colors.Color.purple+"│"+colors.Color.white+"You must include a GitHub repository link such as: https://github.com/Mehfooz123/MDP-SW".center(104, " ").replace("https://github.com/Mehfooz123/MDP-SW", f"{colors.Color.Underline}https://github.com/Mehfooz123/MDP-SW{colors.Color.Nounderline}")+colors.Color.purple+"│")
        print(colors.Color.purple+"│"+"".center(104, " ")+"│")
        print(colors.Color.purple+"│"+colors.Color.cyan+"Type \"exit\" to leave this service. If you got any bug please report it!".center(104, " ").replace("CANCEL", f"{colors.Color.red}CANCEL{colors.Color.cyan}")+colors.Color.purple+"│")
        print(colors.Color.purple+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
        print("")
        colors.window.addToTitle("GitHub")
        print(f"{colors.Color.white}Please enter the URL of the GitHub repository:{colors.Color.reset} ")
        repository_url = input("Enter:")
        if repository_url.lower() == "exit":
            clear_console()
            main_menu()
        try:
            repo_name = repository_url.split("/")[-1].replace(".git", "")
            publisher_name = repository_url.split("/")[-2]
            download_path = os.path.join(os.getcwd(), "github", repo_name)

            if os.path.exists(download_path):
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                download_path = os.path.join(os.getcwd(), "github", f"{repo_name}-{timestamp}")

            git.Repo.clone_from(repository_url, download_path)
            print(f"The repository '{repo_name}' by '{publisher_name}' has been successfully downloaded to {download_path}")

            branches = git.Repo(download_path).branches
            if len(branches) == 1 and branches[0].name == "main":
                print("Only the main branch is available. Downloading main branch...")
                git.Repo(download_path).git.checkout("main")
            elif len(branches) > 1:
                branch_choice = input("Do you want to download a specific branch? (y/n)\n")
                if branch_choice.lower() == "y":
                    branch_names = [f"{branch.name}" for branch in branches]
                    print(f"\nAvailable branches: {', '.join(branch_names)}")
                    while True:
                        branch_name = input("Please enter the name of the branch:\n")
                        if branch_name in branch_names:
                            git.Repo(download_path).git.checkout(branch_name)
                            break
                        else:
                            print("Invalid branch name. Please try again.")
            print("Download complete.")
            sleep(2)
            clear_console()
            main_menu()
        except IndexError as e:
            print("Invalid URL. Please enter a valid GitHub repository link.")
            sleep(2)
            continue
        except Exception as e:
            print("An error occurred. Maybe the link is not correct or the folder name already exists.")
            print(str(e))
            sleep(2)
            clear_console()
            main_menu()
        