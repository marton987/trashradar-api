"""
Django settings for trashradar project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import environ


root = environ.Path(__file__) - 1

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'djangoSecretKey'),
    ALLOWED_HOSTS=(list, ['*']),
    BROKER_URL=(str, 'redis://localhost:6379'),
    DATABASE_URL=(str, 'psql://trashradar:HS8J12MQW~975NS@localhost/trashradar'),
    MEDIA_URL=(str, '/media/'), STATIC_URL=(str, '/static/'),
    EMAIL_BACKEND=(str, 'django.core.mail.backends.smtp.EmailBackend'),
    EMAIL_URL=(str, 'smtp+tls://admin@example.org:password@smtp.gmail.com:587/'),
    DEFAULT_FROM_EMAIL=(str, 'admin@example.org'),
    SPARKPOST_API_KEY=(str, 'sparkPostApiKey'),
    API_HOST=(str, 'https://api.host.com'),
    STRIPE_API_KEY=(str, 'stripeApiKey'),
)

environ.Env.read_env()

BASE_DIR = root()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'corsheaders',
    'django_nose',
    # apps
    'accounts',
    'complaints',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trashradar.urls'

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

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

WSGI_APPLICATION = 'trashradar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db()
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Custom user
AUTH_USER_MODEL = 'accounts.Account'


# SparkPost
SPARKPOST_OPTIONS = {
    'inline_css': True,
    'transactional': True,
}
SPARKPOST_API_KEY = env('SPARKPOST_API_KEY')
EMAIL_BACKEND = env('EMAIL_BACKEND')

# CELERY Configuration
BROKER_URL = env('BROKER_URL')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

public_root = root.path('public/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = env('MEDIA_URL')
STATIC_ROOT = public_root('static')
STATIC_URL = env('STATIC_URL')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}
