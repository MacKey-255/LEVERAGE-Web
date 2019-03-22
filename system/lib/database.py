import os


DATABASES_CONFIG = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'minecraft.sqlite3'),
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'minecraft',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'minecraft',
        'USER': 'mackey',
        'PASSWORD': 'redes',
        'HOST': '10.30.1.31',
        'PORT': '3306',
    },
    'mongodb' : {
        'ENGINE' : 'django_mongodb_engine',
        'NAME' : 'minecraft',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
   }
}
