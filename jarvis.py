import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak( audio ): 
    engine.say(audio)
    engine.runAndWait()
    pass
if __name__=="__main__" :

    speak("Hey Sumiran , how are you doing")

  
def wishMe ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak ("Good Morning")
    elif hour >=12 and hour< 14:
        speak("goodevening")
    else:
         speak("goodnight")


speak('by the way i am EL , how may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)
    try :
         print('Recognazing...')
         query = r.recognize_google(audio,language = "en-in")
         print(f"user said:{query}\n")

    except Exception as e :
            print(e)    
            print("say that aagain please")
            return"None"
    return query
     
if __name__ == "__main__":
    wishMe()
    while True :
        query = takeCommand().lower()
        if  "wikipedia" in query:
                speak('searching wikipedia')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak ("according to wikipedia..")
                print(results)
                speak(results)

        elif "friends" in query:
                speak ("haha to say You may have many friends But there is one gang of you in city of taaj whom you love the most, they are The Gardenerette , also  NEWLY DOODLER tintintinnie . and the hottest lady of our gang ishita. , the most silent ,but the goddess of humor nikkahh...and yum yum yum possible to predict suruuu....and  how is jija  , by the way ,   ..motu ..yes the golu molu ..shruti didi of the whole gang ") 

        elif "class" in query: 
                speak ('tell me  your code baby ')
                try :
                    link = takeCommand()
                    speak('okay cool')
                    open = webbrowser.open( "https://meet.google.com//link")
                except :
                    speak('khud se kr yaar kuch toh')
        elif "assignment" in query :
                 speak("holyshit! tell me what else have you got")
                 work = takeCommand()
                 my_list = [ ]

                 my_list.append(work)
                 speak('noted sweetheart now you have ')
                 speak(my_list)
                        


exit()




