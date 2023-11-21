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



        # ----------------- Funcion para guardar el rostro --------------------------
    def login_f(self,username):
            # ------------------------------Vamos a capturar el rostro-----------------------------------------------------
        cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
        while (True):
            ret, frame = cap.read()  # Leemos el video
            frame = np.flip(frame, axis=1)
            cv2.imshow('Login Facial', frame)  # Mostramos el video en pantalla
            if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
                break
        usuario_login = "../BiometricPic/"+username  # Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
        cv2.imwrite(usuario_login + "LOG.jpg", frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
        cap.release()  # Cerramos
        cv2.destroyAllWindows()

        # username.delete(0)  # Limpiamos los text variables
        # self.entry_Username.delete(0)

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
                cv2.imwrite("../BiometricPic/"+username + "LOG.jpg", cara_reg)
                return pyplot.imshow(data[y1:y2, x1:x2])
            pyplot.show()

            # -------------------------- Detectamos el rostro-------------------------------------------------------

        img ="../BiometricPic/"+username + "LOG.jpg"
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

        im_archivos =os.listdir("../BiometricPic/")  # Vamos a importar la lista de archivos con la libreria os
        if username + ".jpg" in im_archivos:  # Comparamos los archivos con el que nos interesa
            rostro_reg = cv2.imread("../BiometricPic/"+username + ".jpg", 0)  # Importamos el rostro del registro
            rostro_log = cv2.imread("../BiometricPic/"+username + "LOG.jpg", 0)  # Importamos el rostro del inicio de sesion
            similitud = orb_sim(rostro_reg, rostro_log)
            if similitud >= 0.80:

                print("Compatibilidad con la foto del registro: ", similitud)
                return True

            else:
                print("Rostro incorrecto, Cerifique su usuario")
                print("Compatibilidad con la foto del registro: ", similitud)
                return False


        else:
            print("Usuario no encontrado")


            # ----------------- Funcion para guardar el rostro --------------------------


