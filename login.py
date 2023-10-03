import tkinter
import tkinter.messagebox
import customtkinter
from registro import Registro
import language_dictionary as dic
# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Login(customtkinter.CTk):
    def __init__(self):
        green = "#245953"
        green_light = "#408E91"
        pink = "#E49393"
        grey = "#D8D8D8"
        super().__init__()


        # configure window
        self.title(dic.Login3[dic.language])
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)


        # create sidebar frame with widgets

        self.logo_label = customtkinter.CTkLabel(self, text=dic.Login3[dic.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)


        self.username = customtkinter.CTkLabel(self, text=dic.Username[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)



        self.entry_Username = customtkinter.CTkEntry(self)
        self.entry_Username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self, text=dic.Password[dic.language], anchor="w")
        self.contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self, show = "◊")
        self.entry_Contra.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)



        self.sidebar_button_1 = customtkinter.CTkButton(self, text=dic.Login2[dic.language],fg_color=green_light,hover_color=green)
        self.sidebar_button_1.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)




        self.sidebar_button_3 = customtkinter.CTkButton(self,  text=dic.Register[dic.language],fg_color=green_light,hover_color=green, command= self.ejecutar_Ventana)
        self.sidebar_button_3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

    def ejecutar_Ventana(self):
        self.destroy()
        nuevo =Registro()
        nuevo.mainloop()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



