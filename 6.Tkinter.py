"""
Crea una aplicación TKinter llamada calculadora1.py con una apariencia como esta 
(y sin añadir ninguna funcionalidad de momento). El desplegable debe contener los símbolos de las cuatro operaciones 
aritméticas básicas: +, -, * y /
"""
import tkinter as tk
from tkinter import ttk


def calcular():
    try:
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        operacion = combo.get()
        
        if operacion == 'Suma':
            resultado = num1 + num2
        elif operacion == 'Resta':
            resultado = num1 - num2
        elif operacion == 'Multiplicación':
            resultado = num1 * num2
        elif operacion == 'División':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        else:
            resultado = "Selecciona una operación"
        
        res.config(text=f"Resultado: {resultado}")
    except ValueError:
        res.config(text="Error: Entrada inválida")




ventana = tk.Tk()
ventana.title("Ventana de prueba")
# Ventana de 600 x 400
# ubicada en x = 100, y = 200
ventana.geometry("600x400+100+200")

#Num1
lbl_num1 = tk.Label(ventana, text="Número 1:")
lbl_num1.pack()
txt_num1 = tk.Entry(ventana)
txt_num1.pack()


#Num2
lbl_num2 = tk.Label(ventana, text="Número 2:")
lbl_num2.pack()
txt_num2 = tk.Entry(ventana)
txt_num2.pack()

#Operacion
lbl_op = tk.Label(ventana, text="Operación:")
lbl_op.pack()
opciones = ['Suma', 'Resta', 'Multiplicación', 'División']
combo = ttk.Combobox(ventana)
combo['values'] = opciones
combo.pack()

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()


res = tk.Label(ventana, text="Resultado")
res.pack()

ventana.mainloop()