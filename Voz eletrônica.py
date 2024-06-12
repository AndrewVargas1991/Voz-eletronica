# pip install pyttsx3
import pyttsx3

engine = pyttsx3.init()
engine.say(input('Digite o que você desejar: '))
engine.runAndWait()