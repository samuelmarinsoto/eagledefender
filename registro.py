import calendar
import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk
import language_dictionary as dic
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
import menu
import datauser as user
from tkcalendar import Calendar
from datetime import date
import spot

Userspotify = spot.userSpot


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Registro(customtkinter.CTk):
    print("Member:", dic.Member)

    def __init__(self):
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#000000"
        font_style = ('helvic', 20)
        self.imagen_seleccionada = None
        super().__init__()

        # configure window
        # self.attributes("-fullscreen", True)
        self.title(dic.Registration[dic.language])
        self.geometry(f"{800}x{800}")

        # configure grid layout (4x4)

        # create sidebar frame with widgets

        self.tabview = customtkinter.CTkTabview(self, width=800, height=800, fg_color=grey,
                                                segmented_button_selected_color=green,
                                                segmented_button_selected_hover_color=pink)
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add(dic.Data[dic.language])
        self.tabview.add(dic.Game[dic.language])
        self.tabview.add(dic.Personalization[dic.language])
        self.tabview.add("Texturas")
        self.tabview.tab(dic.Data[dic.language]).grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab(dic.Game[dic.language]).grid_columnconfigure(0, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.nombre = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Name[dic.language],
                                             anchor="w")
        self.nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entry_Nombre = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Nombre.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.apellido = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Surname[dic.language],
                                               anchor="w")
        self.apellido.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Apellido = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Apellido.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.correo = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Email[dic.language],
                                             anchor="w")
        self.correo.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.entry_Correo = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Correo.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


        self.edad_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]),
                                                 text=dic.Age[dic.language] + ": 0")
        self.edad_label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


        self.calendario = Calendar(self,mindate=date(1930,1,1),maxdate=date.today())
        self.calendario.place_forget()

        self.edad_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]), text = "Confirmar fecha",fg_color=green_light,
                                                        hover_color=green, command= lambda: [self.DateSelect(),self.toggle_calendar()])
        self.edad_button.place_forget()
        # -------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
                                               text=dic.Username[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.entry_Username = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]))
        self.entry_Username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Password[dic.language],
                                             anchor="w")
        self.contra.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊")
        self.entry_Contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.foto_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), corner_radius=60,
                                                 text=dic.Photo[dic.language])
        self.foto_label.place(relx=0.25, rely=0.7, anchor=customtkinter.CENTER)
        self.camera_icon = ImageTk.PhotoImage(file="camera_icon.png")  # Cargar el ícono
        self.camera_button = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), image=self.camera_icon,
                                                    corner_radius=0,
                                                    width=0, border_width=0,
                                                    text="", command=self.registro_facial)

        self.camera_button.place(relx=0.75, rely=0.9, anchor=customtkinter.CENTER)

        # self.foto = customtkinter.CTkFrame(self.tabview.tab("Juego"), fg_color=grey, corner_radius=100, height=80,width=80)
        # self.foto.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.subir_Foto = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), text="✚",
                                                  fg_color=green_light, hover_color=green, corner_radius=80, width=10,
                                                  command=self.abrir_archivo)
        self.subir_Foto.place(relx=0.25, rely=0.9, anchor=customtkinter.CENTER)

        # ----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]),
                                               text=dic.Theme[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.tabview.tab(dic.Personalization[dic.language]),
            values=[dic.Red[dic.language], dic.Black[dic.language], dic.Blue[dic.language], dic.White[dic.language],
                    dic.Green[dic.language]], fg_color=green_light, button_color=green)
        self.appearance_mode_optionemenu.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]),
                                               text=dic.FavoriteSongs[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        #---------------------------------------------------------------------------------------------
        self.userSpot = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.userSpot.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.SaveuserSpot = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
                                                     text="Save Spotify User",
                                                     fg_color=green_light, hover_color=green,
                                                     command=self.UserSpotSelect)
        self.SaveuserSpot.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)

        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.song_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
                                                        text="Search",
                                                        fg_color=green_light, hover_color=green,
                                                        command=self.SongSelect1)
        self.song_button_1.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        self.song_button_2 = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=self.SongSelect2)
        self.song_button_2.place(relx=0.75, rely=0.6, anchor=customtkinter.CENTER)

        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion3.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        self.song_button_3 = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=self.SongSelect3)
        self.song_button_3.place(relx=0.75, rely=0.7, anchor=customtkinter.CENTER)
        # ---------------------------------------------------------------------------------------------
        # self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
        #                                                 text=dic.Register[dic.language],
        #                                                 fg_color=green_light, hover_color=green,
        #                                                 command=self.registro_facial)
        # self.sidebar_button_1.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.calendario_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
                                                         text="Show/Hide Calendar",
                                                         fg_color=green_light, hover_color=green,
                                                         command=self.toggle_calendar)
        self.calendario_button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.testPlay = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]),
                                                text="Play text",
                                                fg_color=green_light, hover_color=green,
                                                command=self.PlayTEst)
        self.testPlay.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)
    def UserSpotSelect(self):
        User = self.userSpot.get()
        spot.userSpot = User
        print(spot.userSpot)
    def SongSelect1(self):
        SongGet = self.cancion1.get()
        print("Here:",SongGet)
        if SongGet == "":
            return 0
        spot.SearchSong(SongGet)
        user.Songs1[0] = spot.Song1
        print(user.Songs1)

    def SongSelect2(self):
        SongGet = self.cancion2.get()
        if SongGet == "":
            return 0
        spot.SearchSong(SongGet)
        user.Songs1[1] = spot.Song1
        print(user.Songs1)
    def SongSelect3(self):
        SongGet = self.cancion3.get()
        if SongGet == "":
            return 0
        spot.SearchSong(SongGet)
        user.Songs1[2] = spot.Song1
        print(user.Songs1)


    def PlayTEst(self):
        spot.PlaySong(user.Songs1[0])
    def DateSelect(self):
        datese = self.calendario.get_date()
        date_part = datese.split("/")
        month = int(date_part[0])
        day = int(date_part[1])
        if 0 <= int(date_part[2]) <= 23:
            year = int("20"+date_part[2])
        elif 30<= int(date_part[2]) <= 99:
            year = int("19" + date_part[2])
        dateborn = date(year, month, day)
        age = date.today().year-dateborn.year
        user.age = age
        self.update_edad_label(age)


    def update_edad_label(self, value):
        self.edad_label.configure(text=dic.Age[dic.language] + f" :{round(value)}")

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])
        if archivo:
            user.picture = archivo
            print(archivo)
            # Cargar la imagen
            imagen = Image.open(archivo)
            # Redimensionar la imagen según el tamaño deseado (ajusta según tus necesidades)
            imagen.thumbnail((80, 80))
            # Convertir la imagen en un formato compatible con Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)
            # Mostrar la imagen en el CTkLabel
            self.foto_label.configure(image=imagen_tk)
            self.foto_label.configure(text="")
            self.foto_label.image = imagen_tk  # ¡Importante! Debes mantener una referencia a la imagen para que no se elimine de la memoria

    def iniciar(self):
        self.destroy()
        menu.Menu_principal().mainloop()

    def toggle_calendar(self):
        if self.calendario.winfo_ismapped():
            self.calendario.place_forget()
            self.edad_button.place_forget()
        else:
            self.calendario.place(relx=0.8, rely=0.7, anchor=customtkinter.CENTER)
            self.edad_button.place(relx=0.5, rely=0.79, anchor=customtkinter.CENTER)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def registro_facial(self):

        # Vamos a capturar el rostro
        cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
        while (True):
            ret, frame = cap.read()  # Leemos el video
            frame = np.flip(frame, axis=1)
            cv2.imshow(dic.FacialRegistration[dic.language], frame)  # Mostramos el video en pantalla
            if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
                break
        usuario_img = self.entry_Username.get()
        cv2.imwrite(usuario_img + ".jpg",
                    frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
        cap.release()  # Cerramos
        cv2.destroyAllWindows()

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
        # self.iniciar()
