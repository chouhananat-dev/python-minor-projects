import pyttsx3
# pyttsx3 is a text to speech translator module
import wikipedia
# import a 3rd party module as wikipedia
assistant=pyttsx3.init()
# initializing the module and creating an instance of it
speech=input("Enter what you want to search:\n")
result=wikipedia.summary(speech, sentences=2)
# summary method of wikipedia simply summarize the content 
print(result)
assistant.say(result)
assistant.runAndWait()
# runAndWait helps in block execution