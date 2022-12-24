import sys
#Importaciones de directorios


def iniciar():
    while True:
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Ejercicio 1")
        print("[2] Ejercicio 2")
        print("[3]  Ejercicio 3")
        print("[4] Ejercicio 4")
        print("[5] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        if opcion == "1":
            print("Ejercicio 1")
            while True:
                print("========================")
                print("[1] Opcion 1")
                print("[2] Opcion 2")
                print("[3] Salida")
                print("========================")
                opcion2 = input("> ")
                if opcion2 == "1":
                    print("Opcion 1")
                elif opcion2 == "2":
                    print("Opcion 2")
                elif opcion2 == "3":
                    print("Volviendo al menu principal")
                    break

        elif opcion == "2":
            print("Ejercicio 2")

        elif opcion == "3":
            print("Ejercicio 3")

        elif opcion == "4":
            print("Ejercicio 4")
            
        elif opcion == "5":
            print("Saliendo...")
            break
