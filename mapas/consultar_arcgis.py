"""
Carga recursivamente el modulo
"""


def load_src(name, fpath):
    import os
    import imp
    try:
        return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
    except NameError:
        import sys
        is_windows = hasattr(sys, 'getwindowsversion')
        if (is_windows):
            fpath = fpath.replace('/', '\\')
        return imp.load_source(name, os.path.join(os.getcwd(), fpath))
load_src("arcgisme", "../repo/arcgis/arcgis.py")

import arcgisme
import os
import time

service = None

def consultar_features(username, password):
    print("Consultando primer servicio...")
    #source = "http://utility.arcgis.com/usrsvcs/servers/3832d8c34bd94b5e993615cbb07e47d4/rest/services/Edicion/Clientes_por_Clasificacion_Edicion/FeatureServer"
    source = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/arcgis/rest/services/survey123_f2aeed2a8d3242d4a2a0b5337d692676/FeatureServer"
    #source = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/arcgis/rest/services/pruebaarchivos/FeatureServer"
    # OBJECTID = "FID"  # la fila OBJECTID no esta en el servicio
    service = arcgisme.ArcGIS(
        source,
        username=username,
        password=password
    )

    layer_id = 0
    today = time.strftime("%m-%d-%Y")
    # OJO: Hay que tener en cuenta la hora en que se ejecuta cada script,
    # en determinado caso no se ejecuta el mismo dia de los datos si no
    # en una fecha posterior u anterior.
    #print("today", str(today))
    #statement = "CreationDate >= '01-31-2017 00:00:00'"
    #statement = "CreationDate >= '" + str(today) + " 00:00:00'"
    statement = "CreationDate >= '02-02-2017 00:00:00'"
    print("statement", statement)
    geojson = service.get(layer_id, where=statement)
    if(len(geojson) == 0): # No devuelve resultados
        return False
    return geojson["features"]

def consultar_attachment(objectId, username, password):
    print("Consultando segundo servicio...")
    base_url = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/arcgis/rest/services/survey123_f2aeed2a8d3242d4a2a0b5337d692676/FeatureServer"
    service2 = arcgisme.ArcGIS(
        base_url,
        username=username,
        password=password
    )
    layer_id = 0
    service_url = base_url + "/" + str(layer_id) + "/queryAttachments"
    #objectIds=1613&globalIds=&definitionExpression=&attachmentTypes=&size=&resultOffset=&resultRecordCount=&f=pjson&token=

    resultObjectId = objectId
    params = {
        "objectIds": resultObjectId,
        "globalIds": "",
        "definitionExpression": "",
        "attachmentTypes": "",
        "size": "",
        "resultOffset": "",
        "resultRecordCount": "",
        "f": "pjson"
    }
    geojson = service2.get_custom(service_url, params)
    if len(geojson["attachmentGroups"]) == 0: # No hay attachments
        return False
    # Solo se selecciona el primer attachment
    attachment = geojson["attachmentGroups"][0]["attachmentInfos"][0]
    attachmentId = attachment["id"]
    #print("queryAttachments", attachment)

    image_url = base_url + "/" + str(layer_id) + "/" + str(resultObjectId) + "/attachments/" + str(attachmentId)
    #return image_url
    token = str(service2.token)
    print("Token = ", token)
    image_url_token = image_url + "?token=" + token
    print("image_url", image_url)
    return image_url_token
def consultar_arcgis_hoy():
    return consultar_arcgis()

def consultar_arcgis():
    username = os.getenv('ARCGIS_USERNAME', None)
    password = os.getenv('ARCGIS_PASSWORD', None)
    if username is None or password is None:
        print("username: ", username, "; password: ", password)
        print('No se ha puesto usuario y clave como variable de entorno.')
        exit()

    features = consultar_features(username, password)
    #print("features", features)
    if features == False:
        return False
    new_features = []
    for feature in features:
        print("feature.properties.objectId", feature["properties"]["ObjectId"])
        objectId = str(feature["properties"]["ObjectId"])
        attachment = consultar_attachment(objectId, username, password)
        print("attachment", attachment)
        feature["attachment"] = attachment
        new_features.append(feature)
    return new_features
    #return len(geojson["features"])
