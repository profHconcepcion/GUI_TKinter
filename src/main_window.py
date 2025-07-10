'''
COMP 315 TKinter GUI Practice
'''
import tkinter as tk


window = tk.Tk()
window.title('Ventana Principal') # Titulo de la pantalla
window.geometry('300x200') # Dimensiones de la pantalla


lb_header = tk.Label(window, text='Titulo principal de la pantalla')
lb_header.pack()



window.mainloop()

