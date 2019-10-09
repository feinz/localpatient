from django.urls import path
from . import views

#pattern for catalog application
urlpatterns = [
    path('', views.index, name='index'),
]