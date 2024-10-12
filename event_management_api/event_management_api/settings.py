from pathlib import Path
from datetime import timedelta
from decouple import config


SECRET_KEY = config('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#security
CSRF_COOKIE_SECURE = True  # Use HTTPS for CSRF cookie
X_FRAME_OPTIONS = 'DENY'  # Prevent your site from being framed
SECURE_BROWSER_XSS_FILTER = True  # Activate the browser XSS filter
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from MIME-sniffing
SESSION_COOKIE_SECURE = True  # Use HTTPS for session cookies
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS

ALLOWED_HOSTS = ['jaxxy.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'events',
    'accounts',
    'taggit',
    'django_filters',
    'drf_spectacular',
]

REST_FRAMEWORK = {
    
    #jwt authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    #pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,

    #django filter
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    #drf spectacular
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Event Management API',
    'DESCRIPTION': 'RESTful API for managing events, including features for user authentication, event creation, feedback on past events, categorizing, and filtering of events. It allows users to register, create events, categorize them, leave feedback on past events, and filter events based on category or other criteria.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

TAGGIT_CASE_INSENSITIVE = True


#jwt token expiry
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=6)
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_management_api.urls'

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

WSGI_APPLICATION = 'event_management_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'), 
        'USER': config('USER_NAME'),      
        'PASSWORD': config('PASSWORD'),    
        'HOST': config('HOST'),  
        'PORT': '3306',                 # MySQL port, usually 3306
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
