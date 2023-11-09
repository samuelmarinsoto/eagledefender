import customtkinter
from PIL import Image, ImageTk, ImageDraw
import language_dictionary as dic
import registro as registro
from customtkinter import CTkImage, CTkLabel
import warnings
import tkinter
warnings.simplefilter(action='ignore', category=UserWarning)
from login import Login
import tkinter.messagebox
import DataBaseLocal as DataBase
import users as users
import juegoinit
import juegoAI
import HallFame
import datauser as dt
from tkcalendar import Calendar
from datetime import date
import tkinter.filedialog as filedialog
import LanguageDictionary as Lg
from tkinter import PhotoImage
import spot
import os
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
        self.HallOfFame = customtkinter.CTkToplevel(self)
        self.HallOfFame.withdraw()
        self.HallOfFame.geometry(ScreenRes)
        self.RegisterWindow = customtkinter.CTkToplevel(self)
        self.RegisterWindow.withdraw()
        self.RegisterWindow.geometry(ScreenRes)
        self.PersonalizeWindow = customtkinter.CTkToplevel(self)
        self.PersonalizeWindow.withdraw()
        self.PersonalizeWindow.geometry(ScreenRes)
        self.PersonalizeWindow2 = customtkinter.CTkToplevel(self)
        self.PersonalizeWindow2.withdraw()
        self.PersonalizeWindow2.geometry(ScreenRes)
        self.MusicWindow = customtkinter.CTkToplevel(self)
        self.MusicWindow.withdraw()
        self.MusicWindow.geometry(ScreenRes)

        self.LoginWindow.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.MembersWindow.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.PlayWindow.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.HallOfFame.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.RegisterWindow.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.PersonalizeWindow.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.PersonalizeWindow2.protocol("WM_DELETE_WINDOW", self.back_menu)
        self.MusicWindow.protocol("WM_DELETE_WINDOW", self.back_menu)
        """__________________________________________________________________________________________________________"""
        # # configure window
        # self.attributes("-fullscreen",True)
        # self.LoginWindow.attributes("-fullscreen",True)
        # self.MembersWindow.attributes("-fullscreen",True)
        # self.PlayWindow.attributes("-fullscreen",True)
        # self.HallOfFame.attributes("-fullscreen",True)
        # self.RegisterWindow.attributes("-fullscreen",True)
        # self.PersonalizeWindow.attributes("-fullscreen",True)
        # self.PersonalizeWindow2.attributes("-fullscreen",True)
        # self.MusicWindow.attributes("-fullscreen",True)

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

        self.QUIT = customtkinter.CTkButton(self, text="X",fg_color=green_light,hover_color=green, command=self.quit, width=30, height=30)
        self.QUIT.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)
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

        self.LoginWindow.sidebar_button_1 = customtkinter.CTkButton(self.LoginWindow, text=dic.Login2[dic.language],fg_color=green_light,hover_color=green, command=self.login_with_username_and_password)
        self.LoginWindow.sidebar_button_1.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.LoginWindow.sidebar_button_3 = customtkinter.CTkButton(self.LoginWindow, text=dic.Register[dic.language], fg_color=green_light, hover_color=green, command=self.ejecutar_register)
        self.LoginWindow.sidebar_button_3.place(relx=0.5, rely=0.67, anchor=customtkinter.CENTER)


        """_________________________________________________________________________________________________________________"""


        self.PlayWindow.back = customtkinter.CTkButton( self.PlayWindow, text="←", fg_color=green_light, hover_color=green,
                                            command=self.back_menu,width=30, height=30)
        self.PlayWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)


        imagenOne = Image.open("../assets/Windows aux/OnePlayer.png")
        imagenOne_resized = imagenOne.resize((220,220), Image.LANCZOS)
        phOne = ImageTk.PhotoImage(imagenOne_resized)


        imagenTwo = Image.open("../assets/Windows aux/TwoPlayer.png")
        imagenTwo_resized =  imagenTwo.resize((400,400), Image.LANCZOS)
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
        self.default_imageop = ImageTk.PhotoImage(default_image)

        self.PlayWindow.Player1Pic = customtkinter.CTkLabel(self.PlayWindow, image=self.default_imageop, corner_radius=60, text="")
        self.PlayWindow.Player1Pic.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

        self.PlayWindow.Player2Pic = customtkinter.CTkLabel(self.PlayWindow, image=self.default_imageop, corner_radius=60,text="")
        self.PlayWindow.Player2Pic.place(relx=0.9, rely=0.2, anchor=customtkinter.CENTER)
        self.BtnFame = customtkinter.CTkButton(self.PlayWindow, text="hall of fame",
                                                  fg_color=green_light, hover_color=green, command= lambda:  [self.update_hall_of_fame(),self.update_hall_of_fame_scores() ,self.HallOfFame_select()])
        self.BtnFame.place(relx=0.1, rely=0.95, anchor=customtkinter.CENTER)
        #-------------------------------------------------------------------------------------------------------------
        self.selected_photo_path = "../assets/flags/Avatar-Profile.png"
        default_image2 = Image.open(self.selected_photo_path)
        default_image2 = default_image2.resize((40, 40), Image.LANCZOS)
        self.default_imageop3 = ImageTk.PhotoImage(default_image2)
        self.selected_photo_path = "../assets/flags/Podium.png"
        default_image3 = Image.open(self.selected_photo_path)
        default_image3 = default_image3.resize((500, 500), Image.LANCZOS)
        self.default_imageop2 = ImageTk.PhotoImage(default_image3)

        self.HallOfFame.Podium = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop2,
                                                        corner_radius=60, text="")
        self.HallOfFame.Podium.place(relx=0.25, rely=0.5, anchor=customtkinter.CENTER)

        self.HallOfFame.back = customtkinter.CTkButton(self.HallOfFame, text="←", fg_color=green_light,
                                                       hover_color=green,
                                                       command=self.ejecutar_play, width=30, height=30)
        self.HallOfFame.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)

        self.HallOfFame.logo_label = customtkinter.CTkLabel(self.HallOfFame, text="Hall of Fame", font=customtkinter.CTkFont(size=20, weight="bold"))








        self.backgroundTop = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#303044", width= 500, height= 600, corner_radius= 60)
        self.backgroundTop.place(relx=0.75, rely=0.5, anchor=customtkinter.CENTER)

        self.backgroundTopTile = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824",bg_color="#303044" , width = 450, height= 40, corner_radius= 60)
        self.backgroundTopTile.place(relx=0.75, rely=0.14, anchor=customtkinter.CENTER)

        self.rank = customtkinter.CTkLabel(self.HallOfFame, text="Rank",  width = 55, height= 35, corner_radius= 60, font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#181824", fg_color="#303044")
        self.rank.place(relx=0.65, rely=0.14, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.HallOfFame, text="Username", width=55, height=35, corner_radius=60,
                                           font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#181824",
                                           fg_color="#303044")
        self.username.place(relx=0.775, rely=0.14, anchor=customtkinter.CENTER)

        self.score = customtkinter.CTkLabel(self.HallOfFame, text="Score", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#181824",
                                               fg_color="#303044")
        self.score.place(relx=0.9, rely=0.14, anchor=customtkinter.CENTER)

        self.backgroundTop1Name= customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#EDB93F" ,width= 110, height= 40, corner_radius= 60)
        self.backgroundTop1Name.place(relx=0.25, rely=0.56, anchor=customtkinter.CENTER)

        self.backgroundTop2Name = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824",bg_color="#89A3BC" , width = 110, height= 40, corner_radius= 60)
        self.backgroundTop2Name.place(relx=0.118, rely=0.645, anchor=customtkinter.CENTER)

        self.backgroundTop3Name = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#A15347" ,width= 110, height= 40, corner_radius= 60)
        self.backgroundTop3Name.place(relx=0.382, rely=0.71, anchor=customtkinter.CENTER)
        self.top1score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#EDB93F",
                                                     width=110, height=30, corner_radius=60)

        self.backgroundTop4 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                             bg_color="#303044", width=450, height=55, corner_radius=22)
        self.backgroundTop4.place(relx=0.75, rely=0.25, anchor=customtkinter.CENTER)

        self.backgroundTop5 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                                bg_color="#303044", width=450, height=55, corner_radius=22)
        self.backgroundTop5.place(relx=0.75, rely=0.35, anchor=customtkinter.CENTER)



        self.backgroundTop6 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                                bg_color="#303044", width=450, height=50, corner_radius=22)
        self.backgroundTop6.place(relx=0.75, rely=0.45, anchor=customtkinter.CENTER)

        self.backgroundTop7 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                                bg_color="#303044", width=450, height=50, corner_radius=22)
        self.backgroundTop7.place(relx=0.75, rely=0.55, anchor=customtkinter.CENTER)

        self.backgroundTop8 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                                bg_color="#303044", width=450, height=50, corner_radius=22)
        self.backgroundTop8.place(relx=0.75, rely=0.65, anchor=customtkinter.CENTER)

        self.backgroundTop9 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                                bg_color="#303044", width=450, height=50, corner_radius=22)
        self.backgroundTop9.place(relx=0.75, rely=0.75, anchor=customtkinter.CENTER)


        self.backgroundTop10 = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#232334",
                                                                bg_color="#303044", width=450, height=50, corner_radius=22)
        self.backgroundTop10.place(relx=0.75, rely=0.85, anchor=customtkinter.CENTER)

        """ranks#"""
        self.ranktop4 = customtkinter.CTkLabel(self.HallOfFame, text="#4", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                               fg_color="#181824")
        self.ranktop4.place(relx=0.65, rely=0.25, anchor=customtkinter.CENTER)
        self.ranktop5 = customtkinter.CTkLabel(self.HallOfFame, text="#5", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                               fg_color="#181824")
        self.ranktop5.place(relx=0.65, rely=0.35, anchor=customtkinter.CENTER)
        self.ranktop6 = customtkinter.CTkLabel(self.HallOfFame, text="#6", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                               fg_color="#181824")
        self.ranktop6.place(relx=0.65, rely=0.45, anchor=customtkinter.CENTER)
        self.ranktop7 = customtkinter.CTkLabel(self.HallOfFame, text="#7", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                               fg_color="#181824")
        self.ranktop7.place(relx=0.65, rely=0.55, anchor=customtkinter.CENTER)
        self.ranktop8 = customtkinter.CTkLabel(self.HallOfFame, text="#8", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                               fg_color="#181824")
        self.ranktop8.place(relx=0.65, rely=0.65, anchor=customtkinter.CENTER)
        self.ranktop9 = customtkinter.CTkLabel(self.HallOfFame, text="#9", width=55, height=35, corner_radius=60,
                                               font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                               fg_color="#181824")
        self.ranktop9.place(relx=0.65, rely=0.75, anchor=customtkinter.CENTER)

        self.ranktop10 = customtkinter.CTkLabel(self.HallOfFame, text="#10", width=55, height=35, corner_radius=60,
                                                    font=customtkinter.CTkFont(size=16, weight="bold"), bg_color="#232334",
                                                    fg_color="#181824")
        self.ranktop10.place(relx=0.65, rely=0.85, anchor=customtkinter.CENTER)

        """NOmbres"""



        # Player 1 Name Label
        self.HallOfFame.Player1Name = customtkinter.CTkLabel(self.HallOfFame, text="Player1", fg_color="#EDB93F",
                                                             bg_color="#181824", corner_radius=60,text_color="BLACK",
                                                             font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player1Name.place(relx=0.25, rely=0.56, anchor=customtkinter.CENTER)

        # Player 2 Name Label
        self.HallOfFame.Player2Name = customtkinter.CTkLabel(self.HallOfFame, text="Player2", fg_color="#89A3BC",
                                                             bg_color="#181824", corner_radius=60,
                                                             font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player2Name.place(relx=0.12, rely=0.645, anchor=customtkinter.CENTER)

        # Player 3 Name Label
        self.HallOfFame.Player3Name = customtkinter.CTkLabel(self.HallOfFame, text="Player3", fg_color="#A15347",
                                                             bg_color="#181824", corner_radius=60,
                                                             font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player3Name.place(relx=0.38, rely=0.71, anchor=customtkinter.CENTER)

        self.HallOfFame.Player4Name = customtkinter.CTkLabel(self.HallOfFame, text="Player4", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player4Name.place(relx=0.775, rely=0.25, anchor=customtkinter.CENTER)

        self.HallOfFame.Player5Name = customtkinter.CTkLabel(self.HallOfFame, text="Player5", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player5Name.place(relx=0.775, rely=0.35, anchor=customtkinter.CENTER)

        self.HallOfFame.Player6Name = customtkinter.CTkLabel(self.HallOfFame, text="Player6", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player6Name.place(relx=0.775, rely=0.45, anchor=customtkinter.CENTER)

        self.HallOfFame.Player7Name = customtkinter.CTkLabel(self.HallOfFame, text="Player7", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player7Name.place(relx=0.775, rely=0.55, anchor=customtkinter.CENTER)

        self.HallOfFame.Player8Name = customtkinter.CTkLabel(self.HallOfFame, text="Player8", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player8Name.place(relx=0.775, rely=0.65, anchor=customtkinter.CENTER)

        self.HallOfFame.Player9Name = customtkinter.CTkLabel(self.HallOfFame, text="Player9", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player9Name.place(relx=0.775, rely=0.75, anchor=customtkinter.CENTER)

        self.HallOfFame.Player10Name = customtkinter.CTkLabel(self.HallOfFame, text="Player10", fg_color="#181824",
                                                                bg_color="#232334", corner_radius=60,
                                                                font=customtkinter.CTkFont(size=9, weight="bold"))
        self.HallOfFame.Player10Name.place(relx=0.775, rely=0.85, anchor=customtkinter.CENTER)





        """Score"""
        self.top1score.place(relx=0.25, rely=0.615, anchor=customtkinter.CENTER)

        self.top2score = customtkinter.CTkLabel(self.HallOfFame, text="Score", fg_color="#181824", bg_color="#89A3BC",
                                                width=110, height=30, corner_radius=60)
        self.top2score.place(relx=0.118, rely=0.7, anchor=customtkinter.CENTER)

        self.top3score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#A15347",
                                                width=110, height=30, corner_radius=60)
        self.top3score.place(relx=0.382, rely=0.765, anchor=customtkinter.CENTER)

        self.top4score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                width=70, height=35, corner_radius=22)
        self.top4score.place(relx=0.9, rely=0.25, anchor=customtkinter.CENTER)

        self.top5score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                width=70, height=35, corner_radius=22)
        self.top5score.place(relx=0.9, rely=0.35, anchor=customtkinter.CENTER)

        self.top6score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                width=70, height=35, corner_radius=22)
        self.top6score.place(relx=0.9, rely=0.45, anchor=customtkinter.CENTER)

        self.top7score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                width=70, height=35, corner_radius=22)
        self.top7score.place(relx=0.9, rely=0.55, anchor=customtkinter.CENTER)

        self.top8score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                width=70, height=35, corner_radius=22)
        self.top8score.place(relx=0.9, rely=0.65, anchor=customtkinter.CENTER)

        self.top9score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                width=70, height=35, corner_radius=22)
        self.top9score.place(relx=0.9, rely=0.75, anchor=customtkinter.CENTER)

        self.top10score = customtkinter.CTkLabel(self.HallOfFame, text="", fg_color="#181824", bg_color="#232334",
                                                    width=70, height=35, corner_radius=22)
        self.top10score.place(relx=0.9, rely=0.85, anchor=customtkinter.CENTER)

        """ProfilePics"""
        self.HallOfFame.Player1Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#EDB93F",
                                                            bg_color="#EDB93F")
        self.HallOfFame.Player1Pic.place(relx=0.25, rely=0.375, anchor=customtkinter.CENTER)

        self.HallOfFame.Player2Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=100, text="", fg_color="#89A3BC",
                                                            bg_color="#89A3BC")
        self.HallOfFame.Player2Pic.place(relx=0.118, rely=0.46, anchor=customtkinter.CENTER)

        self.HallOfFame.Player3Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#A15347",
                                                            bg_color="#A15347")
        self.HallOfFame.Player3Pic.place(relx=0.383, rely=0.525, anchor=customtkinter.CENTER)

        self.HallOfFame.Player4Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player4Pic.place(relx=0.575, rely=0.25, anchor=customtkinter.CENTER)

        self.HallOfFame.Player5Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player5Pic.place(relx=0.575, rely=0.35, anchor=customtkinter.CENTER)

        self.HallOfFame.Player6Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player6Pic.place(relx=0.575, rely=0.45, anchor=customtkinter.CENTER)

        self.HallOfFame.Player7Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player7Pic.place(relx=0.575, rely=0.55, anchor=customtkinter.CENTER)

        self.HallOfFame.Player8Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player8Pic.place(relx=0.575, rely=0.65, anchor=customtkinter.CENTER)

        self.HallOfFame.Player9Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player9Pic.place(relx=0.575, rely=0.75, anchor=customtkinter.CENTER)

        self.HallOfFame.Player10Pic = customtkinter.CTkLabel(self.HallOfFame, image=self.default_imageop3,
                                                            corner_radius=60, text="", fg_color="#232334",
                                                            bg_color="#232334")
        self.HallOfFame.Player10Pic.place(relx=0.575, rely=0.85, anchor=customtkinter.CENTER)

        #-------------------------------------------------------------------------------------------------------------

        self.RegisterWindow.back = customtkinter.CTkButton(self.RegisterWindow,text="←", fg_color=green_light,  hover_color=green, command=self.ejecutar_login,width=30, height=30)
        self.RegisterWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)
        self.RegisterWindow.logo_label = customtkinter.CTkLabel(self.RegisterWindow, text=dic.Register[dic.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.RegisterWindow.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.RegisterWindow.entry_Nombre = customtkinter.CTkEntry(self.RegisterWindow, placeholder_text=dic.Name[dic.language])
        self.RegisterWindow.entry_Nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.RegisterWindow.entry_Apellido = customtkinter.CTkEntry(self.RegisterWindow, placeholder_text=dic.Surname[dic.language])
        self.RegisterWindow.entry_Apellido.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

        self.RegisterWindow.entry_Correo = customtkinter.CTkEntry(self.RegisterWindow, placeholder_text=dic.Email[dic.language])
        self.RegisterWindow.entry_Correo.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        self.RegisterWindow.edad_label = customtkinter.CTkLabel(self.RegisterWindow, text=dic.Age[dic.language] + ": 0")
        self.RegisterWindow.edad_label.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

        self.age = 0
        self.RegisterWindow.calendario = Calendar(self.RegisterWindow, mindate=date(1930, 1, 1), maxdate=date.today())
        self.RegisterWindow.calendario.place_forget()
        self.RegisterWindow.edad_button = customtkinter.CTkButton(self.RegisterWindow, text="Confirmar fecha",fg_color=green_light, hover_color=green,command=lambda: [self.data_select(), self.toggle_calendar()])

        self.RegisterWindow.calendario_button = customtkinter.CTkButton(self.RegisterWindow, text="Whats your birthday?", fg_color=green_light, hover_color=green, command=self.toggle_calendar)
        self.RegisterWindow.calendario_button.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.RegisterWindow.entry_Username = customtkinter.CTkEntry(self.RegisterWindow,placeholder_text=dic.Username[dic.language])
        self.RegisterWindow.entry_Username.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
        self.RegisterWindow.entry_Contra = customtkinter.CTkEntry(self.RegisterWindow, show="◊",placeholder_text=dic.Password[dic.language])
        self.RegisterWindow.entry_Contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.RegisterWindow.entry_Contra_check = customtkinter.CTkEntry(self.RegisterWindow, show="◊",placeholder_text=dic.VerifyPassword[dic.language])
        self.RegisterWindow.entry_Contra_check.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)
        self.RegisterWindow.toggle_btn = customtkinter.CTkButton(self.RegisterWindow, text="⦾",fg_color=green_light, hover_color=green, command=self.toggle_password_visibility,width=30, height=30)
        self.RegisterWindow.toggle_btn.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)
        self.RegisterWindow.toggle_btn2 = customtkinter.CTkButton(self.RegisterWindow, text="⦾",fg_color=green_light, hover_color=green, command=self.toggle_password_visibility2,width=30, height=30)
        self.RegisterWindow.toggle_btn2.place(relx=0.6, rely=0.55, anchor=customtkinter.CENTER)

        self.RegisterWindow.avatar_label = customtkinter.CTkLabel(self.RegisterWindow, image=self.default_imageop,corner_radius=60, text="")
        self.RegisterWindow.avatar_label.place(relx=0.35, rely=0.7, anchor=customtkinter.CENTER)

        self.RegisterWindow.subir_Foto = customtkinter.CTkButton(self.RegisterWindow,text="✚", hover=True,fg_color=green_light,hover_color=green,corner_radius=50,height=10,width=10,bg_color="transparent", command=self.set_register_pic)
        self.RegisterWindow.subir_Foto.place(relx=0.35, rely=0.75, anchor=customtkinter.CENTER)

        self.RegisterWindow.Continue = customtkinter.CTkButton(self.RegisterWindow, text="Continuar",fg_color=green_light, hover_color=green, command=self.ejecutar_perzonalizar)
        self.RegisterWindow.Continue.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
        #-------------------------------------------------------------------------------------------------------------
        self.Member = False
        self.PersonalizeWindow.back = customtkinter.CTkButton(self.PersonalizeWindow, text="←", fg_color=green_light, hover_color=green,command=self.ejecutar_backperzonalizar, width=30, height=30)
        self.PersonalizeWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)

        self.PersonalizeWindow.logo_label = customtkinter.CTkLabel(self.PersonalizeWindow,  text=Lg.dic["Costumes in Game"][Lg.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PersonalizeWindow.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.PersonalizeWindow.skip = customtkinter.CTkButton(self.PersonalizeWindow, text="Skip",fg_color=green_light, hover_color=green, command=self.ConcludeRegisterSkip)
        self.PersonalizeWindow.skip.place(relx=0.1, rely=0.9, anchor=customtkinter.CENTER)

        self.PersonalizeWindow.next = customtkinter.CTkButton(self.PersonalizeWindow ,  text="→",fg_color=green_light, hover_color=green, command=self.ejecutar_perzonalizar2)
        self.PersonalizeWindow.next.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)
        self.PersonalizeWindow.advice = customtkinter.CTkLabel(self.PersonalizeWindow, text=Lg.dic["Personalization is a unique feature for gold members "][Lg.language], font=customtkinter.CTkFont(size=10, weight="bold"))
        self.PersonalizeWindow.advice.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.PersonalizeWindow.scenarytxt = customtkinter.CTkLabel(self.PersonalizeWindow, text=Lg.dic["Select your scenario"][Lg.language], font=customtkinter.CTkFont(size=15, weight="bold"))
        self.PersonalizeWindow.scenarytxt.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        block1Metal = PhotoImage(file="../assets/Blocks/bloquemetal.png").subsample(7, 7)
        block1Wood = PhotoImage(file="../assets/Blocks/bloquemadera.png").subsample(6, 6)
        block1Cement = PhotoImage(file="../assets/Blocks/bloqueconcreto.png").subsample(6, 6)

        block2Metal = PhotoImage(file="../assets/Blocks/Block2Metal.png").subsample(3, 3)
        block2Wood = PhotoImage(file="../assets/Blocks/Block2Wood.png").subsample(3, 3)
        block2Cement = PhotoImage(file="../assets/Blocks/Block2Cement.png").subsample(3, 3)

        block3Metal = PhotoImage(file="../assets/Blocks/Block3Metal.png").subsample(1, 1)
        block3Wood = PhotoImage(file="../assets/Blocks/Block3Wood.png").subsample(1, 1)
        block3Cement = PhotoImage(file="../assets/Blocks/Block3Cement.png").subsample(1, 1)

        paletteRed = PhotoImage(file="../assets/Palettes/Red.png").subsample(5, 5)
        paletteWhite = PhotoImage(file="../assets/Palettes/White.png").subsample(5, 5)
        paletteGreen = PhotoImage(file="../assets/Palettes/Green.png").subsample(5, 5)
        paletteBlack = PhotoImage(file="../assets/Palettes/Black.png").subsample(5, 5)
        paletteBlue = PhotoImage(file="../assets/Palettes/Blue.png").subsample(5, 5)

        self.scenaryRed = PhotoImage(file="../assets/Scenary/Arena Tileset Rojo.png").subsample(3, 3)
        self.scenaryWhite = PhotoImage(file="../assets/Scenary/Arena Tileset Template Blanco.png").subsample(3, 3)
        self.scenaryGreen = PhotoImage(file="../assets/Scenary/Arena Tileset Template Verde.png").subsample(3, 3)
        self.scenaryBlack = PhotoImage(file="../assets/Scenary/Arena Tileset Template Black.png").subsample(3, 3)
        self.scenaryBlue = PhotoImage(file="../assets/Scenary/Arena Tileset Template Azul.png").subsample(3, 3)

        self.Paleta = "Green"
        self.PersonalizeWindow.buttonred = customtkinter.CTkButton(self.PersonalizeWindow, image=paletteRed,text="",fg_color=green_light, hover_color=green, command=lambda: self.selecPalett("Red"),width=70,height=70)
        self.PersonalizeWindow.buttonred.place(relx=0.7, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow.buttonwhite = customtkinter.CTkButton(self.PersonalizeWindow, image=paletteWhite,text="",fg_color=green_light, hover_color=green, command=lambda: self.selecPalett("White"),width=70,height=70)
        self.PersonalizeWindow.buttonwhite.place(relx=0.3, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow.buttongreen = customtkinter.CTkButton(self.PersonalizeWindow, image=paletteGreen,text="",fg_color=green_light, hover_color=green, command=lambda: self.selecPalett("Green"),width=70,height=70)
        self.PersonalizeWindow.buttongreen.place(relx=0.4, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow.buttonblack = customtkinter.CTkButton(self.PersonalizeWindow, image=paletteBlack,text="",fg_color=green_light, hover_color=green, command=lambda: self.selecPalett("Black"),width=70,height=70)
        self.PersonalizeWindow.buttonblack.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow.buttonblue = customtkinter.CTkButton(self.PersonalizeWindow, image=paletteBlue,text="",fg_color=green_light, hover_color=green, command=lambda: self.selecPalett("Blue"),width=70,height=70)
        self.PersonalizeWindow.buttonblue.place(relx=0.6, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow.Scenario = customtkinter.CTkLabel(self.PersonalizeWindow, image=self.scenaryGreen, corner_radius=60, text="")
        self.PersonalizeWindow.Scenario.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
        #----------------------------------------------------------------------------
        self.Texture = "Block1"
        self.PersonalizeWindow2.back = customtkinter.CTkButton(self.PersonalizeWindow2, text="←", fg_color=green_light, hover_color=green, command=self.ejecutar_register,width=30, height=30)
        self.PersonalizeWindow2.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)
        self.PersonalizeWindow2.logo_label = customtkinter.CTkLabel(self.PersonalizeWindow2,text=Lg.dic["Costumes in Game"][Lg.language],font=customtkinter.CTkFont(size=20, weight="bold"))
        self.PersonalizeWindow2.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.skip = customtkinter.CTkButton(self.PersonalizeWindow2, text="Skip", fg_color=green_light,hover_color=green, command=self.ConcludeRegisterSkip)
        self.PersonalizeWindow2.skip.place(relx=0.1, rely=0.9, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.next = customtkinter.CTkButton(self.PersonalizeWindow2, text="→",fg_color=green_light, hover_color=green, command=self.ejecutar_musicWindow)
        self.PersonalizeWindow2.next.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.advice = customtkinter.CTkLabel(self.PersonalizeWindow2, text=Lg.dic["Personalization is a unique feature for gold members "][Lg.language], font=customtkinter.CTkFont(size=10, weight="bold"))
        self.PersonalizeWindow2.advice.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.scenarytxt = customtkinter.CTkLabel(self.PersonalizeWindow2, text=Lg.dic["Select your texture"][Lg.language], font=customtkinter.CTkFont(size=15, weight="bold"))
        self.PersonalizeWindow2.scenarytxt.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.MetalBlock1 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block1Metal, corner_radius=60, text="")
        self.PersonalizeWindow2.MetalBlock1.place(relx=0.3, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.WoodBlock1 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block1Wood, corner_radius=60, text="")
        self.PersonalizeWindow2.WoodBlock1.place(relx=0.4, rely=0.4, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.CementBlock1 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block1Cement, corner_radius=60, text="")
        self.PersonalizeWindow2.CementBlock1.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.MetalBlock2 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block2Metal, corner_radius=60, text="")
        self.PersonalizeWindow2.MetalBlock2.place(relx=0.3, rely=0.5, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.WoodBlock2 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block2Wood, corner_radius=60, text="")
        self.PersonalizeWindow2.WoodBlock2.place(relx=0.4, rely=0.5, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.CementBlock2 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block2Cement, corner_radius=60, text="")
        self.PersonalizeWindow2.CementBlock2.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.MetalBlock3 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block3Metal, corner_radius=60, text="")
        self.PersonalizeWindow2.MetalBlock3.place(relx=0.3, rely=0.6, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.WoodBlock3 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block3Wood, corner_radius=60, text="")
        self.PersonalizeWindow2.WoodBlock3.place(relx=0.4, rely=0.6, anchor=customtkinter.CENTER)
        self.PersonalizeWindow2.CementBlock3 = customtkinter.CTkLabel(self.PersonalizeWindow2, image=block3Cement, corner_radius=60, text="")
        self.PersonalizeWindow2.CementBlock3.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.Pack1 = customtkinter.CTkButton(self.PersonalizeWindow2, text="Pack 1",fg_color=green_light, hover_color=green, command=lambda: self.selecTexture("Block1"),width=70,height=70)
        self.PersonalizeWindow2.Pack1.place(relx=0.6, rely=0.4, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.Pack2 = customtkinter.CTkButton(self.PersonalizeWindow2, text="Pack 2",fg_color=green_light, hover_color=green, command=lambda: self.selecTexture("Block2"),width=70,height=70)
        self.PersonalizeWindow2.Pack2.place(relx=0.6, rely=0.5, anchor=customtkinter.CENTER)

        self.PersonalizeWindow2.Pack3 = customtkinter.CTkButton(self.PersonalizeWindow2, text="Pack 3",fg_color=green_light, hover_color=green, command=lambda: self.selecTexture("Block3"),width=70,height=70)
        self.PersonalizeWindow2.Pack3.place(relx=0.6, rely=0.6, anchor=customtkinter.CENTER)
        #--------------------------------------------------------------------------------------------------------

        self.UserSpot = ""

        self.Song1 = ""
        self.Song2 = ""
        self.Song3 = ""

        self.MusicWindow.back = customtkinter.CTkButton(self.MusicWindow, text="←", fg_color=green_light, hover_color=green,command=self.ejecutar_perzonalizar2, width=30, height=30)
        self.MusicWindow.back.place(relx=0.001, rely=0.001, anchor=customtkinter.NW)
        self.MusicWindow.logo_label = customtkinter.CTkLabel(self.MusicWindow, text="Music", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.MusicWindow.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.MusicWindow.Advice = customtkinter.CTkLabel(self.MusicWindow, text=Lg.dic["Music Spotify Advise"][Lg.language], font=customtkinter.CTkFont(size=10, weight="bold"))
        self.MusicWindow.Advice.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.MusicWindow.Advice2 = customtkinter.CTkLabel(self.MusicWindow, text=Lg.dic["Music Spotify Advise2"][Lg.language], font=customtkinter.CTkFont(size=10, weight="bold"))
        self.MusicWindow.Advice2.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.MusicWindow.PayContinueWt = customtkinter.CTkButton(self.MusicWindow, text=Lg.dic["Press here"][Lg.language],fg_color=green_light, hover_color=green, command=lambda: self.continue_Pay(False))
        self.MusicWindow.PayContinueWt.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

        self.MusicWindow.PayContinue = customtkinter.CTkButton(self.MusicWindow, text="→",fg_color=green_light, hover_color=green, command=lambda: self.continue_Pay(True))
        self.MusicWindow.PayContinue.place(relx=0.9, rely=0.9, anchor=customtkinter.CENTER)

        self.MusicWindow.UserSpot = customtkinter.CTkEntry(self.MusicWindow, placeholder_text=Lg.dic["Spotify User"][Lg.language])
        self.MusicWindow.UserSpot.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.MusicWindow.Song1 = customtkinter.CTkEntry(self.MusicWindow, placeholder_text=Lg.dic["Song"][Lg.language]+" 1")
        self.MusicWindow.Song1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.MusicWindow.Song2 = customtkinter.CTkEntry(self.MusicWindow, placeholder_text=Lg.dic["Song"][Lg.language]+" 2")
        self.MusicWindow.Song2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.MusicWindow.Song3 = customtkinter.CTkEntry(self.MusicWindow, placeholder_text= Lg.dic["Song"][Lg.language]+" 3")
        self.MusicWindow.Song3.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        #--------------------------------------------------------------------------------------------------------

        self.MembersWindow.Member = customtkinter.CTkLabel(self.MembersWindow, text=Lg.dic["Member"][Lg.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.MembersWindow.Member.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.MembersWindow.Advice = customtkinter.CTkLabel(self.MembersWindow, text=Lg.dic["Pay advise"][Lg.language], font=customtkinter.CTkFont(size=10, weight="bold"))
        self.MembersWindow.Advice.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.MembersWindow.CardNumber = customtkinter.CTkEntry(self.MembersWindow, placeholder_text=Lg.dic["Card Number"][Lg.language])
        self.MembersWindow.CardNumber.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.MembersWindow.CardName = customtkinter.CTkEntry(self.MembersWindow, placeholder_text=Lg.dic["Card Name"][Lg.language])
        self.MembersWindow.CardName.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.MembersWindow.CardDate = customtkinter.CTkEntry(self.MembersWindow, placeholder_text="mm/yy")
        self.MembersWindow.CardDate.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.MembersWindow.CardCode = customtkinter.CTkEntry(self.MembersWindow, placeholder_text=Lg.dic["Card CVV"][Lg.language])
        self.MembersWindow.CardCode.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.MembersWindow.PayContinue = customtkinter.CTkButton(self.MembersWindow, text=Lg.dic["Pay"][Lg.language],fg_color=green_light, hover_color=green, command=self.continue_PayValidate)
        self.MembersWindow.PayContinue.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)




    def continue_PayValidate(self):
        card_number = self.MembersWindow.CardNumber.get()
        card_name = self.MembersWindow.CardName.get()
        card_date = self.MembersWindow.CardDate.get()
        card_code = self.MembersWindow.CardCode.get()
        if card_number == "" or card_name == "" or card_date == "" or card_code == "":
            tkinter.messagebox.showerror("Error", "Faltan datos")
            return 0
        if not dt.validar_tarjeta(card_number, card_date, card_code, card_name)[0]:
            tkinter.messagebox.showerror("Error", dt.validar_tarjeta(card_number, card_date, card_code, card_name)[1])
            return 0
        else:
            tkinter.messagebox.showinfo("Info", "Pago realizado con éxito")
            self.Member = True
            self.ConcludeRegister()

    def continue_Pay(self,UserSpot):
        if UserSpot:
            self.UserSpot = self.MusicWindow.UserSpot.get()
            Song1 = self.MusicWindow.Song1.get()
            Song2 = self.MusicWindow.Song2.get()
            Song3 = self.MusicWindow.Song3.get()
            self.confirm_Songs(Song1, Song2, Song3)
            self.Song1 = Song1
            self.Song2 = Song2
            self.Song3 = Song3
            self.ejecutar_Member()
        else:
            self.UserSpot = ""
            self.ejecutar_Member()
            return 0

    def ejecutar_Member(self):
        self.RegisterWindow.withdraw()
        self.PersonalizeWindow.withdraw()
        self.PersonalizeWindow2.withdraw()
        self.MusicWindow.withdraw()
        self.MembersWindow.deiconify()

    def confirm_Songs(self, song1, song2, song3):
        Songs = [song1, song2, song3]
        for song in Songs:
            if song == "":
                tkinter.messagebox.showerror("Error", "Falta alguna canción")
                return 0
            elif not spot.SearchSong(song):
                tkinter.messagebox.showerror("Error", "Alguna canción no existe")
                return 0
        tkinter.messagebox.showinfo("Info", "Canciones confirmadas")


    def selecPalett(self, color):
        self.Paleta = color
        if color == "Red":
            self.PersonalizeWindow.Scenario.configure(image=self.scenaryRed)
        elif color == "White":
            self.PersonalizeWindow.Scenario.configure(image=self.scenaryWhite)
        elif color == "Green":
            self.PersonalizeWindow.Scenario.configure(image=self.scenaryGreen)
        elif color == "Black":
            self.PersonalizeWindow.Scenario.configure(image=self.scenaryBlack)
        elif color == "Blue":
            self.PersonalizeWindow.Scenario.configure(image=self.scenaryBlue)
        else:
            return 0
    def selecTexture(self, texture):
        green = "#408E91"
        pink = "#E49393"
        self.PersonalizeWindow2.Pack1.configure(fg_color=green)
        self.PersonalizeWindow2.Pack2.configure(fg_color=green)
        self.PersonalizeWindow2.Pack3.configure(fg_color=green)
        self.Texture = texture
        if texture == "Block1":
            self.PersonalizeWindow2.Pack1.configure(fg_color=pink)
        elif texture == "Block2":
            self.PersonalizeWindow2.Pack2.configure(fg_color=pink)
        elif texture == "Block3":
            self.PersonalizeWindow2.Pack3.configure(fg_color=pink)
        else:
            return 0



    def ejecutar_perzonalizar2(self):
        self.MusicWindow.withdraw()
        self.RegisterWindow.withdraw()
        self.PersonalizeWindow.withdraw()
        self.PersonalizeWindow2.deiconify()

    def clean_AllRegister(self):
        self.RegisterWindow.entry_Nombre.delete(0, 'end')
        self.RegisterWindow.entry_Apellido.delete(0, 'end')
        self.RegisterWindow.entry_Username.delete(0, 'end')
        self.RegisterWindow.entry_Contra.delete(0, 'end')
        self.RegisterWindow.entry_Contra_check.delete(0, 'end')
        self.RegisterWindow.entry_Correo.delete(0, 'end')
        self.RegisterWindow.avatar_label.configure(image=self.default_imageop)
        self.age = 0
        self.selected_photo_path = "../assets/flags/Avatar-Profile.png"
        self.RegisterWindow.calendario_button.configure(text="Fecha de nacimiento")
        self.Paleta = "Green"
        self.Texture = "Block1"
        self.MusicWindow.UserSpot.delete(0, 'end')
        self.MusicWindow.Song1.delete(0, 'end')
        self.MusicWindow.Song2.delete(0, 'end')
        self.MusicWindow.Song3.delete(0, 'end')
        self.UserSpot = ""
        self.MembersWindow.CardNumber.delete(0, 'end')
        self.MembersWindow.CardName.delete(0, 'end')
        self.MembersWindow.CardDate.delete(0, 'end')
        self.MembersWindow.CardCode.delete(0, 'end')



    def ejecutar_musicWindow(self):
        self.RegisterWindow.withdraw()
        self.PersonalizeWindow.withdraw()
        self.PersonalizeWindow2.withdraw()
        self.MusicWindow.deiconify()


    def ConcludeRegisterSkip(self):
        question = tkinter.messagebox.askyesno("Info", "Si salta la personalizacion perdera la seleccion pero se registrara como usuario normal, Continuar?")
        if question:
            self.Member = False
            self.ConcludeRegister()
        else:
            return 0

    def Save_imapic(self,username):
        if self.selected_photo_path == "../assets/flags/Avatar-Profile.png":
            return 0
        else:
            Image.open(self.selected_photo_path).save("../ProfilePics/" + username + ".png")
            self.selected_photo_path == "../ProfilePics/" + username + ".png"
            return 1


    def ConcludeRegister(self):
        name = self.RegisterWindow.entry_Nombre.get()
        last_name = self.RegisterWindow.entry_Apellido.get()
        username = self.RegisterWindow.entry_Username.get()
        password = self.RegisterWindow.entry_Contra.get()
        password_check = self.RegisterWindow.entry_Contra_check.get()
        mail = self.RegisterWindow.entry_Correo.get()
        if self.Member == False:
            DataBase.insert_user(username, password,name, last_name,  mail, self.age, self.selected_photo_path,"No","NONE","NONE","NONE","NONE","NONE","NONE","NONE","Block1","Green")
            self.Save_imapic(username)
            self.clean_AllRegister()
            tkinter.messagebox.showinfo("Info", "Usuario registrado con éxito")
            self.back_menu()

        elif self.Member == True:
            DataBase.insert_user(username, password,name, last_name, mail, self.age, self.selected_photo_path,"Yes",self.UserSpot,self.Song1,self.Song2,self.Song3,"NONE","NONE","NONE",self.Texture,self.Paleta)
            self.Save_imapic(username)
            self.clean_AllRegister()
            tkinter.messagebox.showinfo("Info", "Usuario Gold registrado con éxito")
            self.back_menu()
        else:
            tkinter.messagebox.showerror("Error", "No se pudo registrar el usuario")
            return 0

    def VerifyRegister(self):
        name = self.RegisterWindow.entry_Nombre.get()
        last_name = self.RegisterWindow.entry_Apellido.get()
        username = self.RegisterWindow.entry_Username.get()
        password = self.RegisterWindow.entry_Contra.get()
        password_check = self.RegisterWindow.entry_Contra_check.get()
        mail = self.RegisterWindow.entry_Correo.get()

        if not self.check_missing_data()==[]:
                tkinter.messagebox.showerror("Error", "Rellenar"+str(self.check_missing_data()))
                return 0
        if not dt.FirstNameCheck(name):
                tkinter.messagebox.showerror("Error", "Nombre no válido")
                return 0
        if not dt.LastNameCheck(last_name):
                tkinter.messagebox.showerror("Error", "Apellido no válido")
                return 0
        if not dt.validar_usuario(username)[0]:
                tkinter.messagebox.showerror("Error", "Nombre de usuario no válido"+dt.validar_usuario(username)[1])
                return 0
        if not dt.verificar_contrasenas(password, password_check):
                tkinter.messagebox.showerror("Error", "Las contraseñas no coinciden")
                return 0
        if not dt.validar_contrasena (password_check):
                tkinter.messagebox.showerror("Error", "Contraseña no válida")
                return 0
        if not dt.MailCheck(mail)== mail:
                tkinter.messagebox.showerror("Error", str(dt.MailCheck(mail)[1]))
                return 0
        if self.age < 14:
                tkinter.messagebox.showerror("Error", "No se puede registrar un usuario menor de 14 años")
                return 0
        if self.selected_photo_path == "../assets/flags/Avatar-Profile.png":
                message = tkinter.messagebox.askyesno("?", Lg.dic[ "Do you want a profile picture?"][Lg.language])
                if not message:
                    return 1
                else:
                    return 0
        return 1


    def check_missing_data(self):
        missing_fields = []
        if not self.RegisterWindow.entry_Nombre.get():
            missing_fields.append(dic.Name[dic.language])
        if not self.RegisterWindow.entry_Apellido.get():
            missing_fields.append(dic.Surname[dic.language])
        if not self.RegisterWindow.entry_Username.get():
            missing_fields.append(dic.Username[dic.language])
        if not self.RegisterWindow.entry_Contra.get():
            missing_fields.append(dic.Password[dic.language])
        if not self.RegisterWindow.entry_Contra_check.get():
            missing_fields.append(dic.VerifyPassword[dic.language])
        if not self.RegisterWindow.entry_Correo.get():
            missing_fields.append(dic.Email[dic.language])
        if self.age < 0:
            missing_fields.append(dic.Age[dic.language])
        return missing_fields


    def data_select(self):
        auxage = self.RegisterWindow.calendario.get_date()
        age = dt.SelectDate(auxage)
        if age == 0:
            tkinter.messagebox.showerror("Error", "No se selecciono una fecha")
            return 0
        if age < 14:
            tkinter.messagebox.showerror("Error", "No se puede registrar un usuario menor de 14 años")
            return 0
        self.age = age
        self.RegisterWindow.edad_label.configure(text=dic.Age[dic.language] + ": " + str(self.age))

    def toggle_password_visibility(self):
        if self.RegisterWindow.entry_Contra.cget("show") == "◊":
            self.RegisterWindow.entry_Contra.configure(show="")  # Cambiado de config a configure aquí
            self.RegisterWindow.toggle_btn.configure(text="⦿")  # Cambiado de config a configure aquí
        else:
            self.RegisterWindow.entry_Contra.configure(show="◊")  # Cambiado de config a configure aquí
            self.RegisterWindow.toggle_btn.configure(text="⦾")  # Cambiado de config a configure aquí

    def toggle_password_visibility2(self):
        if self.RegisterWindow.entry_Contra_check.cget("show") == "◊":
            self.RegisterWindow.entry_Contra_check.configure(show="")  # Cambiado de config a configure aquí
            self.RegisterWindow.toggle_btn2.configure(text="⦿")  # Cambiado de config a configure aquí
        else:
            self.RegisterWindow.entry_Contra_check.configure(show="◊")  # Cambiado de config a configure aquí
            self.RegisterWindow.toggle_btn2.configure(text="⦾")  # Cambiado de config a configure aquí
    def toggle_calendar(self):
        if self.RegisterWindow.calendario.winfo_ismapped():
            self.RegisterWindow.calendario.place_forget()
            self.RegisterWindow.edad_button.place_forget()
        else:
            self.RegisterWindow.calendario.place(relx=0.7, rely=0.4, anchor=customtkinter.CENTER)
            self.RegisterWindow.edad_button.place(relx=0.7, rely=0.25, anchor=customtkinter.CENTER)
    def ejecutar_login(self):
        """Handle the 'Login' button click event.
               This method is called when the 'Login' button is clicked.
               Args:
                   None
               Returns:
                   None
               """
        self.RegisterWindow.withdraw()
        self.PlayWindow.withdraw()
        self.withdraw()
        self.LoginWindow.deiconify()
    def ejecutar_register(self):
        self.PersonalizeWindow.withdraw()
        self.PersonalizeWindow2.withdraw()
        self.LoginWindow.withdraw()
        self.PlayWindow.withdraw()
        self.withdraw()
        self.RegisterWindow.deiconify()

    def ejecutar_backperzonalizar(self):
        self.PersonalizeWindow2.withdraw()
        self.PersonalizeWindow.deiconify()
    def ejecutar_perzonalizar(self):
        self.PersonalizeWindow2.withdraw()
        if self.VerifyRegister():
            self.RegisterWindow.withdraw()
            self.PlayWindow.withdraw()
            self.withdraw()
            self.PersonalizeWindow.deiconify()
        else:
            return 0

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
                self.set_picperfil(1,Pic)
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
                self.set_picperfil(2,Pic)
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
        self.PersonalizeWindow2.withdraw()
        self.PersonalizeWindow.withdraw()
        self.RegisterWindow.withdraw()
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
    def HallOfFame_select(self):
        self.withdraw()
        self.PlayWindow.withdraw()
        self.LoginWindow.withdraw()
        self.HallOfFame.deiconify()
        self.HallOfFame.resizable(False, False)


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
        self.LoginWindow.withdraw()
        self.HallOfFame.withdraw()
        self.PlayWindow.deiconify()
        #else:
            #self.PlayWindow.withdraw()
            #self.LoginWindow.deiconify()


    def ejecutar_Game_Multiplayer(self):


        if users.player1.verify_log(users.player1.texture, users.player1.palette_color) and users.player2.verify_log(users.player2.texture, users.player2.palette_color):
            juegoinit.iniciar(users.player1, users.player2)
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


    # def abrir_archivo(self,archivo):
    #     #archivo = filedialog.askopenfilename(filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])
    #     if archivo:
    #         #self.selected_photo_path = archivo
    #             # Cargar la imagen
    #         imagen = Image.open(archivo)
    #         imagen = imagen.resize((100, 100), Image.LANCZOS)
    #         circular = self.make_circle_image(imagen)
    #         #Imagentk = ImageTk.PhotoImage(circular)
    #         return ImageTk.PhotoImage(circular)
    #     else:
    #         tkinter.messagebox.showerror("Error", "No se selecciono una imagen")
    #         return 0

    def abrir_archivo(self, relative_path):
        try:
            # Normalize the relative path and remove leading spaces if any
            normalized_path = os.path.normpath(os.path.join(os.getcwd(), relative_path.strip()))

            # Check if the file exists
            if not os.path.exists(normalized_path):
                tkinter.messagebox.showerror("Error", f"Archivo no encontrado: {normalized_path}")
                return None

            # Open and process the image
            with open(normalized_path, 'rb') as img_file:
                img = Image.open(img_file)
                img = img.resize((40, 40), Image.LANCZOS)  # Resize as needed
                circular = self.make_circle_image(img)
                return ImageTk.PhotoImage(circular)
        except FileNotFoundError:
            tkinter.messagebox.showerror("Error", f"Archivo no encontrado: {relative_path}")
            return None
        except Exception as e:  # Catch other possible errors
            tkinter.messagebox.showerror("Error", str(e))
            return None
    def set_register_pic(self):
        archivo = filedialog.askopenfilename(filetypes=[(dic.Photo[dic.language], "*.png *.jpg *.jpeg *.gif *.bmp")])
        if archivo:
            self.selected_photo_path = archivo
            Imagetk = self.abrir_archivo(archivo)
            self.RegisterWindow.avatar_label.configure(image=Imagetk)
            self.RegisterWindow.avatar_label.image = Imagetk
    def set_picperfil(self,player,archivo):
        Imagetk = self.abrir_archivo(archivo)
        if player == 1:
            self.PlayWindow.Player1Pic.configure(image=Imagetk)
            self.PlayWindow.Player1Pic.image = Imagetk

        elif player == 2:
            self.PlayWindow.Player2Pic.configure(image=Imagetk)
            self.PlayWindow.Player2Pic.image = Imagetk
        else:
            tkinter.messagebox.showerror("Error", "No se actualizo la imagen de perfil")
            return 0
    def set_picHallfame(self,player,archivo):
        Imagetk = self.abrir_archivo(archivo)
        if player == 1:
            self.HallOfFame.Player1Pic.configure(image=Imagetk)
            self.HallOfFame.Player1Pic.image = Imagetk

        elif player == 2:
            self.HallOfFame.Player2Pic.configure(image=Imagetk)
            self.HallOfFame.Player2Pic.image = Imagetk

        elif player == 3:
            self.HallOfFame.Player3Pic.configure(image=Imagetk)
            self.HallOfFame.Player3Pic.image = Imagetk
        else:
            #tkinter.messagebox.showerror("Error", "No se actualizo la imagen de perfil")
            return 0



    # Define a new method to fetch top three players and update the display.
    def update_top_three_hall_of_fame(self):
        top_three_players = DataBase.get_top_10_scores()[:3]  # Assuming this fetches the top scores and player names.

        # Iterate over the top three players and update self attributes
        for i, player_info in enumerate(top_three_players):
            username, score, photo_path = player_info  # Assuming the order is username, score, photo path

            # Fetch the image using the path and make it circular
            player_image = self.abrir_archivo(photo_path) if photo_path else None

            # Update the profile picture labels
            if player_image and i == 0:
                self.HallOfFame.Player1Pic.configure(image=player_image)
                self.HallOfFame.Player1Pic.image = player_image  # Keep a reference
                self.HallOfFame.Player1Name.configure(text=username)  # Update the username label
                self.top1score.configure(text=str(score))  # Update the score label
            elif player_image and i == 1:
                self.HallOfFame.Player2Pic.configure(image=player_image)
                self.HallOfFame.Player2Pic.image = player_image
                self.HallOfFame.Player2Name.configure(text=username)
                self.top2score.configure(text=str(score))
            elif player_image and i == 2:
                self.HallOfFame.Player3Pic.configure(image=player_image)
                self.HallOfFame.Player3Pic.image = player_image
                self.HallOfFame.Player3Name.configure(text=username)
                self.top3score.configure(text=str(score))

    def update_hall_of_fame(self):
        # Fetch the top 10 players' scores from the database
        top_ten_players = DataBase.get_top_10_scores()

        # Check if the top players' data is available
        if not top_ten_players:
            tkinter.messagebox.showerror("Error", "No se pudo obtener los puntajes del Hall of Fame.")
            return

        # Update each player's display
        for i, player_data in enumerate(top_ten_players):
            username, score, photo_path = player_data
            player_rank = i + 1  # Player rank (1 through 10)

            # Construct label names based on player rank
            name_label_name = f'Player{player_rank}Name'
            score_label_name = f'top{player_rank}score'
            pic_label_name = f'Player{player_rank}Pic'

            # Fetch the corresponding labels
            name_label = getattr(self.HallOfFame, name_label_name, None)
            score_label = getattr(self.HallOfFame, score_label_name, None)
            pic_label = getattr(self.HallOfFame, pic_label_name, None)

            # Update the name and score labels if they exist
            if name_label:
                name_label.configure(text=username)
            if score_label:
                score_label.configure(text=str(score))

            # Update the profile picture if the label exists
            if pic_label and photo_path:  # Check if the profile picture path exists
                player_image = self.abrir_archivo(photo_path)
                if player_image:  # If an image was successfully loaded
                    pic_label.configure(image=player_image)
                    pic_label.image = player_image  # Keep a reference to the image

    def update_hall_of_fame_scores(self):
        # Assuming 'get_top_10_scores()' returns a list of tuples in the format (username, score, photo_blob)
        top_ten_players_scores = DataBase.get_top_10_scores()
        if not top_ten_players_scores:
            tkinter.messagebox.showerror("Error", "No se pudo obtener los puntajes del Hall of Fame.")
            return

        # A dictionary to map the player rank to the corresponding label
        score_labels = {
            1: self.top1score,
            2: self.top2score,
            3: self.top3score,
            4: self.top4score,
            5: self.top5score,
            6: self.top6score,
            7: self.top7score,
            8: self.top8score,
            9: self.top9score,
            10: self.top10score,
        }
        # Update each label with the corresponding score
        for index, player_info in enumerate(top_ten_players_scores):
            rank = index + 1  # Player rank (1 through 10)
            _, score, _ = player_info  # Get the score part of the tuple

            # Check if there's a label for this rank and update it
            if rank in score_labels:
                score_label = score_labels[rank]
                score_label.configure(text=str(score))  # Update the label with the score
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
