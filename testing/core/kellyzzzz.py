import tkinter as tk
from tkinter import ttk

def validacion_inicial():
    mensajes = []

    nombre_proyecto = entryNombre_Proyecto.get()
    cant_hitos = entrycant_hitos.get()
    bac = entrybac.get()
    tipo_proyecto = comboboxTipo.get()

    if not nombre_proyecto:
        mensajes.append("*Ingresa el nombre del proyecto")
    if not cant_hitos.isdigit() or int(cant_hitos) <= 1:
        mensajes.append("*Ingresa una cantidad de hitos válida")
    try:
        bac_float = float(bac)
        if bac_float <= 0:
            mensajes.append("* Ingresa un presupuesto total válido")
    except ValueError:
        mensajes.append("* Ingresa un presupuesto total válido")
    if not tipo_proyecto:
        mensajes.append("*Ingrese el tipo de proyecto")

    if mensajes:
        mostrar_mensaje("\n".join(mensajes), "red")
    #finalizacion de proceso 1-entrada de datos
    else:
        mensaje_label.config(text="")
        raiz.geometry("400x600")
        continuar.place_forget()
        entryNombre_Proyecto.config(state="disabled")
        entrycant_hitos.config(state="disabled")
        entrybac.config(state="disabled")
        comboboxTipo.config(state="disabled")

        ValorPlanxHito(tipo_proyecto, int(cant_hitos))

def validacion_sec():
    mensajes2 = []
    val = len(entrycampo_hito)
    for entry in entrycampo_hito:  # Iterar sobre los campos Entry
        valor = entry.get()
        try:
            valor_float = float(valor)
            if valor_float <= 0:
                mensajes2.append("* Verifica que los valores sean válidos")
            
        except ValueError:
            mensajes2.append("* Ingresa un valor numérico válido")

    if mensajes2:
        mostrar_mensaje2("\n".join(mensajes2), "red", val)
    else:
        combobox_HitosEval(val)
        combobox_condicion(val)
        

def combobox_HitosEval(val):
    labelHitosEvaluados = ttk.Label(raiz, text="Hitos a evaluar ")
    labelHitosEvaluados.place(x=50, y=300 + val*30)
    comboboxHitos = ttk.Combobox(raiz)
    comboboxHitos['values'] = list(range(1, val+1))
    comboboxHitos['state'] = 'readonly'
    comboboxHitos.place(x=200, y=300 + val*30)

def combobox_condicion(val):
    labelCondicion = ttk.Label(raiz, text="Condicion del proyecto: ")
    labelCondicion.place(x=50, y=330 + val*30)
    comboboxCond = ttk.Combobox(raiz)
    comboboxCond['values']=('Típico','Atípico')
    comboboxCond['state']= 'readonly'
    comboboxCond.place(x=200, y=330 + val*30)
    ###
    calcular_proceso = ttk.Button(raiz, text="Calcular", command=calcular)
    calcular_proceso.place(x=170, y=360 + val*30)

def mostrar_mensaje(mensaje, color):
    mensaje_label.config(text=mensaje, fg=color)

def mostrar_mensaje2(mensaje, color,val):
    mensaje2_label = tk.Label(raiz, text="", fg="black", justify='left')
    mensaje2_label.place(x=50, y=200 + val*30) 
    mensaje2_label.config(text=mensaje, fg=color)

def ValorPlanxHito(tipo_proyecto, cant_hitos):
    a=230
    
    if tipo_proyecto == "Heterogéneo":
        num_hito = ttk.Label(raiz, text="Ingreso De Hitos: ", justify="left")
        num_hito.place(x=50,y = 200)
        for i in range(int(cant_hitos)):
            campo_hito = ttk.Label(raiz, text=f"Hito {i+1}: ")
            campo_hito.place(x=50, y=a)
            entry_hito = ttk.Entry(raiz)
            entry_hito.place(x=200,y=a)
            entrycampo_hito.append(entry_hito)
            a += 25
    
        continuar2 = ttk.Button(raiz, text="Continuar", command=validacion_sec)
        continuar2.place(x=170, y=a+30)

    else:
        mensaje_label = ttk.Label(raiz, text="Valor por hito: BAC/Num. de hitos")
        mensaje_label.place(x=50, y=a + 30)
        combobox_HitosEval(cant_hitos)
        combobox_condicion(cant_hitos)

def calcular():
    label_zzz = ttk.Label(raiz, text="fannyyyyyyyyy", justify="center", foreground="red")
    label_zzz.place(x=200, y=200)
    
#---------------------------------------------------------------------------#
raiz = tk.Tk()
raiz.title("Programa de Gestión de Valor Ganado")
raiz.resizable(1, 1)
raiz.geometry("400x300")

entrycampo_hito = []#valores ingresados  heterogeneo

titulo = tk.Label(raiz, text="MENU", font=("Arial", 16), justify="center")
titulo.place(x=160, y=10)

Nombre_Proyecto = ttk.Label(raiz, text="Nombre del proyecto: ")
Nombre_Proyecto.place(x=50, y=40)
entryNombre_Proyecto = ttk.Entry(raiz)
entryNombre_Proyecto.place(x=200, y=40)

cant_hitos = ttk.Label(raiz, text="Cantidad de hitos: ")
cant_hitos.place(x=50, y=70)
entrycant_hitos = ttk.Entry(raiz)
entrycant_hitos.place(x=200, y=70)

bac = ttk.Label(raiz, text="Presupuesto total (BAC): ")
bac.place(x=50, y=100)
entrybac = ttk.Entry(raiz)
entrybac.place(x=200, y=100)

labelTipo = ttk.Label(raiz, text="Tipo de proyecto: ")
labelTipo.place(x=50, y=130)
comboboxTipo = ttk.Combobox(raiz)
comboboxTipo['values'] = ('Homogéneo', 'Heterogéneo')
comboboxTipo['state'] = 'readonly'
comboboxTipo.place(x=200, y=130)

continuar = ttk.Button(raiz, text="Continuar", command=validacion_inicial)
continuar.place(x=170, y=160)

mensaje_label = tk.Label(raiz, text="", fg="black", justify='left')
mensaje_label.place(x=50, y=190)

raiz.mainloop()