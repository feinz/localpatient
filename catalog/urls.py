from django.urls import path
from . import views

#pattern for catalog application
urlpatterns = [
    path('', views.index, name='index'),
    path('patient_list/', views.PatientListView.as_view(), name='patient_list'),
    path('patient_detail/<int:pk>', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patient/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patient_detail/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_detail_update'),
    path('patient_detail/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_detail_delete'),
    
]