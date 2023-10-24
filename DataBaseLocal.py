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
import random
import bcrypt
from datetime import datetime, timedelta
import base64
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import tkinter.messagebox
import sqlite3
import VerificationCode
# Configuración inicial para la API de Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = 'credentials.json'
CREDENTIALS_FILE = 'token.json'


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


def send_email(sender, to, subject, message_text):
    """
    Sends an email using the Gmail API.

    Args:
        sender (str): Email address of the sender.
        to (str): Email address of the recipient.
        subject (str): Subject of the email.
        message_text (str): Body of the email.
    """
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    raw_msg = base64.urlsafe_b64encode(f"Subject: {subject}\nTo: {to}\n\n{message_text}".encode('utf-8')).decode(
        'utf-8')
    message = {'raw': raw_msg}
    sent_message = service.users().messages().send(userId=sender, body=message).execute()
    print(f"Message sent. Id: {sent_message['id']}")

def connect():
    """
    Establishes and returns a connection with the database.
    If an error occurs, prints the message and returns None.

    Returns:
        sqlite3.Connection: Connection object to the database, or None if an error occurred.
    """
    try:
        conn = sqlite3.connect('EagleDefender.db')  # Create or connect to a SQLite database
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
                Code TEXT,
                DateCode TIMESTAMP,
                Membresía TEXT
            )
        """)

        # Tabla de Personalizaciones
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Personalizaciones (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INTEGER,
                PaletaDeColores TEXT,
                SpotifyUser TEXT,
                Song1 TEXT,
                Song2 TEXT,
                Song3 TEXT,
                FOREIGN KEY (UserID) REFERENCES Users(UserID)
            )
        """)

        # Tabla de Membresía
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MembresíaTabla (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INTEGER,
                NúmeroDeTarjeta TEXT,
                FechaDeVencimiento DATE,
                CVC INTEGER,
                FOREIGN KEY (UserID) REFERENCES Users(UserID)
            )
        """)

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
	"""Verifies if a password matches its encrypted version.

	Args:
		password (str): The plain-text password entered by the user.
		hashed_from_db (bytes): The hashed password retrieved from the database.

	Returns:
		bool: True if the passwords match, False otherwise.
	"""
	if not hashed_from_db:
		print("No hash found for this user.")
		return False
	return bcrypt.checkpw(password.encode('utf-8'), hashed_from_db)


def insert_user(username, password, first_name, last_name, email, age, photo, code):

	"""Inserts a new user into the database with the provided information.

	Args:
		username (str): Desired username.
		password (str): Desired password.
		first_name (str): User's first name.
		last_name (str): User's last name.
		email (str): User's email address.
		age (int): User's age.
		photo (str): Link or path to user's photo.
		code (str): Generated verification code.

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
	            INSERT INTO Users (Username, Password, FirstName, LastName, Email, Age, Photo, Code, DateCode)
	            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	        """, (username, hashed_pass, first_name, last_name, email, age, photo, code, datetime.now()))
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

def save_confirmation_code(email, confirmation_code):
	"""Saves or updates the confirmation code for a user in the database.

    Args:
        email (str): The user's email address.
        confirmation_code (str): The confirmation code to save.
    """
	timestamp = datetime.now()
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("UPDATE Users SET Code = ?, DateCode = ? WHERE Email = ?",
		               (confirmation_code, timestamp, email))
		conn.commit()
	except Exception as e:
		print(f"Ocurrió un error al guardar el código de confirmación: {e}")


def confirm_email(email, entered_code):
	"""Confirms the user's email by comparing the entered code with the stored one.

	    Args:
	        email (str): The user's email address.
	        entered_code (str): The confirmation code entered by the user.

	    Returns:
	        bool: True if the email is confirmed, False otherwise.
	    """
	user = get_user(email)

	if not user:
		print("No existe un usuario con ese correo.")
		return False

	codigo_almacenado = user[8]  # Asumiendo que CodigoConfirmacion es la 9na columna
	print(f"Código almacenado: {codigo_almacenado}")
	print(f"Código ingresado: {entered_code}")

	if str(codigo_almacenado) != str(entered_code):
		print("Los códigos no coinciden.")
		return False

	fecha_codigo_str = user[9]  # Asumiendo que FechaCodigo es la 10ma columna
	if not fecha_codigo_str:
		print("No hay un código de confirmación válido para este correo.")
		return False

	# Verifica si fecha_codigo_str es una instancia de datetime, si es así, úsala directamente
	if isinstance(fecha_codigo_str, datetime):
		fecha_codigo = fecha_codigo_str
	else:  # Si no es un datetime, trata de convertirla (esto maneja casos donde la fecha pueda ser una cadena)
		try:
			fecha_codigo = datetime.strptime(fecha_codigo_str, '%Y-%m-%d %H:%M:%S.%f')
		except ValueError as e:
			print(f"Error: No se pudo convertir fecha_codigo_str a datetime: {e}")
			return False

	if datetime.now() - fecha_codigo > timedelta(minutes=10):
		print("El código ha expirado.")
		return False

	return True


def clear_old_codes():
	"""Deletes old confirmation codes (older than 10 minutes) from the database.
	    """
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("UPDATE Users SET Code = NULL WHERE DateCode < ?",
		               (datetime.now() - timedelta(minutes=10),))
		conn.commit()
	except Exception as e:
		print(f"Ocurrió un error al limpiar códigos antiguos: {e}")


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
			'SELECT UserID, Username, Password, FirstName, LastName, Email, Age, Photo, Code, DateCode FROM '
			'Users WHERE Email = ?', (email,))
		usuario = cursor.fetchone()
		return usuario
	except Exception as e:
		print(f"Ocurrió un error al obtener el usuario: {e}")
		return None



def is_email_registered(email):
	"""Verifica si un correo ya está registrado en la base de datos."""
	user = get_user(email)
	return user is not None


def get_confirmation_code(Email):
	"""Gets the confirmation code for a specific email.

	   Args:
	       Email (str): The email to get the confirmation code for.

	   Returns:
	       str: The confirmation code, or None if not found.
	   """

	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute('SELECT Code FROM Users WHERE Email = ?', (Email,))
		resultado = cursor.fetchone()
		if resultado:
			return resultado[0]
		else:
			return None
	except Exception as e:
		print(f"Ocurrió un error al obtener el código de confirmación: {e}")
		return None


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
		               (codigo_confirmacion, datetime.now(), correo))
		conn.commit()
		return codigo_confirmacion
	except Exception as e:
		print(f"Ocurrió un error al actualizar el código de confirmación: {e}")
		return None


def generate_confirmation_code():
	"""Genera un código de confirmación aleatorio de 6 dígitos y lo retorna."""
	return str(random.randint(100000, 999999))

def main():
    """
    Main function. Manages interaction with the user, allowing them to register, login, or confirm their email.
    """
    create_tables()
    option = input("Do you want to register (R), login (L), or confirm your email (C)? ").upper()

    # Registration
    if option == "R":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        age = int(input("Enter your age: "))
        password = input("Enter your password: ")

        # Check if the email is already registered
        if is_email_registered(email):
            print("This email is already registered.")
            return

        # Generate and save the confirmation code
        confirmation_code = generate_confirmation_code()
        insert_user(name, password, None, None, email, age, None, confirmation_code)
        # Send the confirmation code via email
        send_confirmation_email(email, confirmation_code)
        print("User successfully registered. Please check your email and confirm here.")

    # Login
    elif option == "L":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = get_user(email)

        if user and verify_password(password, user[2]):
            print("Login successful.")
        else:
            print("Incorrect email or password.")

    # Confirm email
    elif option == "C":
        email = input("Enter the email you registered with: ")
        # Generate and save a new confirmation code
        confirmation_code = generate_and_save_code(email)
        if confirmation_code:
            send_confirmation_email(email, confirmation_code)
            print("A new confirmation code has been sent to your email.")
        else:
            print("There was a problem generating a new confirmation code.")
        # Verify the code entered by the user
        entered_code = input("Enter the confirmation code you received by email: ")
        if confirm_email(email, entered_code):
            print("Thank you for confirming your email!")
        else:
            print("There was a problem confirming your email. Make sure the code is correct.")

if __name__ == "__main__":
    main()