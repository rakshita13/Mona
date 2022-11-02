import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyPDF2
import webbrowser
import os
from playsound import playsound
from googletrans import Translator

listener = sr.Recognizer()
engine = pyttsx3.init()
#speaking to me
voices = engine.getProperty('voices')
#to get all the types of voices
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mona' in command:
                command = command.replace('mona', '')
                print(command)
    except:
        pass
    return command


def run_mona():
    command = take_command()
    #taking command from the user
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        #replacing command play with a song
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'favourite movie' in command:
        talk('Maybe Tamasha')
    elif 'morning' in command:
        talk('Hello Don, A very good morning to you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'read' in command:
        book = open('script.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        for num in range(7, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            talk(text)
    elif 'open' in command:
        from AppOpener import run
        run("telegram")
    elif 'google' in command:
        webbrowser.open("https.//google.com")
    elif 'translate' in command:
        translator = Translator()
        from_lang = 'en'
        to_lang = 'hi'
        from gtts import gTTS
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.2)
            voice = listener.listen(source)
            get_sentence = listener.recognize_google(voice)
            try:
                print("Phase to be Translated :" + get_sentence)
                text_to_translate = translator.translate(get_sentence,
                                                         src=from_lang,
                                                         dest=to_lang)
                text = text_to_translate.text
                # Using Google-Text-to-Speech ie, gTTS() method
                speak = gTTS(text=text, lang=to_lang, slow=False)
                speak.save("captured_voice.mp3")
                playsound('captured_voice.mp3')
                os.remove('captured_voice.mp3')
                print(text)
            except:
                print("Unable to Understand the Input")

    else:
        talk('Please say the command again.')


while True:
    run_mona()