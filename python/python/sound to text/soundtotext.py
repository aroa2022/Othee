import speech_recognition as sr

r= sr.Recognizer()
with sr.Microphone() as source:
    print('say any thing')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('you said',text)
    except:
        print('error')