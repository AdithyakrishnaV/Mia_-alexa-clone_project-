import speech_recognition  as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

''' Creator: Adithyakrishna V'''

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
voices = engine.setProperty("voice" , voices[1].id)

def talk(text):
    engine.say("my love")
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "mia" in command:
              command = command.replace("mia", "")
              print(command)

    except:
        pass
    return command

def run_mia():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "what is" in command:
        search = command.replace("what is", "")
        lookfor = wikipedia.summary(search, 1)
        print(lookfor)
        talk(lookfor)
    elif "date" in command:
        talk("sorry no i am in a relation")
    elif "date with adi" in command:
        talk("ofcourse I love to ")
    elif "are you single" in command:
        talk("I'm committed to you")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "are you happy" in command:
        talk(" I am happy when i spend time with you")
    elif "do you love me" in command:
        talk("i don't know why I just love you more than anything")
    elif "i love you" in command:
        talk("I love you too")
    elif "siri" in command:
        talk("Go ask that bitch siri")
    elif "alexa" in command:
        talk("Go ask that bitch alexa")


    else:
        talk("sorry  could you repeat the command")
        print("sorry  could you repeat the command")

while True:
  run_mia()