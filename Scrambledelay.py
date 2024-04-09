import random
import time
start=time.time()
flag=0
#Array of words
a=['word','hello','high','how','zebra','cricket','football','volleyball','tennis','master','abandon','excercise','narrate','rivet' ]
def wordify(w): #Given an array of characters, it makes the word
    c=''
    for i in range(len(w)):
        c=c+w[i]
    return c
print('The scrambled words are given enter the correct word')
for i in range(5): #5 Words scrambled
    if flag==0:
        word=a[random.randint(0,len(a)-1)]
        b=random.sample(word,len(word)) #sample the word array randomly
        f=wordify(b) #It makes the word
        print(f)
        c=input()
        if c==word: #Checking for input word
            print('Correct')
        else:
            print('Wrong the correct answer is ', word)
            flag=1
        time.sleep(2+random.random()*2)
if flag==0:
    stop=time.time()
    timeelapsed=stop-start #finding elapsed time
    print('Your time is ',timeelapsed)
