from django.urls import path
from . import views
from django.views.generic import TemplateView

#pattern for staffinfo application
urlpatterns = [
    path('', views.staffindex, name='staffindex'),
    path('staffregister/', views.staffregister, name='staffregister'),
]