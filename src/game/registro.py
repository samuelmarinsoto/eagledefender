import spotipy
import spotipy.util as util
import src.database.datauser as user
from PIL import Image, ImageTk
import  logGUI.menu as menu


SPOTIPY_CLIENT_ID = '5b219ea7c93c475db3fa7acd846af046'
SPOTIPY_CLIENT_SECRET = '372adbb3af4d4a03a935d894cd5f2af5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

userSpot = ""
scope = 'user-library-read user-modify-playback-state'

token = util.prompt_for_user_token(userSpot, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth=token)

Song1 = ""


def SearchSong(Song):
	global Song1
	result = sp.search(q=Song, type='track', limit=1)
	if not isinstance(Song, str):
		return 0
	elif result['tracks']['items']:
		Song1 = result['tracks']['items'][0]['uri']
		return 1
	else:
		print("Song not found! {song_name}")
		return 0


def SelectSong(Song, Space):
	if SearchSong(Song):
		user.Songs1[Space] = Song1
		return 1
	else:
		return 0


def PlaySong(track_uri):
	sp.start_playback(uris=[track_uri])


def UserSpotSelect(UserSpot):
	global userSpot
	userSpot = UserSpot
	print(userSpot)


import calendar
import tkinter
import tkinter.messagebox
from tkinter import simpledialog

import customtkinter
import tkinter.filedialog as filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk
import src.auxiliar.language_dictionary as dic
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
import src.logGUI.menu as menu
from tkcalendar import Calendar
from datetime import date
import src.auxiliar.spot as spot
import src.database.DataBaseLocal as DataBase
import re
from PIL import Image, ImageDraw
Userspotify = spot.userSpot


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"



