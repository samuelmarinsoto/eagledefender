import customtkinter
from PIL import Image, ImageTk, ImageDraw
import tkinter.filedialog as filedialog
from tkinter import PhotoImage
import language_dictionary as dic
import registro as registro
from customtkinter import CTkImage, CTkLabel
from tkinter import Label, PhotoImage
import warnings
import tkinter
warnings.simplefilter(action='ignore', category=UserWarning)
from login import Login
import tkinter.messagebox
import DataBaseLocal as DataBase
import users as users
import juegoinit
import re
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

        ScreenRes = f"{1024}x{720}"
        # Here create the other windows

        self.LoginWindow = customtkinter.CTkToplevel(self)
        self.LoginWindow.withdraw()
        self.LoginWindow.geometry(ScreenRes)
        self.MembersWindow = customtkinter.CTkToplevel(self)
        self.MembersWindow.withdraw()
        self.MembersWindow.geometry(ScreenRes)
        self.PlayWindow = customtkinter.CTkToplevel(self)
        self.PlayWindow.withdraw()
        self.PlayWindow.geometry(ScreenRes)
        """__________________________________________________________________________________________________________"""
        # configure window

        # self.attributes("-fullscreen",True)
        self.title("CustomTkinter complex_example.py")
        self.geometry(ScreenRes)
        self.current_screen = None
        self.imagen = Image.open("../assets/Windows aux/logo agle_sinfondo.png")

        self.foto_logo_image = ImageTk.PhotoImage(self.imagen)
        self.foto_logo = CTkLabel(self, image=self.foto_logo_image, text=None,
                               fg_color="transparent", bg_color="transparent")  # Use the background color of your main window here.
        self.foto_logo.place(relx=0.5, rely=0.3, anchor='center')

        self.sidebar_button_1 = customtkinter.CTkButton(self, command=self.ejecutar_play, text=dic.Play[dic.language],fg_color=green_light,hover_color=green, width=250, height=50)
        self.sidebar_button_1.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        # imagen = Image.open("assets/flags/Avatar-Profile.png")
        # imagen.thumbnail((100, 100))
        # self.imagen_thumbnail_tk = ImageTk.PhotoImage(imagen)
        """"
        imagen_es = Image.open("../assets/flags/Flag_of_Es.png")
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
        Fr_btn_image = CTkImage(imagen_fr_resized)"""

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
                                                                hover_color=green, command=self.start_facial_login)
        self.LoginWindow.incio_facial.place(relx=0.5, rely=0.53, anchor=customtkinter.CENTER)

        self.LoginWindow.sidebar_button_1 = customtkinter.CTkButton(self.LoginWindow, text=dic.Login2[dic.language],
                                                                    fg_color=green_light,
                                                                    hover_color=green,
                                                                    command=self.login_with_username_and_password)

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


        self.PlayWindow.back = customtkinter.CTkButton( self.PlayWindow, text="←", fg_color=green_light, hover_color=green,
                                            command=self.back_menu,width=30, height=30)
        self.PlayWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)


        imagenOne = Image.open("../assets/Windows aux/OnePlayer.png")
        imagenOne_resized = imagenOne.resize((220,220), Image.LANCZOS)
        phOne = ImageTk.PhotoImage(imagenOne_resized)


        imagenTwo = Image.open("../assets/Windows aux/TwoPlayer.png")
        imagenTwo_resized =  imagenTwo.resize((220,220), Image.LANCZOS)
        phTwo = ImageTk.PhotoImage(imagenTwo_resized)


        self.PlayWindow.logo_label = customtkinter.CTkLabel( self.PlayWindow, text=dic.SelectModegame[dic.language],font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PlayWindow.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.PlayWindow.Oneplayer = customtkinter.CTkButton( self.PlayWindow, text=dic.OnePlayer[dic.language],image=phOne,fg_color=green_light,hover_color=green,command=self.ejecutar_Game_OnePlayer)
        self.PlayWindow.Oneplayer.place(relx=0.25, rely=0.5, anchor=customtkinter.CENTER)
        
        self.PlayWindow.Twoplayer = customtkinter.CTkButton( self.PlayWindow, text=dic.MultiplayerLocal[dic.language],image=phTwo,fg_color=green_light,hover_color=green,command=self.ejecutar_Game_Multiplayer)
        self.PlayWindow.Twoplayer.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

        self.selected_photo_path = "../assets/flags/Avatar-Profile.png"
        default_image = Image.open(self.selected_photo_path)
        default_image = default_image.resize((100, 100), Image.LANCZOS)
        default_imageop = ImageTk.PhotoImage(default_image)

        self.PlayWindow.Player1Pic = customtkinter.CTkLabel(self.PlayWindow, image=default_imageop, corner_radius=60, text="")
        self.PlayWindow.Player1Pic.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

        self.PlayWindow.Player2Pic = customtkinter.CTkLabel(self.PlayWindow, image=default_imageop, corner_radius=60,text="")
        self.PlayWindow.Player2Pic.place(relx=0.9, rely=0.2, anchor=customtkinter.CENTER)


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
    def start_facial_login(self):
        username = self.LoginWindow.entry_Username.get()
        login_instance = Login()  # crea una instancia de la clase Login
        success = login_instance.login_f(username)

        if success:
            # Aquí puedes agregar el código que quieres ejecutar si el inicio facial es exitoso.
            # Por ejemplo, puedes mostrar la ventana principal o mostrar un mensaje de éxito.
            self.PlayWindow.deiconify()
            self.LoginWindow.withdraw()
            tkinter.messagebox.showinfo(title='Inicio facial exitoso', message='Inicio facial exitoso')

        else:
            # Aquí puedes agregar el código que quieres ejecutar si el inicio facial falla.
            tkinter.messagebox.showerror(title='Error', message='Inicio facial fallido. Por favor, inténtalo de nuevo.')


    def login_with_username_and_password(self):
        global username
        username = self.LoginWindow.entry_Username.get()  # Obtiene el nombre de usuario del widget de entrada
        password = self.LoginWindow.entry_Contra.get()  # Obtiene la contraseña del widget de entrada

        if DataBase.validate_user(username, password):
            # Si el inicio de sesión es exitoso
            USERname = DataBase.get_user_by_username(username)[2]
            Pic = DataBase.get_user_by_username(username)[7]
            Merbership = DataBase.get_user_by_username(username)[8]
            Song1 = DataBase.get_user_by_username(username)[9]
            Song2 = DataBase.get_user_by_username(username)[10]
            Song3 = DataBase.get_user_by_username(username)[11]
            Texture = DataBase.get_user_by_username(username)[15]
            Palette = DataBase.get_user_by_username(username)[16]
            if not users.player1.verify_log(users.player1.texture, users.player1.palette_color):
                self.abrir_archivo(1,Pic)
                users.player1.update_Username(USERname)
                users.player1.update_pathimage(Pic)
                users.player1.update_membership(Merbership)
                users.player1.update_song1(Song1)
                users.player1.update_song2(Song2)
                users.player1.update_song3(Song3)
                users.player1.update_texture(Texture)
                users.player1.update_palette_color(Palette)
                print("Doit",Pic)
            elif not users.player1.Username == USERname:
                self.abrir_archivo(2,Pic)
                users.player2.update_Username(USERname)
                users.player2.update_pathimage(Pic)
                users.player2.update_membership(Merbership)
                users.player2.update_song1(Song1)
                users.player2.update_song2(Song2)
                users.player2.update_song3(Song3)
                users.player2.update_texture(Texture)
                users.player2.update_palette_color(Palette)
                users.player2.display_customization()
                print("Doit2")
            else:
                tkinter.messagebox.showerror("Error", "No se puede logear con el mismo usuario")
                return 0
                
            self.PlayWindow.deiconify()
            self.LoginWindow.withdraw()
        else:
            # Si el inicio de sesión falla
            tkinter.messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

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
        self.PlayWindow.withdraw()
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
        self.PlayWindow.deiconify()

    def members_select(self):
        self.withdraw()
        self.LoginWindow.withdraw()
        self.MembersWindow.deiconify()

    def RegisterUser(self):
        self.destroy()
        registro.Registro().mainloop()

    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     """Change the appearance mode of the GUI.
    #            This method is called to change the appearance mode of the GUI.
    #            Args:
    #                new_appearance_mode (str): The new appearance mode to set.
    #            Returns:
    #                None
    #            """
    #     customtkinter.set_appearance_mode(new_appearance_mode)
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

    def ejecutar_play(self):
        #if Logged1(Player):
        self.withdraw()
        self.PlayWindow.deiconify()
        #else:
            #self.PlayWindow.withdraw()
            #self.LoginWindow.deiconify()


    def ejecutar_Game_Multiplayer(self):


        if users.player1.verify_log(users.player1.texture, users.player1.palette_color) and users.player2.verify_log(users.player2.texture, users.player2.palette_color):
            juegoinit.iniciar()
        else:
            tkinter.messagebox.showerror("Error", "No hay suficientes jugadores logeados")
            self.PlayWindow.withdraw()
            self.LoginWindow.deiconify()
        
        
    def ejecutar_Game_OnePlayer(self):


        if users.player1.verify_log(users.player1.texture, users.player1.palette_color):
            juegoAI.iniciar()
        else:
            self.PlayWindow.withdraw()
            self.LoginWindow.deiconify()
        """
        Example
        if Logged1(Player):
            self.destroy()
            pygame.init()
        else:
            self.PlayWindow.withdraw()
            self.LoginWindow.deiconify()
            
       """


    def abrir_archivo(self,player,archivo):
        #archivo = filedialog.askopenfilename(filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])
        if archivo:
            #self.selected_photo_path = archivo
                # Cargar la imagen
            imagen = Image.open(archivo)
            imagen = imagen.resize((100, 100), Image.LANCZOS)
            circular = self.make_circle_image(imagen)
            Imagentk = ImageTk.PhotoImage(circular)

        if player == 1:
            self.PlayWindow.Player1Pic.configure(image=Imagentk)
            self.PlayWindow.Player1Pic.image = Imagentk

        elif player == 2:
            self.PlayWindow.Player2Pic.configure(image=Imagentk)
            self.PlayWindow.Player2Pic.image = Imagentk
        else:
            tkinter.messagebox.showerror("Error", "No se actualizo la imagen de perfil")
            return 0

    @staticmethod
    def make_circle_image(img):
        """
            Convert an image into a circular image.
        """

        img = img.convert("RGBA")


        mask = Image.new("L", img.size, 0)


        draw = ImageDraw.Draw(mask)
        width, height = img.size
        draw.ellipse((0, 0, width, height), fill=255)


        circular_img = Image.composite(img, Image.new("RGBA", img.size, (255, 255, 255, 0)), mask)
        return circular_img
