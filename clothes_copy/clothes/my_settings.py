DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'clothes',
        'USER'     : 'root',
        'PASSWORD' : 'qwqw1212',
        'HOST'     : 'localHost',
        'OPTIONS'  : {'charset': 'utf8mb4'},
        'TEST': {
            'CHARSET'  : 'utf8mb4',
            'COLLATION': 'utf8_general_ci'
        }
    }
}