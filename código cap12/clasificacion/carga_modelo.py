#----------------------------
# CARGA DEL MODELO
#----------------------------


#Carga de la descripción del modelo
archivo_json = open('modelo/modelo_4convoluciones.json', 'r')
modelo_json = archivo_json.read()
archivo_json.close()

#Carga de la descripción de los pesos del modelo
from keras.models import model_from_json
modelo = model_from_json(modelo_json)
# Cargar pesos en el modelo nuevo
modelo.load_weights("modelo/modelo_4convoluciones.h5")


#Definición de las categorías de clasificación
clases = ["Una camiseta/top","Un pantalón","Un jersey","Un vestido","Un abrigo","Una sandalia","Una camisa","Zapatillas","Un bolso","Botines"]