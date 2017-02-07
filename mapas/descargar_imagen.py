def descargar_imagen(url_imagen, nombre_imagen, dir_imagenes="imagenes"):
    import os
    import urllib

    # print("url_imagen", url_imagen)
    #nombre_imagen = url_imagen[url_imagen.rfind("/") + 1:]
    #Absolute PATH
    path = os.path.dirname(__file__).replace("\\","/")
    dir_imagenes = path + "/../" + dir_imagenes
    nombre_imagen = nombre_imagen
    destino_imagen = dir_imagenes + "/" + nombre_imagen
    # print("nombre_imagen", nombre_imagen)
    # print("destino_imagen", destino_imagen)
    urllib.urlretrieve(url_imagen, destino_imagen)

    resultado_imagen = {'nombre_imagen': nombre_imagen,
                        'dir_imagen': destino_imagen}
    return resultado_imagen
    # return os.path.dirname(__file__) + "/result.png"
