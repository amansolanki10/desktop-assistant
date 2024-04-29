import datetime
import os
import subprocess
from time import sleep
import geocoder
import keyboard
import pyautogui
import pyttsx3
import speech_recognition as sr
from pynput.keyboard import Key, Controller
from requests import get

keyboard = Controller()
assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)


def speak(audio):
    assistant.say(audio)
    print(audio)
    assistant.runAndWait()
 #calender
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


import requests

def main():
    api_key = "fda44ce224935fb24621d1d6bc350215"
    # city = input("Enter the city name: ")
    city = 'Valsad'


if __name__ == "__main__":
    main()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Hi Sir , I am Friday , Welcome to the the world of AI and Machine Learning")


def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def whether():
    g = geocoder.ip('me')
    location = g.city
    print(location)
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=a9d4f9b0a5a2a9e3e7d8d8d9d3a3d9d'
    response = get(url)
    data = response.json()
    temp = data['main']['temp']
    temp = int(temp - 273.15)
    print(temp)
    speak('The current temperature in ' + location + ' is ' + str(temp) + ' degree celcius')


chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


def chromeautomation():
    speak('Chrome Automation Started')
    command = takeCommand()
    if 'close this tab' in command:
        pyautogui.hotkey('ctrl', 'w')
        speak('tab closed')
    elif 'open new tab' in command:
        pyautogui.hotkey('ctrl', 't')
        speak('new tab opened')
    elif 'go back' in command:
        pyautogui.hotkey('ctrl', 'left')
        speak('go back')
    elif 'go forward' in command:
        pyautogui.hotkey('ctrl', 'right')
        speak('go forward')
    elif 'refresh' in command:
        pyautogui.hotkey('ctrl', 'r')
        speak('page refreshed')
    elif 'maximize' in command:
        pyautogui.hotkey('ctrl', 'up')
        speak('maximized')
    elif 'minimize' in command:
        pyautogui.hotkey('ctrl', 'down')
        speak('minimized')
    elif 'history' in command:
        pyautogui.hotkey('ctrl', 'h')
        speak('history')
    elif 'home' in command:
        pyautogui.hotkey('ctrl', 'home')
        speak('home')
    elif 'downloads' in command:
        pyautogui.hotkey('ctrl', 'd')
        speak('downloads')


def enable_wifi():
    subprocess.run('netsh interface set interface "Wi-Fi" admin=enable', shell=True)
    speak('Wifi Enabled')


def disable_wifi():
    subprocess.run('netsh interface set interface "Wi-Fi" admin=disable', shell=True)
    speak('Wifi Disabled')





def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            public_ip = data['ip']
            return public_ip
        else:
            print(f"Error: Unable to fetch IP. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None


def close_application(application_name):
    """Close the specified application if it is running."""
    process_id = os.popen("tasklist | findstr /i \"" + application_name + "\"").read().split(" ")[0]

    # Close the application.
    os.system("taskkill /F /PID " + process_id)


def turn_bluetooth_on():
    # Press Windows key to open the Start menu
    pyautogui.press('win')
    datetime.time.sleep(1)  # Wait for the Start menu to open

    # Type 'Bluetooth' to search for Bluetooth settings
    pyautogui.typewrite('Bluetooth')
    datetime.time.sleep(1)  # Wait for the search results

    # Press Enter to open Bluetooth settings
    pyautogui.press('enter')
    datetime.time.sleep(2)  # Wait for Bluetooth settings to open

    pyautogui.press('tab')
    datetime.time.sleep(1)

    # Press Spacebar to toggle Bluetooth on
    pyautogui.press('space')

    # Check if Bluetooth is already on
    if pyautogui.locateOnScreen('Capture.png'):
        print("Bluetooth is already on.")
    else:
        # Press Tab to select the 'Bluetooth & other devices' tab
        pyautogui.press('tab')
        datetime.time.sleep(1)

        # Press Spacebar to toggle Bluetooth on
        pyautogui.press('space')
        print("Bluetooth turned on.")


def turn_bluetooth_off():
    # Press Windows key to open the Start menu
    pyautogui.press('win')
    datetime.time.sleep(1)  # Wait for the Start menu to open

    # Type 'Bluetooth' to search for Bluetooth settings
    pyautogui.typewrite('Bluetooth')
    datetime.time.sleep(1)  # Wait for the search results

    # Press Enter to open Bluetooth settings
    pyautogui.press('enter')
    datetime.time.sleep(2)  # Wait for Bluetooth settings to open

    pyautogui.press('tab')
    datetime.time.sleep(1)

    pyautogui.press('space')

    # Check if Bluetooth is already on
    if pyautogui.locateOnScreen('Capture.png'):
        print("Bluetooth is already off.")
    else:
        # Press Tab to select the 'Bluetooth & other devices' tab
        pyautogui.press('tab')
        datetime.time.sleep(1)

        # Press Spacebar to toggle Bluetooth on
        pyautogui.press('space')
        print("Bluetooth turned on.")
