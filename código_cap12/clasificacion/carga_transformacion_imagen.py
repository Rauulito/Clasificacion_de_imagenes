from carga_modelo import clases, modelo

#---------------------------------------------
# CARGA Y TRANSFORMACIÓN DE UNA IMAGEN
#---------------------------------------------

from PIL import Image, ImageFilter
def transformacion():
    #Carga de la imagen
    imagen = Image.open("imagenes/zapatilla.jpg").convert('L')

    #Dimensión de la imagen
    largo = float(imagen.size[0])
    alto = float(imagen.size[1])

    #Creación de una imagen nueva
    nuevaImagen = Image.new('L', (28, 28), (255))

    #Redimensionamiento de la imagen
    #La imagen es más larga que alta, la ponemos a 20 píxeles
    if largo > alto:
            #Se calcula la relación de ampliación entre la altura y el largo
            relacionAltura = int(round((20.0 / largo * alto), 0))
            if (relacionAltura == 0):
                nAltura = 1

            #Redimensionamiento
            img = imagen.resize((20, relacionAltura), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
            #Posición horizontal
            posicion_alto = int(round(((28 - relacionAltura) / 2), 0))

            nuevaImagen.paste(img, (4, posicion_alto))  # pegar imagen redimensionada en lienzo en blanco
    else:

        relacionAltura = int(round((20.0 / alto * largo), 0))  # redimensionar anchura según relación altura
        if (relacionAltura == 0):  # caso raro pero el mínimo es 1 píxel
            relacionAltura = 1

        #Redimensionamiento
        img = imagen.resize((relacionAltura, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)

        #Cálculo de la posición vertical
        altura_izquierda = int(round(((28 - relacionAltura) / 2), 0))
        nuevaImagen.paste(img, (altura_izquierda, 4))

    #Recuperación de los píxeles
    pixeles = list(nuevaImagen.getdata())

    #Normalización de los píxeles
    tabla = [(255 - x) * 1.0 / 255.0 for x in pixeles]

    import numpy as np
    #Transformación de la tabla en tabla numpy
    img = np.array(tabla)

    #Se transforma la tabla lineal en imagen 28x20
    imagen_test = img.reshape(1, 28, 28, 1)

    prediccion = modelo.predict_classes(imagen_test)
    print()
    print("La imagen es: "+clases[prediccion[0]])
    print()

    #Extracción de las probabilidades
    probabilidades = modelo.predict_proba(imagen_test)

    i=0
    for clase in clases:
        print(clase + ": "+str((probabilidades[0][i]*100))+"%")
        i=i+1
