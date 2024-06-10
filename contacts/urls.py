from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index_view, name="index"),
    path('create/', views.create_contact, name="create"),
]
