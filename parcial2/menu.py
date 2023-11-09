from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import subprocess

menu = Tk()
menu.title("El menu")
menu.geometry("800x580")

#pong
def juegoPong():
    archivo_path = 'pong.py'

    try:
        subprocess.Popen(['python3', archivo_path])
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo_path}")
    except Exception as e:
        print(f'Ocurrió un error al ejecutar el archivo: {e}')

#adivina
def juegoAdivina():
    archivo_path = 'adivina.py'

    try:
        subprocess.Popen(['python3', archivo_path])
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo_path}")
    except Exception as e:
        print(f'Ocurrió un error al ejecutar el archivo: {e}')

#conecta4
def juegoConecta():
    archivo_path = 'conecta4.py'

    try:
        subprocess.Popen(['python3', archivo_path])
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo_path}")
    except Exception as e:
        print(f'Ocurrió un error al ejecutar el archivo: {e}')

#invasion
def juegoInvasion():
    archivo_path = 'invasion/invasion.py'

    try:
        subprocess.Popen(['python3', archivo_path])
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo_path}")
    except Exception as e:
        print(f'Ocurrió un error al ejecutar el archivo: {e}')

label = Label(menu, text='Menú Principal')
label.grid(row=0, column=0)

# Portada primer juego
img1 = Image.open('images/game2.png')
img1 = img1.resize((400, 250))
imagen1 = ImageTk.PhotoImage(img1)
image1 = tk.Label(menu, image=imagen1)
image1.grid(row=3, column=0)
btn1 = Button(menu, text='Iniciar Juego', command=juegoPong)
btn1.grid(row=4, column=0)

# Portada de segundo juego
img2 = Image.open('images/game1.png')
img2 = img2.resize((400, 250))
imagen2 = ImageTk.PhotoImage(img2)
image2 = tk.Label(menu, image=imagen2)
image2.grid(row=3, column=1)
btn2 = Button(menu, text='Iniciar Juego', command=juegoAdivina)
btn2.grid(row=4, column=1)

# Portada de tercer juego
img3 = Image.open('images/game3.png')
img3 = img3.resize((400, 250))
imagen3 = ImageTk.PhotoImage(img3)
image3 = tk.Label(menu, image=imagen3)
image3.grid(row=5, column=0)
btn3 = Button(menu, text='Iniciar Juego', command=juegoInvasion)
btn3.grid(row=6, column=0)

# Portada de cuarto juego
img4 = Image.open('images/game4.png')
img4 = img4.resize((400, 250))
imagen4 = ImageTk.PhotoImage(img4)
image4 = tk.Label(menu, image=imagen4)
image4.grid(row=5, column=1)
btn4 = Button(menu, text='Iniciar Juego', command=juegoConecta)
btn4.grid(row=6, column=1)

mainloop()