#unholy python backend.
import os
import json
dir_path = "paginas/media/galeria"

#Obtiene una lista de los nombres de archivos dentro de la carpeta galeria.
def ContarArchivos():
    imagenes =[]
    for imagen in os.listdir(dir_path):
        #busca si el elemento seleccionado es una imagen de formato png o jpg.
        if os.path.isfile(os.path.join(dir_path,imagen)) and (imagen.endswith(".jpg") or imagen.endswith(".png")):
            imagenes.append(imagen)
    return imagenes
#convierte la lista de nombres de las imagenes en un archivo json.
def ConversionJSON():
    lista = ContarArchivos()
    
    with open("backend\data\ListaImagenes.json", "w") as archivo:
        json.dump(lista, archivo)

ConversionJSON()