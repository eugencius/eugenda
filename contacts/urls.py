from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("search/", views.search, name="search"),
    path("create/", views.create_contact, name="create"),
]
