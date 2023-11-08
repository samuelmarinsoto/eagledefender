"""
Database Login Connection Tester
Herramienta para probar la conexión a la base de datos y realizar funciones de autenticación y registro.

Este script permite al usuario realizar las siguientes acciones:
- Registrarse como un nuevo usuario.
- Acceder con sus credenciales.
- Confirmar su dirección de correo electrónico.

Además, utiliza una base de datos para almacenar información del usuario y Google API para enviar correos electrónicos
de confirmación.
"""
import re
import random
import bcrypt
from datetime import datetime, timedelta
import base64
import os

import pyodbc
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import tkinter.messagebox
import sqlite3
#import database.VerificationCode as VerificationCode
# Configuración inicial para la API de Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = '../credentials.json'
CREDENTIALS_FILE = '../token.json'


def get_credentials():
    """
    Retrieves credentials to authenticate with the Gmail API.

    Returns:
        Credentials: Object containing user credentials.
    """
    creds = None
    if os.path.exists(CREDENTIALS_FILE):
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(CREDENTIALS_FILE, 'w') as token:
                token.write(creds.to_json())
    return creds


def is_valid_email(email):
    if isinstance(email, str):
        if re.search(r'@', email):
            email_split = email.split("@")
            valid_domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com", "live.com", "estudiantec.cr"]
            if email_split[1] in valid_domains:
                return True
    return False

def send_email(sender, to, subject, message_text):
    if is_valid_email(to):
        creds = get_credentials()
        service = build('gmail', 'v1', credentials=creds)

        raw_msg = base64.urlsafe_b64encode(f"Subject: {subject}\nTo: {to}\n\n{message_text}".encode('utf-8')).decode('utf-8')
        message = {'raw': raw_msg}
        sent_message = service.users().messages().send(userId=sender, body=message).execute()
        print(f"Message sent. Id: {sent_message['id']}")
    else:
	    tkinter.messagebox.showerror("Error", "Email not valid. Please use a valid email address. "
	                                          "Accepted domains are: gmail.com, hotmail.com, outlook.com, yahoo.com,"
	                                          " icloud.com, live.com, estudiantec.cr")

def connect():
    """
    Establishes and returns a connection with the database.
    If an error occurs, prints the message and returns None.

    Returns:
        sqlite3.Connection: Connection object to the database, or None if an error occurred.
    """
    try:
        conn = sqlite3.connect('../EagleDefender.db')  # Create or connect to a SQLite database
        return conn
    except Exception as e:
        print(f"An error occurred connecting to the database: {e}")
        return None



def create_tables():
    conn = connect()
    cursor = conn.cursor()
    try:
        # Tabla de Usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL UNIQUE,
                Password BLOB NOT NULL,
                FirstName TEXT,
                LastName TEXT,
                Email TEXT NOT NULL UNIQUE,
                Age INTEGER,
                Photo TEXT,
                Membresía TEXT,
                SpotifyUser TEXT,
                Song1 TEXT,
                Song2 TEXT,
                Song3 TEXT,
                NúmeroDeTarjeta TEXT,
                FechaDeVencimiento DATE,
                CVC INTEGER,
                Texturas TEXT,
                Paletas TEXT
            )
        """)

        # Tabla de Personalizaciones





        conn.commit()

    except Exception as e:
        print(f"Ocurrió un error al crear las tablas: {e}")
    finally:
        cursor.close()
        conn.close()


def hash_password(password):
	"""Encrypts a password using bcrypt.

	Args:
		password (str): The password to be hashed.

	Returns:
		bytes: The hashed password.
	"""
	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed


def verify_password(password, hashed_from_db):
	"""The email or username is already registered.
