import json
import requests
import os


class Impresora:
    """
    Una clase que permite imprimir un mapa dentro de unos parametros
    Para usar se necesita:
    impresora = mapas.imprimir.Impresora()
    url_imagen = impresora.obtener_imagen(Web_Map_as_JSON=gpstring)
    """

    def __init__(self,
                 print_url='https://sampleserver6.arcgisonline.com/arcgis/rest/services/Utilities/PrintingTools/GPServer/Export%20Web%20Map%20Task/execute'):
        self.print_url = print_url

    def obtener_imagen(self, f="json", Format="PNG32", Layout_Template="MAP_ONLY",
                  Web_Map_as_JSON=''):
        params = {
            'f': f,
            'Format': Format,
            'Layout_Template': Layout_Template,
            'Web_Map_as_JSON': Web_Map_as_JSON
        }
        response = requests.get(self.print_url, params=params)
        json = response.json()
        print(json)
        imagen = json["results"][0]["value"]["url"]
        return imagen
