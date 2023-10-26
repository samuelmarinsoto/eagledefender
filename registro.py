import spotipy
import spotipy.util as util
import datauser as user

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
import datauser as user
from tkcalendar import Calendar
from datetime import date
import spot
import DataBaseLocal as DataBase
import re
from PIL import Image, ImageDraw

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
		self.selected_photo_path = "assets/flags/Avatar-Profile.png"

		# configure grid layout (4x4)

		# create sidebar frame with widgets

		self.tabview = customtkinter.CTkTabview(self, width=800, height=800, fg_color=grey,
		                                        segmented_button_selected_color=green,
		                                        segmented_button_selected_hover_color=pink)
		self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
		self.tabview.add(dic.Data[dic.language])
		self.tabview.add(dic.Game[dic.language])
		self.tabview.add(dic.Music[dic.language])
		self.tabview.add(dic.Palettes[dic.language])
		self.tabview.add(dic.Texture[dic.language])
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
		self.entry_Nombre.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

		self.apellido = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Surname[dic.language],
		                                       anchor="w")
		self.apellido.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

		self.entry_Apellido = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
		self.entry_Apellido.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

		self.correo = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Email[dic.language],
		                                     anchor="w")
		self.correo.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

		self.entry_Correo = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
		self.entry_Correo.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

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
		# -------------------------------------------------------------------------------

		self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
		                                         text=dic.Registration[dic.language],
		                                         font=customtkinter.CTkFont(size=20, weight="bold"))
		self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

		self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
		                                       text=dic.Username[dic.language], anchor="w")
		self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
		self.entry_Username = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]))
		self.entry_Username.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

		self.contra = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Password[dic.language],
		                                     anchor="w")
		self.contra.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

		self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊")
		self.entry_Contra.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
		self.contra_check = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]),
		                                           text="Verificar " + dic.Password[dic.language], anchor="w")
		self.contra_check.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

		self.entry_Contra_check = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊")
		self.entry_Contra_check.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
		self.foto_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), corner_radius=60,
		                                         text=dic.Photo[dic.language])
		self.foto_label.place(relx=0.25, rely=0.6, anchor=customtkinter.CENTER)
		self.camera_icon = ImageTk.PhotoImage(file="camera_icon.png")  # Cargar el ícono

		# self.foto = customtkinter.CTkFrame(self.tabview.tab("Juego"), fg_color=grey, corner_radius=100, height=80,width=80)
		# self.foto.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

		default_image_path = "assets/flags/Avatar-Profile.png"

		self.display_avatar_in_circle(default_image_path, self.tabview.tab(dic.Game[dic.language]), 0.5, 0.7)

		self.subir_Foto = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), text="✚",
		                                          fg_color=green_light, hover_color=green, corner_radius=80, width=10,
		                                          command=self.abrir_archivo)
		self.subir_Foto.place(relx=0.3, rely=0.7, anchor=customtkinter.CENTER)

		self.camera_button = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), image=self.camera_icon,
		                                             corner_radius=0, width=0, border_width=0, text="",
		                                             command=self.registro_facial)
		self.camera_button.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)

		# ----------------------------------------------------------------------------------------

		self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
		                                         text=dic.Registration[dic.language],
		                                         font=customtkinter.CTkFont(size=20, weight="bold"))
		self.logo_label.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

		self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Music[dic.language]),
		                                       text=dic.FavoriteSongs[dic.language], anchor="w")
		self.username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
		# ---------------------------------------------------------------------------------------------
		self.userSpot = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
		self.userSpot.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
		self.SaveuserSpot = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
		                                            text="Save Spotify User",
		                                            fg_color=green_light, hover_color=green,
		                                            command=self.UserSpotSelect)
		self.SaveuserSpot.place(relx=0.75, rely=0.3, anchor=customtkinter.CENTER)

		self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
		self.cancion1.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)
		self.song_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
		                                             text="Search",
		                                             fg_color=green_light, hover_color=green,
		                                             command=self.SongSelect1)
		self.song_button_1.place(relx=0.75, rely=0.35, anchor=customtkinter.CENTER)

		self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
		self.cancion2.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
		self.song_button_2 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
		                                             text="Search",
		                                             fg_color=green_light, hover_color=green,
		                                             command=self.SongSelect2)
		self.song_button_2.place(relx=0.75, rely=0.4, anchor=customtkinter.CENTER)

		self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Music[dic.language]))
		self.cancion3.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
		self.song_button_3 = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
		                                             text="Search",
		                                             fg_color=green_light, hover_color=green,
		                                             command=self.SongSelect3)
		self.song_button_3.place(relx=0.75, rely=0.45, anchor=customtkinter.CENTER)
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

		self.calendario_button = customtkinter.CTkButton(self.tabview.tab(dic.Data[dic.language]),
		                                                 text="Show/Hide Calendar",
		                                                 fg_color=green_light, hover_color=green,
		                                                 command=self.toggle_calendar)
		self.calendario_button.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

		self.testPlay = customtkinter.CTkButton(self.tabview.tab(dic.Music[dic.language]),
		                                        text="Play text",
		                                        fg_color=green_light, hover_color=green,
		                                        command=self.PlayTEst)
		self.testPlay.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

		# --------------------------------------------------------------------------------------------------------------------------------
		paletteRed = PhotoImage(file="assets/Palettes/Red.png").subsample(4, 4)
		paletteWhite = PhotoImage(file="assets/Palettes/White.png").subsample(4, 4)
		paletteGreen = PhotoImage(file="assets/Palettes/Green.png").subsample(4, 4)
		paletteBlack = PhotoImage(file="assets/Palettes/Black.png").subsample(4, 4)
		paletteBlue = PhotoImage(file="assets/Palettes/Blue.png").subsample(4, 4)

		self.buttonRed = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
		                                         image=paletteRed, fg_color=grey,
		                                         command=lambda: user.selecPalett("RED"), width=100, height=100)
		self.buttonWhite = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
		                                           image=paletteWhite,
		                                           fg_color=grey, command=lambda: user.selecPalett("WHITE"), width=100,
		                                           height=100)
		self.buttonGreen = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
		                                           image=paletteGreen,
		                                           fg_color=grey, command=lambda: user.selecPalett("GREEN"), width=100,
		                                           height=100)
		self.buttonBlack = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
		                                           image=paletteBlack,
		                                           fg_color=grey, command=lambda: user.selecPalett("BLACK"), width=100,
		                                           height=100)
		self.buttonBlue = customtkinter.CTkButton(self.tabview.tab(dic.Palettes[dic.language]), text="",
		                                          image=paletteBlue,
		                                          fg_color=grey, command=lambda: user.selecPalett("BLUE"), width=100,
		                                          height=100)

		# Coloca los botones en la ventana
		self.buttonRed.place(relx=0.5, rely=0.10)
		self.buttonWhite.place(relx=0.5, rely=0.25)
		self.buttonGreen.place(relx=0.5, rely=0.40)
		self.buttonBlack.place(relx=0.5, rely=0.55)
		self.buttonBlue.place(relx=0.5, rely=0.70)
		# --------------------------------------------------------------------------------------------------------------------------------
		# --------------------------------------------------------------------------------------------------------------------------------
		paletteRed = PhotoImage(file="assets/bloquemetal.png").subsample(4, 4)
		paletteWhite = PhotoImage(file="assets/bloquemadera.png").subsample(4, 4)
		paletteGreen = PhotoImage(file="assets/bloqueconcreto.pngpng").subsample(4, 4)
		# paletteBlack = PhotoImage(file="assets/Palettes/Black.png").subsample(4, 4)
		# paletteBlue = PhotoImage(file="assets/Palettes/Blue.png").subsample(4, 4)

		self.buttonRed = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="",
		                                         image=paletteRed, fg_color=grey,
		                                         command=lambda: user.selecPalett("RED"), width=100, height=100)
		self.buttonWhite = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="",
		                                           image=paletteWhite,
		                                           fg_color=grey, command=lambda: user.selecPalett("WHITE"), width=100,
		                                           height=100)
		self.buttonGreen = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="",
		                                           image=paletteGreen,
		                                           fg_color=grey, command=lambda: user.selecPalett("GREEN"), width=100,
		                                           height=100)
		# self.buttonBlack = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="",
		#                                            image=paletteBlack,
		#                                            fg_color=grey, command=lambda: user.selecPalett("BLACK"), width=100,
		#                                            height=100)
		# self.buttonBlue = customtkinter.CTkButton(self.tabview.tab(dic.Texture[dic.language]), text="",
		#                                           image=paletteBlue,
		#                                           fg_color=grey, command=lambda: user.selecPalett("BLUE"), width=100,
		#                                           height=100)

		# Coloca los botones en la ventana
		self.buttonRed.place(relx=0.5, rely=0.10)
		self.buttonWhite.place(relx=0.5, rely=0.25)
		self.buttonGreen.place(relx=0.5, rely=0.40)
		# self.buttonBlack.place(relx=0.5, rely=0.55)
		# self.buttonBlue.place(relx=0.5, rely=0.70)

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

	def PlayTEst(self):
		spot.PlaySong(user.Songs1[0])

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
		self.update_edad_label(age)

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
		edad = user.age

		# cancion = self.cancion1.get()
		usuario_img = self.entry_Username.get()
		imagen_ruta = 'ProfilePics/' + usuario_img + ".jpg"  # Ruta de la imagen guardada

		# Validaciones antes de insertar el usuario
		if edad < 13:
			tkinter.messagebox.showerror("Error", "El usuario debe tener al menos 13 años para registrarse.")
			return

		if DataBase.is_username_registered(usuario):
			tkinter.messagebox.showerror("Error", "Este nombre de usuario ya está registrado.")
			return

		if DataBase.is_email_registered(correo):
			tkinter.messagebox.showerror("Error", "Este correo ya está registrado.")
			return

		# Llama a la función para insertar los datos en la base de datos
		try:
			DataBase.insert_user(usuario, contra, nombre, apellido, correo, edad, imagen_ruta)
			# Nota: No mostramos el mensaje de éxito aquí.
		except Exception as e:
			print("Error", f"Ocurrió un error al registrar al usuario: {e}")
			return False  # Retornamos False para indicar que el registro no fue exitoso
		# Llama a la función para insertar los datos en la base de datos
		try:

			DataBase.insert_user(self.entry_Username.get(), self.entry_Contra.get(), self.entry_Nombre.get(),
			                     self.entry_Apellido.get(), self.entry_Correo.get(), user.age,
			                     self.selected_photo_path)
			# Nota: No mostramos el mensaje de éxito aquí.
		except Exception as e:
			print("Error", f"Ocurrió un error al registrar al usuario: {e}")
			return False  # Retornamos False para indicar que el registro no fue exitoso
		return True  # Retornamos True para indicar que el registro fue exitoso

	def on_register_button_click(self):
		# Comprobación de la imagen personalizada
		if self.selected_photo_path == "assets/flags/Avatar-Profile.png":
			respuesta = tkinter.messagebox.askyesno("Confirmación",
			                                        "¿Seguro que no quieres tener una foto personalizada?")
			if respuesta == "no":
				return
			else:
				# Si el usuario decide no tener una foto personalizada, establece una imagen predeterminada.
				# (Asegúrate de reemplazar "ruta/de/imagen/predeterminada.png" con la ruta real de la imagen que quieras usar.)
				self.selected_photo_path = "ruta/de/imagen/predeterminada.png"

		missing_fields, missing_tabs = self.check_fields_filled()
		if missing_fields:
			# Mostrar un mensaje de error con los campos y las pestañas que faltan
			missing_info = ', '.join([f"{field} ({tab})" for field, tab in zip(missing_fields, missing_tabs)])
			tkinter.messagebox.showerror("Error", f"Faltan los siguientes campos: {missing_info}")
			return

		# Convertir el nombre de usuario a minúsculas para la verificación
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
		DataBase.send_confirmation_email(self.entry_Correo.get(), self.temp_verification_code)
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

		return missing_fields, missing_tabs

	def update_edad_label(self, value):
		self.edad_label.configure(text=dic.Age[dic.language] + f" :{round(value)}")

	def abrir_archivo(self):
		archivo = filedialog.askopenfilename(filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])
		self.selected_photo_path = archivo
		if archivo:
			user.picture = archivo
			# Cargar la imagen
			imagen = Image.open(archivo)
			usuario_img = self.entry_Username.get()
			img_path = os.path.join("ProfilePics", usuario_img + ".jpg")
			imagen.save(img_path)
			self.display_avatar_in_circle(self.selected_photo_path, self.tabview.tab(dic.Game[dic.language]), 0.5, 0.7)

	def display_avatar_in_circle(self, image_path, parent, relx, rely):
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
		circular_img = Image.composite(img, mask, mask)
		return circular_img

	def make_circle_image_from_img(self, img):
		mask = Image.new("L", (100, 100), 0)
		draw = ImageDraw.Draw(mask)
		draw.ellipse((0, 0, 100, 100), fill=255)
		result = Image.composite(img, Image.new("RGBA", img.size, (0, 0, 0, 0)), mask)
		return result

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
		img_path = os.path.join("ProfilePics", usuario_img + ".jpg")
		cv2.imwrite(img_path, frame)
		# Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
		self.selected_photo_path = usuario_img + ".jpg"
		cap.release()  # Cerramos
		cv2.destroyAllWindows()
		self.display_avatar_in_circle(self.selected_photo_path, None, None, None, self.avatar_label)

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
				cv2.imwrite("ProfilePics", usuario_img + ".jpg", cara_reg)
				pyplot.imshow(data[y1:y2, x1:x2])

		img = usuario_img + ".jpg"
		pixeles = pyplot.imread(img)
		detector = MTCNN()
		caras = detector.detect_faces(pixeles)
		reg_rostro(img, caras)
		# self.iniciar()