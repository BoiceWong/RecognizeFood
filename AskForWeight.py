from Tkinter import *

window = Tk()

# Labels & Entries
label = Label(window, text = "Food!!!", bg = "red", fg = "yellow")
label.pack(fill = X) #just pack the label in the window somewhere, adapts to window size in x direction
label2 = Label(window, text = "Food weight", bg = "orange", fg = "blue")
label2.pack() #adapts to window size in y direction
label3 = Label(window, text = "Food type", bg = "purple", fg = "green")
label3.pack()
label4 = Label(window, text = "Food good?", bg = "black", fg = "white")
label4.pack(fill = X)


# Frames
topFrame = Frame(window)
topFrame.pack(side = TOP) # by default the first goes on the top, can still do it
middleFrame = Frame(window)
middleFrame.pack(side = LEFT)
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM) # apparently no CENTER side

# Buttons
button1 = Button(topFrame, text = "Click me pls", bg = "red", fg = "white") # fg is optional
button2 = Button(middleFrame, text = "Click me too", bg = "blue", fg = "white")
button3 = Button(middleFrame, text = "Click me as well", bg = "green", fg = "white")
button4 = Button(bottomFrame, text = "Click me!", bg = "orange", fg = "white")
button1.pack(side = TOP)
button2.pack(side = LEFT)
button3.pack(side = RIGHT)
button4.pack(side = BOTTOM)

window.mainloop() #keep window continuously on the screen
