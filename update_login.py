import tkinter as tk

import customtkinter
import customtkinter as ctk
# import os
# import cv2
# from matplotlib import pyplot
# from mtcnn.mtcnn import MTCNN
# import numpy as np

# Paleta de colores
green = "#245953"
green_light = "#408E91"
pink = "#E49393"
grey = "#D8D8D8"
font_style = ('helvic', 20)

root = None




def principal():


    global  root

    try:
        root.destroy()
    except:
        None

    root = customtkinter.CTk()

    root.title('Main Menu')
    root.geometry('500x500')  # Establece el tamaño de la ventana principal
    root.configure(fg_color=green)

    # Crear un frame principal para organizar los botones


    Lenguage_options = ctk.CTkComboBox(root, values=["Español", "Ingles", "Fraces"] ).place(x=10, y=10)

    # Agregar un Label como título
    label_title = ctk.CTkLabel(root, text='EAGLE DEFENDER',font= customtkinter.CTkFont(size=50, weight="bold"), fg_color=green,
                               bg_color=green_light, text_color="white")
    label_title.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

    button_play = ctk.CTkButton(root, text='JUGAR', corner_radius=10, fg_color=grey, bg_color=green_light,
                                hover_color=pink, font=font_style,  text_color="black", width=250, height=50,)
    button_play.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

    button_login = ctk.CTkButton(root, text='INICIAR SESION', command=login, corner_radius=10, fg_color=grey,
                                 bg_color=green_light, hover_color=pink, font=font_style, width=250, height=50,
                                 text_color="black")
    button_login.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    root.mainloop()


def login():
    global root
    try:
        root.destroy()
    except:
        None

    root = customtkinter.CTk()
    root.title('Login Window')
    root.geometry('500x500')  # Establece el tamaño de la ventana principal
    root.configure(fg_color=green)

    label_title = customtkinter.CTkLabel(root, text='Please Login', font=('Arial', 20), anchor='center', text_color=grey, fg_color=green)
    label_title.pack(pady=10)
    #
    # # Utilizar un frame para organizar los elementos del formulario
    #
    #
    label_username = customtkinter.CTkLabel(root, text='Username:', anchor='w', text_color=grey, fg_color=green, font=font_style)
    label_username.pack(fill='x', pady=5, padx=5)

    entry_username = customtkinter.CTkEntry(root, text_color=green, fg_color=grey)
    entry_username.pack(fill='x', pady=5, padx=5)
    #
    label_password = customtkinter.CTkLabel(root, text='Password:', anchor='w', text_color=grey, fg_color=green, font=font_style)
    label_password.pack(fill='x', pady=5, padx=5)
    #
    entry_password = customtkinter.CTkEntry(root, show='🔹', text_color=green, fg_color=grey)
    entry_password.pack(fill='x', pady=5, padx=5)
    #
    button_check_login = ctk.CTkButton(root, text='Login', corner_radius=10,fg_color=grey, text_color="black", hover_color=pink, font=font_style)
    button_check_login.pack(pady=10)
    #
    button_back = ctk.CTkButton(root, text='X', command=principal, corner_radius=10, fg_color=grey,
                                bg_color=green_light, hover_color=pink, font=font_style,text_color="black")
    button_back.pack(pady=10)
    Registro = ctk.CTkButton(root, text='registro', corner_radius=10, fg_color=grey,
                                bg_color=green_light, hover_color=pink, font=font_style,text_color="black")
    Registro.pack(pady=10)
    #
    Registro_Facial = ctk.CTkButton(root, text='Reconocimeinto Facial', corner_radius=10, fg_color=grey,
                             bg_color=green_light, hover_color=pink, font=font_style,text_color="black")
    Registro_Facial.pack(pady=10)
    root.mainloop()


# def registrarse():
#     global root
#     global entry_username
#
#     root.destroy()
#     root = customtkinter.CTk()
#     root.title('Login Window')
#     root.geometry('500x500')  # Establece el tamaño de la ventana principal
#     root.configure(fg_color=green)
#
#     label_title = customtkinter.CTkLabel(root, text='Please Login', font=('Arial', 20), anchor='center', fg=grey, bg=green)
#     label_title.pack(pady=10)
#
#     # Utilizar un frame para organizar los elementos del formulario
#     form_frame = tk.Frame(root, bg=green)
#     form_frame.pack(pady=20)
#
#     label_username = tk.Label(form_frame, text='Username:', anchor='w', fg=grey, bg=green, font=font_style)
#     label_username.pack(fill='x', pady=5, padx=5)
#
#     entry_username = tk.Entry(form_frame, fg=green, bg=pink, insertbackground=grey)
#     entry_username.pack(fill='x', pady=5, padx=5)
#
#     label_password = tk.Label(form_frame, text='Password:', anchor='w', fg=grey, bg=green, font=font_style)
#     label_password.pack(fill='x', pady=5, padx=5)
#
#     entry_password = tk.Entry(form_frame, show='🔹', fg=green, bg=pink, insertbackground=grey)
#     entry_password.pack(fill='x', pady=5, padx=5)
#
#     button_check_login = ctk.CTkButton(root, text='Registro Facial', corner_radius=10,
#                                        fg_color=grey, bg_color=green_light, hover_color=pink, font=font_style, command=registro_facial)
#     button_check_login.pack(pady=10)
#
#     button_back = ctk.CTkButton(root, text='Back', command=principal, corner_radius=10, fg_color=grey,
#                                 bg_color=green_light, hover_color=pink, font=font_style)
#     button_back.pack(pady=10)
#     root.mainloop()
#
# def registro_facial():
#     global  entry_username
#     # Vamos a capturar el rostro
#     cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
#     while (True):
#         ret, frame = cap.read()  # Leemos el video
#         frame = np.flip(frame, axis=1)
#         cv2.imshow('Registro Facial', frame)  # Mostramos el video en pantalla
#         if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
#             break
#     usuario_img = entry_username.get()
#     cv2.imwrite(usuario_img + ".jpg",frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
#     cap.release()  # Cerramos
#     cv2.destroyAllWindows()
#
#     entry_username.delete(0)  # Limpiamos los text variables
#     # Label(pantalla, text="Registro Facial Exitoso", fg="green", font=("Calibri", 11)).pack()
#
#     # ----------------- Detectamos el rostro y exportamos los pixeles --------------------------
#
#     def reg_rostro(img, lista_resultados):
#         data = pyplot.imread(img)
#         for i in range(len(lista_resultados)):
#             x1, y1, ancho, alto = lista_resultados[i]['box']
#             x2, y2 = x1 + ancho, y1 + alto
#             pyplot.subplot(1, len(lista_resultados), i + 1)
#             pyplot.axis('off')
#             cara_reg = data[y1:y2, x1:x2]
#             cara_reg = cv2.resize(cara_reg, (150, 200),
#                                   interpolation=cv2.INTER_CUBIC)  # Guardamos la imagen con un tamaño de 150x200
#             cv2.imwrite(usuario_img + ".jpg", cara_reg)
#             pyplot.imshow(data[y1:y2, x1:x2])
#         pyplot.show()
#
#     img = usuario_img + ".jpg"
#     pixeles = pyplot.imread(img)
#     detector = MTCNN()
#     caras = detector.detect_faces(pixeles)
#     reg_rostro(img, caras)
#



#

principal()