import calendar
import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.filedialog as filedialog
from tkinter import PhotoImage, Button
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
        grey = "#D8D8D8"
        font_style = ('helvic', 20)
        self.imagen_seleccionada = None
        super().__init__()
        ResX = 900
        ResY = 500
        ScreenRes = f"{ResX}x{ResY}"

        self.GuestWindow = customtkinter.CTkToplevel(self)
        self.GuestWindow.geometry(ScreenRes)
        #self.withdraw()
        #self.GuestWindow.withdraw()

        if user.Member == True:
            self.GuestWindow.withdraw()
            self.deiconify()
        else:
            self.GuestWindow.deiconify()
            self.withdraw()

        # configure window
        # self.attributes("-fullscreen", True)
        self.title(dic.Registration[dic.language])
        self.geometry(ScreenRes)

        # create sidebar frame with widgets
        self.tabview = customtkinter.CTkTabview(self, width=ResX, height=ResY, fg_color=grey,
                                                segmented_button_selected_color=green,
                                                segmented_button_selected_hover_color=pink)
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add(dic.Data[dic.language])
        self.tabview.add(dic.Game[dic.language])
        self.tabview.add(dic.Music[dic.language])
        self.tabview.add("Paletas")
        self.tabview.add("texturas")
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


        self.calendario = Calendar(self.tabview.tab(dic.Data[dic.language]),mindate=date(1930,1,1),maxdate=date.today())
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
        self.foto_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.foto = customtkinter.CTkFrame(self.tabview.tab("Juego"), fg_color=grey, corner_radius=100, height=80,width=80)
        self.foto.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.subir_Foto = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), text="✚",
                                                  fg_color=green_light, hover_color=green, corner_radius=80, width=10,
                                                  command=self.abrir_archivo)
        self.subir_Foto.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        # ----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
                                                 text=dic.Personalization[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
                                               text=dic.FavoriteSongs[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        #---------------------------------------------------------------------------------------------
        self.userSpot = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
        self.userSpot.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.SaveuserSpot = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                     text="Save Spotify User",
                                                     fg_color=green_light, hover_color=green,
                                                     command=lambda: spot.UserSpotSelect(self.userSpot.get()))
        self.SaveuserSpot.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)

        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
        self.cancion1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.song_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                        text="Search",
                                                        fg_color=green_light, hover_color=green,
                                                        command=lambda: spot.SelectSong(self.cancion1.get(),0))
        self.song_button_1.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
        self.cancion2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        self.song_button_2 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=lambda: spot.SelectSong(self.cancion2.get(),1))
        self.song_button_2.place(relx=0.75, rely=0.6, anchor=customtkinter.CENTER)

        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
        self.cancion3.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        self.song_button_3 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=lambda: spot.SelectSong(self.cancion3.get(),2))
        self.song_button_3.place(relx=0.75, rely=0.7, anchor=customtkinter.CENTER)

        self.testPlay = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                text="Play text",
                                                fg_color=green_light, hover_color=green,
                                                command=lambda: spot.PlaySong(user.Songs1[0]))
        self.testPlay.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)
        # ---------------------------------------------------------------------------------------------
        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("texturas"),
                                                        text=dic.Continue[dic.language],
                                                        fg_color=green_light, hover_color=green,
                                                        command=self.iniciar)
        self.sidebar_button_1.place(relx=0.25, rely=0.9, anchor=customtkinter.CENTER)
        self.sidebar_button_1.forget()

        self.CheckAll = customtkinter.CTkButton(self.tabview.tab("texturas"),text="Check",fg_color=green_light, hover_color=green,command=self.check)
        self.CheckAll.place(relx=0.75, rely=0.9, anchor=customtkinter.CENTER)
        self.calendario_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
                                                         text="Show/Hide Calendar",
                                                         fg_color=green_light, hover_color=green,
                                                         command=self.toggle_calendar)
        self.calendario_button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
        # ------------------------------------------------------------------------------------------------
      
        paletteRed= PhotoImage(file="assets/Palettes/Red.png").subsample(4, 4)
        paletteWhite = PhotoImage(file="assets/Palettes/White.png").subsample(4, 4)
        paletteGreen = PhotoImage(file="assets/Palettes/Green.png").subsample(4, 4)
        paletteBlack = PhotoImage(file="assets/Palettes/Black.png").subsample(4, 4)
        paletteBlue = PhotoImage(file="assets/Palettes/Blue.png").subsample(4, 4)


        self.buttonRed = customtkinter.CTkButton(self.tabview.tab("Paletas"), text="", image= paletteRed, fg_color= grey, command=lambda: user.selecPalett("RED"),width=100,height=100)
        self.buttonWhite = customtkinter.CTkButton(self.tabview.tab("Paletas"), text="", image = paletteWhite, fg_color= grey, command=lambda: user.selecPalett("WHITE"),width=100,height=100)
        self.buttonGreen = customtkinter.CTkButton(self.tabview.tab("Paletas"), text="",image = paletteGreen, fg_color= grey,command=lambda: user.selecPalett("GREEN"),width=100,height=100)
        self.buttonBlack = customtkinter.CTkButton(self.tabview.tab("Paletas"), text="",image=paletteBlack,fg_color= grey,command=lambda: user.selecPalett("BLACK"),width=100,height=100)
        self.buttonBlue = customtkinter.CTkButton(self.tabview.tab("Paletas"), text="", image = paletteBlue,fg_color= grey,command=lambda: user.selecPalett("BLUE"),width=100,height=100)

        # Coloca los botones en la ventana
        self.buttonRed.place(relx=0.25, rely=0.13)
        self.buttonWhite.place(relx=0.25, rely=0.35)
        self.buttonGreen.place(relx=0.25, rely=0.55)
        self.buttonBlack.place(relx=0.75, rely=0.35)
        self.buttonBlue.place(relx=0.75, rely=0.55)

        # ------------------------------------------------------------------------------------------------



        #-------------------------------------------------------------------------------------------------
        self.GuestWindow.nombre = customtkinter.CTkLabel(self.GuestWindow, text=dic.Name[dic.language],
                                             anchor="w")
        self.GuestWindow.nombre.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

        self.GuestWindow.entry_Nombre = customtkinter.CTkEntry(self.GuestWindow)
        self.GuestWindow.entry_Nombre.place(relx=0.5, rely=0.21, anchor=customtkinter.CENTER)

        self.GuestWindow.apellido = customtkinter.CTkLabel(self.GuestWindow, text=dic.Surname[dic.language],
                                               anchor="w")
        self.GuestWindow.apellido.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)

        self.GuestWindow.entry_Apellido = customtkinter.CTkEntry(self.GuestWindow)
        self.GuestWindow.entry_Apellido.place(relx=0.5, rely=0.33, anchor=customtkinter.CENTER)

        self.GuestWindow.correo = customtkinter.CTkLabel(self.GuestWindow, text=dic.Email[dic.language],
                                             anchor="w")
        self.GuestWindow.correo.place(relx=0.5, rely=0.39, anchor=customtkinter.CENTER)

        self.GuestWindow.entry_Correo = customtkinter.CTkEntry(self.GuestWindow)
        self.GuestWindow.entry_Correo.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

        self.GuestWindow.logo_label = customtkinter.CTkLabel(self.GuestWindow,
                                                             text=dic.Registration[dic.language],
                                                             font=customtkinter.CTkFont(size=20, weight="bold"))
        self.GuestWindow.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)######

        self.GuestWindow.username = customtkinter.CTkLabel(self.GuestWindow,
                                                           text=dic.Username[dic.language], anchor="w")
        self.GuestWindow.username.place(relx=0.5, rely=0.51, anchor=customtkinter.CENTER)
        self.GuestWindow.entry_Username = customtkinter.CTkEntry(self.GuestWindow)
        self.GuestWindow.entry_Username.place(relx=0.5, rely=0.57, anchor=customtkinter.CENTER)

        self.GuestWindow.contra = customtkinter.CTkLabel(self.GuestWindow, text=dic.Password[dic.language],
                                                         anchor="w")
        self.GuestWindow.contra.place(relx=0.5, rely=0.63, anchor=customtkinter.CENTER)

        self.GuestWindow.entry_Contra = customtkinter.CTkEntry(self.GuestWindow, show="◊")
        self.GuestWindow.entry_Contra.place(relx=0.5, rely=0.69, anchor=customtkinter.CENTER)

        self.GuestWindow.edad_label = customtkinter.CTkLabel(self.GuestWindow,
                                                             text=dic.Age[dic.language] + ": 0")
        self.GuestWindow.edad_label.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

        self.GuestWindow.calendario1 = Calendar(self.GuestWindow, mindate=date(1930, 1, 1), maxdate=date.today())
        self.GuestWindow.calendario1.place_forget()

        self.GuestWindow.edad_button1 = customtkinter.CTkButton(self.GuestWindow, text="Confirmar fecha",
                                                   fg_color=green_light,
                                                   hover_color=green,
                                                   command=lambda: [self.DateSelectGuest(), self.toggle_calendarGuest()])
        self.GuestWindow.edad_button1.place(relx=0.5, rely=0.75)
        self.GuestWindow.calendario_button1 = customtkinter.CTkButton( self.GuestWindow,
                                                         text="Show/Hide Calendar",
                                                         fg_color=green_light, hover_color=green,
                                                         command=self.toggle_calendarGuest)
        self.GuestWindow.calendario_button1.place(relx=0.5, rely=0.86, anchor=customtkinter.CENTER)

        self.GuestWindow.CheckGuest = customtkinter.CTkButton(self.GuestWindow,text="Check",fg_color=green_light, hover_color=green,command=self.checkGuest)
        self.GuestWindow.CheckGuest.place(relx=0.75, rely=0.9, anchor=customtkinter.CENTER)


        self.GuestWindow.Continue = customtkinter.CTkButton(self.GuestWindow,
                                                        text=dic.Continue[dic.language],
                                                        fg_color=green_light, hover_color=green,
                                                        command=self.iniciar)
        #self.GuestWindow.Continue.place(relx=0.25, rely=0.9, anchor=customtkinter.CENTER)
        self.GuestWindow.Continue.place_forget()


        self.GuestWindow.back = customtkinter.CTkButton(self.GuestWindow,
                                                        text="←",
                                                        fg_color=green_light, hover_color=green,
                                                        command=self.back,width=30, height=30)
        self.GuestWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)   

        self.GuestWindow.edad_button1.place_forget()



    def DateSelect(self):
        datese = self.calendario.get_date()
        if user.SelectDate(datese):
            self.update_edad_label(user.age)
    
    def DateSelectGuest(self):
        datese = self.GuestWindow.calendario1.get_date()
        if user.SelectDate(datese):
            self.update_edad_label(user.age)

    def toggle_calendar(self):
        if self.calendario.winfo_ismapped():
            self.calendario.place_forget()
            self.edad_button.place_forget()
        else:
            self.calendario.place(relx=0.8, rely=0.7, anchor=customtkinter.CENTER)
            self.edad_button.place(relx=0.5, rely=0.79, anchor=customtkinter.CENTER)

    def toggle_calendarGuest(self):
        if self.GuestWindow.calendario1.winfo_ismapped():
            self.GuestWindow.calendario1.place_forget()
            self.GuestWindow.edad_button1.place_forget()
        else:
            self.GuestWindow.calendario1.place(relx=0.8, rely=0.7, anchor=customtkinter.CENTER)
            self.GuestWindow.edad_button1.place(relx=0.5, rely=0.79, anchor=customtkinter.CENTER)
        


    def update_edad_label(self, value):
        self.edad_label.configure(text=dic.Age[dic.language] + f" :{round(value)}")
        self.GuestWindow.edad_label.configure(text=dic.Age[dic.language] + f" :{round(value)}")

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


    def checkGuest(self):
        NameGet = self.GuestWindow.entry_Nombre.get()
        if not user.FirstNameCheck(NameGet):
            self.GuestWindow.Continue.place_forget()
        SurNameGet =  self.GuestWindow.entry_Apellido.get()
        if not user.LastNameCheck(SurNameGet):
            self.GuestWindow.Continue.place_forget()
        UserGet =  self.GuestWindow.entry_Username.get()
        if not user.UsernameCheck(UserGet):
            self.GuestWindow.Continue.place_forget()
        CorreoGet =  self.GuestWindow.entry_Correo.get()
        if not user.MailCheck(CorreoGet):
            self.GuestWindow.Continue.place_forget()
        PasswordGet =  self.GuestWindow.entry_Contra.get()
        if not user.PasswordCheck(PasswordGet):
            self.GuestWindow.Continue.place_forget()
        else:
            self.GuestWindow.Continue.place(relx=0.25, rely=0.9, anchor=customtkinter.CENTER)


    def check(self):
        NameGet = self.entry_Nombre.get()
        if not user.FirstNameCheck(NameGet):
            print("Nombre no válido")
        SurNameGet = self.entry_Apellido.get()
        if not user.LastNameCheck(SurNameGet):
            print("Apellido no válido")
        UserGet = self.entry_Username.get()
        if not user.UsernameCheck(UserGet):
            print("Usuario no válido")
        CorreoGet = self.entry_Correo.get()
        if not user.MailCheck(CorreoGet):
            print("Correo no válido")
        PasswordGet = self.entry_Contra.get()
        if not user.PasswordCheck(PasswordGet):
            print("Contraseña no válida")
        else:
            self.sidebar_button_1.place(relx=0.25, rely=0.9, anchor=customtkinter.CENTER)

    def iniciar(self):
        self.destroy()
        menu.Menu_principal().mainloop()

    def back(self):
        self.destroy()
        menu.Menu_principal().mainloop()

    
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
        user.picpassword = img
        pixeles = pyplot.imread(img)
        detector = MTCNN()
        caras = detector.detect_faces(pixeles)
        reg_rostro(img, caras)
        self.iniciar()
