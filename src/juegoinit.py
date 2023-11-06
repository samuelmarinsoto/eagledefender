from juegoclase import Juego

def iniciar(jugador1, jugador2):
    jugador1_puntos = 0
    jugador2_puntos = 0
    
    juego = Juego(jugador1, jugador2)

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 1 iniciando")

    # juego.fin(jugador1_puntos, jugador2_puntos)
    # match 1
    juego.partida(1)
    
    jugador1_puntos += juego.puntos_defensa
    jugador2_puntos += juego.puntos_atacante

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 2 iniciando")
    
    juego.partida(2)

    jugador1_puntos += juego.puntos_atacante
    jugador2_puntos += juego.puntos_defensa

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 3 iniciando")

    # match 2
    juego.partida(3)

    jugador1_puntos += juego.puntos_defensa
    jugador2_puntos += juego.puntos_atacante

    print(jugador1_puntos)
    print(jugador2_puntos)
    print("partida 4 iniciando")

    juego.partida(4)

    jugador1_puntos += juego.puntos_atacante
    jugador2_puntos += juego.puntos_defensa

    print("chequeando si fin")
    # chequea si ocupamos match 3
    if abs(jugador1_puntos - jugador2_puntos) >= 1000:
        juego.fin(jugador1_puntos, jugador2_puntos)

    else:
        print("no fin")

        print(jugador1_puntos)
        print(jugador2_puntos)
        print("partida 5 iniciando")
        
        # match 3
        juego.partida(5)

        jugador1_puntos += juego.puntos_defensa
        jugador2_puntos += juego.puntos_atacante

        print(jugador1_puntos)
        print(jugador2_puntos)
        print("partida 6 iniciando")

        juego.partida(6)

        jugador1_puntos += juego.puntos_atacante
        jugador2_puntos += juego.puntos_defensa

        print("fin, al fin")

        juego.fin(jugador1_puntos, jugador2_puntos)

import users
iniciar(users.player1, users.player2)
