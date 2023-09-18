


import os
import openai

openai.api_key ="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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hi what is the laptop",
  temperature=0.5,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

y=response['choices'][0]['text']
print(y)
