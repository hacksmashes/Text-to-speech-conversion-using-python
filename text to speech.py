import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)      # [1] represents the female voice, if u need male voice type this [0]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("hey buddy,have a nice day")    # Type here what do u want to hear at the output window
