import tkinter
import tkinter.messagebox
import customtkinter
from login import Login

# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Menu_principal(customtkinter.CTk):
    def __init__(self):
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


        self.sidebar_button_1 = customtkinter.CTkButton(self, command=self.sidebar_button_event, text="JUGAR",fg_color=green_light,hover_color=green)
        self.sidebar_button_1.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.idiomas = customtkinter.CTkComboBox(self, values=["Español", "Ingles", "Fraces"])
        self.idiomas.place(relx=0.17, rely=0.06, anchor=customtkinter.CENTER)


        self.sidebar_button_3 = customtkinter.CTkButton(self, text="INICIAR SESION",fg_color=green_light,hover_color=green, command= self.ejecutar_Ventana)
        self.sidebar_button_3.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)


        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event,fg_color=green_light, button_color=green)
        self.appearance_mode_optionemenu.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)


        self.scaling_label = customtkinter.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["100%", "90%", "80%", "110%", "120%"],
                                                               command=self.change_scaling_event,fg_color=green_light, button_color=green)
        self.scaling_optionemenu.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

    def ejecutar_Ventana(self):
        self.destroy()
        nuevo =Login()
        nuevo.mainloop()



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


