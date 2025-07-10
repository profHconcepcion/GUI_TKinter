'''
COMP 315 TKinter GUI Practice
'''
import tkinter as tk


window = tk.Tk()
window.title('Ventana Principal') # Titulo de la pantalla
window.geometry('300x200') # Dimensiones de la pantalla


lb_header = tk.Label(window, text='Primer Label')
lb_header.pack()

lb_sub_header = tk.Label(window, text='Segundo label')
lb_sub_header.pack()

lb_sub_sub_header = tk.Label(window, text='Tercer Label')
lb_sub_sub_header.pack()

window.mainloop()

