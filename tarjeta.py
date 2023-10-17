import tkinter.messagebox
import customtkinter

import language_dictionary as dic
import registro as register
import members as member

import menu


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Transaccion(customtkinter.CTk):
    def __init__(self):
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        font_style = ('helvic', 20)
        self.imagen_seleccionada = None
        super().__init__()

        # configure window
        # self.attributes("-fullscreen", True)
        self.title(dic.Registration[dic.language])
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)

        # create sidebar frame with widgets

        self.logo_label = customtkinter.CTkLabel(self, text="Transaccion",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)



        self.logo_label = customtkinter.CTkLabel(self, text="Numero de tarjeta", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entry_Tarjeta_Numero = customtkinter.CTkEntry(self)
        self.entry_Tarjeta_Numero.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.logo_label = customtkinter.CTkLabel(self, text="fecha de vencimiento",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Fecha = customtkinter.CTkEntry(self)
        self.entry_Fecha.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.logo_label = customtkinter.CTkLabel(self, text="numero de seguridad",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.entry_seguridad = customtkinter.CTkEntry(self)
        self.entry_seguridad.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Ejecutar Transaccion", fg_color=green_light,
                                                        hover_color=green, command=self.iniciar)
        self.sidebar_button_3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.back = customtkinter.CTkButton(self, text="Vuelta", fg_color=green_light, hover_color=green,
                                            command=self.back_to_login)
        self.back.place(relx=0.02, rely=0.05, anchor=customtkinter.NW)














    def update_edad_label(self, value):
        self.edad_label.configure(text=dic.Age[dic.language]+f" :{round(value)}")


    def iniciar(self):
        self.destroy()
        register.Registro().mainloop()


    def back_to_login(self):
        self.destroy()
        member.Membership().mainloop()


