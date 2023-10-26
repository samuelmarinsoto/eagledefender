import spotipy
import spotipy.util as util
import datauser as user
from PIL import Image, ImageTk

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
import language_dictionary as dic
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
import menu
import datauser
from tkcalendar import Calendar
from datetime import date
import spot
import DataBaseLocal as DataBase
import re
from PIL import Image, ImageDraw
import GuardadoEnDatabaseRegistro as GDBR
Userspotify = spot.userSpot


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Registro(customtkinter.CTk):
    def __init__(self):
        green = "GREEN"
        green_light = "GREEN"
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

        self.tabview = customtkinter.CTkTabview(self.background_label, width=400, height=600, fg_color="#AFAFAF",
                                                segmented_button_selected_color=green,
                                                segmented_button_selected_hover_color=pink,
                                                bg_color="transparent",corner_radius=50)  # Set bg_color to transparent

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
        self.tabview.tab(dic.Palettes[dic.language]).configure(bg_color="transparent", fg_color="transparent")
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
                                                   command=lambda: [GDBR.DateSelect(), GDBR.toggle_calendar()])
        self.edad_button.place_forget()
        self.calendario_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
                                                         text="Whats your birthday?",
                                                         fg_color=green_light, hover_color=green,
                                                         command=GDBR.toggle_calendar)
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

        self.cameraActive = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text="", corner_radius=60)
        self.cameraActive.place(relx=0.65, rely=0.5, anchor=customtkinter.CENTER)

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
            command=GDBR.abrir_archivo
        )
        self.subir_Foto.place(relx=0.46, rely=0.65, anchor=customtkinter.CENTER)

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
            command=GDBR.registro_facial
        )
        self.camera_button.place(relx=0.54, rely=0.65, anchor=customtkinter.CENTER)

        # ----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
                                                 text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
                                               text=dic.FavoriteSongs[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        # ---------------------------------------------------------------------------------------------
        self.SaveuserSpot = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                    text="Save Spotify User",
                                                    fg_color=green_light, hover_color=green,
                                                    command=self.UserSpotSelect)
        self.SaveuserSpot.place(relx=0.8, rely=0.2, anchor=customtkinter.CENTER)




        self.userSpot = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Spotify User")
        self.userSpot.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Song 1")
        self.cancion1.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)
        self.song_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=self.SongSelect1)
        self.song_button_1.place(relx=0.8, rely=0.27, anchor=customtkinter.CENTER)

        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Song 2")
        self.cancion2.place(relx=0.5, rely=0.34, anchor=customtkinter.CENTER)
        self.song_button_2 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=self.SongSelect2)
        self.song_button_2.place(relx=0.8, rely=0.34, anchor=customtkinter.CENTER)

        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]), placeholder_text="Song 3")
        self.cancion3.place(relx=0.5, rely=0.41, anchor=customtkinter.CENTER)
        self.song_button_3 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                     text="Search",
                                                     fg_color=green_light, hover_color=green,
                                                     command=self.SongSelect3)
        self.song_button_3.place(relx=0.8, rely=0.41, anchor=customtkinter.CENTER)
        # ---------------------------------------------------------------------------------------------
        self.register_button_data = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
                                                            text=dic.Register[dic.language],
                                                            fg_color=green_light, hover_color=green,
                                                            command=GDBR.on_register_button_click)
        self.register_button_data.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.register_button_game = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]),
                                                            text=dic.Register[dic.language],
                                                            fg_color=green_light, hover_color=green,
                                                            command=GDBR.on_register_button_click)
        self.register_button_game.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

        self.register_button_music = customtkinter.CTkButton(
            self.tabview.tab(dic.Music[dic.language]),
            text=dic.Register[dic.language],
            fg_color=green_light, hover_color=green,
            command=GDBR.on_register_button_click)
        self.register_button_music.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)



        self.testPlay = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
                                                text="Play text",
                                                fg_color=green_light, hover_color=green,
                                                command=self.PlayTEst)
        self.testPlay.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

        # --------------------------------------------------------------------------------------------------------------------------------
        # ...
        # Dentro de la clase Registro, y luego de tus otros elementos...
        # --------------------------------------------------------------------------------------------------------------------------------
        """Aquí va la inserción de la tarjeta"""

        self.card_title_label = customtkinter.CTkLabel(self.tabview.tab(dic.Members[dic.language]),
                                                       text="Información de Tarjeta",
                                                       font=customtkinter.CTkFont(size=16, weight="bold"))
        self.card_title_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.card_number_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                                        placeholder_text="Número de Tarjeta")
        self.card_number_entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.card_expiry_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                                        placeholder_text="MM/AA")
        self.card_expiry_entry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.card_cvc_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                                     placeholder_text="CVC")
        self.card_cvc_entry.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.card_submit_button = customtkinter.CTkButton(self.tabview.tab(dic.Members[dic.language]),
                                                          text="Confirmar",
                                                          fg_color=green_light, hover_color=green)
        self.card_submit_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        # Agregar un CTkLabel para mostrar el icono de la tarjeta
        self.card_icon_label = customtkinter.CTkLabel(self.tabview.tab(dic.Members[dic.language]), text="")
        self.card_icon_label.place(relx=0.75, rely=0.2, anchor=customtkinter.CENTER)

        # Agregar un CTkLabel para mostrar el icono de la tarjeta
        self.card_icon_label = customtkinter.CTkLabel(self.tabview.tab(dic.Members[dic.language]), text="", width=50, height=50)
        self.card_icon_label.place(relx=0.25, rely=0.2, anchor=customtkinter.CENTER)

        # Modifica el método de creación de la entrada de número de tarjeta para agregar un trace
        self.card_number_var = tkinter.StringVar()
        self.card_number_var.trace("w", self.update_card_icon)
        self.card_number_entry = customtkinter.CTkEntry(self.tabview.tab(dic.Members[dic.language]),
                                              placeholder_text="Número de Tarjeta", textvariable=self.card_number_var)
        self.card_number_entry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        # --------------------------------------------------------------------------------------------------------------------------------
        paletteRed = PhotoImage(file="assets/Palettes/Red.png").subsample(5,5)
        paletteWhite = PhotoImage(file="assets/Palettes/White.png").subsample(5, 5)
        paletteGreen = PhotoImage(file="assets/Palettes/Green.png").subsample(5, 5)
        paletteBlack = PhotoImage(file="assets/Palettes/Black.png").subsample(5, 5)
        paletteBlue = PhotoImage(file="assets/Palettes/Blue.png").subsample(5, 5)

        self.buttonRed = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                 image=paletteRed, fg_color=grey,
                                                 command=lambda: user.selecPalett("RED"), width=70, height=70)

        self.buttonWhite = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                   image=paletteWhite,
                                                   fg_color=grey, command=lambda: user.selecPalett("WHITE"), width=70,
                                                   height=70)
        self.buttonGreen = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                   image=paletteGreen,
                                                   fg_color=grey, command=lambda: user.selecPalett("GREEN"), width=70,
                                                   height=70)
        self.buttonBlack = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                   image=paletteBlack,
                                                   fg_color=grey, command=lambda: user.selecPalett("BLACK"), width=70,
                                                   height=70)
        self.buttonBlue = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
                                                  image=paletteBlue,
                                                  fg_color=grey, command=lambda: user.selecPalett("BLUE"), width=40,
                                                  height=40)

        # Coloca los botones en la ventana
        self.buttonRed.place(relx=0.01, rely=0.5)
        self.buttonWhite.place(relx=0.2, rely=0.5)
        self.buttonGreen.place(relx=0.40, rely=0.5)
        self.buttonBlack.place(relx=0.60, rely=0.5)
        self.buttonBlue.place(relx=0.80, rely=0.5)

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

        # --------------------------------------------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------------------------
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
        self.BlockMetal1.place(relx=0.1, rely=0.1)
        self.BlockWood1.place(relx=0.25, rely=0.1)
        self.BlockCement1.place(relx=0.4, rely=0.1)

        self.BlockMetal2 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block2Metal, text="")
        self.BlockWood2 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block2Wood, text="")
        self.BlockCement2 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block2Cement, text="")
        self.BlockMetal2.place(relx=0.1, rely=0.27)
        self.BlockWood2.place(relx=0.25, rely=0.27)
        self.BlockCement2.place(relx=0.4, rely=0.27)

        self.BlockMetal3 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block3Metal,                                 text="")
        self.BlockWood3 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block3Wood, text="")
        self.BlockCement3 = customtkinter.CTkLabel(self.tabview.tab(dic.Texture[dic.language]), image=block3Cement,                                          text="")
        self.BlockMetal3.place(relx=0.1, rely=0.43)
        self.BlockWood3.place(relx=0.25, rely=0.43)
        self.BlockCement3.place(relx=0.4, rely=0.43)
        self.switchVarPack1 = customtkinter.StringVar(value="off")
        self.switchPack1 = customtkinter.CTkSwitch(self.tabview.tab(dic.Texture[dic.language]), text=None, command=None,
                                                  variable=self.switchVarPack1, onvalue="on", offvalue="off",
                                                  fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                  progress_color="Green")
        self.switchPack1.place(relx=0.6, rely=0.15)
        self.switchVarPack2 = customtkinter.StringVar(value="off")
        self.switchPack2 = customtkinter.CTkSwitch(self.tabview.tab(dic.Texture[dic.language]), text=None, command=None,
                                                    variable=self.switchVarPack2, onvalue="on", offvalue="off",
                                                    fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                    progress_color="Green")
        self.switchPack2.place(relx=0.6, rely=0.3)
        self.switchVarPack3 = customtkinter.StringVar(value="off")
        self.switchPack3 = customtkinter.CTkSwitch(self.tabview.tab(dic.Texture[dic.language]), text=None, command=None,
                                                    variable=self.switchVarPack3, onvalue="on", offvalue="off",
                                                    fg_color="Red", button_color="#AFAFAF", button_hover_color="WHite",
                                                    progress_color="Green")
        self.switchPack3.place(relx=0.6, rely=0.45)
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
        age = date.today().year - dateborn.year

        if age < 13:  # Comprobación de edad
            tkinter.messagebox.showerror("Error", "Debes tener al menos 13 años para registrarte.")
            return

        user.age = age
        GDBR.update_edad_label(age)






# self.iniciar()