"""
	if not hashed_from_db:
		print("No hash found for this user.")
		return False
	return bcrypt.checkpw(password.encode('utf-8'), hashed_from_db)


def insert_user(username, password, first_name, last_name, email, age, photo,membresia, spotify_user, song1, song2, song3, card_number, expiry_date, cvc,texturas, paletas):
    """
    Inserts a new user into the database with the provided information.

    Args:
        ... [same as before, plus the new fields] ...

    Returns:
        bool: True if the user was inserted successfully, False otherwise.
    """
    username = username.lower()
    if age < 13:
        tkinter.messagebox.showerror("Error", "The user must be at least 13 years old to register.")
        return False

    hashed_pass = hash_password(password)

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users (Username, Password, FirstName, LastName, Email, Age, Photo, Membresía, SpotifyUser, Song1, Song2, Song3, NúmeroDeTarjeta, FechaDeVencimiento, CVC, Texturas, Paletas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (username, hashed_pass, first_name, last_name, email, age, photo, membresia, spotify_user, song1, song2, song3,
              card_number, expiry_date, cvc,texturas, paletas))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("The email or username is already registered.")
    except Exception as e:
        print(f"An error occurred while inserting the user: {e}")
    finally:
        cursor.close()
        conn.close()
    return False

#insert_user("admin","Cucaracha123&","admin","admin","jifsentreprise@gmail.com",18,"","No","ANGELOCEL","Yes","Toto","One","123145123","14/24","213","Textura 1","Red")
def insert_personalization_option(username, paleta_de_colores, textura):
    try:
        # Conectarse a la base de datos (reemplaza 'nombre_de_tu_base_de_datos.db' con el nombre real)
        conn = sqlite3.connect('../EagleDefender.db')
        cursor = conn.cursor()

        # Insertar la nueva opción de personalización en la tabla Personalizaciones
        cursor.execute("INSERT INTO Personalizaciones (Username, PaletaDeColores, Textura) VALUES (?, ?, ?)",
                       (username, paleta_de_colores, textura))

        # Confirmar la transacción
        conn.commit()

        # Cerrar la conexiónS
        conn.close()

    except sqlite3.Error as e:
        print("Error al insertar la opción de personalización:", e)

def validate_user(username, password):
	"""Validates user credentials against the database.

	   Args:
	       username (str): The username to validate.
	       password (str): The password to validate.

	   Returns:
	       bool: True if validation is successful, False otherwise.
	   """
	connection = connect()
	cursor = connection.cursor()

	try:
		cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
		row = cursor.fetchone()
		if row:
			hashed_password_from_db = row[2]
			print("Hashed password from DB:", hashed_password_from_db.hex())
			if verify_password(password, hashed_password_from_db):
				return True  # Usuario y contraseña válidos
			else:
				return False  # Contraseña incorrecta
		else:
			return False  # Usuario no encontrado
	except pyodbc.Error as ex:
		print("SQL Error: ", ex)
	finally:
		cursor.close()
		connection.close()


def is_username_registered(username):
    """Checks if a username is already registered in the database.

    Args:
        username (str): The username to check.

    Returns:
        bool: True if the username is registered, False otherwise.
    """

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('SELECT Username FROM Users WHERE Username = ?', (username,))
        usuario = cursor.fetchone()
        return usuario is not None
    except Exception as e:
        print(f"Ocurrió un error al verificar el username: {e}")
        return False


def is_username_registered2(username):
    """Verifica si un nombre de usuario ya está registrado en la base de datos."""
    user = get_user_by_username(username)
    return user is not None

def get_user_by_username(username):
    """Returns the details of a user based on their username.

    Args:
        username (str): The username of the user.

    Returns:
        tuple: User details retrieved from the database, or None if an error occurred.
    """
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT UserID, Username, Password, FirstName, LastName, Email, Age, Photo, SpotifyUser, Song1, Song2, Song3, NúmeroDeTarjeta, FechaDeVencimiento, CVC, Texturas,Paletas FROM '
            'Users WHERE Username = ?', (username,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        print(f"Ocurrió un error al obtener el usuario por nombre de usuario: {e}")
        return None


# def confirm_email(email, entered_code):
# 	"""Confirms the user's email by comparing the entered code with the stored one.
#
# 	    Args:
# 	        email (str): The user's email address.
# 	        entered_code (str): The confirmation code entered by the user.
#
# 	    Returns:
# 	        bool: True if the email is confirmed, False otherwise.
# 	    """
# 	user = get_user(email)
#
# 	if not user:
# 		print("No existe un usuario con ese correo.")
# 		return False
#
# 	codigo_almacenado = user[8]  # Asumiendo que CodigoConfirmacion es la 9na columna
# 	print(f"Código almacenado: {codigo_almacenado}")
# 	print(f"Código ingresado: {entered_code}")
#
# 	if str(codigo_almacenado) != str(entered_code):
# 		print("Los códigos no coinciden.")
# 		return False
#
# 	fecha_codigo_str = user[9]  # Asumiendo que FechaCodigo es la 10ma columna
# 	if not fecha_codigo_str:
# 		print("No hay un código de confirmación válido para este correo.")
# 		return False
#
# 	# Verifica si fecha_codigo_str es una instancia de datetime, si es así, úsala directamente
# 	if isinstance(fecha_codigo_str, datetime):
# 		fecha_codigo = fecha_codigo_str
# 	else:  # Si no es un datetime, trata de convertirla (esto maneja casos donde la fecha pueda ser una cadena)
# 		try:
# 			fecha_codigo = datetime.strptime(fecha_codigo_str, '%Y-%m-%d %H:%M:%S.%f')
# 		except ValueError as e:
# 			print(f"Error: No se pudo convertir fecha_codigo_str a datetime: {e}")
# 			return False
#
# 	if datetime.now() - fecha_codigo > timedelta(minutes=10):
# 		print("El código ha expirado.")
# 		return False
#
# 	return True





