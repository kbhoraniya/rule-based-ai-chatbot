# RULE BASED AI PYTHON CHATBOT

import datetime
import time

name=input ("please,enter your name:")
presenthour=datetime.datetime.now().hour

if 5 <= presenthour <= 11:
    print ("good morning",name)
elif 11 <= presenthour <= 17:
    print ("good afternoon",name)
elif 17 <= presenthour <=20:
    print ("good evening",name)
else:
    print ("good night",name)


print ("hello! welcome to rule based chatbot")
print ("you can ask me basic question,type 'bye' to exit from the bot")

# chatbot memory creation [ dictionary of responses]

responses = {
    "hello":"hi,welcome.how can i help you ?",
    "how are you":"i am very fine🤗 thank you",
    "who are you":"i am smart AI chatbot💻",
    "motivate me":"keep going.every bug of your project makes you a better devloper ✨",
    "happy":"great to hear that",
    "sad":"don't worry,things will get better😊 ",
    "what is the functions":"read chapeter 7",
    "what is python":"python is programming language",
    "how many data type in python":"4 data type in python",
    "what is keyword in python":"keyword are reserved word that cannot be used as variable names",
}

# method/function to get response of chatbot

def getresponsebot(userquestion):
    userquestion=userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion:
            return responses[eachkey]
        
    return "i am not able to tell that yet. i am still in learning mode."

# take user input

while True:

    userinput= input("please ask your question:")
    reply= getresponsebot(userinput)
    
    if userinput.lower() == "bye":
        print ("bot: goodbye! have a nice day")
        break

    time.sleep (1)
    print("bot response:",reply)
     