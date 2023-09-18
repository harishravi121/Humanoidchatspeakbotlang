import os
import openai

openai.api_key ="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"

from google_speech import Speech
from googletrans import Translator
translator = Translator()

srclang='en'
destlang='hi'
while(1):
    ask=input()
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=ask,
      temperature=0.5,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    y=response['choices'][0]['text']
    print(y)
    translated = translator.translate(y, src=srclang, dest=destlang)
    speech = Speech(translated.text, destlang)
    speech.play()

