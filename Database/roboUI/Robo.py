from Brain.AiBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
print(">> Starting The Robo : Wait For Some Seconds.")
from Body.Speak import Speak
print(">> Starting The Robo : Wait For Few Seconds More.")
# from Main import Listen

def MainExecution():
    Speak("Hello Sir")
    Speak("I am AI Robo. I'm Ready to Assist You sir.")

    while True:
        Data = MicExecution()
        Data = str(Data)

        if len(Data)<=3:
            pass
        elif "turn on the tv" in Data:
            Speak("ok..Turning On the Android Tv..")
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionAnswer(Data)
            Speak(Reply)
        elif "india and pakistan" in Data.lower().strip():
            Speak("India is Father of pakistan")
        elif "question" in Data.lower().strip():
            Speak("Ok Sir you can write question")
            ques=input("Enter your question: ")
            Reply = QuestionAnswer(Data)
            Speak(Reply)
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

# MainExecution()