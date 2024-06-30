from django.contrib import admin

from .models import Contact, Category


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "surname",
        "phone",
        "email",
        "creation_date",
        "creator",
    ]
    list_display_links = ["id", "name", "surname"]


admin.site.register(Category)
