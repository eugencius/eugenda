from django.urls import path

from contacts import views

app_name = "contacts"

site = [
    path("", views.IndexBaseView.as_view(), name="index"),
    path("details/<int:pk>", views.ContactDetailsView.as_view(), name="details"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("create/", views.CreateContact.as_view(), name="create"),
    path("edit/<int:pk>", views.EditContact.as_view(), name="edit"),
    path("delete/<int:pk>", views.DeleteContact.as_view(), name="delete"),
]

api = [
    path(
        "api/list/",
        views.ContactsViewsetAPI.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="index_api",
    ),
    path(
        "api/details/<int:pk>",
        views.ContactsViewsetAPI.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="details_api",
    ),
]

urlpatterns = site + api
