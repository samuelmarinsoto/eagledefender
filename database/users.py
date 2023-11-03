


class CustomizationData:
    def __init__(self,Username,pathimage,membership, song1, song2, song3, palette_color, texture):
        self.Username = Username
        self.pathimage = pathimage
        self.membership = membership
        self.song1 = song1
        self.song2 = song2
        self.song3 = song3
        self.palette_color = palette_color
        self.texture = texture

    def update_Username(self, Username):
        self.Username = Username
    def update_pathimage(self, new_pathimage):
        self.pathimage = new_pathimage

    def update_membership(self, new_membership):
        self.membership = new_membership
    def update_song1(self, new_song1):
        self.song1 = new_song1

    def update_song2(self, new_song2):
        self.song2 = new_song2

    def update_song3(self, new_song3):
        self.song3 = new_song3

    def update_palette_color(self, new_palette_color):
        self.palette_color = new_palette_color

    def update_texture(self, new_texture):
        self.texture = new_texture

    def verify_log(self, texture, palette_color):
        if texture == "DefaultTexture" and palette_color == "DefaultPalette":
            return False
        else:
            return True

    def display_customization(self):
        print(f"Song1: {self.song1}")
        print(f"Song2: {self.song2}")
        print(f"Song3: {self.song3}")
        print(f"Palette Color: {self.palette_color}")
        print(f"Texture: {self.texture}")

# Ejemplo de uso
#player_customization = CustomizationData("DefaultSong1", "DefaultSong2", "DefaultSong3", "DefaultPalette", "DefaultTexture")
#player_customization.display_customization()

# Actualizar la personalización
#player_customization.update_song1("NewSong1")
#player_customization.update_palette_color("Red")
#player_customization.display_customization()

player1 = CustomizationData("","","NO","Scatman", "Gasolina Daddy Yankee", "Ace spades", "DefaultPalette", "DefaultTexture")
player2 = CustomizationData("","","NO","Stayin' alive", "Danza kuduro", "Blitzkrieg Pop", "DefaultPalette", "DefaultTexture")