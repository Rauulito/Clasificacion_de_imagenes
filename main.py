#pruebas
#Importamos directorios
import sys
sys.path.insert(0,"/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/aprendizaje_no_supervisado" )
sys.path.insert(0, "/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/generacion_de_datos")
sys.path.insert(0, "/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/Visualizacion_3d_curvas_gaussianas")
#Importamos funciones
from aprendizaje_k_mean import aprendizaje
from clustering2 import clustering2
from datos import datos
from cerezas import cerezas
from albaricoques import albaricoques
from clustering import clustering
from dosd import  dim_2
from tresd import dim_3


def iniciar():
    print("Iniciando...")

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al Albaricoques-Cerezas-Clustering  ")
        print("========================")
        print("[1] Escoga la carpeta")
        print("[2] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")

        if opcion == '1':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] aprendizaje_no_supervisado")
                print("[2] genaricon_de_datos")
                print("[3] Visualizacion_3D_curvas_gaussianas")
                print("[4] Volver al menu principal")
                opcion2 = input("> ")
                if opcion2 == '1':
                    aprendizaje()
                    clustering2()
                    datos()
                elif opcion2 == '2':
                    albaricoques()
                    cerezas()
                    clustering()
                elif opcion2 == '3':
                    dim_2()
                    dim_3()
                elif opcion2 == '4':
                    print("Volviendo...")
                    break
        if opcion == '2':
            print("Saliendo...")
            break
    


if __name__ == "__main__":
    iniciar()