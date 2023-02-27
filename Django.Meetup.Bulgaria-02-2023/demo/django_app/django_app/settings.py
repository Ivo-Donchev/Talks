from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-vh=li^hdb^%6a@j=tde@0z4kil*h!x9$wm9qhb_@2(s6r+xq^r"

DEBUG = True
ALLOWED_HOSTS = ['localhost']
CORS_ORIGIN_WHITELIST = ['http://localhost:3000']

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    'my_app.apps.MyAppConfig'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_app.urls"

WSGI_APPLICATION = "django_app.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SQL queries logger
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         "django.server": {
#             "()": "my_app.logging.CustomWebServerFormatter",
#             "format": (
#                 "{message} \n"
#                 "{create_queries_count}({create_queries_time}s) \t"
#                 "{select_queries_count}({select_queries_time}s) \t"
#                 "{update_queries_count}({update_queries_time}s) \t"
#                 "{delete_queries_count}({delete_queries_time}s) \t"
#                 "{is_transaction}"
#             ),
#             "style": "{",
#         }

#     },
#     'handlers': {
#         "django.server": {
#             "level": "INFO",
#             "class": "logging.StreamHandler",
#             "formatter": "django.server",
#         },
#         "debug_console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "django.server",
#         },
#     },
#     'loggers': {
#         'my_app.views': {
#             "handlers": ["debug_console"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#         "django.server": {
#             "handlers": ["django.server"],
#             "level": "INFO",
#             "propagate": False,
#         },
#     }
# }
