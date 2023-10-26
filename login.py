import tkinter
import tkinter.messagebox
import customtkinter

import DataBaseLocal as DataBase
from registro import Registro
import language_dictionary as dic
import menu
# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
from DataBaseLocal import is_username_registered

class Login(customtkinter.CTk):
    def __init__(self):
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        super().__init__()


        # configure window
        self.title(dic.Login3[dic.language])
        self.attributes("-fullscreen", True)
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)


        # create sidebar frame with widgets

        self.logo_label = customtkinter.CTkLabel(self, text=dic.Login3[dic.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.username = customtkinter.CTkLabel(self, text=dic.Username[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)


        self.entry_Username = customtkinter.CTkEntry(self)
        # insertar un valor predeterminado
        self.entry_Username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self, text=dic.Password[dic.language], anchor="w")
        self.contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self, show = "◊")
        self.entry_Contra.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.back = customtkinter.CTkButton(self, text="Vuelta", fg_color=green_light, hover_color=green, command=self.back_menu)
        self.back.place(relx=0.02, rely=0.05, anchor=customtkinter.NW)

        self.sidebar_button_1 = customtkinter.CTkButton(self, text=dic.Login2[dic.language],fg_color=green_light,hover_color=green)
        self.sidebar_button_1.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


        self.sidebar_button_3 = customtkinter.CTkButton(self,  text=dic.Register[dic.language],fg_color=green_light,hover_color=green, command= self.ejecutar_Ventana)
        self.sidebar_button_3.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.incio_facial = customtkinter.CTkButton(self, text="Inicio facial", fg_color=green_light,
                                                        hover_color=green, command=self.login_facial)
        self.incio_facial.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)



    def back_menu(self):
        self.destroy()
        men = menu.Menu_principal()
        men.mainloop()

    def ejecutar_Ventana(self):
        self.destroy()
        nuevo.mainloop()
    def verificacion_login(self):
        global pantalla
        log_usuario = self.entry_Username.get()
        log_contra = self.entry_Contra.get()



        lista_archivos = os.listdir()  # Vamos a importar la lista de archivos con la libreria os
        if log_usuario in lista_archivos:  # Comparamos los archivos con el que nos interesa
            archivo2 = open(log_usuario, "r")  # Abrimos el archivo en modo lectura
            verificacion = archivo2.read().splitlines()  # leera las lineas dentro del archivo ignorando el resto
            if log_contra in verificacion:
                print("Inicio de sesion exitoso")

            else:
                print("Contraseña incorrecta, ingrese de nuevo")
        else:
            print("Usuario no encontrado")

    def login_facial(self):
        # ------------------------------Vamos a capturar el rostro-----------------------------------------------------
        cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
        while (True):
            ret, frame = cap.read()  # Leemos el video
            frame = np.flip(frame, axis=1)
            cv2.imshow('Login Facial', frame)  # Mostramos el video en pantalla
            if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
                break
        usuario_login = self.entry_Username.get()  # Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
        cv2.imwrite(usuario_login + "LOG.jpg",
                    frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
        cap.release()  # Cerramos
        cv2.destroyAllWindows()

        # ----------------- Funcion para guardar el rostro --------------------------

        def log_rostro(img, lista_resultados):
            data = pyplot.imread(img)
            for i in range(len(lista_resultados)):
                x1, y1, ancho, alto = lista_resultados[i]['box']
                x2, y2 = x1 + ancho, y1 + alto
                pyplot.subplot(1, len(lista_resultados), i + 1)
                pyplot.axis('off')
                cara_reg = data[y1:y2, x1:x2]
                cara_reg = cv2.resize(cara_reg, (150, 200),
                                      interpolation=cv2.INTER_CUBIC)  # Guardamos la imagen 150x200
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
                print("Bienvenido al sistema usuario: ", usuario_login)
                print("Compatibilidad con la foto del registro: ", similitud)
                return True  # Devolvemos True en caso de éxito
            else:
                print("Rostro incorrecto, Cerifique su usuario")
                print("Compatibilidad con la foto del registro: ", similitud)
                return False  # Devolvemos False si la similitud no es suficiente

        else:
            print("Usuario no encontrado")
            return False
