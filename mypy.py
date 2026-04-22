# region 1. Importacoes e configuracoes
import tkinter as tk
import customtkinter as ctk
import math

# endregion

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Calculadora")
app.geometry("400x500")

display = ctk.CTkEntry(app, width=360, height=60, font=("Arial", 32), justify="right")
display.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

# region 5. Bloco de memoria
num1 = 0
num2 = 0

op_sum = "+"
op_prod = "*"
op_div = "/"

# endregion

def button_number(number):
    texto_atual = display.get()
    display.delete(0, 'end')
    display.insert(0, texto_atual + str(number))

def end_display():
    texto_atual = display.get()
    display.delete(0, 'end')
    display.insert(0, texto_atual[:-1])

def end_display0():
    texto_atual = display.get()
    display.delete(0, 'end')   

def apli_Op():
    texto_atual = display.get()
    display.delete(0, 'end')
    global num1, num2, op_div, op_prod, op_sum
    num1 = texto_atual

def insert_algo():
    texto = display.get()
    display.delete(0, 'end')
    display.insert(0, str(texto + "algo"))
   


def Eq_operation():
    global num1, num2
    num1 = float(display.get())
    display.delete(0, 'end') 



    


# region 2. Bloco de operacoes

btn_del = ctk.CTkButton(app, text="-", width=20, height=20, font=("Arial", 24), command=lambda: end_display())
btn_del.grid(row=1, column=3, padx=2, pady=2)

btn_dele = ctk.CTkButton(app, text="--", width=20, height=20, font=("Arial", 24), command=lambda: end_display0())
btn_dele.grid(row=2, column=3, padx=2, pady=2)

btnsum = ctk.CTkButton(app, text="+", width=35, height=35, font=("Arial", 24), command=lambda: insert_algo())
btnsum.grid(row=3, column=3, padx=2, pady=3)

btnEq = ctk.CTkButton(app, text="=", width=35, height=35, font=("Arial", 24), command=lambda: Eq_operation())
btnEq.grid(row=4, column=3, padx=2, pady=3)

# endregion

# region 3. Bloco de numeros
btn7 = ctk.CTkButton(app, text="7", width=65, height=65, font=("Arial", 24), command=lambda: button_number(7))
btn7.grid(row=1, column=0, padx=2, pady=3)

btn8 = ctk.CTkButton(app, text="8", width=65, height=65, font=("Arial", 24), command=lambda: button_number(8))
btn8.grid(row=1, column=1, padx=2, pady=3)

btn9 = ctk.CTkButton(app, text="9", width=65, height=65, font=("Arial", 24), command=lambda: button_number(9))
btn9.grid(row=1, column=2, padx=2, pady=3)

btn4 = ctk.CTkButton(app, text="4", width=65, height=65, font=("Arial", 24), command=lambda: button_number(4))
btn4.grid(row=2, column=0, padx=2, pady=3)

btn5 = ctk.CTkButton(app, text="5", width=65, height=65, font=("Arial", 24), command=lambda: button_number(5))
btn5.grid(row=2, column=1, padx=2, pady=3)

btn6 = ctk.CTkButton(app, text="6", width=65, height=65, font=("Arial", 24), command=lambda: button_number(6))
btn6.grid(row=2, column=2, padx=2, pady=3)

btn1 = ctk.CTkButton(app, text="1", width=65, height=65, font=("Arial", 24), command=lambda: button_number(1))
btn1.grid(row=3, column=0, padx=2, pady=3)

btn2 = ctk.CTkButton(app, text="2", width=65, height=65, font=("Arial", 24), command=lambda: button_number(2))
btn2.grid(row=3, column=1, padx=2, pady=3)

btn3 = ctk.CTkButton(app, text="3", width=65, height=65, font=("Arial", 24), command=lambda: button_number(3))
btn3.grid(row=3, column=2, padx=2, pady=3)
# endregion

app.mainloop()


