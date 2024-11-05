from tkinter import *
from tkinter import messagebox as mb
import requests
import json




#result = requests.get('https://open.er-api.com/v6/latest/USD')
#data = json.loads(result.text)



def exchange():
    pass


window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Введите код валюты').pack(padx=10,pady=10)

entry = Entry()
entry.pack(padx=10,pady=10)

Button(text='Получить курсы обмена к доллару', command=exchange).pack(padx=10,pady=10)

window.mainloop()
