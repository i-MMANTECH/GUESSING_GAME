from tkinter import *
import random

attempts = 20

answer = random.randint(1, 200)

def check_answer():
    global attempts
    global text

    attempts -= 1

    guess = int(entry_window.get())

    if answer == guess:
        text.set("You win Congrats!!")
        btn_check.pack_forget()

    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have " + str(attempts) + "attempts left - Go Higher!!")
    elif guess > answer:
        text.set("Incorrect! You have " + str(attempts) + "attempts left - Go Lower!!")


        return


root = Tk()

root.title("Guess The Number")

root.geometry("500x150")

label = Label(root, text="I have a number between 1 and 200, Can you guess my number?")
label.pack()

entry_window = Entry(root, width=45, borderwidth=5)
entry_window.pack()

btn_check = Button(root, text="Enter", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Exit", command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 20 attempts remaining! Good luck!")

guess_attempts= Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()