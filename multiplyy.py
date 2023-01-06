import random
import time


mensaje = ("Aprendamos a multpicar")

while True:  # bucle que se repite mientras el jugador quiera seguir jugando
    print(mensaje)

    num = int(input("Que tabla de multiplicar quieres practicar?: "))

    print("----------------------------------")
    print("Haz elegido la tabla:", num)
    instrucciones = """  ||Se mostrara la tabla para que la veas, cuando termines de verla,
    pulsa continuar y la tabla desaparecerá y empezaran los ejercicios.||"""
    print(instrucciones)

    print("**************************")

    def tablas(tabla):
        print("----------------")
        print("|1 *", tabla, " = ",  1 * tabla, "  |")
        print("|2 *", tabla, " = ",  2 * tabla, " |")
        print("|3 *", tabla, " = ",  3 * tabla, " |")
        print("|4 *", tabla, " = ",  4 * tabla, " |")
        print("|5 *", tabla, " = ",  5 * tabla, " |")
        print("|6 *", tabla, " = ",  6 * tabla, " |")
        print("|7 *", tabla, " = ",  7 * tabla, " |")
        print("|8 *", tabla, " = ",  8 * tabla, " |")
        print("|9 *", tabla, " = ",  9 * tabla, " |")
        print("|10 *",tabla, " =", 10 * tabla, " |")
        print("----------------")

    tablas(num)

    hacer_ejercicios = input("Quieres continuar con los ejercicios? [s]")

    if hacer_ejercicios == "s":
        print("\033[H\033[J")



    print("----------------------------------")

    veces_jugadas = int(input("Cuantas veces quieres jugar?: "))

    correctas = 0
    inccorrectas = 0



    for i in range(0, veces_jugadas):
        print("   ")
        randomnum = random.randint(1, 10)
        result = num * randomnum
        human_rsult = float(input("Cual es el resultado de {} * {}: ".format(num, randomnum)))
        if human_rsult == result:
            print("Correcto!")
            correctas = correctas + 1
        else:
            print("Incorrecta...")
            print(" ")
            print("La respuesta correcta es: {}".format(result))  # imprimimos la respuesta correcta
            print(" ")
            print("Tienes {} manzanas en {} bolsas, la respuesta total es {}.".format(num, randomnum,result))
            inccorrectas = inccorrectas + 1

    print("----------------------------------")
    print("Tuviste ", correctas, " correctas")
    print("Tuviste ", inccorrectas, " incorrectas")


    print("----------------------------------")
    # preguntamos al jugador si quiere volver a jugar
    continuar_jugando = input("¿Quieres volver a jugar? (s/n) ")
    if continuar_jugando == "n":  # si responde "n", terminamos el bucle y finalizamos el programa
        break
    elif continuar_jugando == "s":
        print("\033[H\033[J")
