#pruebas
#Importamos directorios
import sys
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/codigo(II)/Capa_convolucion")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/codigo(II)/Capa_convolucion_aumentada")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/codigo(II)/Capas_convolucion_aumentada")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/codigo(II)/clasificacion")
#Importamos funciones
from creacion_de_la_red_1 import creacion_de_la_red_1
from creacion_de_la_red_2 import creacion_de_la_red_2
from creacion_de_la_red_3 import creacion_de_la_red_3
from carga_transformacion_imagen import transformacion



def iniciar():
    print("Iniciando...")

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido a la clasificacion de imagenes ")
        print("========================")
        print("[1] Escoga la carpeta")
        print("[2] Cerrar clasificacion   ")
        print("========================")

        opcion = input("> ")

        if opcion == '1':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] 1_capa_convolucion")
                print("[2] 1_capa_convolucion_aumentada")
                print("[3] 4_capas_convolucion_aumentada")
                print("[4] clasificacion")
                print("[5] Volver al menu principal")
                opcion2 = input("> ")
                if opcion2 == '1':
                    creacion_de_la_red_1()
                elif opcion2 == '2':
                    creacion_de_la_red_2()
                elif opcion2 == '3':
                    creacion_de_la_red_3()
                elif opcion2 == '4':
                    transformacion()
                elif opcion2 == '5':
                    print("Volviendo...")
                    break
        if opcion == '2':
            print("Saliendo...")
            break
    


if __name__ == "__main__":
    iniciar()