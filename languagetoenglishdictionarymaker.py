source='முதலமைச்சர் மாநில இளைஞர் விருதுக்கான விண்ணப்பம் அறிவிக்கப்பட்டுள்ளது.. இந்த விருதினை பெறுவதற்கு எப்படி விண்ணப்பிக்க வேண்டும்'
sourcesplit=source.split()
N=len(sourcesplit)
meanings=[0]*N

sortedsource=[0]*N
sortedmeanings=[0]*N


start=[0]*N
from googletrans import Translator
translator = Translator()
srclang='ta'
destlang='en'

for i in range(N):
    
    translated = translator.translate(sourcesplit[i], src=srclang, dest=destlang)
    meanings[i]=translated.text
    start[i]=ord(sourcesplit[i][0])

print(start)
b=start
b.sort()

sortedsource=[0]*N
sortedmeanings=[0]*N


for i in range(N):
    for j in range(i,N):
        if(b[i]==start[j]):
            print(1)
            sortedsource[i]=sourcesplit[j]
            sortedmeanings[i]=meanings[j]
            
print(sortedsource,sortedmeanings)


            
