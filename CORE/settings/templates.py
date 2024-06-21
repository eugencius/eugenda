from . import BASE_DIR
from django.contrib.messages import constants as messages

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "templates/static/"]

# Django messages

MESSAGE_TAGS = {
    messages.SUCCESS: "notification message-success",
    messages.ERROR: "notification message-error",
    messages.WARNING: "notification message-warning",
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"
