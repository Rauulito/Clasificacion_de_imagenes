#************************************************************************************
#
# REDES NEURONALES CON 1 CAPA DE CONVOLUCIONES Y UNA CANTIDAD DE IMAGENES AUMENTADA
#
#************************************************************************************

import pandas as pnd
import numpy as np
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

"""Este archivo sirve para alimentar al archivo creacion_de_la_red"""
#Definición del largo y ancho de la imagen
LARGO_IMAGEN = 28
ANCHO_IMAGEN = 28

#Carga de los datos de entrenamiento
observaciones_entrenamiento = pnd.read_csv('datas/zalando/fashion-mnist_train.csv')

#Solo se guardan las características "píxeles"
X = np.array(observaciones_entrenamiento.iloc[:, 1:])

#Se crea una tabla de categorías con ayuda del módulo Keras
y = to_categorical(np.array(observaciones_entrenamiento.iloc[:, 0]))

#Distribución de los datos de entrenamiento en datos de aprendizaje y datos de validación
#80 % de datos de aprendizaje y 20 % de datos de validación
X_aprendizaje, X_validacion, y_aprendizaje, y_validacion = train_test_split(X, y, test_size=0.2, random_state=13)


# Se redimensionan las imágenes al formato 28*28 y se realiza una adaptación de escala en los datos de los píxeles
X_aprendizaje = X_aprendizaje.reshape(X_aprendizaje.shape[0], ANCHO_IMAGEN, LARGO_IMAGEN, 1)
X_aprendizaje = X_aprendizaje.astype('float32')
X_aprendizaje /= 255

# Se hace lo mismo con los datos de validación
X_validacion = X_validacion.reshape(X_validacion.shape[0], ANCHO_IMAGEN, LARGO_IMAGEN, 1)
X_validacion = X_validacion.astype('float32')
X_validacion /= 255

#Preparación de los datos de prueba
observaciones_test = pnd.read_csv('datas/zalando/fashion-mnist_test.csv')

X_test = np.array(observaciones_test.iloc[:, 1:])
y_test = to_categorical(np.array(observaciones_test.iloc[:, 0]))

X_test = X_test.reshape(X_test.shape[0], ANCHO_IMAGEN, LARGO_IMAGEN, 1)
X_test = X_test.astype('float32')
X_test /= 255