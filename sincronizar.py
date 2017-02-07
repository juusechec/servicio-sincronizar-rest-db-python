#!/usr/bin/env python2.7
from mapas import consultar_arcgis_hoy
from mapas import descargar_imagen
# url_imagen = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/arcgis/rest/services/survey123_f2aeed2a8d3242d4a2a0b5337d692676/FeatureServer/0/1706/attachments/1701"
# nombre_imagen = url_imagen[url_imagen.find("FeatureServer"):]
# nombre_imagen = nombre_imagen.replace("/", "_") + ".jpg"
# print("nombre_imagen", nombre_imagen)
# descargar_imagen(url_imagen, nombre_imagen)
# exit()
###
features = consultar_arcgis_hoy()
if features == False:
    print("No hay datos el dia de hoy.")
for feature in features:
    print("feature", feature)
    if feature["attachment"]:
        url_imagen = feature["attachment"]
        nombre_imagen = url_imagen[url_imagen.find("FeatureServer"):url_imagen.find("?")]
        nombre_imagen = nombre_imagen.replace("/", "_") + ".jpg"
        descargar_imagen(url_imagen, nombre_imagen)
