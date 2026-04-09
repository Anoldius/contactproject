from django.urls import path
from . import views

urlpatterns = [
    # Purpose: Connects the 'home' of this app to the list_contacts function
    path('contacts', views.list_contacts, name='list_contacts'),
]