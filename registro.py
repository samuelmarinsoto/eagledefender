import datetime
import tkinter
import tkinter.messagebox
from tkinter import simpledialog

import customtkinter
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk
import language_dictionary as dic
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
import DataBase
import menu
import re


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Registro(customtkinter.CTk):
    """
       Clase que representa la ventana de registro de la aplicación.

       Esta clase crea una ventana de registro con tres pestañas: Datos, Juego y Personalización. Cada pestaña tiene campos
       para ingresar información de usuario y opciones de personalización.

       Args:
           Ninguno

       Attributes:
           Ninguno

       """
    def __init__(self):

        """
               Inicializa una instancia de la clase Registro.

               Crea una ventana de registro con pestañas para Datos, Juego y Personalización. Dentro de cada pestaña, se
               proporcionan campos para ingresar información de usuario y opciones de personalización.

               """
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        font_style = ('helvic', 20)
        self.imagen_seleccionada = None
        super().__init__()

        # configure window
        self.title(dic.Registration[dic.language])
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)

        # create sidebar frame with widgets

        self.tabview = customtkinter.CTkTabview(self, width=400, height=400, fg_color=grey , segmented_button_selected_color=green, segmented_button_selected_hover_color=pink)
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add(dic.Data[dic.language])
        self.tabview.add(dic.Game[dic.language])
        self.tabview.add(dic.Personalization[dic.language])
        self.tabview.tab(dic.Data[dic.language]).grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab(dic.Game[dic.language]).grid_columnconfigure(0, weight=1)



        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Registration[dic.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


        self.nombre = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Name[dic.language], anchor="w")
        self.nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entry_Nombre = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Nombre.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.apellido = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Surname[dic.language], anchor="w")
        self.apellido.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Apellido = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Apellido.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


        self.correo = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Email[dic.language], anchor="w")
        self.correo.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.entry_Correo = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Correo.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


        self.edad_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text= dic.Age[dic.language]+": 0")
        self.edad_label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.edad_slider = customtkinter.CTkSlider(self.tabview.tab(dic.Data[dic.language]), command=self.update_edad_label, from_=0, to=100, button_color = green, button_hover_color=pink)
        self.edad_slider.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)









        #-------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Username[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.entry_Username = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]))
        self.entry_Username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Password[dic.language], anchor="w")
        self.contra.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊")
        self.entry_Contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.contra_check = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text="Confirmar Contraseña",
                                             anchor="w")
        self.contra_check.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.entry_Contra_check = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊")
        self.entry_Contra_check.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.foto_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), corner_radius=60, text=dic.Photo[dic.language])
        self.foto_label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)



        self.subir_Foto = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), text="✚",fg_color=green_light, hover_color=green, corner_radius=80, width=10, command=self.abrir_archivo)
        self.subir_Foto.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)


        #----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]), text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]), text=dic.Theme[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab(dic.Personalization[dic.language]), values=[dic.Red[dic.language], dic.Black[dic.language], dic.Blue[dic.language],dic.White[dic.language],dic.Green[dic.language]],fg_color=green_light, button_color=green)
        self.appearance_mode_optionemenu.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]), text=dic.FavoriteSongs[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]) )
        self.cancion1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion3.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
                                                        text=dic.Register[dic.language],
                                                        fg_color=green_light, hover_color=green,
                                                        command=self.on_register_button_click)
        self.sidebar_button_1.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
    def verificar_contraseñas(self):
        if self.entry_Contra.get() == self.entry_Contra_check.get():
            return self.entry_Contra_check.get()

    def registrar_usuario(self):
        # Recoge la información del usuario desde la GUI
        usuario = self.entry_Username.get()
        contra = self.verificar_contraseñas()
        if contra is None:
            print("Error", "Las contraseñas no coinciden.")
            return
        nombre = self.entry_Nombre.get()
        apellido = self.entry_Apellido.get()
        correo = self.entry_Correo.get()
        edad = self.edad_slider.get()
        # cancion = self.cancion1.get()
        usuario_img = self.entry_Username.get()
        imagen_ruta = 'ProfilePics/' + usuario_img + ".jpg"  # Ruta de la imagen guardada

        # Genera un nuevo código de confirmación
        codigo = DataBase.generar_codigo_confirmacion()

        # Guarda el código de confirmación en la base de datos
        DataBase.guardar_codigo_confirmacion(correo, codigo)

        # Enviar código de confirmación por correo electrónico
        DataBase.enviar_correo_confirmacion(correo, codigo)

        # Validaciones antes de insertar el usuario
        if edad < 13:
            tkinter.messagebox.showerror("Error", "El usuario debe tener al menos 13 años para registrarse.")
            return

        if DataBase.username_ya_registrado(usuario):
            tkinter.messagebox.showerror("Error", "Este nombre de usuario ya está registrado.")
            return

        if DataBase.correo_ya_registrado(correo):
            tkinter.messagebox.showerror("Error", "Este correo ya está registrado.")
            return
        # Llama a la función para insertar los datos en la base de datos
        try:
            print(f"Debug: Código generado: {codigo}")
            DataBase.insert_user(usuario, contra, nombre, apellido, correo, edad, imagen_ruta, codigo)
            # Nota: No mostramos el mensaje de éxito aquí.
        except Exception as e:
            print("Error", f"Ocurrió un error al registrar al usuario: {e}")
            return False  # Retornamos False para indicar que el registro no fue exitoso

        return True  # Retornamos True para indicar que el registro fue exitoso

    def on_register_button_click(self):
        print("Botón de registro clickeado")

        # Intentamos registrar al usuario.
        if self.registrar_usuario():
            contrasena = self.entry_Contra.get()
            if not self.validar_contrasena(contrasena):
                tkinter.messagebox.showerror("Error",
                                             "La contraseña no cumple con los requisitos. - Mínimo 8 caracteres- Máximo 16 caracteres- Al menos una letra mayúscula- Al menos una letra minúscula- Al menos un número- Al menos un carácter especial: @#$%^&+=")
                return

            # Ahora solicitamos la verificación
            self.solicitar_verificacion()

    def solicitar_verificacion(self):
        # Aquí puedes abrir una nueva ventana o usar la actual para solicitar el código al usuario.
        codigo_ingresado = simpledialog.askstring("Verificación",
                                                  "Por favor, ingresa el código de verificación enviado a tu correo:",
                                                  parent=self)

        correo = self.entry_Correo.get()  # Obtenemos el correo desde la GUI

        if DataBase.confirmar_correo(correo, codigo_ingresado):
            tkinter.messagebox.showinfo("Éxito", "Correo verificado con éxito.")
            # Aquí puedes proceder con el siguiente paso, por ejemplo, registro facial.
            self.registro_facial()
        else:
            tkinter.messagebox.showerror("Error", "El código de verificación es incorrecto o ha expirado.")
            # Opcionalmente, puedes permitir que el usuario lo intente de nuevo o cancelar el registro.

    def update_edad_label(self, value):
        self.edad_label.configure(text=dic.Age[dic.language]+f" :{round(value)}")

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])
        if archivo:
            # Cargar la imagen
            imagen = Image.open(archivo)
            # Redimensionar la imagen según el tamaño deseado (ajusta según tus necesidades)
            imagen = imagen.resize((80, 80), Image.ANTIALIAS)
            # Convertir la imagen en un formato compatible con Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)
            # Mostrar la imagen en el CTkLabel
            self.foto_label.configure(image=imagen_tk)
            self.foto_label.configure(text="")
            self.foto_label.image = imagen_tk  # ¡Importante! Debes mantener una referencia a la imagen para que no se elimine de la memoria

    def cargar_imagen_usuario(self, usuario_img):
        try:
            # Carga la imagen
            imagen = Image.open(usuario_img)
            # Redimensiona la imagen (opcional)
            imagen = imagen.resize((80, 80), Image.ANTIALIAS)
            # Convierte la imagen para usarla en Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)
            # Muestra la imagen (asumiendo que `foto_label` es tu widget para mostrar la imagen)
            self.foto_label.configure(image=imagen_tk)
            self.foto_label.image = imagen_tk
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")

    def validar_usuario(usuario):
        """
        Valida que el nombre de usuario no contenga obscenidades.
        """
        palabras_prohibidas = ["palabra1", "palabra2", "palabra3"]  # Añade las palabras que desees prohibir

        for palabra in palabras_prohibidas:
            if palabra.lower() in usuario.lower():
                return False
        return True

    @staticmethod
    def validar_contrasena(contrasena):
        """
		Valida que la contraseña cumpla con los siguientes requisitos:
		- Mínimo 8 caracteres
		- Máximo 16 caracteres
		- Al menos una letra mayúscula
		- Al menos una letra minúscula
		- Al menos un número
		- Al menos un carácter especial
		"""
        if (8 <= len(contrasena) <= 16 and
                re.search("[a-z]", contrasena) and
                re.search("[A-Z]", contrasena) and
                re.search("[0-9]", contrasena) and
                re.search("[@#$%^&+=]", contrasena)):
            return True
        return False
    def iniciar(self):
        self.destroy()
        menu.Menu_principal().mainloop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def registro_facial(self):
        try:
                # Vamos a capturar el rostro
            cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
            while (True):
                ret, frame = cap.read()  # Leemos el video
                frame = np.flip(frame, axis=1)
                cv2.imshow(dic.FacialRegistration[dic.language], frame)  # Mostramos el video en pantalla
                if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
                    break
            usuario_img = self.entry_Username.get()
            cv2.imwrite(usuario_img + ".jpg",frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario

            cap.release()  # Cerramos
            cv2.destroyAllWindows()
            tkinter.messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.iniciar()
        except Exception as e:
            print(f"Error en registro facial: {e}")

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

        img = usuario_img + ".jpg"
        pixeles = pyplot.imread(img)
        detector = MTCNN()
        caras = detector.detect_faces(pixeles)
        reg_rostro(img, caras)
        self.iniciar()


