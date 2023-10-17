import customtkinter
import language_dictionary as dic
from tarjeta import Transaccion
import login as log
import registro as register


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Membership(customtkinter.CTk):
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

        self.logo_label = customtkinter.CTkLabel(self, text="Seleccion de membresia",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Miembro Gold", fg_color=green_light,
                                                        hover_color=green,
                                                        command=  self.go_transaction)
        self.sidebar_button_3.place(relx=0.5, rely=0.4, anchor=customtkinter.E)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Miembro Invitado", fg_color=green_light,
                                                        hover_color=green, command=self.change_member_guest)
        self.sidebar_button_3.place(relx=0.5, rely=0.4, anchor=customtkinter.W)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Vuelta", fg_color=green_light,
                                                        hover_color=green, command=self.back_menu)
        self.sidebar_button_3.place(relx=0.02, rely=0.05, anchor=customtkinter.NW)

    def go_transaction(self):
        self.destroy()
        men = Transaccion()
        men.mainloop()

    def change_member_guest(self):
        self.destroy()
        dic.MEMBER = 0
        register.Registro().mainloop()

    def back_menu(self):
        self.destroy()
        log.Login().mainloop()
