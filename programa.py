# bien este tienes unos errores
import os
import tkinter

#aqui estoy creando una funcion que no vamos a utilisar mucho
def servidor(conector="redes conectadas ninguna "):
    print(conector)
    print("redes disponibles : chat red.com o : windows.net ")

#aqui estoy creando una funcion del programa
def chat_red():
    print("red conectada chat red ")
    input()
    os.system("cls")
    print("bienvenido a chat red la mejor red para conectarse ")
    print("hola")
    input("que escribes ")
    print("ok ")
    input("que respondes ")
    print("esto es aburrido ")
    input("cuenta un chiste ")
    print("jajajajajajajaj")
    input("escribe algo ")
    print("bueno me acuerdo esa ves donde me volvi millonario quieres escuchar mi historia ")
    l = input("escribe si para escucharla y escribe no para escucharla ")
    if l == "si":
        os.system("cls")
        print("bueno todo paso asi yo abia ganado la loteria pero en mis sueños jajjajajajajajajajjaaj ")
        input("bueno aqui termino la conversasioncon el usuario lol333 la conversasion quedara archivada ")
    else:
        print("bueno")
        input("bueno aqui termino la conversasioncon el usuario lol333 la conversasion quedara archivada ")
#y aqui estoy creando otra funcion para el programa
def windows_net():
    print("red conectada a windows.net")
    input()
    os.system("cls")
    print("bienvenido a windows.net bien vamos a aser tu ventana ")
    permisos = input("primero tienes que darnos permisos para poder aser carpetas escribe si para dare los permisos o escribe no para no darnos los permisos ")
    permisos_optenidos = True
    if permisos_optenidos == True:
        print("bien vamos a empesar ")
        windows = tkinter.Tk()
        windows.title(input("titulo "))
        windows.geometry(input("tamaño "))
        texto = tkinter.Label(windows,text=input("texto ")).pack()
        windows.config(bg=input("color en ingles "))
        windows.mainloop()
    os.system("COPY CON gracia_por_visitar_windows_net.txt")
    os.system("gracias por visitar windows.net vuelva ala pagina que se encuentra en connecto server cuando quiera ")




#y aqui ya es donde el usuario ejecuta las funciones
servidor()
l1 = input("a cual red conectas ")
if l1 == "chat red.com":
    input("contactando con el servidor ")
    for o in range(1,1001):
        print(o)
    input("Sea logrado contactar con el servidor ")
    chat_red()
if l1 == "windows.net":
    input("se contactara con el servidor ")
    for po in range(1,5001):
        print(po)
    windows_net()
else:
    input("lo siento el servidor al que te quieres conectar no se puede detectar ")