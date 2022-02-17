import time
import pytube
import os
import sys
from termcolor import colored
import datetime
import time 
import requests
from plyer import notification

video = None




print(colored(r"""\             __ __  ______      ___     ___   __    __  ____   _       ___    ____  ___      ___  ____  
            |  |  ||      |    |   \   /   \ |  |__|  ||    \ | |     /   \  /    ||   \    /  _]|    \ 
            |  |  ||      |    |    \ |     ||  |  |  ||  _  || |    |     ||  o  ||    \  /  [_ |  D  )
            |  ~  ||_|  |_|    |  D  ||  O  ||  |  |  ||  |  || |___ |  O  ||     ||  D  ||    _]|    / 
            |___, |  |  |      |     ||     ||  `  '  ||  |  ||     ||     ||  _  ||     ||   [_ |    \ 
            |     |  |  |      |     ||     | \      / |  |  ||     ||     ||  |  ||     ||     ||  .  \
            |____/   |__|      |_____| \___/   \_/\_/  |__|__||_____| \___/ |__|__||_____||_____||__|\_|
                                                                                            ""","cyan"))








def download_prompt():
    try:
        while True:
            url = input("-> Input your video URL: ")
            youtube = pytube.YouTube(url)
            video = youtube.streams.get_highest_resolution()
            print("-> Link imported!")
            print("          ")
            print("Your data: ")
            print("-----------")
            print("-> Video title: ")
            print(youtube._title)
            print("-> Is your video age restricted? ")
            print(youtube._age_restricted)
            print("-----------")
            print("          ")
            time.sleep(3)
            proceed = input("Do you wish to proceed? (Enter = yes): ")
            try:
                    if not proceed:    
                        directory = input("Please enter the directory in which you would like to save the linked file (Enter = script directory): ")
                        if directory:
                            print("You have entered an invalid value, please try again.")
                        elif not directory:
                            print("-> Selected desktop as directory!")
                            print("          ")
                            print("Downloading video....")
                            print("          ")
                            print("Downloading video...")
                            print("          ")
                            print("Downloading video..")
                            print("          ")
                            video.download(directory)
                            try:
                                while True:
                                    print("          ")
                                    print("Downloading video...")
                                    print("          ")
                                    time.sleep(0.2)
                                    print("Downloading video..")
                                    print("          ")
                                    time.sleep(0.2)
                                    print("Downloading video.")
                                    print("          ")
                                    time.sleep(0.2)
                                    print("Downloading video..")
                                    print("          ")
                                    time.sleep(0.3)
                                    print("Downloading video...")
                                    print("          ")
                                    time.sleep(0.4)
                                    time.sleep(2)
                                    print("-> Download successful! Keep in mind that it may take some more time for the entirety of the video to be accessible, depending on the speed of your internet!")
                                    print("          ")
                                    notification.notify(
                                        title = "Your YouTube video was successfully downloaded!",
                                        timeout  = 50)
                                    try:
                                        another_video = input("-> Do you wish to download another video? (Enter = yes): ")
                                        if another_video:
                                            print("Please enter a valid value!")
                                        elif not another_video:
                                            download_prompt()

                                    except Exception:
                                        print("An error occured!")

                                    sys.exit("Thank you for using this script!")
                            except Exception:
                                print("An error occured during download!")
                    elif proceed:
                        print("Abandoning process...")
                        break
                        sys.exit("Thank you for using this script!")
            except Exception:
                    print("An error occured!")   
                    break    
                    sys.exit("Thank you for using this script!")
    except Exception:
        print("An error occured!")
        sys.exit("Thank you for using this script!")


download_prompt()