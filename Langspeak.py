
import random

from google_speech import Speech
from googletrans import Translator
translator = Translator()

srclang='en'
destlang='te'
text1=''
i=0

a=['Maggie 40 rupees','Brinjal 35 rupees','Gold 6000 rupees','You are a good person']
while(1):
    i=i+1
    y=random.choice(a)
    print(y)
    translated = translator.translate(y, src=srclang, dest=destlang)
    print(translated.text)
    speech = Speech(translated.text,srclang)
    speech.play()