def get_user(email):
    """Returns the details of a user based on their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            tuple: User details retrieved from the database, or None if an error occurred.
        """
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT UserID, Username, Password, FirstName, LastName, Email, Age, Photo, SpotifyUser, Song1, Song2, Song3, NúmeroDeTarjeta, FechaDeVencimiento, CVC FROM '
            'Users WHERE Email = ?' , (email,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        print(f"Ocurrió un error al obtener el usuario: {e}")
        return None




def is_email_registered(email):
	"""Verifica si un correo ya está registrado en la base de datos."""
	user = get_user(email)
	return user is not None


def send_confirmation_email(email, confirmation_code):
	"""Sends an email with a confirmation code.

	   Args:
	       email (str): The recipient's email address.
	       confirmation_code (str): The confirmation code to send.
	   """
	subject = 'Confirmación de Correo'
	message_text = f'Por favor, confirma tu correo utilizando el siguiente código: {confirmation_code}'
	send_email('jifs.enterprises@gmail.com', email, subject, message_text)

def generate_and_save_code(email):
	"""Generates a new confirmation code, saves it in the database, and returns it.

	   Args:
	       email (str): The email address to generate and save the code for.

	   Returns:
	       str: The generated confirmation code.
	   """

	codigo_confirmacion = generate_confirmation_code()
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("UPDATE Users SET Code = ?, DateCode = ? WHERE Email = ?",
		               (codigo_confirmacion, datetime.now(), email))
		conn.commit()
		return codigo_confirmacion
	except Exception as e:
		print(f"Ocurrió un error al actualizar el código de confirmación: {e}")
		return None


def generate_confirmation_code():
	"""Genera un código de confirmación aleatorio de 6 dígitos y lo retorna."""
	return str(random.randint(100000, 999999))


def insert_membership_status(username, is_member):
	"""
	Inserts the membership status of a user into the database.

	Args:
		username (str): The username of the user.
		is_member (bool): True if the user wants to be a member, False otherwise.

	Returns:
		bool: True if the operation was successful, False otherwise.
	"""
	try:
		conn = connect()
		cursor = conn.cursor()

		# Convert boolean to a recognizable string representation
		membership_status = "Yes" if is_member else "No"

		cursor.execute("""
            UPDATE Users SET Membresía = ? WHERE Username = ?
        """, (membership_status, username))
		conn.commit()
		return True
	except Exception as e:
		print(f"An error occurred while inserting the membership status: {e}")
		return False
	finally:
		cursor.close()
		conn.close()


def insert_membership_details(username, card_number, expiry_date, cvc):
	"""
	Inserts the card details of a user into the database.

	Args:
		username (str): The username of the user.
		card_number (str): The card number of the user.
		expiry_date (str): The expiry date of the card.
		cvc (int): The CVC of the card.

	Returns:
		bool: True if the operation was successful, False otherwise.
	"""
	try:
		conn = connect()
		cursor = conn.cursor()

		cursor.execute("""
            UPDATE Users 
            SET NúmeroDeTarjeta = ?, FechaDeVencimiento = ?, CVC = ? 
            WHERE Username = ?
        """, (card_number, expiry_date, cvc, username))
		conn.commit()
		return True
	except Exception as e:
		print(f"An error occurred while inserting the card details: {e}")
		return False
	finally:
		cursor.close


def update_songs(Song1, Song2,Song3):
    """
    Updates the songs of a user in the database.

    Args:
        Song1 (str): The song 1 of the user.
        Song2 (str): The song 2 of the user.
        Song3 (str): The song 3 of the user.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Users 
            SET Song1 = ?, Song2 = ?, Song3 = ?
           
        """, (Song1, Song2, Song3))
        conn.commit()
        return True
    except Exception as e:
        print(f"An error occurred while updating songs: {e}")
    finally:
        cursor.close()
        conn.close()
    return False


def update_membership_status(username, membership_status):
	"""
	Updates the membership status of a user in the database.

	Args:
		username (str): The username of the user.
		membership_status (str): The new membership status. For example, "Yes" for members, "No" for non-members.

	Returns:
		bool: True if the update was successful, False otherwise.
	"""
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("""
            UPDATE Users 
            SET Membresía = ? 
            WHERE Username = ?
        """, (membership_status, username.lower()))
		conn.commit()
		return True
	except Exception as e:
		print(f"An error occurred while updating membership status: {e}")
	finally:
		cursor.close()
		conn.close()
	return False


def is_user_member(username):
    user = get_user(username)
    if user and user["Membresía"] == "Yes":
        return True
    return False
def main():
	create_tables()
if __name__ == "__main__":
	main()
