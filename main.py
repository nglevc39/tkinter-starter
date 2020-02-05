

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text=0, font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

score = 0

def addToScore():
  global score
  score += 1
  lbl['text'] = score

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 0 , row = 1)

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 1 , row = 2)

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 2 , row = 3)



window.mainloop()     # Keep the window open