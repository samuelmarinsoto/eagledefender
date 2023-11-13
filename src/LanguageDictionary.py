from collections import namedtuple


language = 1
def changeLanguage(lang):
    global language
    if isinstance(lang, str):
    
        if lang == "English":   
            language = 0
        elif lang == "Español":
            language = 1
        elif lang == "Français":
            language = 2
    else:
        return 0 

# Define un namedtuple para las traducciones
Translation = namedtuple("Translation", ["en", "es", "fr"])

# Define el diccionario con las traducciones
dic = {
    "Game": Translation(en="Game", es="Juego", fr="Jeu"),
    "Login": Translation(en="Login", es="Inicio de sesion", fr="Se connecter"),
    "Register": Translation(en="Register", es="Registro", fr="S'inscrire"),
    "Member": Translation(en="Member", es="Miembro", fr="Membre"),
    "Pay section": Translation(en="Pay section", es="Seccion de pago", fr="Section de paiement"),
    "Pay": Translation(en="Pay", es="Pagar", fr="Payer"),
    "Back": Translation(en="Back", es="Atras", fr="Retour"),
    "Costumes in Game": Translation(en="Costumes in Game", es="Personalizaciones en el juego", fr="Costumes dans le jeu"),
    "Do you want a profile picture?": Translation(en="Do you want a profile picture?", es="Deseas foto de perfil?", fr="Voulez-vous une photo de profil?"),
    "Select your scenario": Translation(en="Select your scenario", es="Selecciona tu escenario", fr="Sélectionnez votre scénario"),
    "Personalization is a unique feature for gold members ": Translation(en="Personalization is a unique feature for gold members, that can be select scenary, block texture and music ", es="La personalización es una característica única para los miembros gold, donde podra elegir el escenario, la textura de los bloques y la musica de fondo", fr="La personnalisation est une fonctionnalité unique pour les membres or"),
    "Select your texture": Translation(en="Select your texture pack", es="Selecciona tu pack textura", fr="Sélectionnez votre texture"),
    "Music Spotify Advise": Translation(en = "In Eagle Defender you can choose your favorite music through Spotify, to do this you must have a premium Spotify account and have the program installed on your computer", es="En eagle defender podras elegir tu musica preferida a traves de spotify, para ello deberas tener una cuenta premium de spotify y tener instalado el programa en tu ordenador", fr="En eagle defender, vous pouvez choisir votre musique préférée via spotify, pour cela vous devez avoir un compte premium spotify et avoir le programme installé sur votre ordinateur"),
    "Music Spotify Advise2": Translation(en="If you dont have Spotify account you can use the defualt music", es="Si no tienes cuenta de spotify podras usar la musica por defecto", fr="Si vous n'avez pas de compte spotify, vous pouvez utiliser la musique par défaut"),
    "Select your music": Translation(en="Select your music", es="Selecciona tu musica", fr="Sélectionnez votre musique"),
    "Press here": Translation(en="Press here", es="Presiona aqui", fr="Appuyez ici"),
    "Spotify User": Translation(en="Spotify User", es="Usuario de Spotify", fr="Utilisateur Spotify"),
    "Song": Translation(en="Song", es="Cancion", fr="Chanson"),
    "Pay advise": Translation(en="The personalization of the game is a unique feature for gold members, if you want to enjoy this feature you must pay a monthly fee of 30 USD", es="La personalización del juego es una característica única para los miembros gold, si deseas disfrutar de esta característica deberas pagar una cuota mensual de 30 USD", fr="La personnalisation du jeu est une fonctionnalité unique pour les membres or, si vous souhaitez profiter de cette fonctionnalité, vous devez payer un abonnement mensuel de 30 USD"),
    "Card Number": Translation(en="Card Number", es="Numero de tarjeta", fr="Numéro de carte"),
    "Card Date": Translation(en="Card Date", es="Fecha de tarjeta", fr="Date de la carte"),
    "Card CVV": Translation(en="Card CVV", es="CVV de tarjeta", fr="CVV de la carte"),
    "Card Name": Translation(en="Card Name", es="Nombre de tarjeta", fr="Nom de la carte"),
    "Instructions": Translation(en="Instructions to play", es="Instrucciones para jugar", fr="Instructions joueur"),
    "Objective": Translation(en="Objective", es="Objetivo", fr="Objectif"),
    "How to play": Translation(en="How to play", es="Como jugar", fr="Comment jouer"),
    "Player 1": Translation(en="Player 1", es="Jugador 1", fr="Joueur 1"),
    "Player 2": Translation(en="Player 2", es="Jugador 2", fr="Joueur 2"),
    "Attack": Translation(en="Atack", es="Atacar", fr="Attaque"),
    "Defense": Translation(en="Defense", es="Defender", fr="Défense"),
    "Identify":Translation(en="Is identify by the led:", es="Se identifica por el led:", fr="Il est identifié par la lumière:"),
    "InstructionsControl":Translation(en="Instructions to control", es="Instrucciones para el mando", fr="Instructions de contrôle"),


}

