import datetime
import os
import subprocess
import sys
import time
import webbrowser
import instaloader
import pyautogui
import pyaudio
import pygetwindow
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import speedtest
import wikipedia
from pynput.keyboard import Key, Controller

keyboard = Controller()
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[0].id)


def speak(audio):
    assistant.say(audio)
    print(audio)
    assistant.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Hi Sir , I am Astra , Welcome to the the world of AI and Machine Learning")


chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


def open_chrome_incognito():
    args = [chrome_path, "--incognito"]
    subprocess.Popen(args)
    speak('Chrome opened in incognito mode')


if __name__ == '__main__':

    wishMe()
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("wikipedia on", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'page down' in query or 'next page' in query or 'next' in query:
            # speak('Turning page down, sir')
            keyboard.press(Key.page_down)
            keyboard.release(Key.page_down)
            time.sleep(0.1)

        elif 'page up' in query or 'previous page' in query or 'go back' in query or 'back' in query:
            # speak('Turning page up, sir')
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)
            time.sleep(0.1)

        elif "volume up" in query:  # w
            speak("Turning volume up,sir")

            from asseceries import volumeup

            volumeup()

        elif "volume down" in query:  # w
            speak("Turning volume down, sir")
            from asseceries import volumedown

            volumedown()

        elif "pause" in query:
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause)
            time.sleep(0.1)
            speak("paused")

        elif "play" in query:  # w
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause)
            time.sleep(0.1)
            speak("played")

        elif "mute" in query:  # w
            keyboard.press(Key.media_volume_mute)
            keyboard.release(Key.media_volume_mute)
            time.sleep(0.1)
            speak("muted")

        elif "unmute" in query:  # w
            keyboard.press(Key.media_volume_mute)
            keyboard.release(Key.media_volume_mute)
            time.sleep(0.1)
            speak("unmuted")

        elif 'next song' in query:  # w
            speak('Playing next sir')
            keyboard.press(Key.media_next)
            keyboard.release(Key.media_next)
            time.sleep(0.1)

        elif 'previous song' in query:  # w
            speak('Playing previous sir')
            keyboard.press(Key.media_previous)
            keyboard.release(Key.media_previous)
            time.sleep(0.1)

        elif 'turn on bluetooth' in query:  # w
            speak('Turning on bluetooth, sir')
            from asseceries import turn_bluetooth_on

            turn_bluetooth_on()
            time.sleep(0.1)
            speak('Done sir')

        elif 'turn off bluetooth' in query:  # w
            speak('Turning off bluetooth, sir')
            from asseceries import turn_bluetooth_off

            turn_bluetooth_off()
            time.sleep(0.1)
            speak('Done sir')

        elif 'repeat' in query:  # w
            speak('What should i repeat')
            repeat = takeCommand()
            speak(repeat)

        elif 'what is ' in query:  # w
            speak("Searching...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is ' in query:
            speak("Searching...")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'website' in query:  # w
            speak('opening website')
            speak('This is what i found')
            query = query.replace('jarvis', '')
            query = query.replace('website', '')
            query = query.replace(' ', '')
            web1 = query.replace('open', '')
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak('Done sir')

        elif 'instagram profile' in query or 'profile on instagram' in query:  # w
            speak('Please provide me name of instagram profile')
            name = input('Please provide me name of instagram profile :-')
            web = 'https://www.instagram.com/' + name
            webbrowser.open(web)
            speak(f'Here is the profile of {name}')
            time.sleep(2)
            speak('Would you like to download profile picture?')
            condition = takeCommand().lower()
            if 'yes' in condition:
                speak('Downloading profile picture')
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak('Done sir')
            speak('Done sir')

        elif 'your ip address' in query:  # w
            from asseceries import get_public_ip

            ip = get_public_ip()
            if ip:
                speak(f"My IP address is {ip}")
            else:
                speak("Sorry, unable to get your IP address")

        elif 'where am I' in query or 'where are you' in query:  # w
            speak('Wait sir, i am finding our location')
            from asseceries import get_public_ip

            ip = get_public_ip()
            ip_address = ip
            response = requests.get(
                f"http://api.ipstack.com/{ip_address}?access_key=b3ab8abfd864be4ea616abd011aa69b2&format=1'")  # https://ipstack.com/
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Extract relevant information
                IP = data['ip'],
                City = data['city'],
                Region = data['region_name'],
                Country = data['country_code'],
                Country_name = data['country_code'],
                latitude = data['latitude'],
                longitude = data['longitude'],
                speak(f'Sir my ip address is :-{IP}')
                speak(f"Sir, I am in {City} city , {Region} state,in {Country} country")
                speak("Would you like to open maps to see your location?")
                condition = takeCommand().lower()
                if 'yes' in condition:
                    speak('Opening in maps sir')
                    webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={longitude}+{longitude}")

                speak("Done sir")
            else:
                print("Unable to retrieve location data.")

        elif 'read pdf' in query:
            from asseceries import pdfreader

            pdfreader()

        elif 'launch' in query:  # w
            speak('Please provide me name of website to launch')
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak('Done sir')

        elif 'open youtube' in query:  # w
            speak('What should I search')
            search = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/search?q={search}")
            speak("Searching...")
            speak(f"Here are some results for {search}")

        elif 'open google' in query:  # w
            speak('What should I search')
            search = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={search}")
            speak("Searching...")
            speak(f"Here are some results for {search}")

        elif 'google' in query:  # w
            speak('opening google')
            import webbrowser

            speak('This is what i found')
            query = query.replace('jarvis', '')
            query = query.replace('google', '')
            webbrowser.open('https://www.google.com/search?q=' + query)
            speak('Done sir')

        elif 'incognito mode' in query:  # w
            open_chrome_incognito()
            speak('Done sir')

        elif 'dictionary' in query:
            from asseceries import mean

            speak('Activated Diconary')
            speak('Say the problem to help you with.')
            query = takeCommand().lower()
            mean(query)
            speak('Dictionary Done')

        elif 'let some music begin' in query or 'music' in query:
            speak('Sir Offline, or online')
            query = takeCommand().lower()
            if 'offline' in query:
                music_dir = 'E:\\dj'
                songs = os.listdir(music_dir)
                print(songs)
                for song in songs:
                    if song.endswith(".mp3"):
                        os.startfile(os.path.join(music_dir, song))
            elif 'online' in query:
                webbrowser.open("https://music.youtube.com/")

        elif 'the time' in query:  # w
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open" in query:  # working
            query = query.replace("open", "")
            query = query.replace("jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.press("enter")
            speak("Opening " + query)
            pyautogui.sleep(2)

        elif 'close' in query:  # w
            application_name = takeCommand().lower()
            query = query.replace("jarvis", "")
            from asseceries import close_application

            close_application(application_name)
            speak('closing')

        elif 'screenshot' in query:  # w
            speak('What should I name the file')
            filename = takeCommand()
            speak('Taking screenshot')
            img = pyautogui.screenshot()
            img.save(f"C:\\Jarvis ui automation\\{filename}.png")  # location of the screenshot
            speak('Done sir')
            os.startfile(f'C:\\Jarvis ui automation\\{filename}.png')
            speak('Here is your screenshot')

        elif 'chrome automation' in query:
            from asseceries import chromeautomation

            chromeautomation()

        elif 'enable Wi-Fi' in query:
            speak('Enabling wifi')
            from asseceries import enable_wifi

            enable_wifi()

        elif 'disable Wi-Fi' in query:
            speak('Disabling wifi')
            from asseceries import disable_wifi

            disable_wifi()

        elif 'send message' in query:
            speak('What should I say')
            message = takeCommand()
            pywhatkit.sendwhatmsg("+919484500837", message, 21, 12)
            speak('Message sent')
            speak('Done sir')

        elif 'send email' in query:
            from asseceries import send_email

            speak('What is the subject')
            subject = takeCommand()
            speak('what should I say')
            body = takeCommand()
            send_email(subject, body)
            speak('Email sent')
            speak('Done sir')

        elif "about train" in query:
            import pyttsx3
            import requests
            from pynput.keyboard import Controller

            keyboard = Controller()
            assistant = pyttsx3.init('sapi5')
            voices = assistant.getProperty('voices')
            assistant.setProperty('voice', voices[1].id)


            def speak(audio):
                assistant.say(audio)
                print(audio)
                assistant.runAndWait()


            def format_time(time_str):
                if time_str:
                    hour = int(time_str[:2])
                    minute = time_str[2:]
                    if hour == 0:
                        return f"12:{minute} AM"
                    elif hour < 12:
                        return f"{hour}:{minute} AM"
                    elif hour == 12:
                        return f"12:{minute} PM"
                    else:
                        return f"{hour - 12}:{minute} PM"
                return "N/A"


            url = "https://trains.p.rapidapi.com/"
            trainn = input(speak("Enter train number:"))
            payload = {"search": trainn}
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "02216dc0b5mshd3b45769369672ap19d801jsn617d29ebdc5e",
                "X-RapidAPI-Host": "trains.p.rapidapi.com"
            }
            response = requests.post(url, json=payload, headers=headers)
            for item in response.json():
                speak(f"Train number: {item['train_num']}")
                speak(f"Name: {item['name']}")
                print(f"Train from: {item['train_from']}")
                print(f"Train to: {item['train_to']}")
                print("Data:")
                for key, value in item["data"].items():
                    if key == "days":
                        days = ", ".join([k[:3].capitalize() for k, v in value.items() if v == 1])
                        speak(f"Days: {days}")
                    elif key == "arriveTime":
                        speak(f"Arrival time {format_time(value)}")
                    elif key == "departTime":
                        speak(f"Departure time {format_time(value)}")
                    else:
                        print(f"{key}:{value}")
            speak('Done sir')

        elif "station code" in query:
            import requests

            url = "https://rstations.p.rapidapi.com/"
            speak("Enter station name")
            station_name = input(": ")
            payload = {"search": f"{station_name}"}
            headers = {
                "content-type": "application/json",
                "Content-Type": "application/json",
                "X-RapidAPI-Key": "02216dc0b5mshd3b45769369672ap19d801jsn617d29ebdc5e",
                "X-RapidAPI-Host": "rstations.p.rapidapi.com"
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json())
            speak("Done sir")

        elif "check pnr" in query:
            import requests

            speak("Enter pnr number")
            pnr = input(": ")
            url = f"https://real-time-pnr-status-api-for-indian-railways.p.rapidapi.com/indianrail/{pnr}"
            headers = {
                "X-RapidAPI-Key": "02216dc0b5mshd3b45769369672ap19d801jsn617d29ebdc5e",
                "X-RapidAPI-Host": "real-time-pnr-status-api-for-indian-railways.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            print(response.json())
            speak("Done sir")

        elif 'news' in query:
            from asseceries import news
            news()

        elif 'see you soon' in query:  # w
            speak('See you soon sir')
            sys.exit()
            break

        elif 'bye' in query:  # w
            speak('Bye sir')
            sys.exit()
            break

        elif 'shutdown' in query:
            speak('Shutting down')
            os.system("shutdown /s /t 0")
            break

        elif 'restart' in query:
            speak('Restarting')
            os.system("shutdown /r /t 0")
            break

        elif 'sleep' in query:
            speak('Sleeping')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            break

        elif 'log off' in query:
            speak('Logging off')
            os.system("shutdown /l")
            break

        elif 'lock' in query:  # w
            speak('Locking')
            os.system('rundll32.exe user32.dll,LockWorkStation')
            break

        elif 'hibernate' in query:
            speak('Hibernate')
            os.system('shutdown /h')
            break

        elif 'switch the windows' in query:  # w
            speak('Switching the windows')
            pyautogui.hotkey('win', 'down')
            break

        elif 'minimise' in query:
            speak('Minimizing')
            pyautogui.hotkey('alt', 'f4')

        elif 'maximize' in query:
            speak('Maximizing')
            pyautogui.hotkey('win', 'up')

        elif 'show the desktop' in query:  # w
            speak('Showing the desktop')
            pyautogui.hotkey('win', 'd')

        elif 'show all windows' in query:
            speak('Showing all windows')
            all_windows = pygetwindow.getAllWindows()

        elif "internet speed" in query:  # w
            wifi = speedtest.Speedtest()
            wifi.get_best_server()
            upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
            download_net = wifi.download() / 1048576

            upload_net = round(upload_net, 2)
            download_net = round(download_net, 2)

            speak("Internet Speed is")
            speak(f"Wifi Upload speed is {upload_net} Mbps")
            print("Wifi Upload Speed is:- ", upload_net)
            speak(f"Wifi download speed is {download_net} Mbps")
            print("Wifi Download Speed is:- ", download_net)
            speak(f"Wifi ping is {wifi.results.ping} ms")
            print("Wifi ping is:-", wifi.results.ping)

        elif "remember that" in query or "remind me to do" in query:
            rememberMessage = query.replace("remember that", "")
            rememberMessage = query.replace("friday", "")
            rememberMessage = query.replace("friday remind me to", "")
            rememberMessage = query.replace("friday remind me to do", "")
            rememberMessage = query.replace("remind me to do", "")
            speak("You told me to " + rememberMessage)
            remember = open("Remember.txt", "w")
            remember.write(rememberMessage)
            remember.close()

        elif "what do you remember" in query:
            remember = open("Remember.txt", "r")
            speak("You told me to" + remember.read())

        elif 'whatsapp' in query:
            speak("which service would you like to use")
            ser = takeCommand().lower()
            if 'message' in ser:
                from asseceries import whatsappmessage

                speak('To whom would you like to call')
                name = takeCommand().lower()
                speak('What would you like to say')
                message = takeCommand().lower()
                whatsappmessage(name, message)

            elif 'video call' in ser:
                from asseceries import videocall

                speak('To whom would you like to call')
                name = takeCommand().lower()
                videocall(name)

            elif 'voice call' in ser:
                from asseceries import voicecall

                speak('To whom would you like to message')
                name = takeCommand().lower()
                voicecall(name)

            elif 'so chat' in ser:
                from asseceries import showchat

                speak('To whom would you like to message')
                name = takeCommand().lower()
                showchat(name)

        elif 'translate' in query:
            from asseceries import translate_and_speak

            speak("say the text to translate: ")
            text = takeCommand().lower()

            # Prompt the user for the target language
            speak("Enter the target language (e.g., 'fr' for French): ")
            target_lang = input("Enter the target language (e.g., 'fr' for French): ")

