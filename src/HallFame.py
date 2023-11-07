import DataBaseLocal as DBL



class Puntaje:

    def __init__(self,Username,pathimage, puntaje):
        self.Username = Username
        self.pathimage = pathimage
        self.puntaje = puntaje

    def update_Username(self, Username):
        self.Username = Username
    def update_pathimage(self, new_pathimage):
        self.pathimage = new_pathimage
    def update_puntaje(self, new_puntaje):
        self.puntaje = new_puntaje
    def update_hallfame(self):
       Top10 = DBL.get_top_10_scores()
       Score1.update_Username(Top10[0][0])
       Score1.update_pathimage(Top10[0][1])
       Score1.update_puntaje(Top10[0][2])
       Score2.update_Username(Top10[1][0])
       Score2.update_pathimage(Top10[1][1])
       Score2.update_puntaje(Top10[1][2])
       Score3.update_Username(Top10[2][0])
       Score3.update_pathimage(Top10[2][1])
       Score3.update_puntaje(Top10[2][2])
       """  Score4.update_Username(Top10[3][0])
       Score4.update_pathimage(Top10[3][1])
       Score4.update_puntaje(Top10[3][2])
       Score5.update_Username(Top10[4][0])
       Score5.update_pathimage(Top10[4][1])
       Score5.update_puntaje(Top10[4][2])
       Score6.update_Username(Top10[5][0])
       Score6.update_pathimage(Top10[5][1])
       Score6.update_puntaje(Top10[5][2])"""


Score1 = Puntaje("","", 0)
Score2 = Puntaje("","", 0)
Score3 = Puntaje("","", 0)
Score4 = Puntaje("","", 0)
Score5 = Puntaje("","", 0)
Score6 = Puntaje("","", 0)
Score1.update_hallfame()
