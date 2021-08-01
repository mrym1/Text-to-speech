import pyttsx3  #To install write pip install pyttsx3
friend = pyttsx3.init()
# friend.say("HI how are you?")
speech = input ("Say Something:")
friend.say(speech)
friend.runAndWait()

