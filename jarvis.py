import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import time
import sys
import pyjokes
from playsound import playsound
import smtplib
import pywhatkit
import requests
#from PyDictionary import PyDictionary
from pynotifier import Notification
import psutil
import requests 
from requests import get
import wolframalpha
import pyautogui
import socket
from pywikihow import search_wikihow
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',  150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning aaryan sir, i am jarvis")

    elif hour>=12 and hour<14:
        speak("Good Afternoon aaryan sir, i am jarvis")   

    else:
        speak("Good Evening aaryan sir, i am Jarvis")  
 
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")  
        return "none"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
            # if 1:
            query = takeCommand().lower()
            
            # Logic for executing tasks based on query
            if 'search for' in query:
                speak('just a second sir ...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("Here are the details sir")
                speak(results)

            elif 'open youtube' in query:
                speak("sir, you want to go to home page or you want to play something")
                answerythp = takeCommand().lower()
                if 'home page' in answerythp:
                    webbrowser.open("youtube.com")
                elif 'play' in answerythp: 
                    speak("what do you want to see sir")  
                    wtplay = takeCommand().lower()
                    pywhatkit.playonyt(wtplay)
                else:
                    speak("ok sir")
                
            
            elif 'play' in query:
                query = query.replace("play" , "")
                pywhatkit.playonyt(query)
            elif 'call jerry' in query:
                engine.setProperty('voice', voices[1].id)
                speak("I am here aaryan Sir")
            elif 'call jarvis' in query:
                engine.setProperty('voice', voices[0].id)
                speak("I am back aaryan Sir")

            elif 'open google' in query:
                speak("what do you want to search sir?")
                searchterm = takeCommand().lower()
                webbrowser.open("http://google.com/search?q="+searchterm)

            elif 'open my channel' in query:
                webbrowser.open("youtube.com/aryanszone") 

            elif 'weather in' in query:
                
                words = query.split()
                complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+words[-1]+"&appid=bbf29b9a64c9e77a11f03f9c71dac51f"
                api_link = requests.get(complete_api_link)
                api_data = api_link.json()

                # variables to store and display data
                temp_city = ((api_data['main']['temp']) - 273.15)
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                
                
                speak("its "+ weather_desc +" in "+ words[-1] +" and the current temprature is {:.2f} degree Celsius ".format(temp_city))
            
            elif 'open chess' in query:
                webbrowser.open("chess.com/live")   
        
            elif 'search google for' in query:
                query = query.replace("search" ," ")
                query = query.replace("google" ," ")
                query = query.replace("for" ," ")
                webbrowser.open("http://google.com/search?q="+query)  
    
            elif 'meaning of' in query:
                query =query.split()
                dictionary=PyDictionary()
                meaning = (dictionary.meaning(query[-1])) 
                if meaning == None:
                    speak("sorry sir, i dont know but i will learn it soon") 
                else :
                    
                    speak(str(query[-1])+" is")  
                    speak(meaning)
                    print(meaning)  

            elif 'antonym of' in query:
                query =query.split()
                dictionary=PyDictionary()
                antonym = (dictionary.antonym(query[-1])) 
                if antonym == None:
                    speak("sorry sir, i dont know but i will learn it soon") 
                else :
                    
                    speak("antonym of "+str(query[-1])+" is")  
                    speak(antonym)
                    print(antonym)
                    
            elif 'synonym of' in query:
                query =query.split()
                dictionary=PyDictionary()
                synonym = (dictionary.synonym(query[-1])) 
                if synonym == None:
                    speak("sorry sir, i dont know but i will learn it soon") 
                else :
                    
                    speak("synonym of "+str(query[-1])+" is")  
                    speak(synonym)
                    print(synonym)     
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, abhi {strTime} ho raha hai ")

            elif 'current location' in query or 'my location' in query :
                res = requests.get('https://ipinfo.io/')
                data = res.json()

                city = data['city']

                location = data['loc'].split(',')
                latitude = location[0]
                longitude = location[1]

                speak(city)
                
            
            elif 'battery percentage'in query:
                battery = psutil.sensors_battery()
                percent = battery.percent
                print("sir, the device is "+str(percent)+ " percent charged")
                speak("sir, the device is "+str(percent)+ " percent charged")

            elif 'my ip' in query:
                ipadd = socket.gethostbyname(socket.getfqdn())
                speak("sir, your ip address is "+ipadd)   
                print("sir, your ip address is "+ipadd)  
            
 
            elif 'tell me a joke' in query:
                joke = pyjokes.get_joke()
                speak(joke) 

            elif 'open github' in query:
               webbrowser.open("https://www.github.com")
               speak("opening github")  
            elif 'open facebook' in query:
               webbrowser.open("https://www.facebook.com")
               speak("opening facebook")      
            elif 'open instagram' in query:
               webbrowser.open("https://www.instagram.com")
               speak("opening instagram")    

            elif 'switch window' in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
               
                pyautogui.keyUp("alt")

            elif 'start' in query:
                import pyautogui
                query = query.replace("start" ," ")
                pyautogui.hotkey("ctrl",'esc')
                pyautogui.typewrite(query, interval=0.25)
                pyautogui.press("enter")
            elif 'minimise window' in query:
               pyautogui.keyDown("alt")
               pyautogui.keyDown("space")
               pyautogui.press("n")
               pyautogui.keyUp("space") 
               pyautogui.keyUp("alt")
                                                                            
            elif 'close window' in query:
                pyautogui.hotkey('alt', 'f4')
            
            elif 'go to sleep' in query or 'you can sleep now' in query :
                speak("ok sir, i am going to sleep but you can call me back anytime")
                sys.exit()

            elif "how to do mode" in query or "how to do mod" in query:
                
                speak("how to do mode activated sir, ask me anything")    
                how = takeCommand()
                max_result = 1
                how_to = search_wikihow(how, max_result)
                assert len(how_to) == 1
                how_to[0].print
                speak(how_to[0].summary)

            elif "take screenshot" in query or "take a screenshot" in query:
                speak("what should be the name of the photo sir?")
                inputname = takeCommand().lower()
                name = "\\"+inputname
                ss =pyautogui.screenshot()
                ss.save('C:\\Users\\ARYAN PANDEY\\Desktop\\jarvis\\photos'+name+".png",)
                speak("sir, sceenshot taken and saved with the name "+inputname)
                time.sleep(1)
                speak("do you want to see the saved screenshot right now?")
                openss = takeCommand().lower()
                if "yes" in openss or "open" in openss :
                    webbrowser.open('C:\\Users\\ARYAN PANDEY\\Desktop\\jarvis\\photos'+name+".png",)
                else:
                    speak("as your wish sir")

              
            
        #extra
            elif 'open yahoo' in query:
                webbrowser.open("https://www.yahoo.com")
                speak("opening yahoo")
            
            
            elif 'open gmail' in query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail") 
                
            elif 'open snapdeal' in query:
                webbrowser.open("https://www.snapdeal.com") 
                speak("opening snapdeal")  
                
            elif 'open amazon' in query or 'shop online' in query:
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            elif 'open flipkart' in query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")   
            elif 'open ebay' in query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")       
        #advance mode
            elif "advance mode" in query or "advanced mode" in query:
                speak("password required to switch to advance mode, please sir, enter password manually")
                passw = "aryanhth"
                inputpass = pyautogui.password('Enter password to access advance mode')
                if inputpass == passw:
                    speak("welcome to advance mode sir, this mode can be slow but it is very useful, i will wait for your command")
                    client  = wolframalpha.Client('Q4VLHJ-YWL4LLR8EE')
                    while True :
                        advquery = takeCommand()
                        if advquery == "exit advance mode":
                           break 
                        else:
                            res = client.query(advquery)
                            output = next (res.results).text
                            print(output)
                            speak(output)
                else :
                    speak("incorrect password sir, if you forgot the password then you can refer to your source code")
                    print("incorrect password sir, if you forgot the password then you can refer to your source code")                 
                                    
    
                  