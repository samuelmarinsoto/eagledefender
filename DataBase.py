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
import pyodbc
import bcrypt
from datetime import datetime, timedelta
import base64
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Configuración inicial para la API de Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CLIENT_SECRET_FILE = 'credentials.json'
CREDENTIALS_FILE = 'token.json'


def get_credentials():
	"""Retorna las credenciales para autenticarse con la API de Gmail."""
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
	"""Envía un correo electrónico utilizando la API de Gmail."""
	creds = get_credentials()
	service = build('gmail', 'v1', credentials=creds)

	raw_msg = base64.urlsafe_b64encode(f"Subject: {subject}\nTo: {to}\n\n{message_text}".encode('utf-8')).decode(
		'utf-8')
	message = {'raw': raw_msg}
	send_message = service.users().messages().send(userId=sender, body=message).execute()
	print(f"Message sent. Id: {send_message['id']}")


def connect():
	"""Establishes and returns a connection with the database. If an error occurs, prints the message and returns None."""
	try:
		server = '.\EAGLEDEFENDER'
		database = 'EagleDefender'
		driver = '{ODBC Driver 17 for SQL Server}'
		conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes')

		return conn
	except Exception as e:
		print(f"An error occurred connecting to the database: {e}")
		return None


def create_users_table():
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
            CREATE TABLE Users (
                UserID INT PRIMARY KEY IDENTITY(1,1),
                Username NVARCHAR(255),
                Password NVARCHAR(255),
                FirstName NVARCHAR(255),
                LastName NVARCHAR(255),
                Song NVARCHAR(255),
                Email NVARCHAR(255),
                Age INT,
                Photo NVARCHAR(255),
                Code NVARCHAR(6),
                DateCode DATETIME
            )
        """)
		conn.commit()
	except Exception as e:
		print(f"Ocurrió un error al crear la tabla Users: {e}")


def hash_password(password):
	"""Retorna la contraseña encriptada usando bcrypt."""
	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
	return hashed


def verificar_contrasena(contrasena, hashed_from_db):
	"""Verifica si una contraseña coincide con su versión encriptada."""
	if not hashed_from_db:
		print("No se encontró un hash para este usuario.")
		return False
	return bcrypt.checkpw(contrasena.encode('utf-8'), hashed_from_db)


def insert_user(username, password, first_name, last_name, song, email, age, photo, code):
    hashed_pass = hash_password(password)

    try:
        conn = connect()
        cursor = conn.cursor()
        print("Debug: Preparing to insert user")  # Debug Message
        cursor.execute("""
            INSERT INTO Users (Username, Password, FirstName, LastName, Song, Email, Age, Photo, Code, DateCode)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (username, hashed_pass, first_name, last_name, song, email, age, photo, code, datetime.now()))
        conn.commit()
        print("Debug: User inserted successfully")  # Debug Message
    except pyodbc.IntegrityError:
        print("El correo ya está registrado.")
    except Exception as e:
        print(f"Ocurrió un error al insertar el usuario: {e}")
    finally:
        cursor.close()
        conn.close()


def guardar_codigo_confirmacion(correo, codigo_confirmacion):
	"""Guarda o actualiza el código de confirmación para un usuario en la base de datos."""
	timestamp = datetime.datetime.now()
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("UPDATE Users SET Code = ?, DateCode = ? WHERE Email = ?",
		               (codigo_confirmacion, timestamp, correo))
		conn.commit()
	except Exception as e:
		print(f"Ocurrió un error al guardar el código de confirmación: {e}")


def confirmar_correo(correo, codigo_ingresado):
	"""Confirma el correo del usuario comparando el código ingresado con el almacenado en la base de datos."""
	usuario = obtener_usuario(correo)
	if not usuario:
		print("No existe un usuario con ese correo.")
		return False

	codigo_almacenado = usuario[4]  # Asumiendo que CodigoConfirmacion es la 5ta columna
	print(f"Código almacenado: {codigo_almacenado}")
	print(f"Código ingresado: {codigo_ingresado}")

	if str(codigo_almacenado) != str(codigo_ingresado):
		print("Los códigos no coinciden.")
		return False

	fecha_codigo_str = usuario[5]  # Asumiendo que FechaCodigo es la 6ta columna
	if not fecha_codigo_str:
		print("No hay un código de confirmación válido para este correo.")
		return False
	# Convertir la cadena fecha_codigo_str a un objeto datetime
	fecha_codigo = datetime.strptime(fecha_codigo_str, '%Y-%m-%d %H:%M:%S.%f')

	if datetime.now() - fecha_codigo > timedelta(minutes=10):
		print("El código ha expirado.")
		return False

	return True


