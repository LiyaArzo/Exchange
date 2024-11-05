from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json




#result = requests.get('https://open.er-api.com/v6/latest/USD')
#data = json.loads(result.text)



def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name = cur[code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {c_name} за 1 доллар')

            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Внимание','Введите код валюты')


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)

cur = {
    'RUB':'Российский рубль',
    'EUR':'Евро',
    'GBP':'Британский фунт стерлингов',
    'JPY':'Японская йена',
    'CNY':'Китайский юань',
    'KZT':'Казахский тенге',
    'UZS':'Узбекский сум',
    'CHF':'Швейцарский франк',
    'AED':'Дирхам ОАЭ',
    'CAD':'Канадский доллар'
}

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Введите код валюты').pack(padx=10,pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10,pady=10)
combobox.set('RUB')
combobox.bind('<<ComboboxSelected>>',update_c_label)

c_label = ttk.Label(text='Российский рубль')
c_label.pack(padx=10,pady=10)

Button(text='Получить курсы обмена к доллару', command=exchange).pack(padx=10,pady=10)

window.mainloop()
