import customtkinter
from PIL import Image, ImageTk
import language_dictionary as dic
import registro
from customtkinter import CTkImage, CTkLabel
from tkinter import Label, PhotoImage
from PIL import ImageTk
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


"""A Python script that creates a graphical user interface (GUI) using the Tkinter library.

This GUI includes buttons, labels, and options for appearance settings.

Attributes:
    green (str): A green color code.
    green_light (str): A lighter green color code.
    pink (str): A pink color code.
    grey (str): A grey color code.
"""
class Menu_principal(customtkinter.CTk):
    """Main GUI class for the application."""

    def __init__(self):
        """Initialize the Menu_principal class.

               This method sets up the GUI window, widgets, and appearance settings.

               Args:
                   None

               Returns:
                   None
               """


        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#000000"
        super().__init__()

        ScreenRes = f"{900}x{500}"
        # Here create the other windows

        self.LoginWindow = customtkinter.CTkToplevel(self)
        self.LoginWindow.withdraw()
        self.LoginWindow.geometry(ScreenRes)
        self.MembersWindow = customtkinter.CTkToplevel(self)
        self.MembersWindow.withdraw()
        self.MembersWindow.geometry(ScreenRes)
        self.PayWindow = customtkinter.CTkToplevel(self)
        self.PayWindow.withdraw()
        self.PayWindow.geometry(ScreenRes)
        """__________________________________________________________________________________________________________"""
        # configure window

        # self.attributes("-fullscreen",True)
        self.title("CustomTkinter complex_example.py")
        self.geometry(ScreenRes)
        self.current_screen = None
        self.imagen = Image.open("logo agle_sinfondo.png")

        self.foto_logo_image = ImageTk.PhotoImage(self.imagen)
        self.foto_logo = CTkLabel(self, image=self.foto_logo_image, text=None,
                               fg_color="transparent", bg_color="transparent")  # Use the background color of your main window here.
        self.foto_logo.place(relx=0.5, rely=0.3, anchor='center')

        self.sidebar_button_1 = customtkinter.CTkButton(self, command=self.sidebar_button_event, text=dic.Play[dic.language],fg_color=green_light,hover_color=green, width=250, height=50)
        self.sidebar_button_1.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        # imagen = Image.open("assets/flags/Avatar-Profile.png")
        # imagen.thumbnail((100, 100))
        # self.imagen_thumbnail_tk = ImageTk.PhotoImage(imagen)

        imagen_es = Image.open("assets/flags/Flag_of_Es.png")
        imagen_es_resized = imagen_es.resize(
            (int(23 / 100 * imagen_es.width), int(28 / 100 * imagen_es.height)), Image.ANTIALIAS)
        Es_btn_image = CTkImage(imagen_es_resized)

        # Para 'En_btn_image'
        imagen_en = Image.open("assets/flags/Flag_of_En.png")
        imagen_en_resized = imagen_en.resize(
            (int(20 / 100 * imagen_en.width), int(25 / 100 * imagen_en.height)), Image.ANTIALIAS)
        En_btn_image = CTkImage(imagen_en_resized)

        # Para 'Fr_btn_image'
        imagen_fr = Image.open("assets/flags/Flag_of_Fr.png")
        imagen_fr_resized = imagen_fr.resize(
            (int(100 / 100 * imagen_fr.width), int(100/ 100 * imagen_fr.height)), Image.ANTIALIAS)
        Fr_btn_image = CTkImage(imagen_fr_resized)

        self.languageSelector = customtkinter.CTkComboBox(self, values=["English", "Español", "Français"])
        self.languageSelector.place(relx=0.02,rely=0.05)

        self.ApplyChanges= customtkinter.CTkButton(self, text="ApplyChanges",command=lambda: [dic.changeLanguage(self.languageSelector.get()), self.ejecutar_principal()],width=5,fg_color=green)
        self.ApplyChanges.place(relx=0.02, rely=0.19)#, anchor=customtkinter.CENTER)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text=dic.Login[dic.language],fg_color=green_light,hover_color=green, command= self.ejecutar_login, width=250, height=50)
        self.sidebar_button_3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
        #
        # self.foto_label = customtkinter.CTkLabel(self, corner_radius=60)
        # self.foto_label.place(relx=1, rely=0.009, anchor=customtkinter.NE)
        # self.foto_label.configure(image=self.imagen_thumbnail_tk)
        # self.foto_label.configure()

        """_______________________________________________________________________________________________________________________"""

        self.LoginWindow.logo_label = customtkinter.CTkLabel(self.LoginWindow, text=dic.Login3[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.LoginWindow.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.LoginWindow.username = customtkinter.CTkLabel(self.LoginWindow, text=dic.Username[dic.language], anchor="w")
        self.LoginWindow.username.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        self.LoginWindow.entry_Username = customtkinter.CTkEntry(self.LoginWindow)
        self.LoginWindow.entry_Username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.LoginWindow.contra = customtkinter.CTkLabel(self.LoginWindow, text=dic.Password[dic.language], anchor="w")
        self.LoginWindow.contra.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.LoginWindow.entry_Contra = customtkinter.CTkEntry(self.LoginWindow, show="◊")
        self.LoginWindow.entry_Contra.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

        self.LoginWindow.back = customtkinter.CTkButton(self.LoginWindow, text="←", fg_color=green_light, hover_color=green,
                                            command=self.back_menu,width=30, height=30)
        self.LoginWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)

        self.LoginWindow.incio_facial = customtkinter.CTkButton(self.LoginWindow, text="Inicio facial",
                                                                fg_color=green_light,
                                                                hover_color=green, command=print("self.login_facial"))
        self.LoginWindow.incio_facial.place(relx=0.5, rely=0.53, anchor=customtkinter.CENTER)

        self.LoginWindow.sidebar_button_1 = customtkinter.CTkButton(self.LoginWindow, text=dic.Login2[dic.language], fg_color=green_light,
                                                        hover_color=green)
        self.LoginWindow.sidebar_button_1.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.LoginWindow.sidebar_button_3 = customtkinter.CTkButton(self.LoginWindow, text=dic.Register[dic.language], fg_color=green_light,
                                                        hover_color=green, command=self.RegisterUser)
        self.LoginWindow.sidebar_button_3.place(relx=0.5, rely=0.67, anchor=customtkinter.CENTER)



        """_________________________________________________________________________________________________________________"""

        self.MembersWindow.logo_label = customtkinter.CTkLabel( self.MembersWindow, text="Seleccion de membresia",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.MembersWindow.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.MembersWindow.sidebar_button_3 = customtkinter.CTkButton( self.MembersWindow, text="Miembro Gold", fg_color=green_light,
                                                        hover_color=green,
                                                        command=self.ejecutar_pago)
        self.MembersWindow.sidebar_button_3.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.MembersWindow.sidebar_button_3 = customtkinter.CTkButton( self.MembersWindow, text="Miembro Invitado", fg_color=green_light,
                                                        hover_color=green, command=self.RegisterUser)
        self.MembersWindow.sidebar_button_3.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.MembersWindow.sidebar_button_3 = customtkinter.CTkButton( self.MembersWindow, text="←", fg_color=green_light,
                                                        hover_color=green, command=self.back_menu, width=30, height=30)
        self.MembersWindow.sidebar_button_3.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)

        """______________________________________________________________________________________________________________________"""

        self.PayWindow.logo_label = customtkinter.CTkLabel( self.PayWindow, text="Transaccion",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PayWindow.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.PayWindow.logo_label = customtkinter.CTkLabel( self.PayWindow, text="Numero de tarjeta",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PayWindow.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.PayWindow.entry_Tarjeta_Numero = customtkinter.CTkEntry( self.PayWindow)
        self.PayWindow.entry_Tarjeta_Numero.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.PayWindow.logo_label = customtkinter.CTkLabel( self.PayWindow, text="fecha de vencimiento",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PayWindow.logo_label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.PayWindow.entry_Fecha = customtkinter.CTkEntry( self.PayWindow)
        self.PayWindow.entry_Fecha.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.PayWindow.logo_label = customtkinter.CTkLabel( self.PayWindow, text="numero de seguridad",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PayWindow.logo_label.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.PayWindow.entry_seguridad = customtkinter.CTkEntry( self.PayWindow)
        self.PayWindow.entry_seguridad.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.PayWindow.sidebar_button_3 = customtkinter.CTkButton( self.PayWindow, text="Ejecutar Transaccion", fg_color=green_light,
                                                        hover_color=green, command= lambda:[self.MemberChange(),self.RegisterUser()])
        self.PayWindow.sidebar_button_3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.PayWindow.back = customtkinter.CTkButton( self.PayWindow, text="←", fg_color=green_light, hover_color=green,
                                            command=self.back_menu,width=30, height=30)
        self.PayWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)
    def ejecutar_login(self):
        """Handle the 'Login' button click event.
               This method is called when the 'Login' button is clicked.
               Args:
                   None
               Returns:
                   None
               """
        self.withdraw()
        self.LoginWindow.deiconify()

        #self.destroy()
        #nuevo =Login()
       #nuevo.mainloop()

    def ejecutar_principal(self):
        """Handle the 'Ejecutar Principal' button click event.
                This method is called when the 'Ejecutar Principal' button is clicked.
                Args:
                    None
                Returns:
                    None
                """
        self.destroy()
        menu = Menu_principal()
        menu.mainloop()

    def back_menu(self):
        self.LoginWindow.withdraw()
        self.PayWindow.withdraw()
        self.MembersWindow.withdraw()
        self.deiconify()

    def quitGame(self):
        self.destroy()

    def ejecutar_pago(self):
        """Handle the 'Ejecutar Pago' button click event.

                This method is called when the 'Ejecutar Pago' button is clicked.

                Args:
                    None

                Returns:
                    None
                """
        self.withdraw()
        self.MembersWindow.withdraw()
        self.PayWindow.deiconify()

    def members_select(self):
        self.withdraw()
        self.LoginWindow.withdraw()
        self.MembersWindow.deiconify()

    def RegisterUser(self):
        self.destroy()
        registro.Registro().mainloop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Change the appearance mode of the GUI.
               This method is called to change the appearance mode of the GUI.
               Args:
                   new_appearance_mode (str): The new appearance mode to set.
               Returns:
                   None
               """
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        """Change the scaling of widgets in the GUI.
               This method is called to change the scaling of widgets in the GUI.
               Args:
                   new_scaling (str): The new scaling factor to set.
               Returns:
                   None
               """
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        """Handle the sidebar button click event.
               This method is called when a sidebar button is clicked.
               Args:
                   None
               Returns:
                   None
               """
        print("sidebar_button click")


