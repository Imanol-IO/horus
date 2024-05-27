#import os
from pathlib import Path
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESSQL = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "db",
        "USER": "postgres", 
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'horus',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',  # O la dirección IP de tu servidor MySQL
        'PORT': '3306',  # El puerto predeterminado de MySQL es 3306
    }
}
