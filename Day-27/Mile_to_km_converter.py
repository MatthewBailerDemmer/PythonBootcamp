from tkinter import *

def convert():
    number = float(input.get())
    number_converted = round(number * 1.60934)
    result_label_1.config(text=f"{number_converted}")

window = Tk()
window.minsize(width=300, height=100)
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

input = Entry()
input.insert(END, string="0")
input.config(width=20, )
input.grid(column=1, row=0)

input_label = Label(text="Miles")
input_label.grid(column=2,row=0)

result_label = Label(text="is equal to ")
result_label.grid(column=0,row=1)

result_label_1 = Label(text="0")
result_label_1.grid(column=1,row=1)

result_label_2 = Label(text="Km")
result_label_2.grid(column=2,row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()