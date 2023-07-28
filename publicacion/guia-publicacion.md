1. Primero se tuvo que instalar la libreria gunicorn en el entorno con el siguiente comando "pip install gunicorn"
2. En el settings de nuestro proyecto de django remplazamos ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"] y agregamos STATIC_ROOT = os.path.join(BASE_DIR, 'static')
3. En el archivo urls de nuestro proyecto importamos from django.contrib.staticfiles.urls import staticfiles_urlpatterns y agregamos urlpatterns += staticfiles_urlpatterns()
4. Luego ponemos el siguiente comando en consola estando dentro del proyecto "python manage.py collectstatic"
5. Levantamos el proyecto con gunicor "gunicorn --bind 0.0.0.0:8000 proyectoUno.wsgi"
6. En una consola hacemos lo siguiente: sudo nano /etc/systemd/system/mi_servicio.service
7. AL entar dentro colocamos lo siguiente remplazando con tu propias direcciones
[Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=jhoel-VirtualBox
# el grupo del sistema operativo que permite la comunicación a desde el servido>
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del >
WorkingDirectory=/home/jhoel/Escritorio/Jhoel/trabajo-final-2bim-JAOC1930/proye>

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entorno>
Environment="/home/jhoel/Escritorio/Jhoel/entorno/bin"

# Detallar el comando para iniciar el servicio
8. Por motivos desconocidos me sale error al querer ejecutar el siguiente comando sudo systemctl start application
