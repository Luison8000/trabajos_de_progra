

def mostrar_menu():
    print("Habitaciones:")
    print("1. Azul")
    print("2. Roja")
    print("3. Verde")
    print("4. Rosa")
    print("5. Gris")
    print("6. Salir")
    print()
def elegir_habitacion():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")
        
        if opcion == '1':
            print(" habitacion Azul.\n")
        elif opcion == '2':
            print("habitacion Roja.\n")
        elif opcion == '3':
            print("habitacion verde.\n")
        elif opcion == '4':
            print("habitacion Rosa.\n")
        elif opcion == '5':
            print("habitacion Gris.\n")
        elif opcion == '6':
            print("nos vemos pronto")
            break
        else:
            print("elige una opción del 1 al 6.\n")
def main():
    elegir_habitacion()

if __name__ == "__main__":
    main()
    