Ins = {

    "Attack":Translation(en="B Fire \n A Water \n Y Bomb \n X Action ",es="B Fuego \n A Agua \n Y Bomba \n X Accion",fr="B Feu \n A Eau \n Y Bombe \n X Action"),
    "Rotate":Translation(en="→ ←Aim \n > Pause",es="→ ← Apuntar \n > Pausa",fr="→ ← Tourner \n > Pause"),
    "Joy":Translation(en="Joystick \n ↑ ↓\n ← → ",es="Analogo \n ↑ ↓\n ← → ",fr="Joystick \n ↑ ↓\n ← → "),

    "Block":Translation(en="B Metal\n A Wood\n Y Concrete \n Put the eagle",es="B Metal\n A Madera\n Y Concreto \n Poner el aguila",fr="B Métal\n A Bois\n Y Béton \n Mettre l'aigle"),
    "Rote Block":Translation(en="→ ← Rotate block \n > Pause",es="→ ← Rotar bloque \n > Pausa",fr="→ ← Tourner bloc \n > Pause "),
    "Joy Block":Translation(en="Move block \n ↑ ↓\n ← → ",es="Mueve el blcque \n ↑ ↓\n ← → ",fr="Déplacer le bloc \n ↑ ↓\n ← → "),

    "Objetive":Translation(en="The objective of the game is to destroy the enemy's eagle",es="El objetivo del juego es destruir el aguila enemiga",fr="L'objectif du jeu est de détruire l'aigle ennemi"),
    "Objetive2":Translation(en="To do this, you must destroy the blocks that protect it, \n you cand do with some projectiles that you have",es="Para ello deberas destruir los bloques que lo protegen, \n podras hacerlo con algunos de los proyectiles que tienes",fr="Pour ce faire, vous devez détruire les blocs qui le protègent, \n vous pouvez le faire avec certains des projectiles que vous avez"),
    "Objetive3":Translation(en="You can do with some of projectiles that you have",es="Podras hacerlo con algunos de los proyectiles que tienes",fr="Vous pouvez le faire avec certains des projectiles que vous avez"),
    "Objetive4":Translation(en="You can choose between: \nbomb      fire      water",es="Podras elegir entre \nbomba      fuego      agua",fr="Vous pouvez choisir entre \nbombe      feu      eau"),

    #defensa
    "Objetive.0":Translation(en="The objective of the game is to protect your eagle",es="El objetivo del juego es proteger tu aguila",fr="L'objectif du jeu est de protéger votre aigle"),
    "Objetive.2":Translation(en="To do this you must place blocks to protect it",es="Para ello deberas colocar bloques para protegerlo",fr="Pour ce faire, vous devez placer des blocs pour le protéger"),
    "Objetive.3":Translation(en="You can defend the eagle place blocks",es="Podras defender el aguila colocando bloques",fr="Vous pouvez défendre l'aigle en plaçant des blocs"),
    "Objetive.4":Translation(en="You can can choose between: \nconcrete     metal     wood",es="Podras elegir entre \nconcreto     metal     madera",fr="Vous pouvez choisir entre \nbéton     métal     bois"),
    "LifeBlock":Translation(en=" The block have durability, so they could be destroy by the projetiles \nConcrete 10 pts     Acero 5 pts     Madera 3 pts",es="Los bloques tienen durabilidad, por lo que podran ser destruidos por los proyectiles \nConcreto 10 pts     Acero 5 pts     Madera 3 pts",fr="Les blocs ont une durabilité, ils doivent donc être détruits par les projectiles \nBéton 10 pts     Acier 5 pts     Bois 3 pts"),
    "LifeProjectile":Translation(en="The projectiles have points of attack \n Bomb 10 pts     Fire 5 pts     Water 3 pts",es="Los proyectiles tienen puntos de ataque \n Bomba 10 pts     Fuego 5 pts     Agua 3 pts",fr="Les projectiles ont des points d'attaque \n Bombe 10 pts     Feu 5 pts     Eau 3 pts"),


    #como jugar
    "How to play":Translation(en="How to play",es="Como jugar",fr="Comment jouer"),
    "Play1":Translation(en="The game have two rounds and have two games by round, \nin the change of game the players change of role",es="El juego tiene dos rondas y tiene dos juegos por ronda,\n en el cambio de partida los jugadores cambian de rol",fr="Le jeu a deux tours et a deux jeux par tour,\n dans le changement de jeu les joueurs changent de rôle"),
    "Play2":Translation(en="If the players are matched in all rounds \n the game will do other round",es="Si los jugadores quedan empatados en todas las rondas \n el juego hara otra ronda",fr="Si les joueurs sont assortis dans tous les tours \n le jeu fera un autre tour"),
    "Play3":Translation(en="The player that have more points in the end of game win",es="El jugador que tenga mas puntos al final del juego gana",fr="Le joueur qui a le plus de points à la fin du jeu gagne"),
    "How to Win?":Translation(en="How Win",es="Como ganar",fr="Comment gagner"),
    "PointsAttack":Translation(en="The attacker that destroy the enemy's eagle gains 10 points, \n also gains 1 point for each block that destroy",es="El atacante que destruya el aguila enemiga gana 10 puntos, \n tambien gana 1 punto por cada bloque que destruya",fr="L'attaquant qui détruit l'aigle ennemi gagne 10 points, \n gagne également 1 point pour chaque bloc qu'il détruit"),
    "PointsDefender":Translation(en="The defender whose eagle is not destroyed gains 10 points,\n also gains 1 point for each block that is not destroyed.",es="El defensor cuyo aguila no sea destruida gana 10 puntos, \n tambien gana 1 punto por cada bloque que no sea destruido",fr="Le défenseur dont l'aigle n'est pas détruit gagne 10 points, \n gagne également 1 point pour chaque bloc qui n'est pas détruit"),

}

#EXAMPLE Lg.dic["Login"][Lg.language]