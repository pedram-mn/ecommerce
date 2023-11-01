from datetime import timedelta

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "The Shop Admin",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "My Shop",
    "site_logo": 'logo.png',
    # Welcome text on the login screen
    "welcome_sign": "Welcome to shop panel! :)",

    # Copyright on the footer
    "copyright": "Shop",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "user.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # model admin to link to (Permissions checked against model)
        {"model": "user.User"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "user.User"}
    ],

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # for the full list of 5.13.0 free icon classes
    "icons": {
        "customer.Customer": "fas fa-users-cog",
        "core.User": "fas fa-user",
        "auth.Group": "fas fa-users-cog",
        "customer.Address": "fas fa-address-card",
        "Order.Coupon": "fa fa-credit-card",
        "Order.Order": "fa fa-th-list",
        "Order.OrderItem": "fa fa-plus-square",
        "Order.Status": "fa fa-check-square",
        "Product.Brand": "fa fa-check-square",
        "Product.Category": "fa fa-check-square",
        "Product.Discount": "fa fa-check-square",
        "Product.Product": "fa fa-check-square",
        "Product.Comment": "fa fa-check-square",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "show_ui_builder": True,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"user.User": "collapsible"},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-gray",
    "accent": "accent-primary",
    "navbar": "navbar-indigo navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-purple",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}

"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(z2f6e!q$d-w)5*08%z5v1su%!i3g88!3uckq(i!6@p!95n+r0'
# python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
# ToDo Django environs
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',  # For customizing django admin panel.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # REST framework
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_celery_beat',
    'corsheaders',

    'core',
    'customer',
    'product',
    'order',
    'landing',
    'django_extensions',  # This will help us find the urls.
    'sass_processor',  # Using Scss and Sass files on project
    'mathfilters',  # Allowing the math operations on dtl.
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'order.context.cart_number',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'db',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Statics
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static", 'static/', ]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

# STATIC_ROOT = BASE_DIR / 'static'
# SassProcessor
SASS_PROCESSOR_ROOT = STATIC_URL

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'core.User'

# Django logging system
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'short-formatter': {
            'format': '{levelname} ({asctime}): "{message}"',
            'style': '{',
        },
        'verbose-formatter': {
            'format': '{levelname} ({asctime}): "{message}" at  {module} (process: {process.d}, thread: {thread.d})',
            'style': '{',
        },
    },
    'filters': {
        'length_limit': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda record: not len(record.getMessage()) < 20
        },

    },
    'handlers': {
        'my-console-handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'short-formatter',
            'filters': ['length_limit'],
        },
        'my-file-handler': {
            'class': 'logging.FileHandler',  # Write file!
            'filename': BASE_DIR / 'a-test.log',
            'formatter': 'verbose-formatter',
            'level': 'ERROR'
        },
    },
    'root': {
        'handlers': ['my-console-handler'],
        'level': 'DEBUG',
    },
    'loggers': {
        'project': {
            'handlers': ['my-file-handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'project.developers': {
            'handlers': ['my-file-handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
# If the anonymous user tries to open login required pages will be redirected to this url.
LOGIN_URL = "/customer/login/"

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'pedram.monazzami@gmail.com'
EMAIL_HOST_PASSWORD = 'yhtbeofqfbhzbpcf'

# AUTHENTICATION SETTINGS

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# JWT SETTINGS

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=8),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
}

# CORS SETTINGS

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# CELERY SETTINGS

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_DEFAULT_QUEUE = 'default'

# CELERY BEAT SETTINGS

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
