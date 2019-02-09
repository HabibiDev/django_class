DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog_db',
        'USER': 'admin_blog',
        'PASSWORD': '753951',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'INFO.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'email_backend':'django.core.mail.backends.filebased.EmailBackend'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'mylogger': {
            'handlers': ['file', 'console', 'mail_admins'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

EMAIL_FILE_PATH = '/tmp/mass/'
ADMINS = [('Anton','example@mail.ru')]
INTERNAL_IPS = '127.0.0.1'
