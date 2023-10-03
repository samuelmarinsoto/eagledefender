import tkinter as tk
import DataBase

class VerificacionCodigo(tk.Toplevel):
	def __init__(self, parent, email):
		super().__init__(parent)
		self.title("Verificación de Código")
		self.geometry("300x150")

		self.label = tk.Label(self, text="Introduce el código de verificación enviado a tu correo:")
		self.label.pack(pady=10)

		self.entry_codigo = tk.Entry(self)
		self.entry_codigo.pack(pady=10)

		self.boton_verificar = tk.Button(self, text="Verificar Código", command=lambda: self.verificar_codigo(email))
		self.boton_verificar.pack(pady=10)

	def verificar_codigo(self, email):
		# Obtener el código ingresado por el usuario
		codigo_ingresado = self.entry_codigo.get()

		# Obtener el código de la base de datos
		codigo_db = DataBase.obtener_codigo_confirmacion(email)  # Función de tu script

		# Comparar los códigos y dar feedback al usuario
		if codigo_ingresado == codigo_db:
			tk.messagebox.showinfo("Verificación", "¡Correo verificado exitosamente!")
			self.destroy()  # Cierra la ventana si el código es correcto
		else:
			tk.messagebox.showerror("Error", "Código incorrecto. Por favor, intenta de nuevo.")
