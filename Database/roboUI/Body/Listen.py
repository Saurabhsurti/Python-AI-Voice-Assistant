# Hindi or English - Command
# English

import speech_recognition as sr
from googletrans import Translator

# 1 - Listen: Hindi or English

def Listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source, 0, 5)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="hi")

    except:
        return ""
    
    query=str(query).lower()
    return query

# print(Listen())

# 2 - Translation
def TranslationHinToEng(Text):
    line=str(Text)
    translate = Translator()
    result = translate.translate(line)
    data=result.text
    print(f"You : {data}.")
    return data

# TranslationHinToEng()


# 3 - connect
def MicExecution():
    query=Listen()
    data = TranslationHinToEng(query)
    return data