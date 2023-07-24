from tkinter import *

def dollar_nis():
    dollar = float(dollar_input.get())
    nis = dollar * 3.66
    money_resule_label.config(text=nis)


window = Tk()
window.title("Money Converter")
window.minsize(500,300)

dollar_input = Entry(width=7)
dollar_input.grid(column=1, row=0)# api

dollar_label = Label(text="Enter Dollar amount $")
dollar_label.grid(column=0, row=0)

is_equal_label = Label(text="is equal to ")
is_equal_label.grid(column=0, row=2)

money_resule_label = Label(text="0")
money_resule_label.grid(column=1, row=2)

nis_label = Label(text="NIS")
nis_label.grid(column=2, row=2)

calculate_button = Button(text="calculate", command=dollar_nis)
calculate_button.grid(column=1 ,row=3)
window.mainloop()