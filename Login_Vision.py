# --------------------------------------Importamos librerias--------------------------------------------

from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np

#tabla de color:

verde_oscuro = "#245953"
verde = "#408E91"
rosa = "#E49393"
gris = "#D8D8D8"
# ------------------------ Crearemos una funcion que se encargara de registrar el usuario ---------------------

#
#

def pantalla_principal_verdad():
    global pantalla  # Globalizamos la variable para usarla en otras funciones
    try:
        pantalla.destroy()
    except:
        None
    pantalla = Tk()
    # cuadro  =  Canvas(pantalla, width=400,height=300,bg=rosa,borderwidth=0)
    # cuadro.place(x = 50,y = 150)
    pantalla.configure(bg=verde_oscuro)
    pantalla.minsize(500, 500)  # Asignamos el tamaño de la ventana
    pantalla.title("Jugar")  # Asignamos el titulo de la pantalla
    Label(text="Eagle Defender", bg=verde, width=50, height="2", font=('Arial Black', 20, 'italic', 'bold'),
          fg=gris).place(x=-225, y=0)  # Asignamos caracteristicas de la ventana

    # ------------------------- Vamos a Crear los Botones ------------------------------------------------------

    Button(text="JUGAR", height=1, width=15, command=lambda: print("inicia partida"), borderwidth=10, bg=rosa,
           font=('Arial Black', 20, 'italic', 'bold'), fg="white").place(x=110, y=200)

    Button(text="Iniciar Sesion", height=1, width=13, command=login, borderwidth=10, bg=verde,
           font=('Arial Black', 10, 'italic', 'bold'), fg="white").place(x=200, y=320)

    pantalla.mainloop()






def pantalla_principal():
    global pantalla  # Globalizamos la variable para usarla en otras funciones
    try:
        pantalla.destroy()
    except:
        None
    pantalla = Tk()
    pantalla.configure(bg = verde_oscuro)
    pantalla.minsize(500,500) # Asignamos el tamaño de la ventana
    pantalla.title("registro")  # Asignamos el titulo de la pantalla
    Label(text="Eagle Defender", bg=verde, width=50, height="2",font=('Arial Black', 20, 'italic', 'bold'),fg = gris).place(x= -225,y = 0)  # Asignamos caracteristicas de la ventana

    # ------------------------- Vamos a Crear los Botones ------------------------------------------------------

    Button(text="Iniciar Sesion", height=1, width=15,command= login , borderwidth=10, bg = gris, font=('Arial Black', 20, 'italic', 'bold'), fg = "black").place(x= 100, y=200)

    Button(text="¿No tienes cuenta?", height=1, width=20,command=registro, borderwidth=10, bg = gris,font=('Arial Black', 10, 'italic', 'bold'), fg= "black").place(x =150, y =320)

    pantalla.mainloop()



#
def registrar_usuario():
    usuario_info = usuario_entrada.get()  # Obetnemos la informacion alamcenada en usuario
    contra_info = contra_entrada.get()  # Obtenemos la informacion almacenada en contra

    archivo = open(usuario_info, "w")  # Abriremos la informacion en modo escritura
    archivo.write(usuario_info + "\n")  # escribimos la info
    archivo.write(contra_info)
    archivo.close()

    # Limpiaremos los text variable
    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)

    # Ahora le diremos al usuario que su registro ha sido exitoso
    Label(pantalla, text="Registro Convencional Exitoso", fg="green", font=("Calibri", 11)).pack()


# --------------------------- Funcion para almacenar el registro facial --------------------------------------

def registro_facial():
    # Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while (True):
        ret, frame = cap.read()  # Leemos el video
        frame = np.flip(frame, axis=1)
        cv2.imshow('Registro Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break
    usuario_img = usuario_entrada.get()
    cv2.imwrite(usuario_img + ".jpg",frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END)  # Limpiamos los text variables
    contra_entrada.delete(0, END)
    Label(pantalla, text="Registro Facial Exitoso", fg="green", font=("Calibri", 11)).pack()

    # ----------------- Detectamos el rostro y exportamos los pixeles --------------------------

    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150, 200),
                                  interpolation=cv2.INTER_CUBIC)  # Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img + ".jpg", cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img + ".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)


