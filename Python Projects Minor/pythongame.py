# creating a rock-paper-scissor game in python
import random
# importing random module
import pyttsx3
comp_string="123"
result=""
assistant=pyttsx3.init()
print("Welcome to the rock-paper_scissor game 🪨📄✂️")
assistant.say("Welcome to the rock-paper-scissor game. Enter your choice please")
assistant.runAndWait()
while True:
    # taking user choice:
    user_choice=input('''
        Enter Your Choice:
            1.Rock
            2.Paper
            3.Scissor
    ''')
    comp_choice=random.choice(comp_string)

    if(user_choice==comp_choice):
        result="Draw!"
    elif(user_choice=='1' and comp_choice=='2'):
        result="Oh, You Loss!"
    elif(user_choice=='2' and comp_choice=='3'):
        result="Oh, You Loss!"
    elif(user_choice=='3' and comp_choice=='1'):
        result="Oh, You Loss!"
    elif(user_choice=='1' and comp_choice=='3'):
        result="hey, You won!"
    elif(user_choice=='2' and comp_choice=='1'):
        result="hey, You won!"
    elif(user_choice=='3' and comp_choice=='2'):
        result="hey, You won!"
    else:
        result="I think you took wrong choice!"

    print(result)
    print(f"Computer choice: {comp_choice}")
    quit=input("Wanna continue? Press enter or type 'end' to exit..")
    if quit=="end":
        break
print("Game ended!")
assistant.stop()
