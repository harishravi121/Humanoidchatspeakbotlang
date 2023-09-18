import pyttsx3
import random
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

responses1=['Physics is great and fun','Ground state of Hydrogen is -13.6eV','BEC is Bose Einstein Condensate at nano kelvin','h=6e-34 Js and c=3e8 m/s']
responses2=['FInd the divergence of r^2cos(\\ theta) er','E=mc^2 and \gamma=1/\sqrt(v^2-c^2)','EMF of a line is Blv','Power radiated by a hot black body is AesigmaT^4']
responses3=['We have to go to conferences and publish in journals like nature, science and EJPD']
responses=responses1+responses2+responses3
while 1:
    a=input()
    z2=random.choice(responses)
    #print('Ketterle the physicist : ' ,random.choice(responses))

    engine.say(z2)
    engine.runAndWait()
