"""
-Brayan Vargas
-C6Q124
-Grupo # 5
"""

# -----------------------------------------------FUNCIONES-----------------------------------------------

def leer_validar_adn():
    #valida el ingreso
    adn = input("(Solo se permiten: A, T, G, C)\nIngrese la cadena de ADN: ").upper()

    if len(adn) == 0:
        print("Error: La cadena no puede estar vacía.")
        exit()

    for base in adn:
        if base not in "ATGC":
            print("Error: La cadena de ADN contiene caracteres inválidos.")
            exit()

    print("Secuencia correcta:", adn)
    return adn


def adn_a_arn(adn):
    #convierte el ADN a ARN
    arn = ""
    for base in adn:
        if base == "A":
            arn += "U"
        elif base == "T":
            arn += "A"
        elif base == "G":
            arn += "C"
        elif base == "C":
            arn += "G"
    return arn


def tiene_start_stop(adn):
    if len(adn) % 3 != 0:
        print("No es multiplo de 3")
        return False


    separacion = []
    for i in range(0, len(adn), 3):
        separacion.append(adn[i:i+3])

    if separacion[0] != "ATG" or separacion[-1] != "TGA":
        return False

    # La subcadena entre ATG y TGA debe tener al menos un codon
    if len(separacion) <= 2:
        return False

    for i in range(1, len(separacion) - 1):
        if separacion[i] == "ATG" or separacion[i] == "TGA":
            return False

    return True


def calcular_frecuencias(adn):
    a = 0
    t = 0
    g = 0
    c = 0
    for base in adn:
        if base == "A":
            a += 1
        elif base == "T":
            t += 1
        elif base == "G":
            g += 1
        elif base == "C":
            c += 1

    print("=== Frecuencias ===")
    print("A=" + str(a) + " C=" + str(c) + " T=" + str(t) + " G=" + str(g))
    print("=== Histograma ===")
    print("A" * a)
    print("C" * c)
    print("T" * t)
    print("G" * g)


def menu(adn):
    while True:
        print("\n  ===Menú===")
        print("1. Pasar ADN a ARN")
        print("2. Tiene StartStop")
        print("3. Frecuencias")
        print("4. Salir del programa")

        opcion = int(input("Opción: "))

        if opcion == 1:
            arn = adn_a_arn(adn)
            print("ADN:", adn)
            print("ARN:", arn)

        elif opcion == 2:
            if tiene_start_stop(adn):
                print("Cumple StartStop")
            else:
                print("No cumple StartStop")

        elif opcion == 3:
            calcular_frecuencias(adn)

        elif opcion == 4:
            print("Saliendo del programa...")
            break

        elif opcion == 5:
            print(adn)
        
        else:
            print("Opción no válida.")


# -----------------------------------------------MAIN-----------------------------------------------
if __name__ == "__main__":
    print("\n-----------------Sistema de ADN y ARN-----------------\n")
    print("Carnet:C6Q124  Nombre:Brayan Vargas  Grupo: 5")
    print("=======================================================")
    print("              Universidad de Costa Rica")
    print("-Escuela de Ciencias de la Computación e Informática-")
    print("  -Proyecto final de introducción a la Computación-")
    print("=======================================================\n")

    adn = leer_validar_adn()
    menu(adn)