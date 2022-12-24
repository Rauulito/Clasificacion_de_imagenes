from preparacion import X_aprendizaje, y_aprendizaje, ANCHO_IMAGEN, LARGO_IMAGEN, X_test, y_test, X_validacion, y_validacion

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

#Se especifican las dimensiones de la imagen de entrada
dimensionImagen = (ANCHO_IMAGEN, LARGO_IMAGEN, 1)

#Se crea la red neuronal capa por capa
redNeurona1Convolucion = Sequential()

#1- Adición de la capa de convolución que contiene
#  Capa coculta de 32 neuronas
#  Un filtro de 3x3 (Kernel) recorriendo la imagen
#  Una función de activación de tipo ReLU (Rectified Linear Activation)
#  Una imagen de entrada de 28px * 28 px
redNeurona1Convolucion.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=dimensionImagen))

#2- Definición de la función de pooling con un filtro de 2px por 2 px
redNeurona1Convolucion.add(MaxPooling2D(pool_size=(2, 2)))

#3- Adición de una función de ignorancia
redNeurona1Convolucion.add(Dropout(0.2))

#5 - Se transforma en una sola línea
redNeurona1Convolucion.add(Flatten())

#6 - Adición de una red neuronal compuesta por 128 neuronas con una función de activación de tipo Relu
redNeurona1Convolucion.add(Dense(128, activation='relu'))

#7 - Adición de una red neuronal compuesta por 10 neuronas con una función de activación de tipo softmax
redNeurona1Convolucion.add(Dense(10, activation='softmax'))

#8 - Compilación del modelo
import keras
redNeurona1Convolucion.compile(loss=keras.losses.categorical_crossentropy,
optimizer=keras.optimizers.Adam(),
metrics=['accuracy'])


#9 - Aprendizaje
historico_aprendizaje  = redNeurona1Convolucion.fit(X_aprendizaje, y_aprendizaje,
batch_size=256,
epochs=10,
verbose=1,
validation_data=(X_validacion, y_validacion))


#10 - Evaluación del modelo
evaluacion = redNeurona1Convolucion.evaluate(X_test, y_test, verbose=0)
print('Error:', evaluacion[0])
print('Precisión:', evaluacion[1])



#11 - Visualización de la fase de aprendizaje
import matplotlib.pyplot as plt

#Datos de precisión (accurary)
plt.plot(historico_aprendizaje.history['accuracy'])
plt.plot(historico_aprendizaje.history['val_accuracy'])
plt.title('Precisión del modelo')
plt.ylabel('Precisión')
plt.xlabel('Epoch')
plt.legend(['Aprendizaje', 'Test'], loc='upper left')
plt.show()

#Datos de validación y error
plt.plot(historico_aprendizaje.history['loss'])
plt.plot(historico_aprendizaje.history['val_loss'])
plt.title('Error')
plt.ylabel('Error')
plt.xlabel('Epoch')
plt.legend(['Aprendizaje', 'Test'], loc='upper left')
plt.show()