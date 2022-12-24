from preparacion import ANCHO_IMAGEN, LARGO_IMAGEN, X_aprendizaje, X_test, X_validacion, y_aprendizaje, y_test, y_validacion, BatchNormalization

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

def creacion_de_la_red_3():
    #Se especifican las dimensiones de la imagen de entrada
    dimensionImagen = (ANCHO_IMAGEN, LARGO_IMAGEN, 1)

    #Se crea la red neuronal capa por capa

    redNeuronas4Convolucion = Sequential()
    redNeuronas4Convolucion.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=dimensionImagen))
    redNeuronas4Convolucion.add(BatchNormalization())

    redNeuronas4Convolucion.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    redNeuronas4Convolucion.add(BatchNormalization())
    redNeuronas4Convolucion.add(MaxPooling2D(pool_size=(2, 2)))
    redNeuronas4Convolucion.add(Dropout(0.25))

    redNeuronas4Convolucion.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    redNeuronas4Convolucion.add(BatchNormalization())
    redNeuronas4Convolucion.add(Dropout(0.25))

    redNeuronas4Convolucion.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    redNeuronas4Convolucion.add(BatchNormalization())
    redNeuronas4Convolucion.add(MaxPooling2D(pool_size=(2, 2)))
    redNeuronas4Convolucion.add(Dropout(0.25))

    redNeuronas4Convolucion.add(Flatten())

    redNeuronas4Convolucion.add(Dense(512, activation='relu'))
    redNeuronas4Convolucion.add(BatchNormalization())
    redNeuronas4Convolucion.add(Dropout(0.5))

    redNeuronas4Convolucion.add(Dense(128, activation='relu'))
    redNeuronas4Convolucion.add(BatchNormalization())
    redNeuronas4Convolucion.add(Dropout(0.5))

    redNeuronas4Convolucion.add(Dense(10, activation='softmax'))

    #8 - Compilación del modelo
    import keras
    redNeuronas4Convolucion.compile(loss=keras.losses.categorical_crossentropy,
    optimizer=keras.optimizers.Adam(),
    metrics=['accuracy'])


    #9 - Aumento de la cantidad de imágenes
    from keras.preprocessing.image import ImageDataGenerator
    generador_imagenes = ImageDataGenerator(rotation_range=8,
    width_shift_range=0.08,
    shear_range=0.3,
    height_shift_range=0.08,
    zoom_range=0.08)


    nuevas_imagenes_aprendizaje = generador_imagenes.flow(X_aprendizaje, y_aprendizaje, batch_size=256)
    nuevas_imagenes_validacion = generador_imagenes.flow(X_validacion, y_validacion, batch_size=256)


    #10 - Aprendizaje
    import time
    start = time.clock();
    historico_aprendizaje = redNeuronas4Convolucion.fit_generator(nuevas_imagenes_aprendizaje,
    steps_per_epoch=48000//256,
    epochs=50,
    validation_data=nuevas_imagenes_validacion,
    validation_steps=12000//256,
    use_multiprocessing=False,
    verbose=1 )

    stop = time.clock();

    print("Tiempo de aprendizaje = "+str(stop-start))

    #11 - Evaluación del modelo
    evaluacion = redNeuronas4Convolucion.evaluate(X_test, y_test, verbose=0)
    print('Error:', evaluacion[0])
    print('Precisión:', evaluacion[1])


    #12 - Visualización de la fase de aprendizaje
    import matplotlib.pyplot as plt

    #Datos de precisión (accuracy)
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


    #Guardado del modelo
    # serializar modelo a JSON
    modelo_json = redNeuronas4Convolucion.to_json()
    with open("modelo/modelo_4convoluciones.json", "w") as json_file:
        json_file.write(modelo_json)

    # serializar pesos a HDF5
    redNeuronas4Convolucion.save_weights("modelo/modelo_4convoluciones.h5")
    print("¡Modelo guardado!")