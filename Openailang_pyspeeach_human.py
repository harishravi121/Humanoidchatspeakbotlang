import os
import openai
import pyttsx3
import speech_recognition as sr
import random
r=sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',random.randint(150,260))
openai.api_key ="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"

from google_speech import Speech
from googletrans import Translator
translator = Translator()

srclang='en'
destlang='en'
text1=''
while(1):
    text1=''
    a=random.randint(0,3)
    if(a>=2):
        r=sr.Recognizer()
        with sr.Microphone() as source: 
            print("Please Say something:")
            audio = r.listen(source)

        try:
            text1=r.recognize_google(audio,language=srclang)
            print("You said: " +text1 )
        except Exception as e:
            print(e)
        translated = translator.translate(text1, src=srclang, dest=destlang)
        sent=translated.text
    if(a==0):
        sent='Tell something interesting'
        print('I will say something')
    if(a==1):
        jk=random.choice(['astronomy','physics','chemistry','biology','economics'])
        sent='Tell a great joke about '+jk
        print('I will tell a joke')
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=sent,
      temperature=0.5,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    y=response['choices'][0]['text']
    print(y)
    engine.setProperty('rate',random.randint(150,260))
    
    engine.say(y)
    engine.runAndWait()

