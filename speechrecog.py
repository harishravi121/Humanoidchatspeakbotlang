import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source: 
    print("Please Say something:")
    audio = r.listen(source)

try:
    text1=r.recognize_google(audio)
    print("You said: " +text1 )
except Exception as e:
    print(e)