def limpiar_codigos_antiguos():
	"""Elimina códigos de confirmación antiguos (mayores a 10 minutos) de la base de datos."""
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute("UPDATE Users SET Code = NULL WHERE DateCode < ?",
		               (datetime.datetime.now() - datetime.timedelta(minutes=10),))
		conn.commit()
	except Exception as e:
		print(f"Ocurrió un error al limpiar códigos antiguos: {e}")


def obtener_usuario(email):
	"""Retorna los detalles de un usuario basado en su correo electrónico."""
	try:
		conn = connect()
		cursor = conn.cursor()
		cursor.execute(
			'SELECT UserID, Username, Password, FirstName, LastName, Song, Email, Age, Photo, Code, DateCode FROM '
			'Users WHERE Email = ?', (email,))
		usuario = cursor.fetchone()
		return usuario
	except Exception as e:
		print(f"Ocurrió un error al obtener el usuario: {e}")
		return None


def correo_ya_registrado(correo):
	"""Verifica si un correo ya está registrado en la base de datos."""
	usuario = obtener_usuario(correo)
	return usuario is not None


def obtener_codigo_confirmacion(Email):
	"""Obtiene el código de confirmación para un correo específico."""
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


def enviar_correo_confirmacion(correo, codigo_confirmacion):
	"""Envía un correo electrónico con un código de confirmación."""
	subject = 'Confirmación de Correo'
	message_text = f'Por favor, confirma tu correo utilizando el siguiente código: {codigo_confirmacion}'
	send_email('jifs.enterprises@gmail.com', correo, subject, message_text)


def generar_y_guardar_codigo(correo):
	"""Genera un nuevo código de confirmación, lo guarda en la base de datos y lo retorna."""
	codigo_confirmacion = generar_codigo_confirmacion()
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


def generar_codigo_confirmacion():
	"""Genera un código de confirmación aleatorio de 6 dígitos y lo retorna."""
	return str(random.randint(100000, 999999))



def main():
    """Main function. Manages interaction with the user, allowing them to register, login, or confirm their email."""
    create_users_table()
    option = input("Do you want to register (R), login (L), or confirm your email (C)? ").upper()

    # Registration
    if option == "R":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        age = int(input("Enter your age: "))
        password = input("Enter your password: ")

        # Check if the email is already registered
        if correo_ya_registrado(email):
            print("This email is already registered.")
            return

        # Generate and save the confirmation code
        confirmation_code = generar_codigo_confirmacion()
        insert_user(name, password, None, None, None, email, age, None, confirmation_code)
        # Send the confirmation code via email
        enviar_correo_confirmacion(email, confirmation_code)
        print("User successfully registered. Please check your email and confirm here.")

    # Login
    elif option == "L":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = obtener_usuario(email)

        if user and verificar_contrasena(password, user[2]):
            print("Login successful.")
        else:
            print("Incorrect email or password.")

    # Confirm email
    elif option == "C":
        email = input("Enter the email you registered with: ")
        # Generate and save a new confirmation code
        confirmation_code = generar_y_guardar_codigo(email)
        if confirmation_code:
            enviar_correo_confirmacion(email, confirmation_code)
            print("A new confirmation code has been sent to your email.")
        else:
            print("There was a problem generating a new confirmation code.")
        # Verify the code entered by the user
        entered_code = input("Enter the confirmation code you received by email: ")
        if confirmar_correo(email, entered_code):
            print("Thank you for confirming your email!")
        else:
            print("There was a problem confirming your email. Make sure the code is correct.")

if __name__ == "__main__":
    main()