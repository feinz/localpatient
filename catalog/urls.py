from django.urls import path
from . import views

#pattern for catalog application
urlpatterns = [
    path('', views.index, name='index'),
    # path('patient_list/', views.PatientListView.as_view(), name='patient_list'),
    path('patient_list/', views.PatientListView.as_view(), name='patient_list'),
    path('patient_detail/<int:pk>', views.PatientDetailView.as_view(), name='patient_detail'),
    # path('patient/<int:pk>', views.patient_detail, name='patient_detail'),
]