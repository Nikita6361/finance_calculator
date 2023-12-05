from tkinter import *
from tkinter.ttk import *
from decimal import Decimal, getcontext

import decimal
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


def apply_opp(combo, numa, numb):
    if combo.get() == "Сложение":  
        result = numa + numb
    elif combo.get() == "Разность":
        result = numa - numb
    elif combo.get() == "Умножение":
        result = numa * numb
    elif combo.get() == "Деление":
        if numb == 0:
            label_result['text'] = 'Ошибка: Деление на ноль'
            return None
        else:
            result = numa / numb
            result = round(result, 6)
    return result


def on_click(): 
    try:
        if not check_number(entry_num1.get()) or not check_number(entry_num2.get()):
            raise ValueError
        num1 = Decimal(entry_num1.get().replace(',', '.').replace(" ", ""))
        num2 = Decimal(entry_num2.get().replace(',', '.').replace(" ", ""))
        num3 = Decimal(entry_num3.get().replace(',', '.').replace(" ", ""))
        num4 = Decimal(entry_num4.get().replace(',', '.').replace(" ", ""))
        result = apply_opp(combo2, num2, num3)
        if result is None:
            return
        if abs(result) > 1000000000000:
            label_result['text'] = 'Переполнение'
            return
        
        operations = ["Сложение", "Разность", "Умножение", "Деление"]
        if operations.index(combo1.get()) < operations.index(combo3.get()):
            result = apply_opp(combo3, result, num4)
            if result is None:
                return
            if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
                return
            result = apply_opp(combo1, num1, result)
            if result is None:
                return
            if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
                return
        else:
            result = apply_opp(combo1, num1, result)
            if result is None:
                return
            if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
                return
            result = apply_opp(combo3, result, num4)
            if result is None:
                return
            if abs(result) > 1000000000000:
                label_result['text'] = 'Переполнение'
                return
        label_result['text'] = f'Результат: {format_decimal(result, 6)}'
        if combor.get() == 'Бухгалтерское':
            rounded = result.quantize(
                decimal.Decimal('1'),
                rounding=decimal.ROUND_HALF_EVEN
            )
        elif combor.get() == 'Математическое':
            rounded = result.quantize(
                decimal.Decimal('1'),
                rounding=decimal.ROUND_HALF_UP
            )
        else:
            rounded = result.quantize(
                decimal.Decimal('1'),
                rounding=decimal.ROUND_DOWN
            )
        label_round['text'] = rounded
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
entry_num1.place(x=20, y=100, width=60)

label1 = Label(root, text='(')
label1.place(x=125, y=100)

entry_num2 = Entry(root)
entry_num2.place(x=170, y=100, width=60)

entry_num3 = Entry(root)
entry_num3.place(x=320, y=100, width=60)

label2 = Label(root, text=')')
label2.place(x=425, y=100)

entry_num4 = Entry(root)
entry_num4.place(x=470, y=100, width=60)


selected = BooleanVar()


combo1 = Combobox(root)
combo1.place(x=65, y=200, width=120)

combo1['values'] = ("Сложение", "Разность", "Умножение", "Деление")
combo1.current(0) 

combo2 = Combobox(root)
combo2.place(x=215, y=200, width=120)

combo2['values'] = ("Сложение", "Разность", "Умножение", "Деление")
combo2.current(0)

combo3 = Combobox(root)
combo3.place(x=365, y=200, width=120)

combo3['values'] = ("Сложение", "Разность", "Умножение", "Деление")
combo3.current(0) 

combor = Combobox(root)
combor.place(x=300, y=250, width=200)

combor['values'] = ("Математическое", "Бухгалтерское", "Усечение")
combor.current(0) 

button_sum = Button(root, text='Получить результат', command=on_click)
button_sum.place(x=100, y=250)

label_result = Label(root, text='Результат:')
label_result.place(x=50, y=300)
label_result.config(width=50)

label_round = Label(root, text='Округленный результат:')
label_round.place(x=50, y=330)
label_round.config(width=50)

root.mainloop()
