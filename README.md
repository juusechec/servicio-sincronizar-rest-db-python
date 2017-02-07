  # Proyecto de Generación de reportes con python

Se generan reportes PDF a partir de la implementación REST de los servicios de arcgis server o arcgis online.

# Dependencias

- Python >= 3.5
- python-arcgis-rest-query
- Flask *

# Instalación dependencias Centos 7
```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh # a todo sí
pip install flask
pip install python-docx
sudo yum install -y libreoffice
```

# Pasos de instalación

1) Instalar una de las dependencias: (escriba los comandos preferiblemente en git-bash)

```bash
cd reportes-python # entrar al directorio descargado
git clone https://github.com/Schwanksta/python-arcgis-rest-query repo
```

2) Establece las variables de entorno para el usuario y el password de arcgis online:

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

- En GNU/Linux:

```bash
export ARCGIS_USERNAME='usuario_arcgis_online'
export ARCGIS_PASSWORD='clave_arcgis_online'
```
Opcionalmente agrega esas líneas en el ***~/.bashrc***

3) Cree unos directorios necesarios para el despliegue:
```bash
mkdir imagenes
mkdir documentos
```

4) Ejecutar el webservice:

```bash
python3 webservice.py
```
