import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import PhotoImage
from login import Login
import language_dictionary as dic
from tarjeta import Transaccion


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Menu_principal(customtkinter.CTk):
    """
       Clase que representa el menú principal de la aplicación.

       Esta clase crea una ventana de menú principal con opciones para jugar, cambiar el idioma, iniciar sesión y configurar la apariencia y escala de la interfaz.

       Args:
           Ninguno

       Attributes:
           Ninguno

       """
    def __init__(self):
        """
                Inicializa una instancia de la clase Menu_principal.

                Crea una ventana de menú principal con opciones y botones interactivos.

                """
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        super().__init__()


        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)


        # create sidebar frame with widgets



        self.logo_label = customtkinter.CTkLabel(self, text="EAGLE DEFENDER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.sidebar_button_1 = customtkinter.CTkButton(self, command=self.sidebar_button_event, text=dic.Play[dic.language],fg_color=green_light,hover_color=green)
        self.sidebar_button_1.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        Es_btn = PhotoImage(file=r"assets\flags\Flag_of_Es.png").subsample(23, 28)
        En_btn = PhotoImage(file=r"assets\flags\Flag_of_En.png").subsample(20, 25)
        Fr_btn = PhotoImage(file=r"assets\flags\Flag_of_Fr.png").subsample(10, 15)

        self.idiomaEs = customtkinter.CTkButton(self, text="", image=Es_btn, command=lambda: [dic.changeLanguage(0), self.ejecutar_principal()], width=5,fg_color=green)
        self.idiomaEn = customtkinter.CTkButton(self, text="", image=En_btn, command=lambda: [dic.changeLanguage(1), self.ejecutar_principal()],width=5,fg_color=green)
        self.idiomaFr= customtkinter.CTkButton(self, text="", image=Fr_btn,command=lambda: [dic.changeLanguage(2), self.ejecutar_principal()],width=5,fg_color=green)

        self.idiomaEn.place(relx=0.02, rely=0.05)#, anchor=customtkinter.CENTER)
        self.idiomaEs.place(relx=0.02, rely=0.12)#, anchor=customtkinter.CENTER)
        self.idiomaFr.place(relx=0.02, rely=0.19)#, anchor=customtkinter.CENTER)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text=dic.Login[dic.language],fg_color=green_light,hover_color=green, command= self.ejecutar_Ventana)
        self.sidebar_button_3.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)


        self.appearance_mode_label = customtkinter.CTkLabel(self, text=dic.AppearanceMode[dic.language], anchor="w")
        self.appearance_mode_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=[dic.Light[dic.language], dic.Dark[dic.language], dic.System[dic.language]],command=self.change_appearance_mode_event,fg_color=green_light, button_color=green)
        self.appearance_mode_optionemenu.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)


        self.scaling_label = customtkinter.CTkLabel(self, text=dic.UI_Cof[dic.language]+":", anchor="w")
        self.scaling_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["100%", "90%", "80%", "110%", "120%"],command=self.change_scaling_event,fg_color=green_light, button_color=green)
        self.scaling_optionemenu.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.sidebar_button_1 = customtkinter.CTkButton(self,text="💳", fg_color=green_light,hover_color=green, command=self.ejecutar_pago)
        self.sidebar_button_1.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

    def ejecutar_Ventana(self):
        """
         Abre la ventana de inicio de sesión al hacer clic en el botón "Login".

         Args:
             Ninguno

         Returns:
             Ninguno

         """
        self.destroy()
        nuevo =Login()
        nuevo.mainloop()

    def ejecutar_principal(self):

        """
        Abre la ventana del menú principal al cambiar el idioma.

        Args:
            Ninguno

        Returns:
            Ninguno

        """

        self.destroy()
        menu = Menu_principal()
        menu.mainloop()


    def ejecutar_pago(self):
        """
                Abre la ventana de transacciones al hacer clic en el botón "💳".

                Args:
                    Ninguno

                Returns:
                    Ninguno

                """
        self.destroy()
        menu = Transaccion()
        menu.mainloop()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")