# ------------------------Crearemos una funcion para asignar al boton registro --------------------------------
def registro():
    global pantalla

    global usuario_entrada
    global contra_entrada


    global pantalla1
    pantalla.destroy()


    pantalla = Tk()  # Esta pantalla es de un nivel superior a la principal
    pantalla.title("Registro")
    pantalla.minsize(500,500)  # Asignamos el tamaño de la ventana
    pantalla.configure(bg = verde)

    # --------- Empezaremos a crear las entradas ----------------------------------------



    Label(pantalla, text="Registro facial: debe de asignar un usuario:").pack()
    Label(pantalla, text = "").pack()  #Dejamos un poco de espacio
    Label(pantalla, text="Registro tradicional: debe asignar usuario y contraseña:").pack()
    Label(pantalla, text="").pack()  # Dejamos un poco de espacio
    Label(pantalla, text="Usuario * ").pack()  # Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla)  # Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()
    Label(pantalla, text="Contraseña * ").pack()  # Mostramos en la pantalla 1 la contraseña
    contra_entrada = Entry(pantalla)  # Creamos un text variable para que el usuario ingrese la contra
    contra_entrada.pack()
    Label(pantalla, text="").pack()  # Dejamos un espacio para la creacion del boton
    Button(pantalla, text="Registro Tradicional", width=15, height=1,command=registrar_usuario,bg = rosa).pack()  # Creamos el boton

    # ------------ Vamos a crear el boton para hacer el registro facial --------------------
    Label(pantalla, text="").pack()
    Button(pantalla, text="Registro Facial", width=15, height=1, command=registro_facial, bg = rosa).pack()
    Button(pantalla, text="Regreso", width=15, height=1, command=pantalla_principal, bg=rosa).pack()
    pantalla.mainloop()

