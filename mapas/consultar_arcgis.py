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
    geojson = service.get(layer_id, where="CreationDate >= '01-31-2017 00:00:00'")
    return geojson["features"]

def consultar_attachment(objectId, username, password):
    print("Consultando segundo servicio...")
    source2 = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/arcgis/rest/services/survey123_f2aeed2a8d3242d4a2a0b5337d692676/FeatureServer/"
    service2 = arcgisme.ArcGIS(
        source2,
        username=username,
        password=password
    )

    service_url = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/arcgis/rest/services/survey123_f2aeed2a8d3242d4a2a0b5337d692676/FeatureServer/0/queryAttachments"
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
    attachment = geojson["attachmentGroups"][0]["attachmentInfos"][0]
    attachmentId = attachment["id"]
    print("queryAttachments", attachment)

    image_url = "http://services3.arcgis.com/ry5R3Rlqp1fSnwj4/ArcGIS/rest/services/survey123_f2aeed2a8d3242d4a2a0b5337d692676/FeatureServer/0/" + str(resultObjectId) + "/attachments/" + str(attachmentId)
    print("image_url", image_url)

def consultar_arcgis():
    username = os.getenv('ARCGIS_USERNAME', None)
    password = os.getenv('ARCGIS_PASSWORD', None)
    if username is None or password is None:
        print("username: ", username, "; password: ", password)
        print('No se ha puesto usuario y clave como variable de entorno.')
        exit()

    features = consultar_features(username, password)
    #print("features", features)
    for feature in features:
        print("feature.properties.objectId", feature["properties"]["ObjectId"])
        objectId = str(feature["properties"]["ObjectId"])
        attachment = consultar_attachment(objectId, username, password)
        print(attachment)

    return 0
    #return len(geojson["features"])
