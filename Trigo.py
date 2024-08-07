import code
import datetime
import os
import smtplib
import sys
import webbrowser
from http import server
from re import search
from unittest import result
from urllib import request

# import psutils
# import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():

    


    

    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour<12:
        speak("Good morning Sir!")
          

    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
       

    else:
         speak("Good Evening Sir!") 

   
    """speak("recognizing systems....")
    speak("system recognization successfull")"""
          

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir The time is {strTime}")

   

    battery=psutil.sensors_battery()
    percentage = battery.percent
    speak(f"battery level is {percentage} percent.") 

    if percentage <=20:
        speak("battery saver is on, sir, i think you should plugin your device")


    
    search = "temprature in bhavnagar"
    url= f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    weather = data.find("div",class_="BNeawe" ).text
    speak(f"current{search} is {weather}, and it's a beutifull day outside!") 

     



    speak("sir Trigo is online and rady, please tell me how may i help you.") 



    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognition...")
   
        
        query = r.recognize_google(audio, language= 'en-in')
        print("User said:",  query)

    except Exception as e:
       # print(e)
      

        print("Sorry sir please Say that again.....")
        
    
        return "None"
    return query 

def senEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com.587')
    server.ehlo()
    server.starttls()
    server.login('utsavsutariya0102@gmail.com','utsav1204')
    server.sendmail('utsavsutariya0102@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishMe() 
    while True:
    
     query = takeCommand().lower()
    # Logic for executing task based on query
     if 'wikipedia'  in query:
        speak("searching wikipedia....")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia.....")
        print(result)
        speak(result)

     elif 'youtube' in query:
         webbrowser.open("youtube.com")
         speak("sir, youtube is open")
          

     elif 'google' in query:
         webbrowser.open("google.com")
         speak("sir,google is open")  

     elif 'stackoverflow' in query:
         webbrowser.open("stackoverflow.com")  
         speak("sir,stackoverflow is open")

     elif 'email to dev' in query:
          try:
              speak("Ok Sir, What should i say?")
              content = takeCommand()
              to = "savaliyadev15@gmail.com"
              senEmail(to,content)
              speak("Email has been sent sir...!")   
         
          except Exception as e:
            print(e)
            speak("Sorry Sir, I am not able to sent this mail right now, Please try again")   



     elif 'song' in query:
            speak("ok sir")
            music_dir = "C:\\Users\\Utsav\\Music\\New folder"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 
            

     elif 'music' in query:
            speak("ok sir")
            music_dir = "C:\\Users\\Utsav\\Music\\New folder"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 


               
                

     elif 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir The time is {strTime}")

     elif 'code' in query:
         codePath = "C:\\Users\\Utsav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath) 
         speak("sir,visual code is open")

     elif 'intro' in query:
         print("Hello. my self  Trigo, I am a virtual Assistant of Utsav Sutariya, I done your all virtual work like open website, open application, send massages and etc., my current version is 1.2.4, thank you")  
         speak("Hello, my self  Trigo, I am a vertual Assistant of Utsav Sutariya, I done your all vertual work like open website, open application, send massages and etc., my current version is 1.2.4, thank you") 

     elif 'tell about you' in query:
         print("Hello. my self  Trigo, I am a virtual Assistant of Utsav Sutariya, I done your all virtual work like open website, open application, send massages and etc., my current version is 1.2.4, thank you")  
         speak("Hello. my self  Trigo, I am a vertual Assistant of Utsav Sutariya, I done your all vertual work like open website, open application, send massages and etc., my current version is 1.2.4, thank you")  

     elif 'Trigo' in query:
         speak("Hello sir, You Need My Help?")

     elif 'cherissa' in query:
         speak("Hello sir, You Need My Help?") 

     elif 'sirisha' in query:
         speak("Hello sir, You Need My Help?")    

     elif 'terisa' in query:
         speak("Hello sir, You Need My Help?")   

     elif 'cherisha' in query:
         speak("Hello sir, You Need My Help?")        

     elif 'yes' in query:
         speak("please tell me,how may help you, sir")   

     elif  'thank you'in query:
         speak("No problem Sir")


     elif 'email to dev' in query:
          try:
              speak("Ok Sir, What should i say?")
              content = takeCommand()
              to = "savaliyadev15@gmail.com"
              senEmail(to,content)
              speak("Email has been sent sir...!")   
         
          except Exception as e:
              print(e)
              speak("Sorry Sir, I am not able to sent this mail right now, Please try again")    

     

     elif 'shutdown' in query:
            speak("Sir,system is shoutdown in less than 1 minute")
            os.system('shutdown -s') 

     elif "chrome" in query:
         codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
         os.startfile(codePath)
         speak("sir, chrome is open")

     elif "auto whatsapp" in query:
         codePath = "C:\\Auto Whatsapp\\auto whatsapp.py"
         os.startfile(codePath)
         speak("sir auto whatsapp is open in visual code")

    
        
     elif 'whatsapp' in query:
         webbrowser.open("whatsapp.com")
         speak("sir, whatsapp  is open")   

     elif 'powershell' in query:
         codePath = "C:\\Users\\Utsav\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell.lnk"
         os.startfile(codePath)
         speak("sir, powershell has open") 

     elif 'link' in query:
         codePath = "C:\\Users\\Utsav\\OneDrive\\Documents\\link of text book\\https---drive.google.com-folderview-id=1-IR-zQVKQ23acSA1kmz3HAJvzl2XjyaD.url"
         os.startfile(codePath)
         speak('sir, text book link is open')

     elif 'textbook' in query:
         codePath = "C:\\Users\\Utsav\\OneDrive\\Documents\\Text Book"
         os.startfile(codePath)
         speak("sir, text book folder is open" )


     elif 'testbook' in query:
         codePath = "C:\\Users\\Utsav\\OneDrive\\Documents\\Text Book"
         os.startfile(codePath)
         speak("sir, text book folder is open" ) 

     elif 'read' in query:
         codePath = "C:\\Users\\Utsav\\OneDrive\\Documents\\Text Book"
         os.startfile(codePath)
         speak("sir, text book folder is open" )     

     elif 'reading' in query:
         codePath = "C:\\Users\\Utsav\\OneDrive\\Documents\\Text Book"
         os.startfile(codePath)
         speak("sir, text book folder is open" )        

     elif 'instagram' in query:
         webbrowser.open("instagram.com")
         speak("sir,your instagram is open")

     elif 'flipkart' in query:
         webbrowser.open("flipkart.com")
         speak("sir, flipkart is open")

     elif 'amazon' in query:
         webbrowser.open("amazon.com")
         speak("sir, amazon is open")

     elif 'spotify' in query:
         webbrowser.open("spotify.com")
         speak("sir,spotify is open")  


     elif 'team' in query:
         codePath = "C:\\Users\\Utsav\\OneDrive\\Desktop\\Microsoft Teams.lnk"
         os.startfile(codePath)
         speak("Sir, team is open")
         

     elif 'bye' in query:
          os.system('shutdown -s')
          speak("bye,sir")
    
            



              
       

     elif 'rest' in query:
         speak("ok,sir")
         sys.exit()
         

     elif 'facebook' in query:
         webbrowser.open("facebook.com")
         speak("sir, facebbok is open")

    

     elif 'good girl' in query:
         speak("thank you,sir")

     elif 'so jao' in query:
         speak("ok sir, good night!")

     elif 'temperature' in query:
         search = query
         url= f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         weather = data.find("div",class_="BNeawe" ).text
         speak(f"current{search} is {weather}")

           

     elif 'battery' in query:
         battery=psutil.sensors_battery()
         percentage = battery.percent
         speak(f"sir, battery level is {percentage} percent ")

     elif 'clap' in query:
         speak("yes, sir")   

     
     elif "advice" in query:
         res = requests.get("https://api.adviceslip.com/advice").json()
         print(res)
         speak(res['slip']['advice'])    

     elif "advise" in query:
         res = requests.get("https://api.adviceslip.com/advice").json()
         speak(res['slip']['advice'])   

     elif 'who'  in query:
        speak("Findig data....")
        query=query.replace("who","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result)   

     elif 'where'  in query:
        speak("Findig  data....")
        query=query.replace("where","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result)  

     elif 'what'  in query:
        speak("Findig data....")
        query=query.replace("what","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result)   

     elif 'why'  in query:
        speak("Finding data....")
        query=query.replace("why","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result)   

     elif 'which'  in query:
        speak("Findig data....")
        query=query.replace("which","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result)   

     elif 'when'  in query:
        speak("Findig  data....")
        query=query.replace("when","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result) 


     

     elif 'exit' in query:
        speak("Ok Sir, As You Wish!")
        sys.exit() 

     elif 'restart' in query:
        speak("ok sir, i will restart!")
        os.system("shutdown /r /t 0")    

     elif 'rest' in query:
        speak("ok sir")
        sys.exit()   


     elif 'give' in query:

        speak("Findig  data....")
        query=query.replace("give","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result) 


     elif 'find' in query:

        speak("Findig  data....")
        query=query.replace("find","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to my data, sir....")
        print(result )
        speak(result)   



     elif '.com' in query:

            query = query.replace("open", "")
            query = query.replace(".com", "")
            #query_01 = query_01.replace(" ", "")
            #query_01=query_01.lstrip()
            #print(query)
            # query=query.replace("query","query.lower()")
            # query.lower()
            webbrowser.open(f"{query}.com")
            speak(f"sir,{query} is open")

     


  
   
         
 
         
        

    
  


  


    
        
         
   

             


    



   

     

        