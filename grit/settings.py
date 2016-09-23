# -*- coding: utf-8 -*-
"""
Django settings for grit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = (
    # whatever comes before
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g2b!21-czk!k1=eu9$6a1alsq6%jr^j)+vt!ark_o%rwe1j#fp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'exile_ui',
    'cuser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grit',
    'empresa',
    'empresa.riesgo',
    'norma',
    'norma.formulario',
    'notificacion',
    'usr',
    'validable',
    'epc',
)

EXILE_UI = {
    'site_title': 'Rondax',
    'site_header': 'Rondax',
    'index_title': 'Software para las rondas operativos',
    'media': {
        'logo': {
            'dashboard': '/media/piscix_logo/Icono-f-t.png',
            'page': '/media/piscix_logo/Icono-200px.png',
            'login': '/media/piscix_logo/Icono-s-t.png'
        },
        'icons':{
            'formulario': {
                'icon': 'content_paste',
                'groups': [
                    'Variables',
                    'Configuración'
                ],
                'models':{
                    'Tipo': {'icon':'settings', 'group': 'Configuración'},
                    'Formulario': {'icon':'assignment', 'group': 'Variables'},
                    'Campo': {'icon':'input', 'group':'Variables'},
                    'Registro': {'icon':'insert_comment', 'group':'Variables'},
                    'Valor': {'icon': 'settings', 'group':'Variables'},
                    'Entrada': {'icon': 'assignment_returned', 'group':'Variables'}
                }
            },
            'empresa': {
                'icon': 'settings',
                'groups': [
                ],
                'models': {
                    'Asistencia': {}
                },
            },'riesgo': {
                'icon': 'settings',
                'groups': [
                ],
                'models': {
                    'ElementoProteger': {}
                },
            },'norma': {
                'icon': 'settings',
                'groups': [
                ],
                'models': {
                    'Norma': {},
                    'Item': {},
                    'Formato': {}
                }
            },'epc': {
                'icon': 'settings',
                'groups': [
                    'EPC'
                ],
                'models': {
                    'Contrato': {'group': 'EPC', 'icon': 'library_books'},
                    'Contratista': {'group': 'EPC', 'icon': 'person'},
                    'Material': {'group': 'EPC', 'icon': 'layers'},
                    'OrdenTrabajo': {'group': 'EPC', 'icon': 'near_me'},
                    'Actividad': {'group': 'EPC', 'icon': 'access_time'},
                    'Proyecto': {'group': 'EPC', 'icon': 'folder_open' },
                    'TipoAdquisiscion': {'group': 'EPC', 'icon': 'toys' },
                }
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
        'name': 'formulario',
        'models': [
            'Tipo',
            'Formulario',
            'Campo',
            'Registro',
            'Valor',
            'Entrada',
        ]
    },
    {
        'name': 'empresa',
        'models': [
            'Asistencia',
            'User'
        ]
    },{
        'name': 'riesgo',
        'models': [
            'Criticidad',
            'ElementoProteger',
            'CargoRiesgo',
            'Riesgo',
            'EvaluacionRiesgos',
            'EvaluacionEmpresa',
        ]
    },
    {
        'name': 'norma',
        'models': [
            'Norma',
            'Item',
            'Formato'
        ]
    },
    {
        'name': 'epc',
        'models': [
            'Contratista',
            'Material',
            'OrdenTrabajo',
            'Actividad',
            'Proyecto',
        ]
    },
    {
        'name': 'logout'
    }
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cuser.middleware.CuserMiddleware',
)

ROOT_URLCONF = 'grit.urls'

WSGI_APPLICATION = 'grit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'grit',
        'USER': 'postgres',
        'PASSWORD': 'Exile*74522547',
        'HOST': '127.0.0.1',
        'PORT': '5432',     
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-la'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/var/www/grit/static/'
STATIC_URL = '/static/'#'http://192.168.42.130/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/grit/media/'
