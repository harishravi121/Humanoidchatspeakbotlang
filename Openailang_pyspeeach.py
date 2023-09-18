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
    with sr.Microphone() as source: 
        print("Please Say something:")
        audio = r.listen(source)

    try:
        text1=r.recognize_google(audio)
        print("You said: " +text1 )
    except Exception as e:
        print(e)
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text1,
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