class Registro(customtkinter.CTk):
    def __init__(self):
        green = "#E49393"
        green_light = "Green"
        pink = "PINK"
        grey = "#000000"
        font_style = ('consolas', 20)
        self.imagen_seleccionada = None
        super().__init__()

        # Crear un CTkLabel para contener la imagen de fondo
        # Crear un CTkLabel para contener la imagen de fondo


        # configure window
        # self.attributes("-fullscreen", True)
        self.title(dic.Registration[dic.language])
        self.geometry(f"{1024}x{1024}")
        self.selected_photo_path = "assets/flags/Avatar-Profile.png"
        self.background_label = customtkinter.CTkLabel(self, width=1024, height=1024, text=None, bg_color="WHITE")
        # Establecer la imagen de fondo al CTkLabel
        self.background_image = ImageTk.PhotoImage(Image.open("assets/BackGround/pattern.png"))
        self.background_label.configure(image=self.background_image)
        self.background_label.image = self.background_image  # mantener una referencia a la imagen
        self.background_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        # configure grid layout (4x4)

        self.tabview = customtkinter.CTkTabview(self.background_label, width=500, height=600)
        # Asegúrate de mantener una referencia a la imagen para evitar que sea recolectada por el recolector de basura de Python
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add(dic.Data[dic.language])
        self.tabview.add(dic.Game[dic.language])
        self.tabview.add(dic.Music[dic.language])
        self.tabview.add(dic.Members[dic.language])
        self.tabview.add(dic.Palettes[dic.language])
        self.tabview.add(dic.Texture[dic.language])
        self.tabview.tab(dic.Data[dic.language]).grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab(dic.Game[dic.language]).grid_columnconfigure(0, weight=1)
        self.tabview.tab(dic.Data[dic.language]).configure(bg_color="transparent", fg_color="transparent")
        self.tabview.tab(dic.Music[dic.language]).configure(bg_color="transparent", fg_color="transparent")
        self.tabview.tab(dic.Game[dic.language]).configure(bg_color="transparent", fg_color="transparent")
        self.tabview.tab(dic.Members[dic.language]).configure( bg_color="transparent", fg_color="transparent")
        self.tabview.tab(dic.Palettes[dic.language]).configure(bg_color= "transparent", fg_color="transparent")
        self.tabview.tab(dic.Texture[dic.language]).configure(bg_color="transparent", fg_color="transparent")

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        # self.nombre = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Name[dic.language],
        #                                      anchor="w")
        # self.nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entry_Nombre = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]), placeholder_text=dic.Name[dic.language])
        self.entry_Nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        # self.apellido = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Surname[dic.language],
        #                                        anchor="w")
        # self.apellido.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.entry_Apellido = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]), placeholder_text=dic.Surname[dic.language])
        self.entry_Apellido.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)

        # self.correo = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Email[dic.language],
        #                                      anchor="w")
        # self.correo.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Correo = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]), placeholder_text=dic.Email[dic.language])
        self.entry_Correo.place(relx=0.5, rely=0.34, anchor=customtkinter.CENTER)

        self.edad_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]),
                                                 text=dic.Age[dic.language] + ": 0")
        self.edad_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.calendario = Calendar(self, mindate=date(1930, 1, 1), maxdate=date.today())
        self.calendario.place_forget()

        self.edad_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]), text="Confirmar fecha",
                                                   fg_color=green_light,
                                                   hover_color=green,
                                                   command=lambda: [self.DateSelect(), self.toggle_calendar()])
        self.edad_button.place_forget()
        self.calendario_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
                                                         text="Whats your birthday?",
                                                         fg_color=green_light, hover_color=green,
                                                         command=self.toggle_calendar)
        self.calendario_button.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        # -------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        # self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
        #                                        text=dic.Username[dic.language], anchor="w")
        # self.username.place(relx=0.5, rely=0.32, anchor=customtkinter.CENTER)
        self.entry_Username = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), placeholder_text=dic.Username[dic.language])
        self.entry_Username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        # self.contra = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Password[dic.language],
        #                                      anchor="w")
        # self.contra.place(relx=0.5, rely=0.42, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊", placeholder_text=dic.Password[dic.language])
        self.entry_Contra.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)
        # self.contra_check = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
        #                                            text="Verificar " + dic.Password[dic.language], anchor="w")
        # self.contra_check.place(relx=0.5, rely=0.52, anchor=customtkinter.CENTER)

        self.entry_Contra_check = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊", placeholder_text=dic.VerifyPassword[dic.language])
        self.entry_Contra_check.place(relx=0.5, rely=0.34, anchor=customtkinter.CENTER)

        # self.foto = customtkinter.CTkFrame(self.tabview.tab("Juego"), fg_color=grey, corner_radius=100, height=80,width=80)
        # self.foto.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


        #
        # # Foto label
        # self.foto_label = customtkinter.CTkLabel(
        #     self.tabview.tab(dic.Game[dic.language]),
        #     corner_radius=60,
        #     text=dic.Photo[dic.language],
        #     bg_color="transparent",  # Fondo transparente
        #     fg_color="transparent"  # Texto transparente
        # )
        # self.foto_label.place(relx=0.45, rely=0.23, anchor=customtkinter.CENTER)
        #
        # # Facial label
        # self.facial_label = customtkinter.CTkLabel(
        #     self.tabview.tab(dic.Game[dic.language]),
        #     corner_radius=60,
        #     text=dic.Facial[dic.language],
        #     bg_color="transparent",  # Fondo transparente
        #     fg_color="transparent"  # Texto transparente
        # )
        # self.facial_label.place(relx=0.55, rely=0.23, anchor=customtkinter.CENTER)
        self.selected_photo_path = "assets/flags/Avatar-Profile.png"
        self.selected_picpassword = ""
        #default_image_path = "assets/flags/Avatar-Profile.png"
        default_image = Image.open(self.selected_photo_path)
        default_image = default_image.resize((100, 100), Image.ANTIALIAS)
        default_imageop = ImageTk.PhotoImage(default_image)



        self.avatar_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),image=default_imageop,corner_radius=60,text="")
        self.avatar_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)



        #self.display_avatar_in_circle(default_image_path, self.tabview.tab(dic.Game[dic.language]), 0.5, 0.19)
        # Botón para subir foto
        self.subir_Foto = customtkinter.CTkButton(
            self.tabview.tab(dic.Game[dic.language]),
            text="✚",
            hover = True,
            fg_color=green_light,
            hover_color=green,
            corner_radius=50,
            height=10,
            width=10,
            bg_color="transparent",  # Fondo transparente
            command=self.abrir_archivo
        )
        self.subir_Foto.place(relx=0.43, rely=0.65, anchor=customtkinter.CENTER)

        # Botón de cámara
        self.camera_icon = ImageTk.PhotoImage(file="camera_icon.png")  # Cargar el ícono
        self.camera_button = customtkinter.CTkButton(
            self.tabview.tab(dic.Game[dic.language]),
            image=self.camera_icon,
            corner_radius=0,
            width=0,
            border_width=0,
            text="",
            bg_color="transparent",  # Fondo transparente
            fg_color="transparent", # Fondo transparente
            command=self.registro_facial
        )
        self.camera_button.place(relx=0.57, rely=0.65, anchor=customtkinter.CENTER)

        # ----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
                                               text=dic.FavoriteSongs[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        # ---------------------------------------------------------------------------------------------
        # self.SaveuserSpot = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
        #                                             text="Save Spotify User",
        #                                             fg_color=green_light, hover_color=green,
        #                                             command=self.UserSpotSelect)
        # self.SaveuserSpot.place(relx=0.8, rely=0.2, anchor=customtkinter.CENTER)




        self.userSpot = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Spotify User")
        self.userSpot.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Song 1")
        self.cancion1.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)


        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Song 2")
        self.cancion2.place(relx=0.5, rely=0.34, anchor=customtkinter.CENTER)


        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Song 3")
        self.cancion3.place(relx=0.5, rely=0.41, anchor=customtkinter.CENTER)

        # ---------------------------------------------------------------------------------------------
        self.register_button_data = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
                                                            text=dic.Register[dic.language],
                                                            fg_color=green_light, hover_color=green,
                                                            command=self.on_register_button_click)
        self.register_button_data.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.register_button_game = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]),
                                                            text=dic.Register[dic.language],
                                                            fg_color=green_light, hover_color=green,
                                                            command=self.on_register_button_click)
        self.register_button_game.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.register_button_music = customtkinter.CTkButton(
            self.tabview.tab(dic.Music[dic.language]),
            text=dic.Register[dic.language],
            fg_color=green_light, hover_color=green,
            command=self.on_register_button_click)
        self.register_button_music.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)



        # self.testPlay = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
        #                                         text="Play text",
        #                                         fg_color=green_light, hover_color=green,
        #                                         command=self.PlayTEst)
        # self.testPlay.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

        # --------------------------------------------------------------------------------------------------------------------------------
        # ...
        # Dentro de la clase Registro, y luego de tus otros elementos...
        # --------------------------------------------------------------------------------------------------------------------------------
        """Aquí va la inserción de la tarjeta"""

        self.card_title_label = customtkinter.CTkLabel(self.tabview.tab(dic.Members[dic.language]),
                                                       text="Información de Tarjeta",
                                                       font=customtkinter.CTkFont(size=16, weight="bold"))
        self.card_title_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        # Agregar un CTkLabel para mostrar el icono de la tarjeta
        self.card_icon_label = customtkinter.CTkLabel(self.tabview.tab(dic.Members[dic.language]), text="", width=50,
                                                      height=50)
        self.card_icon_label.place(relx=0.3, rely=0.2, anchor=customtkinter.CENTER)

        # Modifica el método de creación de la entrada de número de tarjeta para agregar un trace
        self.card_number_var = tkinter.StringVar()
        self.card_number_var.trace("w", self.update_card_icon)


        self.card_number_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                                        placeholder_text="Número de Tarjeta")
        self.card_number_entry.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        self.switchVarMembresia = customtkinter.StringVar(value="on")
        print(self.switchVarMembresia.get())
        self.switchMembresia = customtkinter.CTkSwitch(
            self.tabview.tab(dic.Members[dic.language]), text=None,
            variable=self.switchVarMembresia, onvalue="on", offvalue="off",
            fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
            progress_color="Green",  command=self.update_submit_button_state)

        self.switchMembresia.place(relx=0.555, rely=0.18, anchor=customtkinter.CENTER)


        self.card_expiry_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                                        placeholder_text="MM/AA")
        self.card_expiry_entry.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

        self.card_cvc_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                                     placeholder_text="CVC")
        self.card_cvc_entry.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
        # Agrega un rastreo al switch de membresía para llamar a la función cuando cambie




        self.switchVarMembresia.trace("w", lambda *args: self.toggle_tabs_access())


        # self.card_number_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
        #                                                 placeholder_text="Número de Tarjeta")
        # self.card_number_entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.card_submit_button = customtkinter.CTkButton(self.tabview.tab(dic.Members[dic.language]),
                                                          text="Confirmar",
                                                          fg_color=green_light, hover_color=green,
                                                          command=self.on_register_button_click)
        self.card_submit_button.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.update_submit_button_state()

        # --------------------------------------------------------------------------------------------------------------------------------
        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Palettes[dic.language]),
                                                 text="Selección paleta de colores",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        paletteRed = PhotoImage(file="assets/Palettes/Red.png").subsample(5,5)
        paletteWhite = PhotoImage(file="assets/Palettes/White.png").subsample(5, 5)
        paletteGreen = PhotoImage(file="assets/Palettes/Green.png").subsample(5, 5)
        paletteBlack = PhotoImage(file="assets/Palettes/Black.png").subsample(5, 5)
        paletteBlue = PhotoImage(file="assets/Palettes/Blue.png").subsample(5, 5)

        self.buttonRed = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                 image=paletteRed, fg_color="#2B2B2B",
                                                 command=lambda: user.selecPalett("RED"), width=70, height=70, state="disabled")

        self.buttonWhite = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                   image=paletteWhite,
                                                   fg_color="#2B2B2B", command=lambda: user.selecPalett("WHITE"), width=70,
                                                   height=70, state="disabled")
        self.buttonGreen = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                   image=paletteGreen,
                                                   fg_color="#2B2B2B", command=lambda: user.selecPalett("GREEN"), width=70,
                                                   height=70,   state="disabled")
        self.buttonBlack = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                   image=paletteBlack,
                                                   fg_color="#2B2B2B", command=lambda: user.selecPalett("BLACK"), width=70,
                                                   height=70,  state="disabled")
        self.buttonBlue = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                  image=paletteBlue,
                                                  fg_color="#2B2B2B", command=lambda: user.selecPalett("BLUE"), width=40,
                                                  height=40, state="disabled")

        # Coloca los botones en la ventana
        self.buttonRed.place(relx=0.01, rely=0.2)
        self.buttonWhite.place(relx=0.2, rely=0.2)
        self.buttonGreen.place(relx=0.40, rely=0.2)
        self.buttonBlack.place(relx=0.60, rely=0.2)
        self.buttonBlue.place(relx=0.80, rely=0.2)

        self.switchVarRed = customtkinter.StringVar(value="off")
        self.switchRed = customtkinter.CTkSwitch(self.tabview.tab(dic.Palettes[dic.language]), text=None, command=None,
                                              variable=self.switchVarRed, onvalue="on", offvalue="off", fg_color="Red",
                                              button_color="#AFAFAF", button_hover_color="WHite", progress_color="Green")
        self.switchRed.place(relx=0.08, rely=0.4)
        self.switchVarWhite = customtkinter.StringVar(value="off")
        self.switchWhite = customtkinter.CTkSwitch(self.tabview.tab(dic.Palettes[dic.language]), text=None, command=None,
                                                variable=self.switchVarWhite, onvalue="on", offvalue="off",
                                                fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                progress_color="Green")
        self.switchWhite.place(relx=0.25, rely=0.4)
        self.switchVarGreen = customtkinter.StringVar(value="off")
        self.switchGreen = customtkinter.CTkSwitch(self.tabview.tab(dic.Palettes[dic.language]), text=None, command=None,
                                                variable=self.switchVarGreen, onvalue="on", offvalue="off",
                                                fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                progress_color="Green")
        self.switchGreen.place(relx=0.450, rely=0.4)
        self.switchVarBlack = customtkinter.StringVar(value="off")
        self.switchBlack = customtkinter.CTkSwitch(self.tabview.tab(dic.Palettes[dic.language]), text=None, command=None,
                                                variable=self.switchVarBlack, onvalue="on", offvalue="off",
                                                fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                progress_color="Green")
        self.switchBlack.place(relx=0.650, rely=0.4)
        self.switchVarBlue = customtkinter.StringVar(value="off")
        self.switchBlue = customtkinter.CTkSwitch(self.tabview.tab(dic.Palettes[dic.language]), text=None, command=None,
                                                  variable=self.switchVarBlue, onvalue="on", offvalue="off",
                                                    fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                    progress_color="Green")
        self.switchBlue.place(relx=0.85, rely=0.4)
        self.card_submit_button = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]),
                                                          text="Confirmar",
                                                          fg_color=green_light, hover_color=green,
                                                          command=self.on_register_button_click)
        self.card_submit_button.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.update_submit_button_state()
        # --------------------------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------------------
        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]),
                                                 text="Selección textura",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        block1Metal= PhotoImage(file="assets/Blocks/bloquemetal.png").subsample(7, 7)
        block1Wood = PhotoImage(file="assets/Blocks/bloquemadera.png").subsample(6, 6)
        block1Cement = PhotoImage(file="assets/Blocks/bloqueconcreto.png").subsample(6, 6)

        block2Metal = PhotoImage(file="assets/Blocks/Block2Metal.png").subsample(3, 3)
        block2Wood = PhotoImage(file="assets/Blocks/Block2Wood.png").subsample(3, 3)
        block2Cement = PhotoImage(file="assets/Blocks/Block2Cement.png").subsample(3, 3)

        block3Metal = PhotoImage(file="assets/Blocks/Block3Metal.png").subsample(1, 1)
        block3Wood = PhotoImage(file="assets/Blocks/Block3Wood.png").subsample(1, 1)
        block3Cement = PhotoImage(file="assets/Blocks/Block3Cement.png").subsample(1, 1)

        self.BlockMetal1 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]),image=block1Metal,text="")
        self.BlockWood1 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block1Wood, text="")
        self.BlockCement1 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block1Cement,text="")
        self.BlockMetal1.place(relx=0.2, rely=0.2)
        self.BlockWood1.place(relx=0.35, rely=0.2)
        self.BlockCement1.place(relx=0.5, rely=0.2)

        self.BlockMetal2 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block2Metal, text="")
        self.BlockWood2 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block2Wood, text="")
        self.BlockCement2 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block2Cement, text="")
        self.BlockMetal2.place(relx=0.2, rely=0.37)
        self.BlockWood2.place(relx=0.35, rely=0.37)
        self.BlockCement2.place(relx=0.5, rely=0.37)

        self.BlockMetal3 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block3Metal,                                 text="")
        self.BlockWood3 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block3Wood, text="")
        self.BlockCement3 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block3Cement,                                          text="")
        self.BlockMetal3.place(relx=0.2, rely=0.53)
        self.BlockWood3.place(relx=0.35, rely=0.53)
        self.BlockCement3.place(relx=0.5, rely=0.53)
        self.switchVarPack1 = customtkinter.StringVar(value="off")
        self.switchPack1 = customtkinter.CTkSwitch(self.tabview.tab(dic.Texture[dic.language]), text=None, command=None,
                                                  variable=self.switchVarPack1, onvalue="on", offvalue="off",
                                                  fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                  progress_color="Green")
        self.switchPack1.place(relx=0.65, rely=0.25)
        self.switchVarPack2 = customtkinter.StringVar(value="off")
        self.switchPack2 = customtkinter.CTkSwitch(self.tabview.tab(dic.Texture[dic.language]), text=None, command=None,
                                                    variable=self.switchVarPack2, onvalue="on", offvalue="off",
                                                    fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                    progress_color="Green")
        self.switchPack2.place(relx=0.65, rely=0.4)
        self.switchVarPack3 = customtkinter.StringVar(value="off")
        self.switchPack3 = customtkinter.CTkSwitch(self.tabview.tab(dic.Texture[dic.language]), text=None, command=None,
                                                    variable=self.switchVarPack3, onvalue="on", offvalue="off",
                                                    fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                    progress_color="Green")
        self.switchPack3.place(relx=0.65, rely=0.55)
        self.card_submit_button = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]),
                                                          text="Confirmar",
                                                          fg_color=green_light, hover_color=green,
                                                          command=self.on_register_button_click)
        self.card_submit_button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
        self.update_submit_button_state()
        # paletteBlack = PhotoImage(file="assets/Palettes/Black.png").subsample(4, 4)
        # paletteBlue = PhotoImage(file="assets/Palettes/Blue.png").subsample(4, 4)
        #
        # self.buttonRed = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="Option 1",
        #                                          fg_color=grey,
        #                                          command=lambda: user.selectTexture("OP1"), width=100, height=100)
        # self.buttonWhite = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="Option 2",
        #
        #                                            fg_color=grey, command=lambda: user.selectTexture("OP2"), width=100,
        #                                            height=100)
        # self.buttonGreen = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="Option 3",
        #                                            fg_color=grey, command=lambda: user.selectTexture("OP3"), width=100,
        #                                            height=100)
