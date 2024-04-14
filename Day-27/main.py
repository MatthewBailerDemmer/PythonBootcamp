from tkinter import *
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
#add´s padding to all the widgets
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))


my_label["text"] = "New Text"
my_label.config(text="New Text")
#Adding padding to just one widget
my_label.config(padx=50, pady=50)

my_label.grid(column=0, row=0)

#Button

def button_clicked():
    #my_label["text"] = "I got clicked"
    my_label.config(text=str(input.get()))


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

window.mainloop()