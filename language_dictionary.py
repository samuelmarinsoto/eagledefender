from collections import namedtuple
language = 0
Word = namedtuple('Word',['es','en','fr'])
Phrase = namedtuple('Phrase',['es','en','fr'])
Member: int = 0
def changeLanguage(lang):
    """
        Cambia la variable global de idioma
        Args:
            int: 0 español, 1 ingles, 2 frances.
        Returns:
            None
     """
    global language
    if isinstance(lang,str):
        if lang == "Español":
            language = 0
        elif lang == "English":
            language = 1
        elif lang == "Français":
            language = 2
    else:
        return 0




#____________________Diccionario de palabras en español, ingles y frances_______________________

Login = Word('INICIAR SESION','LOG IN','SE CONNECTER')
Login3 = Word('Iniciar sesión','Log in','Se connecter')
Login2 = Word('Iniciar','Log in','Se connecter')
Play = Word('JUGAR','PLAY','JOUER')
WithoutAcc = Phrase('No tiene cuenta?', 'Dont have account?','Vous n` avez pas de compte ?')
UI_Cof = Word('Escalado de la interfaz de usuario','UI Scaling','Mise à léchelle de l interface utilisateu')
Password = Word('Contraseña', 'Password', 'Mot de passe')
Username = Word('Usuario', 'Username', "Nom d'utilisateur")
Register = Word('Registrarse', 'Register', "S'inscrire")
AppearanceMode = Word('Modo de apariencia', 'Appearance Mode', "Mode d\'apparence")
Data = Word('Datos', 'Data', 'Données')
Registration = Word('Registro', 'Registration', 'Inscription')
Name = Word('Nombre', 'Name', 'Nom')
Surname = Word('Apellido', 'Surname', 'Nom de famille')
Email = Word('Correo', 'Email', 'E-mail')
Age = Word('Edad', 'Age', 'Âge')
Game = Word('Juego', 'Game', 'Jeu')
Photo = Word('Foto', 'Photo', 'Photo')
Theme = Word('Tema', 'Theme', 'Thème')
FavoriteSongs = Word('Canciones favoritas', 'Favorite Songs', 'Chansons préférées')
Red = Word('Rojo', 'Red', 'Rouge')
Black = Word('Negro', 'Black', 'Noir')
Blue = Word('Azul', 'Blue', 'Bleu')
White = Word('Blanco', 'White', 'Blanc')
Green = Word('Verde', 'Green', 'Vert')
Personalization = Word('Personalización', 'Personalization', 'Personnalisation')
FacialRegistration = Word('Registro facial', 'Facial Registration', 'Enregistrement facial')
Dark = Word('Oscuro', 'Dark', 'Sombre')
Light = Word('Claro', 'Light', 'Clair')
System = Word('Sistema', 'System', 'Système')
Music = Word('Musica','Music','Musique')
Texture = Word('Texturas','Texture','Textures')
Palettes = Word('Paletas de color', 'Color palettes','Palettes de couleurs')
Facial = Word('LogFace','','')
Members = Word('Member','','')



