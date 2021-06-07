from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

root = Tk()
root.title("Currency Converter")
root.geometry("600x300")
root.config(bg="#1877f2")
frame = Frame(root)

response = requests.get("https://v6.exchangerate-api.com/v6/a24d5559a57a8ed22b9fd2a0/latest/USD")
data = response.json()

label1 = Label(root, text="Please enter the amount:")
label1.config(bg="#1877f2", font="200")
label1.place(x=50,y=50)
entry= Entry(root)
entry.config(borderwidth="5", bg="blue")
entry.place(x=270, y=50)
label2 = Label(root, text="Choice a currency:")
label2.config(bg="#1877f2", font="200")
label2.place(x=50, y=120)
currency = ttk.Combobox(root, values=list(data['conversion_rates'].values()))
currency.place(x=270, y=120)
label4 = Label(root, text="")

def convert():
    total_amount = 0
    if currency.get() != 'USD':
        total_amount = float(entry.get()) / float(currency.get())
    elif currency.get() == 'USD':
        total_amount = entry.get()
    amount.config(text=total_amount)


button = Button(root, text="Convert", command=convert)
button.config(bg="blue", borderwidth="5", fg="white")
button.place(x=100, y=180)
amount = Label(root, text="")
amount.config(bg="#1877f2", font="200")
amount.place(x=270, y=180)




root.mainloop()
