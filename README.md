  # Proyecto de Syncronización de Servicio REST ArcGIS Online con base de datos local usando ArcPY

Se sincroniza día a día los servicios REST con una GeoDatabase en Oracle.

# Dependencias

- Python >= 2.7
- python-arcgis-rest-query

# Instalación dependencias Windows 10
```bash
pip install requests
```

# Pasos de instalación

1) Instalar una de las dependencias: (escriba los comandos preferiblemente en git-bash),
no haga esto si ya tiene el directorio repo con los archivos.

```bash
cd reportes-python # entrar al directorio descargado
git clone https://github.com/Schwanksta/python-arcgis-rest-query repo
```

2) Establece las variables de entorno para el usuario y el password de arcgis online:

- En Windows (Interfaz gráfica):
Siga los pasos del sitio https://kb.wisc.edu/cae/page.php?id=24500

- En Windows (cmd):

```bash
SET ARCGIS_USERNAME=usuario_arcgis_online
SET ARCGIS_PASSWORD=clave_arcgis_online
```

- En Windows (powershell):
```bash
$env:ARCGIS_USERNAME = "usuario_arcgis_online"
$env:ARCGIS_PASSWORD = "clave_arcgis_online"
```

3) Cree unos directorios necesarios para el despliegue:
```bash
mkdir imagenes
```

4) Ejecutar la sincronización (powershell, bash):

```bash
C:\Python27\ArcGIS10.4\python.exe E:\Users\jorge\Documents\acueducto\servicio\sincronizar.py
```

5) Ejecutar la sincronización con CRON programa en GO (https://golang.org/), se abre el ejecutable ***runservice.exe***.