#
# # ------------------------------------------- Funcion para verificar los datos ingresados al login ------------------------------------
#
def verificacion_login():
    global pantalla
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, END)
    contra_entrada2.delete(0, END)

    lista_archivos = os.listdir()  # Vamos a importar la lista de archivos con la libreria os
    if log_usuario in lista_archivos:  # Comparamos los archivos con el que nos interesa
        archivo2 = open(log_usuario, "r")  # Abrimos el archivo en modo lectura
        verificacion = archivo2.read().splitlines()  # leera las lineas dentro del archivo ignorando el resto
        if log_contra in verificacion:
            print("Inicio de sesion exitoso")
            Label(pantalla, text="Inicio de Sesion Exitoso", fg="green", font=("Calibri", 11)).pack()
        else:
            print("Contraseña incorrecta, ingrese de nuevo")
            Label(pantalla, text="Contraseña Incorrecta", fg="red", font=("Calibri", 11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla, text="Usuario no encontrado", fg="red", font=("Calibri", 11)).pack()


# --------------------------Funcion para el Login Facial --------------------------------------------------------
def login_facial():
    # ------------------------------Vamos a capturar el rostro-----------------------------------------------------
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while (True):
        ret, frame = cap.read()  # Leemos el video
        frame = np.flip(frame, axis=1)
        cv2.imshow('Login Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break
    usuario_login = verificacion_usuario.get()  # Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
    cv2.imwrite(usuario_login + "LOG.jpg",
                frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    usuario_entrada2.delete(0, END)  # Limpiamos los text variables
    contra_entrada2.delete(0, END)

    # ----------------- Funcion para guardar el rostro --------------------------

    def log_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150, 200), interpolation=cv2.INTER_CUBIC)  # Guardamos la imagen 150x200
            cv2.imwrite(usuario_login + "LOG.jpg", cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    # -------------------------- Detectamos el rostro-------------------------------------------------------

    img = usuario_login + "LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)

    # -------------------------- Funcion para comparar los rostros --------------------------------------------
    def orb_sim(img1, img2):
        global pantalla
        orb = cv2.ORB_create()  # Creamos el objeto de comparacion

        kpa, descr_a = orb.detectAndCompute(img1, None)  # Creamos descriptor 1 y extraemos puntos claves
        kpb, descr_b = orb.detectAndCompute(img2, None)  # Creamos descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  # Aplicamos el comparador a los descriptores

        regiones_similares = [i for i in matches if
                              i.distance < 70]  # Extraemos las regiones similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares) / len(matches)  # Exportamos el porcentaje de similitud

    # ---------------------------- Importamos las imagenes y llamamos la funcion de comparacion ---------------------------------

    im_archivos = os.listdir()  # Vamos a importar la lista de archivos con la libreria os
    if usuario_login + ".jpg" in im_archivos:  # Comparamos los archivos con el que nos interesa
        rostro_reg = cv2.imread(usuario_login + ".jpg", 0)  # Importamos el rostro del registro
        rostro_log = cv2.imread(usuario_login + "LOG.jpg", 0)  # Importamos el rostro del inicio de sesion
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.98:
            Label(pantalla, text="Inicio de Sesion Exitoso", fg="green", font=("Calibri", 11)).pack()
            print("Bienvenido al sistema usuario: ", usuario_login)
            print("Compatibilidad con la foto del registro: ", similitud)
        else:
            print("Rostro incorrecto, Cerifique su usuario")
            print("Compatibilidad con la foto del registro: ", similitud)
            Label(pantalla, text="Incompatibilidad de rostros", fg="red", font=("Calibri", 11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla, text="Usuario no encontrado", fg="red", font=("Calibri", 11)).pack()
#
#
# # ------------------------Funcion que asignaremos al boton login -------------------------------------------------
#
def login():
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2
    global pantalla
    pantalla.destroy()

    pantalla = Tk()
    pantalla.title("Login")
    pantalla.minsize(500,500)  # Creamos la ventana
    pantalla.configure(bg = verde)
    Label(pantalla, text="Login facial: debe de asignar un usuario:", bg=verde).pack()
    Label(pantalla, text="Login tradicional: debe asignar usuario y contraseña:", bg=verde).pack()
    Label(pantalla, text="").pack()  # Dejamos un poco de espacio

    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()

    # ---------------------------------- Ingresamos los datos --------------------------
    Label(pantalla, text="Usuario * ", bg = verde).pack()
    usuario_entrada2 = Entry(pantalla, textvariable=verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla, text="Contraseña * ", bg=verde).pack()
    contra_entrada2 = Entry(pantalla, textvariable=verificacion_contra)
    contra_entrada2.pack()
    Label(pantalla, text="").pack()
    Button(pantalla, text="Inicio de Sesion Tradicional", width=20, height=1, command= verificacion_login, bg=verde_oscuro,borderwidth=10).pack()

    # ------------ Vamos a crear el boton para hacer el login facial --------------------
    Label(pantalla, text="", bg=verde).pack()
    Button(pantalla, text="Inicio de Sesion Facial", width=20, height=1,  command=login_facial,bg=verde_oscuro,borderwidth=10).pack()
    Button(pantalla, text="Regreso", width=15, height=1, command=pantalla_principal, bg=verde_oscuro,borderwidth=10).pack()
    Button(text="¿No tienes cuenta?", height=1, width=20, command=registro, borderwidth=10, bg=verde_oscuro,font=('Arial Black', 10, 'italic', 'bold'), fg="black").pack()
    pantalla.mainloop()


# ------------------------- Funcion de nuestra pantalla principal ------------------------------------------------




pantalla_principal_verdad()