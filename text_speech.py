from  tkinter import * 
import pyttsx3

window = Tk()
window.title("Text to Speech")
window.geometry("220x230")

#initalise the libary pyttsx3
engine = pyttsx3.init()

def speak_text():
    text = textbox.get("1.0", END) #1.0 = first line character 0 
    engine.say(text)
    engine.runAndWait() # waits befour untill in finshed whole text 

label = Label(window, text = "Text to Speech", font = ("times", 30))
textbox = Text(window, width = 30, height = 10)
button = Button(window, text = "Submit", command = speak_text, font = ("times", 20))

label.grid(row = 1, column = 1)
textbox.grid(row = 2, column = 1)
button.grid(row = 3, column = 1)

window.mainloop()