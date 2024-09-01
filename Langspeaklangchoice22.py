$Fun code by Harish for company written in Bangalore in 2024
import random

from google_speech import Speech
from googletrans import Translator
translator = Translator()

srclang='en'
destlang='zh-CN'
destlangs=['kn','ta','te','hi','zh-CN','de']
text1=''
i=0

a=['Maggie forty rupees','Brinjal thirty five rupees','Gold six thousand rupees','You are a good person']
while(1):
    i=i+1
    a=['Maggie '+str(random.randint(25,80))+' rupees','Brinjal '+str(random.randint(25,80))+' rupees','Gold '+str(random.randint(2995,8990))+' rupees','You are a good person']
    y=random.choice(a)
    destlang=random.choice(destlangs)
    print(y)
    translated = translator.translate(y, src=srclang, dest=destlang)
    print(translated.text)
    speech = Speech(translated.text,destlang)
    speech.play()

