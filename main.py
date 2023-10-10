from tkinter import *
from tkinter.ttk import *
from decimal import Decimal, getcontext

getcontext().prec = 20  # устанавливаем точность вычислений

def format_decimal(number, decimal_places):
    return f'{number:.{decimal_places}f}'

def on_click(): 
    try:
        if combo.get() == "Сложение":  
            num1 = Decimal(entry_num1.get().replace(',', '.'))
            num2 = Decimal(entry_num2.get().replace(',', '.'))
            result = num1 + num2

            if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
            else:
                label_result['text'] = f'Результат: {format_decimal(result, 15)}'
        else:
            num1 = Decimal(entry_num1.get().replace(',', '.'))
            num2 = Decimal(entry_num2.get().replace(',', '.'))
            result = num1 - num2

            if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
            else:
                label_result['text'] = f'Результат: {format_decimal(result, 15)}'
    except ValueError:
        label_result['text'] = 'Ошибка ввода'



root = Tk()

root.geometry("600x500")

root.configure(bg='pink')
root.title('Калькулятор')

Font_tuple = ("Comic Sans MS", 13, "bold")
label_info = Label(root, text='Калькулятор: Баранов Никита Сергеевич, 4 курс, 4 группа, 2023 год')
label_info.place(x=50, y=20)
label_info.configure(font=Font_tuple)

entry_num1 = Entry(root)
entry_num1.place(x=70, y=100)

entry_num2 = Entry(root)
entry_num2.place(x=300, y=100)

selected = BooleanVar()


combo = Combobox(root)
combo.place(x=200, y=200)

combo['values'] = ("Сложение", "Разность")
combo.current(0) 

button_sum = Button(root, text='Получить результат', command=on_click)
button_sum.place(x=220, y=300)

label_result = Label(root, text='Результат:')
label_result.place(x=50, y=400)
label_result.config(width=50)

root.mainloop()
