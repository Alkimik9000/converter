from tkinter import *
window = Tk()
window.title("Money Converter")
window.minsize(500,300)

dollar_input = Entry()
dollar_input.pack()

dollar_label = Label(text="Enter Dollar amount $")
dollar_label.pack()

is_equal_label = Label(text="is equal to ")
is_equal_label.pack()

money_resule_label = Label(text="0")
money_resule_label.pack()

nis_label = Label(text="NIS")
nis_label.pack()
window.mainloop()