#---------------------------------------------------------------------------------------------------------------------------------
        def on_switch_palette_active(switchVar):
            if switchVar.get() == "on":
                switches = [self.switchVarRed, self.switchVarWhite, self.switchVarGreen, self.switchVarBlack,
                            self.switchVarBlue]
                for s in switches:
                    if s != switchVar:
                        s.set("off")

        def on_switch_texture_active(switchVar):
            if switchVar.get() == "on":
                switches = [self.switchVarPack1, self.switchVarPack2, self.switchVarPack3]
                for s in switches:
                    if s != switchVar:
                        s.set("off")



        # Enlazar la función a los eventos de activación de los Switch de palettes
        self.switchVarRed.trace("w", lambda *args: on_switch_palette_active(self.switchVarRed))
        self.switchVarWhite.trace("w", lambda *args: on_switch_palette_active(self.switchVarWhite))
        self.switchVarGreen.trace("w", lambda *args: on_switch_palette_active(self.switchVarGreen))
        self.switchVarBlack.trace("w", lambda *args: on_switch_palette_active(self.switchVarBlack))
        self.switchVarBlue.trace("w", lambda *args: on_switch_palette_active(self.switchVarBlue))

        # Enlazar la función a los eventos de activación de los Switch de texture
        self.switchVarPack1.trace("w", lambda *args: on_switch_texture_active(self.switchVarPack1))
        self.switchVarPack2.trace("w", lambda *args: on_switch_texture_active(self.switchVarPack2))
        self.switchVarPack3.trace("w", lambda *args: on_switch_texture_active(self.switchVarPack3))

        # 3. Deshabilitar todos los Switch si el usuario no es miembro.
        if self.switchVarMembresia == "off":
            self.switchRed.configure(state="disabled")
            self.switchWhite.configure(state="disabled")
            self.switchGreen.configure(state="disabled")
            self.switchBlack.configure(state="disabled")
            self.switchBlue.configure(state="disabled")
            self.switchPack1.configure(state="disabled")
            self.switchPack2.configure(state="disabled")
            self.switchPack3.configure(state="disabled")

    def update_submit_button_state(self):
        if self.switchVarMembresia.get() == "off":
            self.card_submit_button.configure(state="disabled")
        else:
            self.card_submit_button.configure(state="normal")
        self.toggle_tabs_access()

    #---------------------------------------------------------------------------------------------------------------------------------
        # # Coloca los botones en la ventana
        # self.buttonRed.place(relx=0.5, rely=0.10)
        # self.buttonWhite.place(relx=0.5, rely=0.25)
        # self.buttonGreen.place(relx=0.5, rely=0.40)

    # self.buttonBlack.place(relx=0.5, rely=0.55)
    # self.buttonBlue.place(relx=0.5, rely=0.70)


    def update_card_icon(self, *args):
        card_number = self.card_number_var.get()

        if card_number.startswith("4"):
            original_image = Image.open("assets/cards/visa.png")
        elif card_number.startswith("5"):
            original_image = Image.open("assets/cards/mastercard.png")
        elif card_number.startswith("34") or card_number.startswith("37"):
            original_image = Image.open("assets/cards/amex.png")
        else:
            self.card_icon_label.configure(image=None)  # quitar imagen si el número no coincide
            return

        # Cambia el tamaño de la imagen
        resized_image = original_image.resize((50, 50), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(resized_image)

        self.card_icon_label.configure(image=card_image)
        self.card_icon_label.image = card_image  # mantener referencia a la imagen

    def toggle_tabs_access(self):
        if self.switchVarMembresia.get() == "off":
            # Desactiva los widgets en las pestañas excepto el switch de membresía
            for widget in self.tabview.tab(dic.Members[dic.language]).winfo_children():
                if widget != self.switchMembresia:
                    widget.configure(state="disabled")
            for widget in self.tabview.tab(dic.Palettes[dic.language]).winfo_children():
                widget.configure(state="disabled")
            for widget in self.tabview.tab(dic.Texture[dic.language]).winfo_children():
                widget.configure(state="disabled")
        else:
            # Activa todos los widgets en las pestañas
            for widget in self.tabview.tab(dic.Members[dic.language]).winfo_children():
                widget.configure(state="normal")
            for widget in self.tabview.tab(dic.Palettes[dic.language]).winfo_children():
                widget.configure(state="normal")
            for widget in self.tabview.tab(dic.Texture[dic.language]).winfo_children():
                widget.configure(state="normal")
    def disable_widgets_except_switch(self, tab_name, switch_variable):
        # Obtiene la lista de widgets en la pestaña especificada
        tab_widgets = self.tabview.tab(tab_name).winfo_children()

        # Desactiva todos los widgets excepto el switch
        for widget in tab_widgets:
            if widget != switch_variable:
                widget.configure(state="disabled")

    def enable_all_widgets(self, tab_name):
        # Activa todos los widgets en la pestaña especificada
        tab_widgets = self.tabview.tab(tab_name).winfo_children()
        for widget in tab_widgets:
            widget.configure(state="normal")
    def iniciar(self):
        self.destroy()
        menu.Menu_principal().mainloop()

    def toggle_calendar(self):
        if self.calendario.winfo_ismapped():
            self.calendario.place_forget()
            self.edad_button.place_forget()
        else:
            self.calendario.place(relx=0.8, rely=0.7, anchor=customtkinter.CENTER)
            self.edad_button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

    def UserSpotSelect(self):
        User = self.userSpot.get()
        spot.userSpot = User
        print(spot.userSpot)

    def SongSelect1(self):
        SongGet = self.cancion1.get()
        print("Here:", SongGet)
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


    def VerifyTexture(self):
        TextureOp = ["OP1","OP2","OP3"]
        if isinstance(user.Texture,str):
            if user.Texture in TextureOp:
                return 1
            else:
                return 0
        else:
            return 0

    def VerifyPalette(self):
        PaletteOp = ["RED","GREEN","BLACK","BLUE","WHITE"]
        if isinstance(user.Palette,str):
            if user.Palette in PaletteOp:
                return 1
            else:
                return 0
        else:
            return 0
    def VerifySongs(self):
        try:
            for song in user.Songs1:
                if song == "":
                    raise ValueError("Una canción está vacía")
        except ValueError as e:
            print(f"Error: {e}")
            return 0

        try:
            for song in user.Songs1:
                result = spot.VerifySong(song)
                if not result:
                    raise ValueError(f"Fallo la verificación de la canción: {song}")
        except ValueError as e:
            print(f"Error: {e}")
            return 0
        return 1

    def PlayTEst(self):
        spot.PlaySong(user.Songs1[0])


    #def VerifyTexture(self):

    def DateSelect(self):
        datese = self.calendario.get_date()
        date_part = datese.split("/")
        month = int(date_part[0])
        day = int(date_part[1])
        if 0 <= int(date_part[2]) <= 23:
            year = int("20" + date_part[2])
        elif 30 <= int(date_part[2]) <= 99:
            year = int("19" + date_part[2])
        dateborn = date(year, month, day)
        self.age = date.today().year - dateborn.year  # Guarda la edad en una variable de instancia
        print(self.age)
        if self.age < 13:  # Comprobación de edad
            tkinter.messagebox.showerror("Error", "Debes tener al menos 13 años para registrarte.")
            return
        self.update_edad_label(self.age)
    def validar_usuario(usuario):
        """
        Valida que el nombre de usuario no contenga obscenidades.
        """
        palabras_prohibidas = ["palabra1", "palabra2", "palabra3"]  # Añade las palabras que desees prohibir
        for palabra in palabras_prohibidas:
            if palabra.lower() in usuario.lower():
                return False
        return True

    def verificar_contrasenas(self):
        if self.entry_Contra.get() == self.entry_Contra_check.get():
            return self.entry_Contra_check.get()

    def check_verification_code(self, user_input_code):
        if user_input_code == self.temp_verification_code:
            # El código es correcto, procede con el registro
            self.registrar_usuario()
            self.temp_verification_code = None
            self.destroy()
            



        else:
            # El código es incorrecto, muestra un mensaje de error
            tkinter.messagebox.showerror("Error", "Código de verificación incorrecto.")

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
                re.search("[@#$%^&+=.,!/*()-<>]", contrasena)):
            return True
        return False

    def registrar_usuario(self):
        # Recoge la información del usuario desde la GUI
        usuario = self.entry_Username.get()
        contra = self.verificar_contrasenas()
        if contra is None:
            tkinter.messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        nombre = self.entry_Nombre.get()
        apellido = self.entry_Apellido.get()
        correo = self.entry_Correo.get()
        edad = self.age  # Accede a la edad desde la variable de instancia
        membresia = self.switchVarMembresia.get()
        spotify_user1 = self.userSpot.get()
        song1 = self.cancion1.get()
        song2 = self.cancion2.get()
        song3 = self.cancion3.get()
        card = self.card_number_entry.get()
        expiration = self.card_expiry_entry.get()
        cvc = self.card_cvc_entry.get()
        paleta = self.get_active_palettes()
        textura = self.get_active_textures()
        # cancion = self.cancion1.get()
        usuario_img = self.entry_Username.get()
        imagen_ruta = 'ProfilePics/' + usuario_img + ".jpg"  # Ruta de la imagen guardada

        edad = self.age  # Accede a la edad desde la variable de instancia

        if edad < 13:
            tkinter.messagebox.showerror("Error", "El usuario debe tener al menos 13 años para registrarse.")
            return

        if DataBase.is_username_registered(usuario):
            tkinter.messagebox.showerror("Error", "Este nombre de usuario ya está registrado.")
            return

        if DataBase.is_email_registered(correo):
            tkinter.messagebox.showerror("Error", "Este correo ya está registrado.")
            return
        if self.switchVarMembresia.get() == "on":
            # Llama a la función para insertar los datos en la base de datos
            try:
                DataBase.insert_user(usuario, contra, nombre, apellido, correo, edad, imagen_ruta, "Yes",
                                     spotify_user1, song1, song2, song3, card, expiration, cvc)
                print(DataBase.insert_user(usuario, contra, nombre, apellido, correo, edad, imagen_ruta, "Yes",
                                     spotify_user1, song1, song2, song3, card, expiration, cvc))

                DataBase.insert_personalization_option(usuario, paleta, textura)
                print(DataBase.insert_personalization_option(usuario, paleta, textura))
                tkinter.messagebox.showinfo(title="Registro", message="El usuario GOLD se ha registrado exitosamente.")

            # Nota: No mostramos el mensaje de éxito aquí.
            except Exception as e:
                print("Error", f"Ocurrió un error al registrar al usuario GOLD: {e}")
                return False  # Retornamos False para indicar que el registro no fue exitoso
        if self.switchVarMembresia.get() == "off":
            try:
                DataBase.insert_user(usuario, contra, nombre, apellido, correo, edad, imagen_ruta, "No" ,
                                     spotify_user1, song1, song2, song3, None, None, None)

                print( DataBase.insert_user(usuario, contra, nombre, apellido, correo, edad, imagen_ruta, "No" ,
                                     spotify_user1, song1, song2, song3, None, None, None))
                tkinter.messagebox.showinfo(title="Registro", message="El usuario BASE se ha registrado exitosamente.")

                # Nota: No mostramos el mensaje de éxito aquí.
            except Exception as e:
                print("Error", f"Ocurrió un error al registrar al usuario BASE: {e}")
                return False  # Retornamos False para indicar que el registro no fue exitoso

        # try:
        #
        #     DataBase.insert_user(self.entry_Username.get(), self.entry_Contra.get(), self.entry_Nombre.get(),
        #                          self.entry_Apellido.get(), self.entry_Correo.get(), user.age,
        #                          self.selected_photo_path, None, self.userSpot.get(), self.cancion1.get(),
        #                             self.cancion2.get(), self.cancion3.get(), None, None)
        # # Nota: No mostramos el mensaje de éxito aquí.
        # except Exception as e:
        #     print("Error", f"1Ocurrió un error al registrar al usuario: {e}")
        #     return False  # Retornamos False para indicar que el registro no fue exitoso
        print("retornamos true")
        return True  # Retornamos True para indicar que el registro fue exitoso

    def get_active_palettes(self):
        active_palettes = []

        # Verifica el estado de cada switch de paleta y agrega la paleta activa a la lista
        if self.switchVarRed.get() == "on":
            active_palettes.append("Red")

        if self.switchVarWhite.get() == "on":
            active_palettes.append("White")

        if self.switchVarGreen.get() == "on":
            active_palettes.append("Green")

        if self.switchVarBlack.get() == "on":
            active_palettes.append("Black")

        if self.switchVarBlue.get() == "on":
            active_palettes.append("Blue")

        return active_palettes

    def get_active_textures(self):
        active_textures = []

        # Verifica el estado de cada switch de textura y agrega la textura activa a la lista
        if self.switchVarPack1.get() == "on":
            active_textures.append("Textura 1")

        if self.switchVarPack2.get() == "on":
            active_textures.append("Textura 2")

        if self.switchVarPack3.get() == "on":
            active_textures.append("Textura 3")

        # Agrega más texturas según sea necesario

        return active_textures
    def on_register_button_click(self):

        error_occurred = False
        missing_fields, missing_tabs = self.check_fields_filled()
        if missing_fields:
            # Mostrar un mensaje de error con los campos y las pestañas que faltan
            missing_info = ', '.join([f"{field} ({tab})" for field, tab in zip(missing_fields, missing_tabs)])
            tkinter.messagebox.showerror("Error", f"Faltan los siguientes campos: {missing_info}")
            return
        if self.selected_photo_path is None or self.selected_photo_path == "assets/flags/Avatar-Profile.png":
            respuesta = tkinter.messagebox.askyesno("Confirmación",
                                                    "¿Seguro que no quieres tener una foto personalizada?")
            if respuesta == "no":
                return
            else:
                self.selected_photo_path = "assets/flags/Avatar-Profile.png"
        # Convertir el nombre de usuario a minúsculas para la verificación
        ## Comprobar si el switch de membresía está activo
        if self.switchVarMembresia.get() == "on":
            # Verificar si al menos un switch en "palettes" está activo
            palettes_switches = [self.switchVarRed, self.switchVarWhite, self.switchVarGreen,
                                 self.switchVarBlack, self.switchVarBlue]
            if not any([sw.get() == "on" for sw in palettes_switches]):
                tkinter.messagebox.showerror("Error",
                                             f"Hace falta seleccionar una paleta en {dic.Palettes[dic.language]}")
                return

            # Verificar si al menos un switch en "texture" está activo
            texture_switches = [self.switchVarPack1, self.switchVarPack2, self.switchVarPack3]
            if not any([sw.get() == "on" for sw in texture_switches]):
                tkinter.messagebox.showerror("Error",
                                             f"Hace falta seleccionar una textura en {dic.Texture[dic.language]}")
                return

        username = self.entry_Username.get().lower()

        # Verifica si el correo electrónico o el nombre de usuario ya están registrados
        if DataBase.is_email_registered(self.entry_Correo.get()):
            tkinter.messagebox.showerror("Error", "Este correo ya está registrado.")
            return

        if DataBase.is_username_registered(username):
            tkinter.messagebox.showerror("Error", "Este nombre de usuario ya está registrado.")
            return

        contrasena = self.entry_Contra.get()
        if not self.validar_contrasena(contrasena):
            tkinter.messagebox.showerror("Error",
                                         "La contraseña no cumple con los requisitos. - Mínimo 8 caracteres- Máximo 16 caracteres- Al menos una letra mayúscula- Al menos una letra minúscula- Al menos un número- Al menos un carácter especial: @#$%^&+=.,!/*()-<>")
            return
        self.temp_verification_code = DataBase.generate_confirmation_code()
        print(f"Código de confirmación generado: {self.temp_verification_code}")
        try:
            # Intenta guardar los datos en la base de datos y enviar el correo electrónico
            if not self.check_membership_fields_filled():
                respuesta = tkinter.messagebox.askyesno("Confirmación", "¿Seguro que no quieres ser miembro?")
                if respuesta:
                    # Guarda en la base de datos que el usuario decidió no ser miembro
                    DataBase.insert_membership_status(self.entry_Username.get(), False)
                    DataBase.update_membership_status(self.entry_Username.get(), "No")
                else:
                    # Redirige al usuario a la pestaña de membresía
                    self.select_tab(dic.Members[dic.language])
                    error_occurred = True  # Marca que ocurrió un error
            else:
                # Guarda en la base de datos que el usuario decidió ser miembro y los detalles correspondientes
                DataBase.insert_membership_status(self.entry_Username.get(), True)
                DataBase.update_membership_status(self.entry_Username.get(), "Yes")
                DataBase.insert_membership_details(self.entry_Username.get(), self.card_number_var.get(),
                                                   self.card_expiry_entry.get(), self.card_cvc_entry.get())

            # Intenta enviar el correo electrónico
            DataBase.send_confirmation_email(self.entry_Correo.get(), self.temp_verification_code)


        except Exception as e:
            tkinter.messagebox.showerror("Error",
                                         f"Error al guardar los datos o enviar el correo electrónico: {str(e)}")
            error_occurred = True  # Marca que ocurrió un error

            # Si no ocurrió ningún error, realiza la verificación
        if not error_occurred:
            self.solicitar_verificacion()

    def solicitar_verificacion(self):
        # Aquí puedes abrir una nueva ventana o usar la actual para solicitar el código al usuario.
        codigo_ingresado = simpledialog.askstring("Verificación",
                                                  "Por favor, ingresa el código de verificación enviado a tu correo:",
                                                  parent=self)
        self.check_verification_code(codigo_ingresado)

    def check_fields_filled(self):
        """
        Verifica si todos los campos necesarios están llenos.
        Retorna una lista de campos faltantes y sus pestañas asociadas.
        """
        missing_fields = []
        missing_tabs = []

        if not self.entry_Nombre.get():
            missing_fields.append(dic.Name[dic.language])
            missing_tabs.append(dic.Data[dic.language])

        if not self.entry_Apellido.get():
            missing_fields.append(dic.Surname[dic.language])
            missing_tabs.append(dic.Data[dic.language])

        if not self.entry_Correo.get():
            missing_fields.append(dic.Email[dic.language])
            missing_tabs.append(dic.Data[dic.language])
        if not user.age:
            missing_fields.append(dic.Age[dic.language])
            missing_tabs.append(dic.Data[dic.language])

        # Verificar campos en la pestaña Juego
        if not self.entry_Username.get():
            missing_fields.append(dic.Username[dic.language])
            missing_tabs.append(dic.Game[dic.language])
        if not self.entry_Contra.get():
            missing_fields.append(dic.Password[dic.language])
            missing_tabs.append(dic.Game[dic.language])
        if not user.picture:
            missing_fields.append(dic.Photo[dic.language])
            missing_tabs.append(dic.Game[dic.language])
        if not self.userSpot.get():
            missing_fields.append("Spotify User")
            missing_tabs.append(dic.Music[dic.language])
        if not self.cancion1.get():
            missing_fields.append("Song1")
            missing_tabs.append(dic.Music[dic.language])
        if not self.cancion2.get():
            missing_fields.append("Song1")
            missing_tabs.append(dic.Music[dic.language])
        if not self.cancion3.get():
            missing_fields.append("Song1")
            missing_tabs.append(dic.Music[dic.language])

        return missing_fields, missing_tabs

    def check_membership_fields_filled(self):
        """Verifica si los campos de membresía están llenos."""
        if not self.card_number_var.get() or not self.card_expiry_entry.get() or not self.card_cvc_entry.get():
            return False
        return True
    def update_edad_label(self, value):
        self.edad_label.configure(text=dic.Age[dic.language] + f" :{round(value)}")

    def select_tab(self, tab_name):
        # Establecer la pestaña con el nombre 'tab_name' como visible
        self.tabview.set(tab_name)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(
            filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])

        if archivo:
            self.selected_photo_path = archivo
            # Cargar la imagen
            imagen = Image.open(archivo)
            imagen = imagen.resize((100, 100), Image.ANTIALIAS)
            circular = self.make_circle_image(imagen)
            Imagentk = ImageTk.PhotoImage(circular)
            self.avatar_label.configure(image=Imagentk)
            self.avatar_label.image = Imagentk

    # usuario_img = self.entry_Username.get()
    # img_path = os.path.join("ProfilePics", usuario_img + ".jpg")
    # imagen.save(img_path)
    # self.display_avatar_in_circle(self.selected_photo_path, self.tabview.tab(dic.Game[dic.language]), 0.5, 0.19)

    """def display_avatar_in_circle(self, image_path, parent, relx, rely):
        # Cargar la imagen
        img = Image.open(image_path)
        # Redimensionar la imagen a 100x100
        img = img.resize((100, 100), Image.ANTIALIAS)
        # Convertir la imagen en circular
        circular_img = self.make_circle_image_from_img(img)
        # Convertir la imagen en un formato compatible con Tkinter
        imagen_tk = ImageTk.PhotoImage(circular_img)
        # Mostrar la imagen en un label
        self.avatar_label = tkinter.Label(parent, image=imagen_tk, bg=parent["bg"])
        self.avatar_label.image = imagen_tk  # ¡Importante! Mantener una referencia a la imagen
        self.avatar_label.place(relx=relx, rely=rely, anchor=customtkinter.CENTER)
        """

    @staticmethod
    def make_circle_image(img):
        """
        Convert an image into a circular image.
        """
        # Make sure the image has an alpha channel for transparency
        img = img.convert("RGBA")

        # Create a blank white image
        mask = Image.new("L", img.size, 0)

        # Draw a white circle on the mask
        draw = ImageDraw.Draw(mask)
        width, height = img.size
        draw.ellipse((0, 0, width, height), fill=255)

        # Apply the mask to the image
        circular_img = Image.composite(img, Image.new("RGBA", img.size, (255, 255, 255, 0)), mask)
        return circular_img

    """
    def make_circle_image_from_img(self, img):
        # Asegurarse de que la imagen tiene un canal alfa
        img = img.convert("RGBA")

        # Crear una máscara con un círculo blanco en un fondo negro
        mask = Image.new("L", (100, 100), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 100, 100), fill=255)

        # Usar la máscara para recortar la imagen original
        result = Image.composite(img, Image.new("RGBA", img.size, (0, 0, 0, 0)), mask)

        return result"""

    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)

    def displayPhoto(self,usuario_img):
        img = usuario_img + ".jpg"
        imgpng = "ProfilePics/" + usuario_img + ".png"
        imagen = Image.open(imgpng)
        imagen = imagen.resize((100, 100), Image.ANTIALIAS)
        circular = self.make_circle_image(imagen)
        Imagentk = ImageTk.PhotoImage(circular)
        self.avatar_label.configure(image=Imagentk)
        self.avatar_label.image = Imagentk

        pixeles = pyplot.imread(img)
        detector = MTCNN()
        caras = detector.detect_faces(pixeles)
        self.reg_rostro(img, caras, usuario_img)

    def registro_facial(self):
        global usuario_img
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

        img = self.entry_Username.get() + ".jpg"
        pixeles = pyplot.imread(img)
        detector = MTCNN()
        caras = detector.detect_faces(pixeles)
        self.reg_rostro(img, caras)

    # Vamos a capturar el rostro


    def reg_rostro(self,img, lista_resultados):
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











