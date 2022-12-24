#pruebas
#Importamos directorios
import sys
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/código_cap12/1_capa_convolucion")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/código_cap12/1_capa_convolucion_aumentada")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/código_cap12/4_capas_convolucion_aunmentada")
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Clasificacion_de_imagenes/código_cap12/clasificacion")
#Importamos funciones
from creacion_de_la_red_1 import creacion_de_la_red_1
from preparacion_1 import PreparacionDatos_1
from creacion_de_la_red_2 import creacion_de_la_red_2
from Preparacion_2 import preparacion_2
from creacion_de_la_red_3 import creacion_de_la_red_3
from preparacion_3 import preparar_datos_3
from carga_modelo import carga
from carga_transformacion_imagen import transformacion



def iniciar():
    print("Iniciando...")

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al Albaricoques-Cerezas-Clustering  ")
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