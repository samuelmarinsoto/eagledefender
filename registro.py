import tkinter
import tkinter.messagebox
import customtkinter


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Registro(customtkinter.CTk):
    def __init__(self):
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        super().__init__()

        # configure window
        self.title("Log In ")
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)

        # create sidebar frame with widgets

        self.tabview = customtkinter.CTkTabview(self, width=400, height=400, )
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add("Datos")
        self.tabview.add("Juego")
        self.tabview.add("Personalizacion")
        self.tabview.tab("Datos").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Juego").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Datos"), dynamic_resizing=False,values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Registro", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.username = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Username", anchor="w")
        self.username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        self.entry_Username = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.entry_Username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self.tabview.tab("Datos"), text="Contraseña", anchor="w")
        self.contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab("Datos"), show = "◊")
        self.entry_Contra.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)


        self.nombre = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.nombre.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.apellido = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.apellido.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.cancion_Favorita = customtkinter.CTkEntry(self.tabview.tab("Datos"))
        self.cancion_Favorita.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)





        self.sidebar_button_3 = customtkinter.CTkButton(self.tabview.tab("Datos"),fg_color=green_light,hover_color=green)
        self.sidebar_button_3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)




    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)