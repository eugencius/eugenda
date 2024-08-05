from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from contacts import views

app_name = "contacts"

contacts_api_router = SimpleRouter()
contacts_api_router.register("api", views.ContactsViewsetAPI, basename="recipes-api")

site = [
    path("", views.IndexBaseView.as_view(), name="index"),
    path("details/<int:pk>", views.ContactDetailsView.as_view(), name="details"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("create/", views.CreateContact.as_view(), name="create"),
    path("edit/<int:pk>", views.EditContact.as_view(), name="edit"),
    path("delete/<int:pk>", views.DeleteContact.as_view(), name="delete"),
]

api = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(contacts_api_router.urls)),
]

urlpatterns = site + api
