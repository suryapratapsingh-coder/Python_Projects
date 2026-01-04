import datetime
import time

name = input("tell me your name!")
presenthour=datetime.datetime.now().hour

if 5<=presenthour <=11:
    print("good morning,",name)

elif 11<= presenthour <=17:
    print("good afternoon,",name)

elif 17<= presenthour <=20:
    print("good evening,",name)

else:
    print("good night,",name)            




print("Welcome to Your ChatBot")
print("You can ask me basic question , Type 'bye' to exit from the bot")

#chatbot memory creation

responses ={
    "hello":"Hi, welcome. how can i help you?",
    "how are you": "i am very fine. thank you ",
    "motive me": "keep going . every bug of your project makes you a better developer",
    "who are you":"i am your personal chat bot",
    "function kya hote hai":"function is block of code"

}

#method

def getResponseBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "i am not able to tell that yet. "
while True:
    userInput=input("please ask your questions:")
    reply=getResponseBot(userInput) 
    print("Bot Response:",reply)

    if "bye" in userInput.lower():
        break
