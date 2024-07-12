from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.IndexBaseView.as_view(), name="index"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("create/", views.CreateContact.as_view(), name="create"),
]
