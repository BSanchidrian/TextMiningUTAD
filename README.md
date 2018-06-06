# TextMiningUTAD

Practica final de verificación y desarrollo de programas


# Instalacion

La aplicacion usa Django 2.0, la cual necesita Python 3.4 o superior.

```bash
sudo apt install python3-pip
sudo pip3 install django

# dependencias
sudo pip3 install redis
sudo pip3 install bs4
sudo pip3 install selenium
```

* Es necesario que chromedriver esté inluido en el PATH para poder pasar los test que utilizan Selenium

```bash
python3 manage.py test
```

Se puede verificar la version de Django usando:

```bash
python3 -m django --version
```

Una vez este instalado correctamente ejecutar con:

```bash
python3 manage.py runserver
```

La web se puede acceder desde http://localhost:8000/verificacion/