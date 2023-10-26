
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
import menu
import DataBaseLocal as DataBase
import re
from PIL import Image, ImageDraw

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

	missing_fields, missing_tabs = self.check_fields_filled()
	if missing_fields:
		# Mostrar un mensaje de error con los campos y las pestañas que faltan
		missing_info = ', '.join([f"{field} ({tab})" for field, tab in zip(missing_fields, missing_tabs)])
		tkinter.messagebox.showerror("Error", f"Faltan los siguientes campos: {missing_info}")
		return
	if self.selected_photo_path == "assets/flags/Avatar-Profile.png":
		respuesta = tkinter.messagebox.askyesno("Confirmación",
		                                        "¿Seguro que no quieres tener una foto personalizada?")
		if respuesta == "no":
			return
		else:
			# Si el usuario decide no tener una foto personalizada, establece una imagen predeterminada.
			# (Asegúrate de reemplazar "ruta/de/imagen/predeterminada.png" con la ruta real de la imagen que quieras usar.)
			self.selected_photo_path = "ruta/de/imagen/predeterminada.png"
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


# def change_appearance_mode_event(self, new_appearance_mode: str):
#     customtkinter.set_appearance_mode(new_appearance_mode)

def change_scaling_event(self, new_scaling: str):
	new_scaling_float = int(new_scaling.replace("%", "")) / 100
	customtkinter.set_widget_scaling(new_scaling_float)


def reg_rostro(self, img, lista_resultados, usuario_img):
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
	img_path2 = os.path.join("ProfilePics", usuario_img + ".png")
	cv2.imwrite(img_path, frame)
	cv2.imwrite(img_path2, frame)
	# Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
	self.selected_picpassword = usuario_img + ".jpg"
	cap.release()  # Cerramos
	cv2.destroyAllWindows()
	self.displayPhoto(usuario_img)


def displayPhoto(self, usuario_img):
	img = usuario_img + ".jpg"
	imgpng = "ProfilePics/" + usuario_img + ".png"
	imagen = Image.open(imgpng)
	imagen = imagen.resize((100, 100), Image.ANTIALIAS)
	circular = self.make_circle_image(imagen)
	Imagentk = ImageTk.PhotoImage(circular)
	self.cameraActive.configure(image=Imagentk)
	self.cameraActive.image = Imagentk

	pixeles = pyplot.imread(img)
	detector = MTCNN()
	caras = detector.detect_faces(pixeles)
	self.reg_rostro(img, caras, usuario_img)


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

	missing_fields, missing_tabs = self.check_fields_filled()
	if missing_fields:
		# Mostrar un mensaje de error con los campos y las pestañas que faltan
		missing_info = ', '.join([f"{field} ({tab})" for field, tab in zip(missing_fields, missing_tabs)])
		tkinter.messagebox.showerror("Error", f"Faltan los siguientes campos: {missing_info}")
		return
	if self.selected_photo_path == "assets/flags/Avatar-Profile.png":
		respuesta = tkinter.messagebox.askyesno("Confirmación",
		                                        "¿Seguro que no quieres tener una foto personalizada?")
		if respuesta == "no":
			return
		else:
			# Si el usuario decide no tener una foto personalizada, establece una imagen predeterminada.
			# (Asegúrate de reemplazar "ruta/de/imagen/predeterminada.png" con la ruta real de la imagen que quieras usar.)
			self.selected_photo_path = "ruta/de/imagen/predeterminada.png"
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


# def change_appearance_mode_event(self, new_appearance_mode: str):
#     customtkinter.set_appearance_mode(new_appearance_mode)

def change_scaling_event(self, new_scaling: str):
	new_scaling_float = int(new_scaling.replace("%", "")) / 100
	customtkinter.set_widget_scaling(new_scaling_float)


def reg_rostro(self, img, lista_resultados, usuario_img):
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
	img_path2 = os.path.join("ProfilePics", usuario_img + ".png")
	cv2.imwrite(img_path, frame)
	cv2.imwrite(img_path2, frame)
	# Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
	self.selected_picpassword = usuario_img + ".jpg"
	cap.release()  # Cerramos
	cv2.destroyAllWindows()
	self.displayPhoto(usuario_img)


def displayPhoto(self, usuario_img):
	img = usuario_img + ".jpg"
	imgpng = "ProfilePics/" + usuario_img + ".png"
	imagen = Image.open(imgpng)
	imagen = imagen.resize((100, 100), Image.ANTIALIAS)
	circular = self.make_circle_image(imagen)
	Imagentk = ImageTk.PhotoImage(circular)
	self.cameraActive.configure(image=Imagentk)
	self.cameraActive.image = Imagentk

	pixeles = pyplot.imread(img)
	detector = MTCNN()
	caras = detector.detect_faces(pixeles)
	self.reg_rostro(img, caras, usuario_img)
