DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

PROJECT_APPS = [
    "accounts",
    "contacts",
]


INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS
