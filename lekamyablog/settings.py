import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("ALLOWED_HOSTS", "").split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    # 'https://lekamyangambibenido.up.railway.app',
    # 'https://*.railway.app'
]


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'blog',
    'accounts',
    
    'corsheaders',
    'ckeditor',
    'rest_framework',
]

DEFAULT_CHARSET = 'utf-8'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lekamyablog.urls'

CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
# Durée de session par défaut
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2  # 2 semaines
# # Durée de session prolongée pour "Se souvenir de moi"
# ACCOUNT_SESSION_REMEMBER = True

handler404 = 'blog.views.custom_404' 
handler403 = 'blog.views.custom_403'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lekamyablog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': os.getenv('LOCAL_DATABASE_NAME'),
        'USER': os.getenv('LOCAL_DATABASE_USER'),
        'PASSWORD': os.getenv('LOCAL_DATABASE_PASSWORD'),
        'HOST': os.getenv('LOCAL_DATABASE_HOST'),
        'PORT': os.getenv('LOCAL_DATABASE_PORT'),
    }
}

"""DATABASE_URL = os.environ.get('DATABASE_URL')

if os.getenv('ENVIRONMENT') == 'production':
    db_info = urlparse(DATABASE_URL)
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': db_info.path[1:],  
            'USER': db_info.username,
            'PASSWORD': db_info.password,
            'HOST': db_info.hostname,
            'PORT': db_info.port,
            'OPTIONS': {
                'sslmode': 'require',  
            },
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': os.getenv('LOCAL_DATABASE_NAME'),
        'USER': os.getenv('LOCAL_DATABASE_USER'),
        'PASSWORD': os.getenv('LOCAL_DATABASE_PASSWORD'),
        'HOST': os.getenv('LOCAL_DATABASE_HOST'),
        'PORT': os.getenv('LOCAL_DATABASE_PORT'),
    }
}"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

""""if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
    
    # Configuration AWS S3
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_SIGNATURE_NAME = 's3v4'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_S3_VERIFY = True
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = 'public-read'
    
    # Définition de MEDIA_URL pour qu'il pointe vers S3
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"""

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

LANGUAGE_COOKIE_NAME = 'site_language'

TIME_ZONE = 'Africa/Ndjamena'

USE_TZ = True
USE_I18N = True 
USE_L10N = True 


LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('English (US)')),
    ('ar', _('العربية')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Dr Lekamya Ngambi BenIdo",
    "site_header": "Administration du site",
    "site_logo": "assets/img/favicon.png",
    "theme": "slate",

    "navigation_expanded": True,

    "custom_css": "admin/css/custom_admin.css",

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "blog.Article": "fas fa-book",
        "blog.ContactMessage": "fas fa-envelope",
    },

    "copyright": "Abakarix4dev",
}

