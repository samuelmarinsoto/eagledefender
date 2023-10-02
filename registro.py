import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Registro(customtkinter.CTk):
    def __init__(self):
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        font_style = ('helvic', 20)
        self.imagen_seleccionada = None
        super().__init__()

        # configure window
        self.title("Log In ")
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)

        # create sidebar frame with widgets

        self.tabview = customtkinter.CTkTabview(self, width=400, height=400, fg_color=grey , segmented_button_selected_color=green, segmented_button_selected_hover_color=pink)
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add("Datos")
        self.tabview.add("Juego")
        self.tabview.add("Personalizacion")
        self.tabview.tab("Datos").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Juego").grid_columnconfigure(0, weight=1)



        self.logo_label = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Registro", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


        self.nombre = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Nombre", anchor="w")
        self.nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entry_Nombre = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.entry_Nombre.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.apellido = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Apellido", anchor="w")
        self.apellido.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Apellido = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.entry_Apellido.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


        self.correo = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Correo", anchor="w")
        self.correo.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.entry_Correo = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.entry_Correo.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


        self.edad_label = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Edad: 0")
        self.edad_label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.edad_slider = customtkinter.CTkSlider(self.tabview.tab("Datos"), command=self.update_edad_label, from_=0, to=100, button_color = green, button_hover_color=pink)
        self.edad_slider.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)









        #-------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab("Juego"), text="Registro",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab("Juego"), text="Username", anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.entry_Username = customtkinter.CTkEntry(self.tabview.tab("Juego"))
        self.entry_Username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self.tabview.tab("Juego"), text="Contraseña", anchor="w")
        self.contra.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab("Juego"), show="◊")
        self.entry_Contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


        self.foto = customtkinter.CTkFrame(self.tabview.tab("Juego"), fg_color=grey, corner_radius=100, height=80,width=80)
        self.foto.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.subir_Foto = customtkinter.CTkButton(self.tabview.tab("Juego"), text="✚",
                                                        fg_color=green_light, hover_color=green, corner_radius=80, width=10, command=self.abrir_archivo)
        self.subir_Foto.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)


        #----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab("Personalizacion"), text="Registro",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab("Personalizacion"), text="Tema", anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Personalizacion"), values=["rojo", "negro", "azul","blanco","verde"],fg_color=green_light, button_color=green)
        self.appearance_mode_optionemenu.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab("Personalizacion"), text="Canciones Favoritas", anchor="w")
        self.username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab("Personalizacion") )
        self.cancion1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab("Personalizacion"))
        self.cancion2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab("Personalizacion"))
        self.cancion3.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab("Personalizacion"), text="Registrarse",
                                                    fg_color=green_light, hover_color=green)
        self.sidebar_button_1.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)



    def update_edad_label(self, value):
        self.edad_label.configure(text=f"Edad: {round(value)}")

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if archivo:
            # Cargar la imagen
            imagen = Image.open(archivo)
            # Redimensionar la imagen según el tamaño deseado (ajusta según tus necesidades)
            imagen = imagen.resize((80, 80), Image.ANTIALIAS)
            # Convertir la imagen en un formato compatible con Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)
            # Mostrar la imagen en el CTkFrame
            self.foto.configure(image=imagen_tk)
            self.foto.image = imagen_tk  # ¡Importante! Debes mantener una referencia a la imagen para que no se elimine de la memoria



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)