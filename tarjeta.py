import tkinter.messagebox
import customtkinter

import language_dictionary as dic


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
        self.title(dic.Registration[dic.language])
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)

        # create sidebar frame with widgets

        self.tabview = customtkinter.CTkTabview(self, width=400, height=400, fg_color=grey , segmented_button_selected_color=green, segmented_button_selected_hover_color=pink)
        self.tabview.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.tabview.add(dic.Data[dic.language])
        self.tabview.add(dic.Game[dic.language])
        self.tabview.add(dic.Personalization[dic.language])
        self.tabview.tab(dic.Data[dic.language]).grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab(dic.Game[dic.language]).grid_columnconfigure(0, weight=1)



        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Registration[dic.language], font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)


        self.nombre = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Name[dic.language], anchor="w")
        self.nombre.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.entry_Nombre = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Nombre.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.apellido = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Surname[dic.language], anchor="w")
        self.apellido.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Apellido = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Apellido.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


        self.correo = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text=dic.Email[dic.language], anchor="w")
        self.correo.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.entry_Correo = customtkinter.CTkEntry(self.tabview.tab(dic.Data[dic.language]))
        self.entry_Correo.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


        self.edad_label = customtkinter.CTkLabel(self.tabview.tab(dic.Data[dic.language]), text= dic.Age[dic.language]+": 0")
        self.edad_label.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.edad_slider = customtkinter.CTkSlider(self.tabview.tab(dic.Data[dic.language]), command=self.update_edad_label, from_=0, to=100, button_color = green, button_hover_color=pink)
        self.edad_slider.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)









        #-------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Username[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
        self.entry_Username = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]))
        self.entry_Username.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.contra = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), text=dic.Password[dic.language], anchor="w")
        self.contra.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.entry_Contra = customtkinter.CTkEntry(self.tabview.tab(dic.Game[dic.language]), show="◊")
        self.entry_Contra.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.foto_label = customtkinter.CTkLabel(self.tabview.tab(dic.Game[dic.language]), corner_radius=60, text=dic.Photo[dic.language])
        self.foto_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


        # self.foto = customtkinter.CTkFrame(self.tabview.tab("Juego"), fg_color=grey, corner_radius=100, height=80,width=80)
        # self.foto.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.subir_Foto = customtkinter.CTkButton(self.tabview.tab(dic.Game[dic.language]), text="✚",
                                                        fg_color=green_light, hover_color=green, corner_radius=80, width=10, command=self.abrir_archivo)
        self.subir_Foto.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)


        #----------------------------------------------------------------------------------------

        self.logo_label = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]), text=dic.Registration[dic.language],
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]), text=dic.Theme[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab(dic.Personalization[dic.language]), values=[dic.Red[dic.language], dic.Black[dic.language], dic.Blue[dic.language],dic.White[dic.language],dic.Green[dic.language]],fg_color=green_light, button_color=green)
        self.appearance_mode_optionemenu.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.username = customtkinter.CTkLabel(self.tabview.tab(dic.Personalization[dic.language]), text=dic.FavoriteSongs[dic.language], anchor="w")
        self.username.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.cancion1 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]) )
        self.cancion1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.cancion2 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
        self.cancion3 = customtkinter.CTkEntry(self.tabview.tab(dic.Personalization[dic.language]))
        self.cancion3.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

        self.sidebar_button_1 = customtkinter.CTkButton(self.tabview.tab(dic.Personalization[dic.language]), text=dic.Register[dic.language],
                                                    fg_color=green_light, hover_color=green, command=lambda :[self.registrar_usuario(),self.registro_facial()])
        self.sidebar_button_1.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)



        # Limpiaremos los text variable


        # Ahora le diremos al usuario que su registro ha sido exitoso

    def update_edad_label(self, value):
        self.edad_label.configure(text=dic.Age[dic.language]+f" :{round(value)}")


    def iniciar(self):
        self.destroy()
        menu.Menu_principal().mainloop()


