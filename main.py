from tkinter import *
from tkinter.ttk import *
from decimal import Decimal, getcontext
import re

getcontext().prec = 20  # устанавливаем точность вычислений

def check_number(number):
    # Паттерн для проверки формата чисел
    pattern = r'^[+-]?(\d{1,3}( ?\d{3})*|\d+)(\.\d+)?$'
    
    # Проверка соответствия числа паттерну
    if re.match(pattern, number):
        return True
    else:
        return False


def format_decimal(number, precision=6):
    # Преобразуем число в строку
    number_str = str(number)
    
    # Разделяем целую и десятичную части числа
    parts = number_str.split(".")
    
    # Форматируем целую часть числа
    integer_part = "{:,}".format(int(parts[0])).replace(",", " ")
    
    # Форматируем десятичную часть числа, если она есть
    decimal_part = ""
    if len(parts) > 1:
        decimal_part = parts[1][:precision]
    if number < 0 and integer_part[0] != "-":
        integer_part = "-" + integer_part
    
    if decimal_part == "":
        return integer_part
    # Выводим отформатированное число
    return f"{integer_part}.{decimal_part}"



def on_click(): 
    try:
        if not check_number(entry_num1.get()) or not check_number(entry_num2.get()):
            raise ValueError
        num1 = Decimal(entry_num1.get().replace(',', '.').replace(" ", ""))
        num2 = Decimal(entry_num2.get().replace(',', '.').replace(" ", ""))
        if combo.get() == "Сложение":  
            result = num1 + num2
        elif combo.get() == "Разность":
            result = num1 - num2
        elif combo.get() == "Умножение":
            result = num1 * num2
        elif combo.get() == "Деление":
            if num2 == 0:
                label_result['text'] = 'Ошибка: Деление на ноль'
                return None
            else:
                result = num1 / num2
                result = round(result, 6)
        if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
        else:
            label_result['text'] = f'Результат: {format_decimal(result, 6)}'
        
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

combo['values'] = ("Сложение", "Разность", "Умножение", "Деление")
combo.current(0) 

button_sum = Button(root, text='Получить результат', command=on_click)
button_sum.place(x=220, y=300)

label_result = Label(root, text='Результат:')
label_result.place(x=50, y=400)
label_result.config(width=50)

root.mainloop()
